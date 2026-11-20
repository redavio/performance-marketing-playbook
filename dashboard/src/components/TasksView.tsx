import { useState } from "react";
import type { Results } from "../types";
import { CADENCES, ui } from "./ui";

/** The operating rhythm: tasks with first due dates and playbook links. */
export default function TasksView({ res, initialCadence = "" }: { res: Results; initialCadence?: string }) {
  const [cadence, setCadence] = useState<string>((CADENCES as readonly string[]).includes(initialCadence) ? initialCadence : "");
  const rows = res.tasks.filter((t) => !cadence || t.cadence === cadence);
  return (
    <section className="overflow-x-auto" data-shot="3">
      <div className="mb-2 mt-4 flex flex-wrap gap-1.5">
        <button type="button" className={ui.pill(!cadence)} onClick={() => setCadence("")}>All ({res.tasks.length})</button>
        {CADENCES.map((c) => (
          <button key={c} type="button" className={ui.pill(cadence === c)} onClick={() => setCadence(c)}>
            {c} ({res.tasks.filter((t) => t.cadence === c).length})
          </button>
        ))}
      </div>
      <p className={ui.help}>The operating rhythm, with a first due date for each task from the start date. Import recurring-tasks.csv into ClickUp, Asana or Notion.</p>
      <table className={ui.table}>
        <thead><tr>{["Task", "Cadence", "First due", "Owner", "Playbook section"].map((h) => <th key={h} className={ui.th}>{h}</th>)}</tr></thead>
        <tbody>
          {rows.map((t) => {
            const link = t.how.match(/https?:\/\/\S+/)?.[0];
            return (
              <tr key={t.id}>
                <td className={`${ui.cell} min-w-[240px]`}>{t.name}</td>
                <td className={ui.td}>{t.recurrence}</td>
                <td className={ui.td}>{t.first_due}</td>
                <td className={ui.td}>{t.owner}</td>
                <td className={ui.td}>
                  {link ? <a href={link} target="_blank" rel="noreferrer" className="text-brand underline underline-offset-[3px]">{t.section}</a> : t.section}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </section>
  );
}
