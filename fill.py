#!/usr/bin/env python3
"""Fill the Performance Marketing Playbook deliverables from a company's inputs.

Standard library only. The math matches deliverables/defaults.md, the budget tracker
formulas and the Redavio MCP server, so all three give the same numbers.

    python3 fill.py math inputs.json            # print the plan numbers
    python3 fill.py plan inputs.json --out out  # write every deliverable, filled in
    python3 fill.py calibrate experiments.csv   # back-test ICS scores against results

inputs.json needs pipeline_goal (or revenue_goal) and deal_size. Everything else is
optional; see DEFAULTS below or deliverables/defaults.md.
"""
import csv
import io
import json
import re
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATES = HERE / "deliverables"

DEFAULTS = {
    "company": "Your company",
    "months": 12,
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
REQUIRED = ("deal_size",)


def resolve(raw):
    """Merge inputs over defaults and record which values are defaults."""
    if not raw.get("pipeline_goal") and not raw.get("revenue_goal"):
        raise ValueError("Enter a pipeline_goal (or a revenue_goal).")
    for key in REQUIRED:
        if not raw.get(key):
            raise ValueError(f"Enter {key}.")
    inp = dict(DEFAULTS)
    inp.update({k: v for k, v in raw.items() if v not in (None, "", [])})
    inp["defaulted"] = sorted(k for k in DEFAULTS if k not in raw or raw.get(k) in (None, "", []))
    for k in ("mql_to_sql", "sql_to_sao", "win_rate", "capture_share"):
        v = float(inp[k])
        inp[k] = v / 100 if v > 1 else v  # accept 25 or 0.25
    for k in ("pipeline_goal", "revenue_goal", "deal_size", "cost_per_mql_capture", "cost_per_mql_creation"):
        if inp.get(k) is not None:
            inp[k] = float(inp[k])
    inp["months"] = int(inp["months"])
    if isinstance(inp["channels"], str):
        inp["channels"] = [c.strip() for c in inp["channels"].split(",") if c.strip()]
    if isinstance(inp["competitors"], str):
        inp["competitors"] = [c.strip() for c in inp["competitors"].split(",") if c.strip()]
    return inp


def compute(inp):
    """Work back from the goal. Returns totals; monthly = total / months."""
    if inp.get("revenue_goal") and not inp.get("pipeline_goal"):
        pipeline = inp["revenue_goal"] / inp["win_rate"]
    else:
        pipeline = inp["pipeline_goal"]
    saos = pipeline / inp["deal_size"]
    sqls = saos / inp["sql_to_sao"]
    mqls = sqls / inp["mql_to_sql"]
    cap, cre = inp["capture_share"], 1 - inp["capture_share"]
    blended = inp["cost_per_mql_capture"] * cap + inp["cost_per_mql_creation"] * cre
    budget = mqls * blended
    m = {
        "pipeline_goal": pipeline,
        "revenue": inp.get("revenue_goal") or pipeline * inp["win_rate"],
        "saos": saos,
        "sqls": sqls,
        "mqls": mqls,
        "closed_won": saos * inp["win_rate"],
        "blended_cost_per_mql": blended,
        "budget": budget,
        "capture_budget": budget * cap,
        "creation_budget": budget * cre,
        "cost_per_sao": budget / saos,
        "pipeline_to_spend": pipeline / budget,
    }
    m["monthly"] = {k: v / inp["months"] for k, v in m.items() if k not in ("blended_cost_per_mql", "cost_per_sao", "pipeline_to_spend")}
    return m


def labels(inp):
    if str(inp["motion"]).lower().startswith("product"):
        return {"MQL": "Signup", "SQL": "PQL", "MQLs": "Signups", "SQLs": "PQLs"}
    return {"MQL": "MQL", "SQL": "SQL", "MQLs": "MQLs", "SQLs": "SQLs"}


def half_up(x, places=0):
    """Round half up (62.5 -> 63), the way JavaScript's Math.round does, so the MCP server matches."""
    q = Decimal(1).scaleb(-places)
    return Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP)


