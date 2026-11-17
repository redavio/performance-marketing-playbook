# Performance Marketing Playbook: v1 spec

Frozen copy of the approved spec (approved 2026-11-17; revised 2026-11-17 so demand creation is never counted toward the pipeline goal). The build and the reviewer check against this file.

## 1. Problem

Running B2B SaaS performance marketing well, at a startup or an established company, takes judgment that lives in people's heads: what to set up first, how to measure it, how to spend, how to test, how to report. Many marketers who own it come from brand or product marketing and don't know the nuances. AI assistants give generic answers. There is no opinionated, step-by-step playbook that a person or their AI can follow and act on.

## 2. Who it's for

- **The non-specialist** (brand or product marketer, founder) who now owns paid acquisition. They follow it step by step.
- **The expert** (senior performance marketer, head of growth). They use it as a checklist, a planning kit and a way to explain their approach.
- **Their AI.** Claude or any MCP client reads the playbook and turns it into next steps and documents.

## 3. What ships

- **Public GitHub repo** (github.com/redavio/…): the playbook as markdown, one file per section, plus the deliverable templates (docs, sheets and a slide deck).
- **Claude skill** that applies the playbook to the user's situation.
- **Tools on the Redavio MCP server** (section 9), so anyone's AI can query it.
- **Library page** on redavio.com.

Free and open source. Slack and a web app are not in v1.

## 4. Principles

Four principles that apply to every section and every initiative. Written as plain names with no acronym; users can rename them.

| Principle | Means |
| --- | --- |
| Strategic alignment | Work ties to business goals: pipeline and revenue targets, unit economics, budget, voice of customer, positioning, and Sales. |
| Operational excellence | Efficient and automated: recurring routines, connected tools (APIs, MCP servers), alerts, clean handoffs. |
| Rapid experimentation | Always testing, with a backlog, a scoring method, a test log and readouts. |
| Data driven | Clean tracking, the value of each conversion, data stitched across sources, and proof of cause where it matters. |

## 5. Outline

**Channels in scope.** Demand capture: paid search (Google, Microsoft), SEO, AEO/GEO, review sites (G2, Capterra), website conversion rate optimization. Demand creation: paid social (LinkedIn, Meta, Reddit), YouTube and connected TV, display and retargeting, ABM platforms, sponsorships (newsletters, podcasts, events), content syndication. Email and lifecycle sit alongside both. Each channel names its best outside sources (for example SaaStr and Exit Five for B2B SaaS marketing, Search Engine Land for search).

| # | Section | Covers |
| --- | --- | --- |
| 1 | Principles | The four principles and how to use them |
| 2 | Align to the business | Goals, unit economics (CAC, payback, LTV), guardrails, motion (sales-led vs product-led), voice of customer, working with Sales |
| 3 | Measurement | Funnel stages (MQL to closed won), tracking, value per conversion, offline conversions, attribution models (first touch, last touch, linear, position-based, data-driven, self-reported) vs proof of cause, and measuring capture vs creation (section 7) |
| 4 | Demand capture | Paid search on Google and Microsoft (bidding, structure, query mining), SEO, AEO/GEO (showing up in AI answers), and website conversion rate optimization |
| 5 | Demand creation | Paid social, YouTube and CTV, display, ABM, sponsorships, syndication |
| 6 | Budget | Allocation by marginal return, pacing, forecasting, annual and quarterly budget planning, and the budget tracker (back into budget from the pipeline goal, split across capture and creation) |
| 7 | Experimentation program | Backlog, ICS scoring (Impact, Confidence, Simplicity), test design, reading results, and a test log that checks past scores against results |
| 8 | Reporting and communication | Weekly update, monthly report, QBR, quarterly and annual plans, postmortems: who each is for, what goes in it, when it goes out |
| 9 | Operating rhythm | Recurring tasks by day, week, month, quarter, year |
| 10 | Operations and AI | Automation, alerts, agents, connecting tools via APIs and MCP |
| 11 | Cross-channel and working with others | How channels affect each other (creation lifts branded search, direct and AI-answer traffic), one plan and one report across channels; Sales, RevOps, Finance, agencies and vendors |
| 12 | What's new | New placements (ChatGPT ads, Reddit, podcasts) and platform changes |

## 6. Format of every section

- **Why it matters:** one or two lines.
- **Ask first:** the questions to answer before acting.
- **Do this:** numbered steps with sensible defaults.
- **If you see X, do Y:** a short decision list.
- **Metrics:** what to watch.
- **Common mistakes.**
- **Call an expert when:** where the non-specialist should stop.
- **Tools:** related tools, each marked exists or planned (section 10). Sources: the best outside resources for that section, each with what it's good for.

Plain words, no filler. Any benchmark number states its source, or is labelled a rule of thumb.

## 7. Funnel stages and measuring capture vs creation

**Funnel stages.** Names vary by CRM, so the user maps their own. Typical: MQL (hand-raiser: demo or contact request; non-hand-raiser: content download, webinar) → SQL (meeting scheduled) → SAO (sales-accepted opportunity; enters pipeline) → Closed won. Plans, the budget tracker and reports all use these stages, and the conversion rates between them drive the budget math.

