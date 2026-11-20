import type { Input } from "../types";

// Formatting only: every number on screen comes from fill.py, which does all the math.
export const money = (n: number) => `$${Math.round(n).toLocaleString("en-US")}`;
export const count = (n: number) => (n >= 10 ? Math.round(n).toLocaleString("en-US") : (Math.round(n * 10) / 10).toFixed(1));
export const pct = (n: number) => `${Math.round(n * 100)}%`;
const RATES = ["mql_to_sql", "sql_to_sao", "win_rate", "creation_share"];
const DOLLARS = ["pipeline_goal", "revenue_goal", "deal_size", "cost_per_mql_capture"];
export const CADENCES = ["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"] as const;

export const showInput = (i: Input) => {
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

export const ui = {
  muted: "text-zinc-500 dark:text-zinc-400",
  help: "my-3 text-sm text-zinc-500 dark:text-zinc-400",
  h2: "mb-2 mt-6 text-lg font-semibold",
  table: "mb-4 mt-2 w-full border-collapse text-sm",
  th: "border-b border-zinc-200 px-2 py-2 text-left align-bottom font-medium text-zinc-500 dark:border-zinc-700 dark:text-zinc-400",
  td: "whitespace-nowrap border-b border-zinc-200 px-2 py-2 dark:border-zinc-700",
  cell: "border-b border-zinc-200 px-2 py-2 dark:border-zinc-700",
  total: "font-semibold",
  tag: "whitespace-nowrap rounded-full border border-zinc-200 px-1.5 py-px text-xs text-zinc-500 dark:border-zinc-700 dark:text-zinc-400",
  pill: (on: boolean) =>
    `rounded-full border px-3.5 py-1.5 text-sm ${
      on ? "border-brand bg-brand text-white" : "border-zinc-200 hover:bg-zinc-50 dark:border-zinc-700 dark:hover:bg-zinc-800"
    }`,
};
