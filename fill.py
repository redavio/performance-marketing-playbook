#!/usr/bin/env python3
"""Fill the Performance Marketing Playbook deliverables from a company's inputs.

Standard library only (python-pptx is used if installed, to fill the PowerPoint deck).
The math matches deliverables/defaults.md, the budget tracker formulas and the Redavio
MCP server (redavio-web src/lib/playbook.ts); scripts/playbook-parity.mts in that repo
checks they agree, so change both together.

    python3 fill.py math inputs.json            # print the plan numbers
    python3 fill.py plan inputs.json --out out  # write every deliverable, filled in
    python3 fill.py calibrate experiments.csv   # back-test ICS scores against results

inputs.json needs pipeline_goal (or revenue_goal) and deal_size. Everything else is
optional; see DEFAULTS below or deliverables/defaults.md.
"""
import csv
import datetime as dt
import io
import json
import re
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATES = HERE / "deliverables"
REPO = "https://github.com/redavio/performance-marketing-playbook/blob/main"

DEFAULTS = {
    "company": "Your company",
    "months": 12,
    "start_date": None,  # filled with the next Monday
    "motion": "sales-led",
    "mql_to_sql": 0.25,
    "sql_to_sao": 0.60,
    "win_rate": 0.20,
    "sales_cycle_days": 90,
    "capture_share": 0.60,
    "cost_per_mql_capture": 300,
    "cost_per_mql_creation": 450,
    "channels": ["Google Ads", "Microsoft Ads", "LinkedIn Ads"],
    "crm": "HubSpot",
    "competitors": [],
    "icp": "",
}
LABELS = {
    "company": "company name",
    "months": "period length",
    "start_date": "start date",
    "motion": "motion",
    "mql_to_sql": "MQL to SQL rate",
    "sql_to_sao": "SQL to SAO rate",
    "win_rate": "win rate",
    "sales_cycle_days": "sales cycle",
    "capture_share": "capture/creation split",
    "cost_per_mql_capture": "capture cost per MQL",
    "cost_per_mql_creation": "creation cost per MQL",
    "channels": "channels",
    "crm": "CRM",
    "competitors": "competitors",
    "icp": "ICP",
}
NUMERIC = ("mql_to_sql", "sql_to_sao", "win_rate", "sales_cycle_days", "capture_share", "cost_per_mql_capture", "cost_per_mql_creation")
# A channel counts as demand capture if its name contains one of these; everything else is creation.
CAPTURE_WORDS = ("google", "microsoft", "bing", "search", "seo", "aeo", "geo", "g2", "capterra", "review")
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def empty(v):
    return v is None or v == "" or v == [] or v == {}


def next_monday(today=None):
    today = today or dt.date.today()
    return today + dt.timedelta(days=(7 - today.weekday()) % 7 or 7)


def resolve(raw):
    """Merge inputs over defaults and record which values are defaults."""
    if empty(raw.get("pipeline_goal")) and empty(raw.get("revenue_goal")):
        raise ValueError("Enter a pipeline_goal (or a revenue_goal).")
    if empty(raw.get("deal_size")):
        raise ValueError("Enter deal_size (average first-year deal value).")
    inp = dict(DEFAULTS)
    inp.update({k: v for k, v in raw.items() if not empty(v)})
    inp["defaulted"] = [k for k in DEFAULTS if empty(raw.get(k))]
    for k in ("mql_to_sql", "sql_to_sao", "win_rate", "capture_share"):
        v = float(inp[k])
        inp[k] = v / 100 if v > 1 else v  # accept 25 or 0.25
    for k in ("pipeline_goal", "revenue_goal", "deal_size", "cost_per_mql_capture", "cost_per_mql_creation"):
        if not empty(inp.get(k)):
            inp[k] = float(inp[k])
    inp["months"] = int(inp["months"])
    inp["sales_cycle_days"] = int(inp["sales_cycle_days"])
    for k in ("channels", "competitors"):
        if isinstance(inp[k], str):
            inp[k] = [c.strip() for c in inp[k].split(",") if c.strip()]
    start = inp["start_date"]
    inp["start_date"] = dt.date.fromisoformat(start) if start else next_monday()
    return inp


