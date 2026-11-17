---
name: performance-marketing-playbook
description: Opinionated, step-by-step guidance for B2B SaaS performance marketing, plus filled-in deliverables (plan, budget tracker, recurring tasks, slide template, weekly update and monthly report, QBR and annual plan decks, postmortems, experiment database with ICS scoring). Use when someone asks what to do about paid search, SEO, AEO, paid social, ABM, budget, attribution, measurement, testing, reporting or operating rhythm at a B2B SaaS company, or wants a marketing plan, budget, QBR, postmortem or test backlog built from their numbers.
license: MIT
compatibility: The guidance is markdown. fill.py needs Python 3.8 or later, standard library only, no network.
---

# Performance Marketing Playbook

The playbook is in `playbook/` (12 sections) and the deliverable templates are in `deliverables/`, both in the same folder as this file. Answer from them. Don't add generic advice that contradicts them.

## When someone asks what to do

1. Pick the 1-3 sections that fit the question:

   | Question is about | Read |
   | --- | --- |
   | Priorities, how to approach the work | 01-principles.md |
   | Goals, CAC, payback, product-led vs sales-led, working with Sales, where to start | 02-align-to-the-business.md |
   | Tracking, funnel stages, offline conversions, attribution, proof of cause | 03-measurement.md |
   | Paid search, SEO, AEO/GEO, review sites, landing pages, CRO | 04-demand-capture.md |
   | LinkedIn, Meta, Reddit, YouTube, CTV, display, ABM, sponsorships, syndication, email | 05-demand-creation.md |
   | How much to spend, allocation, pacing, forecasting, planning | 06-budget.md |
   | Testing, backlog, ICS scoring, sample size | 07-experimentation.md |
   | Weekly update, monthly report, QBR, annual plan, postmortems | 08-reporting-and-communication.md |
   | Daily, weekly, monthly, quarterly, yearly routines | 09-operating-rhythm.md |
   | Automation, alerts, agents, APIs, MCP | 10-operations-and-ai.md |
   | How channels affect each other, Sales, RevOps, Finance, agencies | 11-cross-channel-and-working-with-others.md |
   | New placements and platform changes | 12-whats-new.md |

2. Read those files. If the person's situation is unclear, ask the section's "Ask first" questions that matter most (two or three, not all).
3. Answer with the section's steps and defaults, applied to their situation. Name the "If you see X, do Y" rule that fits. Say when to call an expert if they've reached that point.
4. Point to the tools the section lists. Redavio's tools run through the Redavio MCP server at https://www.redavio.com/mcp if the person has it connected.
5. Offer the deliverable that turns the advice into a file (below).

## When someone wants a deliverable

1. Get their inputs. Only two are needed: a pipeline goal (or revenue goal) and the average deal size. Everything else has a default in `deliverables/defaults.md`; ask for the ones they know (conversion rates, cost per MQL, months, motion, channels, CRM, competitors, ICP) and say which defaults you used.
2. Write the inputs to a JSON file, for example:

   ```json
   {"company": "Acme", "pipeline_goal": 3000000, "deal_size": 30000, "mql_to_sql": 0.3}
   ```

3. Run, using the path to the folder this file is in:

   ```
   python3 <skill-folder>/fill.py plan inputs.json --out <output-folder>
   ```

   It writes all seven deliverables filled in: planning-doc.md, budget-tracker.csv (live formulas), recurring-tasks.csv, slide-template.md, regular-updates.md, planning-and-review-decks.md, experiment-database.csv. `python3 fill.py math inputs.json` prints just the numbers. Never do the funnel or budget math yourself; use the script's numbers.
4. If the person has Google Docs, Sheets, Slides, ClickUp, Asana or Notion connected, create the deliverables there: the planning doc and updates as docs, the budget tracker and experiment database as sheets (import the CSV so formulas stay live), the decks in Slides starting from `deliverables/slide-template.pptx`, the recurring tasks as recurring tasks. Otherwise give them the files.
5. To back-test experiment scores: `python3 fill.py calibrate experiments.csv` on their filled experiment database.

## Rules

- Numbers come from fill.py or the person's data, never from memory.
- Defaults are rules of thumb. Say so, and tell them to replace each one with three months of their own data.
- Judge demand capture and demand creation on their own measures (03-measurement.md). Never judge creation on last click.
- Recommend changes; don't make changes to ad accounts. If the person wants a budget change applied, Ad Budget Optimizer does it after they approve.
