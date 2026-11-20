import { ui } from "./ui";

/** A row of headline numbers. */
export default function Cards({ cards }: { cards: [string, string, string][] }) {
  return (
    <div className="my-5 grid grid-cols-[repeat(auto-fit,minmax(170px,1fr))] gap-3">
      {cards.map(([label, value, sub]) => (
        <div key={label} className="rounded-xl border border-zinc-200 p-3.5 dark:border-zinc-700">
          <div className={`text-xs ${ui.muted}`}>{label}</div>
          <div className="my-1 text-2xl font-semibold">{value}</div>
          <div className={`text-xs ${ui.muted}`}>{sub}</div>
        </div>
      ))}
    </div>
  );
}