def channel_type(name):
    n = name.lower()
    return "capture" if any(w in n for w in CAPTURE_WORDS) else "creation"


def compute(inp):
    """Work back from the goal. A pipeline goal wins over a revenue goal when both are given."""
    if empty(inp.get("pipeline_goal")):
        pipeline = inp["revenue_goal"] / inp["win_rate"]
    else:
        pipeline = inp["pipeline_goal"]
    saos = pipeline / inp["deal_size"]
    sqls = saos / inp["sql_to_sao"]
    mqls = sqls / inp["mql_to_sql"]
    cap, cre = inp["capture_share"], 1 - inp["capture_share"]
    # Budget split by share, each part buying MQLs at its own cost: MQLs = B*cap/cc + B*cre/cr.
    blended = 1 / (cap / inp["cost_per_mql_capture"] + cre / inp["cost_per_mql_creation"])
    budget = mqls * blended
    m = {
        "pipeline_goal": pipeline,
        "revenue": pipeline * inp["win_rate"],
        "saos": saos,
        "sqls": sqls,
        "mqls": mqls,
        "closed_won": saos * inp["win_rate"],
        "budget": budget,
        "capture_budget": budget * cap,
        "creation_budget": budget * cre,
        "capture_mqls": budget * cap / inp["cost_per_mql_capture"],
        "creation_mqls": budget * cre / inp["cost_per_mql_creation"],
    }
    m["monthly"] = {k: v / inp["months"] for k, v in m.items()}
    m["blended_cost_per_mql"] = blended
    m["cost_per_sao"] = budget / saos
    m["pipeline_to_spend"] = pipeline / budget
    return m


def channel_plan(inp, m):
    """Each channel gets an equal share of its group's budget unless channel_shares says otherwise."""
    shares = inp.get("channel_shares") or {}
    rows = []
    for group, gbudget in (("capture", m["capture_budget"]), ("creation", m["creation_budget"])):
        names = [c for c in inp["channels"] if channel_type(c) == group]
        for c in names:
            share = float(shares[c]) if c in shares else 1 / len(names)
            share = share / 100 if share > 1 else share
            rows.append((c, group, share, gbudget * share))
    return rows


def labels(inp):
    if str(inp["motion"]).lower().startswith("product"):
        return {"MQL": "Signup", "SQL": "PQL", "MQLs": "Signups", "SQLs": "PQLs", "sql_meaning": "product-qualified"}
    return {"MQL": "MQL", "SQL": "SQL", "MQLs": "MQLs", "SQLs": "SQLs", "sql_meaning": "meeting scheduled"}


def half_up(x, places=0):
    """Round half up (62.5 -> 63), the way JavaScript's Math.round does, so the MCP server matches."""
    return Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)


def money(x):
    return f"${half_up(x):,.0f}"


def count(x):
    return f"{half_up(x):,.0f}" if x >= 10 else f"{half_up(x, 1):,.1f}"


def pct(x):
    return f"{half_up(x * 100):.0f}%"


def num(x):
    """Write 30000 not 30000.0, matching the MCP server."""
    return int(x) if float(x).is_integer() else x


def month_label(start, i):
    y, mo = divmod(start.month - 1 + i, 12)
    return f"{MONTHS[mo]} {start.year + y}"


