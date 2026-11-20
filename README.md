# Performance Marketing Playbook

An opinionated, step-by-step playbook for B2B SaaS performance marketing, at a startup or an established company. It tells you what to set up first, how to measure it, how to spend, how to test and how to report, and it turns that into files you can use: a plan, a budget tracker, recurring tasks, update and deck templates, and an experiment database.

It's written for three readers:

- **The non-specialist** (brand or product marketer, founder) who now owns paid acquisition. Follow it step by step.
- **The expert.** Use it as a checklist, a planning kit and a way to explain your approach.
- **Your AI.** Claude or any MCP client reads it and turns it into next steps and documents.

## The playbook

| # | Section |
| --- | --- |
| 1 | [Principles](playbook/01-principles.md) |
| 2 | [Align to the business](playbook/02-align-to-the-business.md) |
| 3 | [Measurement](playbook/03-measurement.md) |
| 4 | [Demand capture](playbook/04-demand-capture.md) |
| 5 | [Demand creation](playbook/05-demand-creation.md) |
| 6 | [Budget](playbook/06-budget.md) |
| 7 | [Experimentation](playbook/07-experimentation.md) |
| 8 | [Reporting and communication](playbook/08-reporting-and-communication.md) |
| 9 | [Operating rhythm](playbook/09-operating-rhythm.md) |
| 10 | [Operations and AI](playbook/10-operations-and-ai.md) |
| 11 | [Cross-channel and working with others](playbook/11-cross-channel-and-working-with-others.md) |
| 12 | [What's new](playbook/12-whats-new.md) |

Every section has the same parts: why it matters, what to ask first, steps with defaults, decision rules, metrics, common mistakes, when to call an expert, and tools and sources.

## The deliverables

Enter a pipeline goal and your average deal size. Everything else has a default you can change ([defaults.md](deliverables/defaults.md)). Budget is worked back from the goal.

| Deliverable | File |
| --- | --- |
| Planning doc | [planning-doc.md](deliverables/planning-doc.md) |
| Budget tracker (import into Google Sheets; formulas stay live) | [budget-tracker.csv](deliverables/budget-tracker.csv) |
| Recurring tasks (import into ClickUp, Asana or Notion) | [recurring-tasks.csv](deliverables/recurring-tasks.csv) |
| Slide template | [slide-template.pptx](deliverables/slide-template.pptx), [outline](deliverables/slide-template.md) |
| Weekly update and monthly report | [regular-updates.md](deliverables/regular-updates.md) |
| QBR, annual plan and postmortems | [planning-and-review-decks.md](deliverables/planning-and-review-decks.md) |
| Experiment database with ICS scoring | [experiment-database.csv](deliverables/experiment-database.csv) |

A filled example for a made-up company is in [examples/acme](examples/acme).

## Use it

**With any AI, through the Redavio MCP server.** Add `https://www.redavio.com/mcp` as a connector in Claude (or any MCP client). Ask what to do, or ask for a deliverable. Two tools serve the playbook: `playbook_guide` (a question in, the relevant sections and next steps out) and `playbook_deliverable` (a deliverable and your inputs in, the filled file out). The same server runs Redavio's other tools, so the playbook can hand off, for example from landing page advice to Landing Page Analyzer.

**As a Claude skill.** `npx skills add redavio/performance-marketing-playbook`, then ask, for example, "We need $3M in pipeline next year at a $30K deal size. Build the plan."

**By hand.** Read the sections. Fill the deliverables with the script (Python 3.8+, no installs):

```
python3 fill.py plan examples/acme-inputs.json --out my-plan   # all seven deliverables
python3 fill.py math examples/acme-inputs.json                 # just the numbers
python3 fill.py calibrate my-experiments.csv                   # back-test your ICS scores
python3 -m pytest                                              # tests
```

## Dashboard

`dashboard/` is a React app that shows the plan, the budget and the task rhythm. It reads one file, `results.json`, written by `fill.py`, and computes nothing itself, so it always shows the same numbers as the deliverables.

```bash
python3 fill.py math my-inputs.json --json dashboard/public/results.json   # or add --json to plan
cd dashboard && npm install && npm run dev
```

`results.json` holds the inputs used (and which are defaults), the funnel from goal to budget, the budget by channel and month, and the tasks with first due dates. The one in `dashboard/public/` is the Acme example. To share the dashboard, deploy the `dashboard` folder to Vercel (or any static host) with your `results.json` in `public/`. Anyone can also open a results file with the "Open results file" button, or point at one with `?src=`.

## Make it yours

The playbook is a starting point, not a finished product. Fork it and change anything:

- **Brand the dashboard.** It ships unbranded. Set your name and logo in
  `dashboard/src/brand.ts` and your brand color (one CSS variable, `--brand`) at the
  top of `dashboard/src/index.css`. It's styled with Tailwind and follows the
  system's light or dark mode.
- **Reuse the screens in your own app.** The screens live in
  `dashboard/src/components/` and take the result (typed in `dashboard/src/types.ts`)
  as props; they load nothing themselves. `dashboard/src/App.tsx` is the only part
  that reads `results.json`, so copy the components and types into any React +
  Tailwind app and feed them from your own API. Add a `brand` color to your
  Tailwind config.
- **Change the screens or build your own app.** Everything on screen comes from one file, `results.json`. Build your own React app, internal tool or AI agent on it.
- **Change the defaults and the math.** Defaults are in `fill.py` (`DEFAULTS`) and [defaults.md](deliverables/defaults.md); the math is in `compute()` in `fill.py`.
- **Change the deliverables.** The templates are in `deliverables/`; `{{name}}` fields are filled from your inputs.

## Principles

Four principles run through every section: strategic alignment, operational excellence, rapid experimentation and data driven. Rename them if you like.

## License

MIT. Free and open source. Product names mentioned are trademarks of their owners. Made by [Redavio](https://www.redavio.com).