def money(x):
    return f"${half_up(x):,.0f}"


def count(x):
    return f"{half_up(x):,.0f}" if x >= 10 else f"{half_up(x, 1):,.1f}"


def pct(x):
    return f"{half_up(x * 100):.0f}%"


def fields(inp, m):
    """Everything a template can reference as {{name}}."""
    lab = labels(inp)
    d = set(inp["defaulted"])
    note = lambda k: " (default)" if k in d else ""
    f = {
        "company": inp["company"],
        "period": f"{inp['months']} months",
        "months": str(inp["months"]),
        "motion": inp["motion"],
        "crm": inp["crm"] + note("crm"),
        "channels": ", ".join(inp["channels"]) + note("channels"),
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
        "closed_won": count(m["closed_won"]),
        "blended_cost_per_mql": money(m["blended_cost_per_mql"]),
        "budget": money(m["budget"]),
        "capture_budget": money(m["capture_budget"]),
        "creation_budget": money(m["creation_budget"]),
        "cost_per_sao": money(m["cost_per_sao"]),
        "pipeline_to_spend": f"{half_up(m['pipeline_to_spend'], 1):.1f}x",
        "monthly_budget": money(m["monthly"]["budget"]),
        "monthly_mqls": count(m["monthly"]["mqls"]),
        "monthly_saos": count(m["monthly"]["saos"]),
        "monthly_pipeline": money(m["monthly"]["pipeline_goal"]),
        "defaults_used": ", ".join(inp["defaulted"]) or "none",
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


def budget_tracker_csv(inp, m):
    """A sheet that stays live: inputs at the top, every plan number is a formula."""
    lab = labels(inp)
    rows = [
        ["Budget tracker", inp["company"], ""],
        ["Inputs", "Value", "Source"],
        ["Pipeline goal", round(m["pipeline_goal"]), "yours" if inp.get("pipeline_goal") else "revenue goal ÷ win rate"],  # B3
        ["Average deal size", num(inp["deal_size"]), "yours"],  # B4
        ["Months in period", inp["months"], src(inp, "months")],  # B5
        [f"{lab['MQL']} → {lab['SQL']}", inp["mql_to_sql"], src(inp, "mql_to_sql")],  # B6
        [f"{lab['SQL']} → SAO", inp["sql_to_sao"], src(inp, "sql_to_sao")],  # B7
        ["SAO → Closed won (win rate)", inp["win_rate"], src(inp, "win_rate")],  # B8
        ["Capture share of budget", inp["capture_share"], src(inp, "capture_share")],  # B9
        ["Creation share of budget", "=1-B9", "formula"],  # B10
        [f"Cost per {lab['MQL']}, capture", num(inp["cost_per_mql_capture"]), src(inp, "cost_per_mql_capture")],  # B11
        [f"Cost per {lab['MQL']}, creation", num(inp["cost_per_mql_creation"]), src(inp, "cost_per_mql_creation")],  # B12
        ["", "", ""],
        ["Plan (worked back from the goal)", "Total", "Per month"],  # 14
        ["SAOs needed", "=B3/B4", "=B15/$B$5"],  # 15
        [f"{lab['SQLs']} needed", "=B15/B7", "=B16/$B$5"],  # 16
        [f"{lab['MQLs']} needed", "=B16/B6", "=B17/$B$5"],  # 17
        [f"Blended cost per {lab['MQL']}", "=B11*B9+B12*B10", ""],  # 18
        ["Budget", "=B17*B18", "=B19/$B$5"],  # 19
        ["Capture budget", "=B19*B9", "=B20/$B$5"],  # 20
        ["Creation budget", "=B19*B10", "=B21/$B$5"],  # 21
        ["Expected closed-won revenue", "=B3*B8", "=B22/$B$5"],  # 22
        ["Cost per SAO", "=B19/B15", ""],  # 23
        ["Pipeline to spend", "=B3/B19", ""],  # 24
        ["", "", ""],
    ]
    head = ["Month", "Planned spend", "Actual spend", f"Planned {lab['MQLs']}", f"Actual {lab['MQLs']}",
            f"Planned {lab['SQLs']}", f"Actual {lab['SQLs']}", "Planned SAOs", "Actual SAOs", "Planned pipeline",
            "Actual pipeline, capture", "Actual pipeline, creation (lower confidence)", "Pipeline vs plan"]
    rows.append(head)  # row 26
    first = len(rows) + 1
    for i in range(inp["months"]):
        r = first + i
        rows.append([f"Month {i + 1}", "=$C$19", "", "=$C$17", "", "=$C$16", "", "=$C$15", "",
                     "=$B$3/$B$5", "", "", f'=IF(K{r}="","",(K{r}+N(L{r}))/J{r}-1)'])
    last = first + inp["months"] - 1
    tot = len(rows) + 1
    rows.append(["Total"] + [f"=SUM({c}{first}:{c}{last})" for c in "BCDEFGHIJKL"] + [f'=IF(K{tot}=0,"",(K{tot}+L{tot})/J{tot}-1)'])
    rows.append(["", "", ""])
    rows.append(["Notes", "Creation's pipeline is credited from self-reported source and influenced pipeline. Treat it as lower confidence than capture's.", ""])
    out = io.StringIO()
    csv.writer(out).writerows(rows)
    return out.getvalue()


def num(x):
    """Write 30000 not 30000.0, matching the MCP server."""
    return int(x) if float(x).is_integer() else x


def src(inp, key):
    return "default (rule of thumb)" if key in inp["defaulted"] else "yours"


def plan(inp, outdir):
    m = compute(inp)
    f = fields(inp, m)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    for name in ("planning-doc.md", "regular-updates.md", "planning-and-review-decks.md", "slide-template.md"):
        (outdir / name).write_text(render((TEMPLATES / name).read_text(), f))
    for name in ("recurring-tasks.csv", "experiment-database.csv"):
        (outdir / name).write_text((TEMPLATES / name).read_text())
    (outdir / "budget-tracker.csv").write_text(budget_tracker_csv(inp, m))
    return sorted(p.name for p in outdir.iterdir())


def calibrate(path):
    """Back-test: how close were predicted lifts to actual lifts, by confidence score?"""
    rows = list(csv.DictReader(open(path, newline="")))
    done = []
    for r in rows:
        try:
            pred = float(str(r["Predicted lift %"]).strip("%"))
            act = float(str(r["Actual lift %"]).strip("%"))
            conf = float(r["Confidence (1-10)"])
        except (KeyError, ValueError):
            continue
        done.append((conf, pred, act))
    if not done:
        return "No finished tests yet: fill in Predicted lift % and Actual lift % to back-test your scores."
    lines = [f"Finished tests with a prediction and a result: {len(done)}"]
    bands = [("Confidence 1-4", 1, 4), ("Confidence 5-7", 5, 7), ("Confidence 8-10", 8, 10)]
    for name, lo, hi in bands:
        b = [(p, a) for c, p, a in done if lo <= c <= hi]
        if not b:
            continue
        err = sum(a - p for p, a in b) / len(b)
        hit = sum(1 for p, a in b if (p > 0) == (a > 0)) / len(b)
        lines.append(f"{name}: {len(b)} tests, actual minus predicted lift averages {err:+.1f} points, direction right {hit:.0%} of the time")
    if len(done) < 10:
        lines.append("Fewer than 10 finished tests: treat this as a first read, not a calibration.")
    lines.append("If high-confidence tests miss as often as low-confidence ones, score confidence lower until they don't.")
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
        print(json.dumps({k: (round(v, 2) if isinstance(v, float) else v) for k, v in m.items() if k != "monthly"}, indent=2))
        print("Per month:", json.dumps({k: round(v, 2) for k, v in m["monthly"].items()}))
        print("Defaults used:", ", ".join(inp["defaulted"]) or "none")
        return 0
    out = argv[argv.index("--out") + 1] if "--out" in argv else "out"
    print("Wrote:", ", ".join(plan(inp, out)), "to", out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