def fields(inp, m):
    """Everything a template can reference as {{name}}."""
    lab = labels(inp)
    d = set(inp["defaulted"])
    note = lambda k: " (default)" if k in d else ""
    numeric_defaults = [LABELS[k] for k in inp["defaulted"] if k in NUMERIC]
    chans = channel_plan(inp, m)
    channel_rows = "\n".join(f"| {c} | {g} | {pct(s)} of {g} | {money(b)} | {money(b / inp['months'])} |" for c, g, s, b in chans)
    f = {
        "company": inp["company"],
        "period": f"{inp['months']} months from {month_label(inp['start_date'], 0)}" + note("months"),
        "months": str(inp["months"]),
        "start_date": inp["start_date"].isoformat(),
        "motion": inp["motion"],
        "crm": inp["crm"] + note("crm"),
        "channels": ", ".join(inp["channels"]) + note("channels"),
        "channel_rows": channel_rows or "| No channels entered | | | | |",
        "competitors": ", ".join(inp["competitors"]) or "None entered",
        "icp": inp["icp"] or "Not entered",
        "pipeline_goal": money(m["pipeline_goal"]),
        "revenue": money(m["revenue"]),
        "deal_size": money(inp["deal_size"]),
        "mql_to_sql": pct(inp["mql_to_sql"]) + note("mql_to_sql"),
        "sql_to_sao": pct(inp["sql_to_sao"]) + note("sql_to_sao"),
        "win_rate": pct(inp["win_rate"]) + note("win_rate"),
        "sales_cycle_days": f"{inp['sales_cycle_days']} days" + note("sales_cycle_days"),
        "capture_share": pct(inp["capture_share"]) + note("capture_share"),
        "creation_share": pct(1 - inp["capture_share"]) + note("capture_share"),
        "cost_per_mql_capture": money(inp["cost_per_mql_capture"]) + note("cost_per_mql_capture"),
        "cost_per_mql_creation": money(inp["cost_per_mql_creation"]) + note("cost_per_mql_creation"),
        "saos": count(m["saos"]),
        "sqls": count(m["sqls"]),
        "mqls": count(m["mqls"]),
        "capture_mqls": count(m["capture_mqls"]),
        "creation_mqls": count(m["creation_mqls"]),
        "closed_won": count(m["closed_won"]),
        "blended_cost_per_mql": money(m["blended_cost_per_mql"]),
        "budget": money(m["budget"]),
        "capture_budget": money(m["capture_budget"]),
        "creation_budget": money(m["creation_budget"]),
        "cost_per_sao": money(m["cost_per_sao"]),
        "pipeline_to_spend": f"{half_up(m['pipeline_to_spend'], 1):.1f}x",
        "monthly_budget": money(m["monthly"]["budget"]),
        "monthly_mqls": count(m["monthly"]["mqls"]),
        "monthly_sqls": count(m["monthly"]["sqls"]),
        "monthly_saos": count(m["monthly"]["saos"]),
        "monthly_closed_won": count(m["monthly"]["closed_won"]),
        "monthly_pipeline": money(m["monthly"]["pipeline_goal"]),
        "defaults_used": ", ".join(numeric_defaults) or "none",
    }
    f.update(lab)
    return f


def render(text, f):
    def sub(mt):
        key = mt.group(1)
        if key not in f:
            raise KeyError(f"Template asks for {{{{{key}}}}}, which isn't a known field.")
        return f[key]
    return re.sub(r"\{\{(\w+)\}\}", sub, text)


def to_csv(rows):
    out = io.StringIO()
    csv.writer(out, lineterminator="\r\n").writerows(rows)
    return out.getvalue()


def src(inp, key):
    return "default (rule of thumb)" if key in inp["defaulted"] else "yours"


