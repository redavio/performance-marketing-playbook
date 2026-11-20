import type { Results } from "../types";
import Cards from "./Cards";
import { count, money, showInput, ui } from "./ui";

/** The pipeline goal worked back to the budget you need, and the inputs behind it. */
export default function PlanView({ res }: { res: Results }) {
  const p = res.plan;
  return (
    <section className="overflow-x-auto">
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
        <p className={ui.help}>Worked back from the goal, through demand capture only. Demand creation is a set share of budget on top, never counted toward the goal.</p>
        <table className={ui.table}>
          <thead><tr>{["Step", "Total", "Per month", "How"].map((h) => <th key={h} className={ui.th}>{h}</th>)}</tr></thead>
          <tbody>
            {res.funnel.map((f) => {
              const dollars = !["saos", "sqls", "mqls"].includes(f.key);
              const td = `${ui.td} ${f.key === "budget" ? ui.total : ""}`;
              return (
                <tr key={f.key}>
                  <td className={td}>{f.label}</td>
                  <td className={td}>{dollars ? money(f.total) : count(f.total)}</td>
                  <td className={td}>{dollars ? money(f.per_month) : count(f.per_month)}</td>
                  <td className={`${ui.cell} ${ui.muted}`}>{f.how}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
      <h2 className={ui.h2}>Inputs</h2>
      <p className={ui.help}>Replace a default with your own number once you have three months of data, then run fill.py again.</p>
      <table className={ui.table}>
        <thead><tr>{["Input", "Value", "Source"].map((h) => <th key={h} className={ui.th}>{h}</th>)}</tr></thead>
        <tbody>
          {res.inputs.map((i) => (
            <tr key={i.key}>
              <td className={ui.td}>{i.label[0].toUpperCase() + i.label.slice(1)}</td>
              <td className={ui.cell}>{showInput(i)}</td>
              <td className={ui.td}>{i.default ? <span className={ui.tag}>default</span> : i.value === null || i.value === "" ? "–" : "yours"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}