| | Demand capture (paid search, SEO, AEO) | Demand creation (paid social, YouTube and CTV, display, ABM, sponsorships, syndication) |
| --- | --- | --- |
| Primary measure | Pipeline and revenue, cost per qualified opportunity | Target-account reach and engagement, pipeline velocity, self-reported "how did you hear about us" |
| Window | Short | Longer; never judged on last click |
| Proof of cause | Brand vs non-brand checks, geo holdouts | Lift tests, holdout accounts |

## 8. Deliverables ("spin it up")

Every run produces files, not just answers. Inputs vary by company and every one can be customized. The user enters a pipeline goal (revenue goal too, if they have one) and their average deal size. Budget is worked back from the goal. Everything else is optional, with stated defaults the user can change: stage conversion rates, sales cycle, channels, CRM, competitors, ICP, and motion (product-led swaps MQLs for signups and product-qualified leads). The tool returns each deliverable filled in:

1. **Planning doc:** goals, funnel stages, unit economics, competitors, channel mix, budget.
2. **Budget tracker** (Google Sheet): start from the pipeline or revenue goal and work back through demand capture only: SAOs, SQLs and MQLs needed (stage conversion rates), then capture's budget (MQLs × capture cost per MQL). Demand creation gets a set share of budget on top (default 30%) and is never counted toward the goal: the plan assigns it no MQLs or pipeline. It is judged on its own measures (target-account engagement, self-reported source, influenced pipeline, labelled lower confidence). Budget by channel, plan vs actual by month.
3. **Recurring-task list:** the operating rhythm as tasks, ready to import into ClickUp, Asana or Notion.
4. **Slide template** (Google Slides or PowerPoint): the base deck every presentation below uses, filled with the company's numbers.
5. **Regular updates:** weekly update (results vs goal, what changed, what's next, asks) and monthly report.
6. **Planning and review decks:** QBR (last quarter's postmortem plus next quarter's plan), annual plan, and postmortems for the year, the quarter, or any test, launch or campaign.
7. **Experiment database** (a table in Sheets, Airtable or Notion) with ICS scoring (Impact, Confidence, Simplicity) and a test log. It back-tests the scores: each test's predicted impact and confidence sit next to its result, so the team sees how accurate past scores were and calibrates new ones.

The user's own AI creates these in their tools (Google Docs, Sheets, Slides, ClickUp, Notion) through their own connectors. Redavio never touches their accounts. Plain copies sit in the repo.

## 9. MCP tools

- **playbook_guide**: a question or situation in, the relevant sections and next steps out, including which Redavio tools to call next (e.g. landing page optimization points to Landing Page Analyzer, on the same MCP server).
- **playbook_deliverable**: a deliverable name plus company inputs in, the filled deliverable out.

No paid AI on our side: the server returns playbook content, and the user's AI does the reasoning, matching the other Redavio MCP tools.

## 10. Related tools (the "Tools" line)

| Tool | Status | Section |
| --- | --- | --- |
| Ad Copy Analyzer, Landing Page Analyzer | Exists (Library) | Experimentation, Demand capture |
| Marketing Correlation Analyzer | Exists (Library) | Measurement |
| Ad Budget Optimizer | Exists (Library, free) | Budget |
| Paid search playbook (performance-os) | Exists, public (open source) | Demand capture |
| Account Influence Analyzer (ABM) | Planned | Demand creation, Measurement |
| Driver breakdown (Deep Diver rebuild) | Planned | Measurement |

Also in the Library: Research Agent (a brief on the news that matters; What's new), Google Sheet to CMS Landing Page (landing pages in bulk; Demand capture), and the Redavio MCP server, which gives the user's AI all of these. Each section's Tools line links to the Library, so new tools show up without editing the playbook.

## 11. Not in v1

- Actions of its own. The playbook guides and hands off: any action, including a change to an ad account, happens in the Redavio tool it calls on the same MCP server (e.g. Ad Budget Optimizer applies a budget once the user approves).
- Slack, a web app.
- Channel-by-channel depth beyond the "Do this" steps (grows in later versions).
- Industries other than B2B SaaS.

## 12. Done means

- All 12 sections written in the section 6 format.
- All 7 deliverables produce a usable file (doc, sheet or deck) from sample inputs.
- A test set of about 15 realistic questions (e.g. "brand marketer, no offline conversions, $50K a month: what first?") gets answers that match the playbook, via both the skill and the MCP tools.
- A fresh reviewer, given only this spec and the output, finds no gaps, unsupported claims or filler left unfixed.
- The owner tries it locally in Claude and approves before anything is published.

## 13. Decisions

1. The name is Performance Marketing Playbook.
2. The principles go by plain names, no acronym.
3. performance-os is public and open source; the playbook links to it.
4. ICS scoring (Impact, Confidence, Simplicity).
5. Inputs are flexible; pipeline goal and deal size go in, budget is worked back from the goal (section 8).