def budget_tracker_csv(inp, m):
    """A sheet that stays live: inputs at the top, every plan number is a formula.
    Format the rate cells as percentages after import."""
    lab = labels(inp)
    rows, at = [], {}

    def add(row, name=None):
        rows.append(row)
        if name:
            at[name] = len(rows)
        return len(rows)

    B = lambda name: f"B{at[name]}"
    C = lambda name: f"C{at[name]}"
    add(["Budget tracker", inp["company"], ""])
    add(["Inputs", "Value", "Source"])
    rev_given = not empty(inp.get("revenue_goal"))
    add(["Revenue goal", num(inp["revenue_goal"]) if rev_given else "", "yours" if rev_given else "optional"], "revenue_goal")
    add(["SAO → Closed won (win rate)", inp["win_rate"], src(inp, "win_rate")], "win")
    if empty(inp.get("pipeline_goal")):
        add(["Pipeline goal", f"={B('revenue_goal')}/{B('win')}", "revenue goal ÷ win rate"], "pipe")
    else:
        add(["Pipeline goal", num(inp["pipeline_goal"]), "yours (wins over a revenue goal)"], "pipe")
    add(["Average deal size", num(inp["deal_size"]), "yours"], "deal")
    add(["Months in period", inp["months"], src(inp, "months")], "months")
    add(["Start date", inp["start_date"].isoformat(), src(inp, "start_date")])
    add([f"{lab['MQL']} → {lab['SQL']}", inp["mql_to_sql"], src(inp, "mql_to_sql")], "m2s")
    add([f"{lab['SQL']} → SAO", inp["sql_to_sao"], src(inp, "sql_to_sao")], "s2o")
    add(["Capture share of budget", inp["capture_share"], src(inp, "capture_share")], "cap")
    add(["Creation share of budget", f"=1-{B('cap')}", "formula"], "cre")
    add([f"Cost per {lab['MQL']}, capture", num(inp["cost_per_mql_capture"]), src(inp, "cost_per_mql_capture")], "cc")
    add([f"Cost per {lab['MQL']}, creation", num(inp["cost_per_mql_creation"]), src(inp, "cost_per_mql_creation")], "cr")
    add(["", "", ""])
    add(["Plan (worked back from the goal)", "Total", "Per month"])
    M = f"$B${at['months']}"
    add(["SAOs needed", f"={B('pipe')}/{B('deal')}", ""], "saos")
    add([f"{lab['SQLs']} needed", f"={B('saos')}/{B('s2o')}", ""], "sqls")
    add([f"{lab['MQLs']} needed", f"={B('sqls')}/{B('m2s')}", ""], "mqls")
    add([f"Blended cost per {lab['MQL']}", f"=1/({B('cap')}/{B('cc')}+{B('cre')}/{B('cr')})", ""], "blend")
    add(["Budget", f"={B('mqls')}*{B('blend')}", ""], "budget")
    add(["Capture budget", f"={B('budget')}*{B('cap')}", ""], "capb")
    add(["Creation budget", f"={B('budget')}*{B('cre')}", ""], "creb")
    add([f"Capture {lab['MQLs']}", f"={B('capb')}/{B('cc')}", ""], "capm")
    add([f"Creation {lab['MQLs']}", f"={B('creb')}/{B('cr')}", ""], "crem")
    add(["Expected closed-won revenue", f"={B('pipe')}*{B('win')}", ""], "rev")
    add(["Cost per SAO", f"={B('budget')}/{B('saos')}", ""], "cps")
    add(["Pipeline to spend", f"={B('pipe')}/{B('budget')}", ""])
    for name in ("saos", "sqls", "mqls", "budget", "capb", "creb", "capm", "crem", "rev"):
        rows[at[name] - 1][2] = f"={B(name)}/{M}"
    add(["", "", ""])
    add(["Budget by channel", "Type", "Share of its group", "Budget", "Per month"])
    chans = channel_plan(inp, m)
    if not chans:
        add(["No channels entered", "", "", "", ""])
    for c, g, s, _ in chans:
        r = len(rows) + 1
        group = B("capb") if g == "capture" else B("creb")
        add([c, g, num(round(s, 4)), f"={group}*C{r}", f"=D{r}/{M}"])
    add(["", "", ""])
    add(["Month", "Planned spend", "Actual spend", "Spend vs plan", f"Planned {lab['MQLs']}", f"Actual {lab['MQLs']}",
         f"Planned {lab['SQLs']}", f"Actual {lab['SQLs']}", "Planned SAOs", "Actual SAOs", "Actual cost per SAO",
         "Planned pipeline", "Actual sourced pipeline", "Pipeline vs plan",
         "Influenced pipeline, creation (lower confidence; not added to sourced)", "Planned cost per SAO", "Cost per SAO vs plan"])
    first = len(rows) + 1
    for i in range(inp["months"]):
        r = first + i
        add([month_label(inp["start_date"], i), f"=$C${at['budget']}", "", f'=IF(C{r}="","",C{r}/B{r}-1)',
             f"=$C${at['mqls']}", "", f"=$C${at['sqls']}", "", f"=$C${at['saos']}", "",
             f'=IF(OR(C{r}="",J{r}="",J{r}=0),"",C{r}/J{r})', f"={B('pipe')}/{M}",
             "", f'=IF(M{r}="","",M{r}/L{r}-1)', "", f"=$B${at['cps']}", f'=IF(K{r}="","",K{r}/P{r}-1)'])
    last = first + inp["months"] - 1
    rng = lambda c: f"{c}{first}:{c}{last}"
    t = len(rows) + 1
    add(["Total", f"=SUM({rng('B')})", f"=SUM({rng('C')})",
         f'=IF(COUNT({rng("C")})=0,"",SUM({rng("C")})/SUMIF({rng("C")},"<>",{rng("B")})-1)',
         f"=SUM({rng('E')})", f"=SUM({rng('F')})", f"=SUM({rng('G')})", f"=SUM({rng('H')})",
         f"=SUM({rng('I')})", f"=SUM({rng('J')})", f'=IF(J{t}=0,"",C{t}/J{t})',
         f"=SUM({rng('L')})", f"=SUM({rng('M')})",
         f'=IF(COUNT({rng("M")})=0,"",SUM({rng("M")})/SUMIF({rng("M")},"<>",{rng("L")})-1)',
         f"=SUM({rng('O')})", f"=$B${at['cps']}", f'=IF(K{t}="","",K{t}/P{t}-1)'])
    add(["", "", ""])
    add(["Notes", "Variance columns compare actuals only against the months that have actuals. Influenced pipeline is shown, never added to sourced pipeline. Format the rate cells (B4, B9-B12) as percentages.", ""])
    return to_csv(rows)


