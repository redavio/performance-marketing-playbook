import { useEffect, useState } from "react";
import { BRAND } from "./brand";
import type { Input, Results, Task } from "./types";

// Formatting only: every number on screen comes from fill.py, which does all the math.
const money = (n: number) => `$${Math.round(n).toLocaleString("en-US")}`;
const count = (n: number) => (n >= 10 ? Math.round(n).toLocaleString("en-US") : (Math.round(n * 10) / 10).toFixed(1));
const pct = (n: number) => `${Math.round(n * 100)}%`;
const RATES = ["mql_to_sql", "sql_to_sao", "win_rate", "creation_share"];
const DOLLARS = ["pipeline_goal", "revenue_goal", "deal_size", "cost_per_mql_capture"];
const CADENCES = ["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"] as const;
const VIEWS = { plan: "Plan", budget: "Budget", tasks: "Tasks" } as const;
type View = keyof typeof VIEWS;

const params = new URLSearchParams(location.search);
const startView = (params.get("view") as View) in VIEWS ? (params.get("view") as View) : "plan";

export default function App() {
  const [res, setRes] = useState<Results | null>(null);
  const [error, setError] = useState("");
  const [view, setView] = useState<View>(startView);

  useEffect(() => {
    const src = params.get("src") || "results.json";
    fetch(src)
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(`Couldn't load ${src}.`))))
      .then(setRes)
      .catch((e) => setError(e.message));
  }, []);

  const open = (file: File) =>
    file.text().then((t) => {
      try {
        setRes(JSON.parse(t));
        setError("");
      } catch {
        setError("That file isn't a playbook results file.");
      }
    });

  return (
    <div className="page">
      <header>
        <div>
          <h1>{BRAND.logo && <img src={BRAND.logo} alt="" className="logo" />}{BRAND.name} <span className="muted">· {VIEWS[view]}</span></h1>
          {res && <p className="muted">{res.company}. {res.period}.</p>}
        </div>
        <label className="file">
          Open results file
          <input type="file" accept=".json" onChange={(e) => e.target.files?.[0] && open(e.target.files[0])} />
        </label>
      </header>
      {error && <p className="note">{error} Run fill.py with --json results.json, then open the file here.</p>}
      {res && (
        <>
          <nav>
            {(Object.keys(VIEWS) as View[]).map((v) => (
              <button key={v} className={view === v ? "on" : ""} onClick={() => setView(v)}>{VIEWS[v]}</button>
            ))}
          </nav>
          {view === "plan" && <Plan res={res} />}
          {view === "budget" && <Budget res={res} />}
          {view === "tasks" && <Tasks res={res} />}
        </>
      )}
    </div>
  );
}

function Cards({ cards }: { cards: [string, string, string][] }) {
  return (
    <div className="cards">
      {cards.map(([label, value, sub]) => (
        <div key={label} className="card">
          <div className="muted small">{label}</div>
          <div className="big">{value}</div>
          <div className="muted small">{sub}</div>
        </div>
      ))}
    </div>
  );
}

const showInput = (i: Input) => {
  if (i.value === null || i.value === "" || (Array.isArray(i.value) && !i.value.length)) return "–";
  if (Array.isArray(i.value)) return i.value.join(", ");
  if (typeof i.value === "number") {
    if (RATES.includes(i.key)) return pct(i.value);
    if (DOLLARS.includes(i.key)) return money(i.value);
    if (i.key === "months") return `${i.value} months`;
    if (i.key === "sales_cycle_days") return `${i.value} days`;
  }
  return String(i.value);
};

