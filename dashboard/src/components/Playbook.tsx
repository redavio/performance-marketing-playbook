import { useState } from "react";
import type { Results } from "../types";
import BudgetView from "./BudgetView";
import PlanView from "./PlanView";
import TasksView from "./TasksView";
import { ui } from "./ui";

export const VIEWS = { plan: "Plan", budget: "Budget", tasks: "Tasks" } as const;
export type View = keyof typeof VIEWS;

/**
 * The whole playbook screen for one results.json: a one-line summary, then Plan / Budget / Tasks.
 * Takes the result as props and loads nothing itself, so any app can render it (this repo's
 * dashboard reads results.json; a hosted app can pass the same object from its own API).
 */
export default function Playbook({
  res,
  initialView = "plan",
  initialCadence = "",
}: {
  res: Results;
  initialView?: View;
  initialCadence?: string;
}) {
  const [view, setView] = useState<View>(initialView);
  return (
    <div>
      <p className={`text-sm ${ui.muted}`}>{res.company}. {res.period}.</p>
      <nav className="mb-2 mt-4 flex flex-wrap gap-1.5">
        {(Object.keys(VIEWS) as View[]).map((v) => (
          <button key={v} type="button" className={ui.pill(view === v)} onClick={() => setView(v)}>{VIEWS[v]}</button>
        ))}
      </nav>
      {view === "plan" && <PlanView res={res} />}
      {view === "budget" && <BudgetView res={res} />}
      {view === "tasks" && <TasksView res={res} initialCadence={initialCadence} />}
    </div>
  );
}