def recurring_tasks_csv(inp):
    """The task list with a first due date per task, from the start date."""
    start = inp["start_date"]
    nxt = lambda months: _first_monday(start, months)
    first_due = {"Daily": start, "Weekly": start, "Monthly": nxt(1), "Quarterly": nxt(3), "Yearly": nxt(12)}
    rows = list(csv.reader(io.StringIO((TEMPLATES / "recurring-tasks.csv").read_text())))
    head = rows[0]
    off = head.index("Due offset (days)")
    keep = [i for i in range(len(head)) if i != off]
    out = [head[:2] + ["Description", "First due"] + [head[i] for i in keep[2:]]]
    sec = head.index("Playbook section")
    for r in rows[1:]:
        cadence = r[head.index("Cadence")]
        slug = SECTION_FILES.get(r[sec][:2], "")
        desc = f"From the playbook's operating rhythm. How: {REPO}/playbook/{slug}" if slug else "From the playbook's operating rhythm."
        due = first_due[cadence] + dt.timedelta(days=int(r[off] or 0))
        out.append(r[:2] + [desc, due.isoformat()] + [r[i] for i in keep[2:]])
    return to_csv(out)


def _first_monday(start, months_ahead):
    y, mo = divmod(start.month - 1 + months_ahead, 12)
    d = dt.date(start.year + y, mo + 1, 1)
    return d + dt.timedelta(days=(7 - d.weekday()) % 7)


SECTION_FILES = {
    "01": "01-principles.md", "02": "02-align-to-the-business.md", "03": "03-measurement.md",
    "04": "04-demand-capture.md", "05": "05-demand-creation.md", "06": "06-budget.md",
    "07": "07-experimentation.md", "08": "08-reporting-and-communication.md", "09": "09-operating-rhythm.md",
    "10": "10-operations-and-ai.md", "11": "11-cross-channel-and-working-with-others.md", "12": "12-whats-new.md",
}