function Plan({ res }: { res: Results }) {
  const p = res.plan;
  return (
    <section>
      <div data-shot="1">
        <Cards
          cards={[
            ["Pipeline goal", money(p.pipeline_goal), `${count(p.saos)} SAOs`],
            ["Budget", money(p.budget), `${money(res.monthly.budget)} a month`],
            ["Cost per SAO", money(p.cost_per_sao), `${money(p.capture_cost_per_sao)} from capture alone`],
            ["Pipeline to spend", `${(Math.round(p.pipeline_to_spend * 10) / 10).toFixed(1)}x`, "pipeline per $1 spent"],
            ["Expected revenue", money(p.revenue), `${count(p.closed_won)} closed-won deals`],
          ]}
        />
        <p className="help">Worked back from the goal, through demand capture only. Demand creation is a set share of budget on top, never counted toward the goal.</p>
        <table className="funnel">
          <thead><tr><th>Step</th><th>Total</th><th>Per month</th><th>How</th></tr></thead>
          <tbody>
            {res.funnel.map((f) => {
              const dollars = !["saos", "sqls", "mqls"].includes(f.key);
              return (
                <tr key={f.key} className={f.key === "budget" ? "total" : ""}>
                  <td>{f.label}</td>
                  <td>{dollars ? money(f.total) : count(f.total)}</td>
                  <td>{dollars ? money(f.per_month) : count(f.per_month)}</td>
                  <td className="muted">{f.how}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
      <h2>Inputs</h2>
      <p className="help">Replace a default with your own number once you have three months of data, then run fill.py again.</p>
      <table>
        <thead><tr><th>Input</th><th>Value</th><th>Source</th></tr></thead>
        <tbody>
          {res.inputs.map((i) => (
            <tr key={i.key}>
              <td>{i.label[0].toUpperCase() + i.label.slice(1)}</td>
              <td className="wrap">{showInput(i)}</td>
              <td>{i.default ? <span className="tag">default</span> : i.value === null || i.value === "" ? "–" : "yours"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

function Budget({ res }: { res: Results }) {
  const p = res.plan;
  const chans = res.budget.channels;
  const l = res.labels;
  return (
    <section>
      <div data-shot="2">
        <Cards
          cards={[
            ["Budget", money(p.budget), `${money(res.monthly.budget)} a month`],
            ["Demand capture", money(p.capture_budget), `${money(res.monthly.capture_budget)} a month, counted toward the goal`],
            ["Demand creation", money(p.creation_budget), `${money(res.monthly.creation_budget)} a month, on top`],
          ]}
        />
        <table>
          <thead><tr><th>Channel</th><th>Type</th><th>Share of its group</th><th></th><th>Budget</th><th>Per month</th></tr></thead>
          <tbody>
            {chans.map((c) => (
              <tr key={c.channel}>
                <td>{c.channel}</td>
                <td>{c.type}</td>
                <td>{pct(c.share_of_group)}</td>
                <td><div className="bar"><span style={{ width: pct(c.share_of_group) }} /></div></td>
                <td>{money(c.total)}</td>
                <td>{money(c.per_month)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <h2>By month</h2>
      <p className="help">The plan per month. Put actuals next to it in the budget tracker sheet.</p>
      <table>
        <thead>
          <tr>
            <th>Month</th><th>Spend</th>{chans.map((c) => <th key={c.channel}>{c.channel}</th>)}
            <th>{l.MQLs}</th><th>{l.SQLs}</th><th>SAOs</th><th>Pipeline</th>
          </tr>
        </thead>
        <tbody>
          {res.budget.months.map((m) => (
            <tr key={m.month}>
              <td>{m.month}</td>
              <td>{money(m.spend)}</td>
              {chans.map((c) => <td key={c.channel}>{money(m.by_channel[c.channel])}</td>)}
              <td>{count(m.mqls)}</td><td>{count(m.sqls)}</td><td>{count(m.saos)}</td><td>{money(m.pipeline)}</td>
            </tr>
          ))}
          <tr className="total">
            <td>Total</td><td>{money(p.budget)}</td>
            {chans.map((c) => <td key={c.channel}>{money(c.total)}</td>)}
            <td>{count(p.mqls)}</td><td>{count(p.sqls)}</td><td>{count(p.saos)}</td><td>{money(p.pipeline_goal)}</td>
          </tr>
        </tbody>
      </table>
    </section>
  );
}

function Tasks({ res }: { res: Results }) {
  const fromUrl = params.get("cadence");
  const [cadence, setCadence] = useState<string>(CADENCES.includes(fromUrl as Task["cadence"]) ? (fromUrl as string) : "");
  const rows = res.tasks.filter((t) => !cadence || t.cadence === cadence);
  return (
    <section data-shot="3">
      <div className="toggle">
        <button className={!cadence ? "on" : ""} onClick={() => setCadence("")}>All ({res.tasks.length})</button>
        {CADENCES.map((c) => (
          <button key={c} className={cadence === c ? "on" : ""} onClick={() => setCadence(c)}>
            {c} ({res.tasks.filter((t) => t.cadence === c).length})
          </button>
        ))}
      </div>
      <p className="help">The operating rhythm, with a first due date for each task from the start date. Import recurring-tasks.csv into ClickUp, Asana or Notion.</p>
      <table>
        <thead><tr><th>Task</th><th>Cadence</th><th>First due</th><th>Owner</th><th>Playbook section</th></tr></thead>
        <tbody>
          {rows.map((t) => {
            const link = t.how.match(/https?:\/\/\S+/)?.[0];
            return (
              <tr key={t.id}>
                <td className="wrap">{t.name}</td>
                <td>{t.recurrence}</td>
                <td>{t.first_due}</td>
                <td>{t.owner}</td>
                <td>{link ? <a href={link} target="_blank" rel="noreferrer">{t.section}</a> : t.section}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </section>
  );
}
