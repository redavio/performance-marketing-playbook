// Shape of results.json, written by fill.py (python3 fill.py math inputs.json --json results.json).

export interface Input {
  key: string;
  label: string;
  value: string | number | string[] | null;
  /** True when the value is the playbook's default, not one you entered. */
  default: boolean;
}

export interface FunnelStep {
  key: string;
  label: string;
  total: number;
  per_month: number;
  /** How the number is worked out, in words. */
  how: string;
}

export interface Channel {
  channel: string;
  type: "capture" | "creation";
  share_of_group: number;
  total: number;
  per_month: number;
}

export interface Month {
  month: string;
  spend: number;
  by_channel: Record<string, number>;
  mqls: number;
  sqls: number;
  saos: number;
  pipeline: number;
}

export interface Task {
  id: string;
  name: string;
  cadence: "Daily" | "Weekly" | "Monthly" | "Quarterly" | "Yearly";
  recurrence: string;
  owner: string;
  section: string;
  principle: string;
  first_due: string;
  how: string;
}

export interface Results {
  company: string;
  start_date: string;
  months: number;
  period: string;
  labels: { MQL: string; SQL: string; MQLs: string; SQLs: string; sql_meaning: string };
  inputs: Input[];
  defaults_used: string[];
  plan: {
    pipeline_goal: number; revenue: number; saos: number; sqls: number; mqls: number; closed_won: number;
    budget: number; capture_budget: number; creation_budget: number;
    cost_per_sao: number; capture_cost_per_sao: number; pipeline_to_spend: number;
  };
  monthly: Record<string, number>;
  funnel: FunnelStep[];
  budget: { channels: Channel[]; months: Month[] };
  tasks: Task[];
}