def fill_deck(f, path):
    """Write a filled slide-template.pptx if python-pptx is installed. Returns True if written."""
    try:
        sys.path.insert(0, str(HERE / "scripts"))
        from build_slide_template import build  # noqa: E402
    except ImportError:
        return False
    build(path, f)
    return True


def plan(inp, outdir):
    m = compute(inp)
    f = fields(inp, m)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    for name in ("planning-doc.md", "regular-updates.md", "planning-and-review-decks.md", "slide-template.md"):
        (outdir / name).write_text(render((TEMPLATES / name).read_text(), f))
    (outdir / "experiment-database.csv").write_text((TEMPLATES / "experiment-database.csv").read_text())
    (outdir / "recurring-tasks.csv").write_text(recurring_tasks_csv(inp))
    (outdir / "budget-tracker.csv").write_text(budget_tracker_csv(inp, m))
    fill_deck(f, outdir / "slide-template.pptx")
    return sorted(p.name for p in outdir.iterdir())


def calibrate(path):
    """Back-test: how close were predicted lifts to actual lifts, by Confidence and by Impact score?"""
    rows = list(csv.DictReader(open(path, newline="")))
    done = []
    for r in rows:
        try:
            pred = float(str(r["Predicted lift %"]).strip("%"))
            act = float(str(r["Actual lift %"]).strip("%"))
            conf = float(r["Confidence (1-10)"])
            imp = float(r["Impact (1-10)"])
        except (KeyError, ValueError):
            continue
        won = str(r.get("Significant?", "")).strip().lower() in ("yes", "y", "true") and (act > 0) == (pred > 0)
        done.append((conf, imp, pred, act, won))
    if not done:
        return "No finished tests yet: fill in Predicted lift % and Actual lift % to back-test your scores."
    lines = [f"Finished tests with a prediction and a result: {len(done)}"]
    bands = (("1-4", 0, 5), ("5-7", 5, 8), ("8-10", 8, 11))  # lower bound inclusive, upper exclusive
    for label, idx in (("Confidence", 0), ("Impact", 1)):
        for name, lo, hi in bands:
            b = [d for d in done if lo <= d[idx] < hi]
            if not b:
                continue
            err = sum(d[3] - d[2] for d in b) / len(b)
            won = sum(1 for d in b if d[4]) / len(b)
            avg = sum(d[3] for d in b) / len(b)
            lines.append(f"{label} {name}: {len(b)} tests, won {won:.0%} (significant, in the predicted direction), "
                         f"average actual lift {avg:+.1f}%, actual minus predicted {err:+.1f} points")
    if len(done) < 10:
        lines.append("Fewer than 10 finished tests: treat this as a first read, not a calibration.")
    lines.append("Lift is signed as entered: for a metric where lower is better (like cost per SAO), enter a fall as a positive lift.")
    lines.append("Higher Confidence should win more often, and higher Impact should lift more. If not, score lower until it does.")
    return "\n".join(lines)


def main(argv):
    if len(argv) < 3 or argv[1] not in ("math", "plan", "calibrate"):
        print(__doc__)
        return 1
    if argv[1] == "calibrate":
        print(calibrate(argv[2]))
        return 0
    inp = resolve(json.load(open(argv[2])))
    if argv[1] == "math":
        m = compute(inp)
        print(json.dumps({k: round(v, 2) for k, v in m.items() if k != "monthly"}, indent=2))
        print("Per month:", json.dumps({k: round(v, 2) for k, v in m["monthly"].items()}))
        print("Budget by channel:", json.dumps([(c, g, round(s, 4), round(b, 2)) for c, g, s, b in channel_plan(inp, m)]))
        print("Defaults used:", ", ".join(LABELS[k] for k in inp["defaulted"]) or "none")
        return 0
    out = argv[argv.index("--out") + 1] if "--out" in argv else "out"
    print("Wrote:", ", ".join(plan(inp, out)), "to", out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
