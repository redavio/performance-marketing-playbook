import type { Results } from "../types";
import Cards from "./Cards";
import { count, money, pct, ui } from "./ui";

/** The budget split by channel, capture and creation, then by month. */
export default function BudgetView({ res }: { res: Results }) {
  const p = res.plan;
  const chans = res.budget.channels;
  const l = res.labels;
  return (
    <section className="overflow-x-auto">
      <div data-shot="2">
        <Cards
          cards={[
            ["Budget", money(p.budget), `${money(res.monthly.budget)} a month`],
            ["Demand capture", money(p.capture_budget), `${money(res.monthly.capture_budget)} a month, counted toward the goal`],
            ["Demand creation", money(p.creation_budget), `${money(res.monthly.creation_budget)} a month, on top`],
          ]}
        />
        <table className={ui.table}>
          <thead><tr>{["Channel", "Type", "Share of its group", "", "Budget", "Per month"].map((h, i) => <th key={i} className={ui.th}>{h}</th>)}</tr></thead>
          <tbody>
            {chans.map((c) => (
              <tr key={c.channel}>
                <td className={ui.td}>{c.channel}</td>
                <td className={ui.td}>{c.type}</td>
                <td className={ui.td}>{pct(c.share_of_group)}</td>
                <td className={`${ui.td} w-1/4 min-w-[120px]`}>
                  <svg className="block h-2 w-full" aria-hidden="true">
                    <rect width="100%" height="100%" rx="4" className="fill-zinc-100 dark:fill-zinc-800" />
                    <rect width={pct(c.share_of_group)} height="100%" rx="4" className="fill-brand" />
                  </svg>
                </td>
                <td className={ui.td}>{money(c.total)}</td>
                <td className={ui.td}>{money(c.per_month)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <h2 className={ui.h2}>By month</h2>
      <p className={ui.help}>The plan per month. Put actuals next to it in the budget tracker sheet.</p>
      <table className={ui.table}>
        <thead>
          <tr>
            {["Month", "Spend", ...chans.map((c) => c.channel), l.MQLs, l.SQLs, "SAOs", "Pipeline"].map((h) => <th key={h} className={ui.th}>{h}</th>)}
          </tr>
        </thead>
        <tbody>
          {res.budget.months.map((m) => (
            <tr key={m.month}>
              <td className={ui.td}>{m.month}</td>
              <td className={ui.td}>{money(m.spend)}</td>
              {chans.map((c) => <td key={c.channel} className={ui.td}>{money(m.by_channel[c.channel])}</td>)}
              <td className={ui.td}>{count(m.mqls)}</td>
              <td className={ui.td}>{count(m.sqls)}</td>
              <td className={ui.td}>{count(m.saos)}</td>
              <td className={ui.td}>{money(m.pipeline)}</td>
            </tr>
          ))}
          <tr className={ui.total}>
            <td className={ui.td}>Total</td>
            <td className={ui.td}>{money(p.budget)}</td>
            {chans.map((c) => <td key={c.channel} className={ui.td}>{money(c.total)}</td>)}
            <td className={ui.td}>{count(p.mqls)}</td>
            <td className={ui.td}>{count(p.sqls)}</td>
            <td className={ui.td}>{count(p.saos)}</td>
            <td className={ui.td}>{money(p.pipeline_goal)}</td>
          </tr>
        </tbody>
      </table>
    </section>
  );
}
