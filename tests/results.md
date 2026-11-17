# Test results

Second-pass check, 2026-11-17, against SPEC.md. Each question answered two ways: (A) as the skill (SKILL.md: pick sections, read them, numbers from `fill.py`); (B) through the local MCP server (`playbook_guide`, `playbook_deliverable` at http://localhost:3100/mcp, reading this checkout). Numbers below are tool output, not hand math.

## Results

| # | Question | A: skill | B: MCP | Sections picked by playbook_guide | Tools listed by playbook_guide | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Brand marketer, no offline conversions, $50K/mo: what first? | PASS | PASS | 1, 2, 3 (right) | Correlation Analyzer only (partial fit) | Fix data driven first (01 step 2), map stages, click IDs, daily offline uploads, optimize to valued MQLs (03 steps 1-4); $50K/mo by hand = call an expert / Ad Budget Optimizer (06). The guide's tool list misses performance-os (offline conversion setup) and Ad Budget Optimizer. |
| 2 | $3M pipeline, $30K deal: how much to spend? Build the plan. | PASS | PASS | 6 (right; 2 would also fit) | Ad Budget Optimizer (fits) | fill.py and planning-doc: 100 SAOs, 167 SQLs, 667 MQLs, blended $346, budget $230,769 ($19,231/mo), capture $138,462 / creation $92,308, cost per SAO $2,308. MCP budget-tracker returns formulas only, so the AI must take the numbers from planning-doc. |
| 3 | Split budget between Google and LinkedIn? | PASS | PASS | 4, 6, 5 (right) | LPA, Ad Copy, performance-os, Ad Budget Optimizer, Account Influence (noisy) | 60/40 capture/creation default, then marginal return (06 steps 3-4). fill.py with those two channels: Google $138,462, LinkedIn $92,308. Microsoft 10-20% of search if added (04). |
| 4 | CEO wants to cut LinkedIn on last click. | PASS | PASS | 11, 8, 3 (good; misses 5) | Correlation Analyzer, Driver breakdown (planned) (fits) | Capture vs creation table (03), holdout + self-reported + branded search trend (05, 11 rules). The exact "leadership asks for last-click ROI" rule is in 05, which the guide doesn't return; 11 carries the equivalent rule. |
| 5 | Which attribution model? | PASS | PASS | 3 (right) | Correlation Analyzer (fits) | Data-driven in platform for bidding, linear in CRM, self-reported alongside; attribution is not proof of cause (03 steps 5-6). |
| 6 | Prove paid search is incremental? | PASS | PASS | 3, 4 (right) | Correlation, LPA, Ad Copy, performance-os (LPA/Ad Copy are noise) | Brand vs non-brand checks, geo holdouts, one cause test a year (rule of thumb); call an expert to design a geo holdout (04, 07). |
| 7 | Sales says MQLs are junk. | PASS | PASS | 2, 3, 11 (right) | Correlation Analyzer (fits) | Review 20 leads together, split hand-raiser vs content MQLs, bid to SQL/SAO with offline conversions, MQL→SQL by channel in the weekly. 02 and 11 describe the 20-lead check differently (see Still open). |
| 8 | Weekly update template for leadership. | PASS | PASS | 8, 9 (right) | Driver breakdown, Ad Budget Optimizer (BO is noise) | regular-updates deliverable filled: monthly plan $19,231 spend, 56 MQLs, 8.3 SAOs, $250,000 pipeline. |
| 9 | QBR deck outline for next week. | PASS | PASS | 8 (right) | Driver breakdown (fits) | QBR outline from planning-and-review-decks, timing "last two weeks of the quarter"; pptx base deck filled by fill.py. MCP returns a blank outline without inputs, filled with inputs. |
| 10 | Product-led with free signups: does this work? | PASS | PASS | 2, 3 (right) | Correlation Analyzer (weak fit) | Motion swap Signup/PQL, optimize to activation (02). Labels flow into tracker, planning doc and pptx. Defaults stay sales-led ($300 per signup) and the planning doc's Priorities and risk line still say MQL/SQL (see Still open). |
| 11 | Prioritize: demo-page pricing, LinkedIn video, competitor terms. | PASS | PASS | 7, 5, 1 (right) | Ad Copy, LPA, Account Influence (fits) | ICS from the experiment database: pricing range 6.7, competitor split 6.3, LinkedIn video 5.7; run highest first, design sample size and stop date, 2-3 live per channel. calibrate tested by Confidence and Impact band with win rate. |
| 12 | What to do every day, week, month? Put it in ClickUp. | PASS | FAIL | 9 (right) | Ad Budget Optimizer (fits D2/D4/M4) | Daily/weekly/monthly lists correct, with description and first due date; recurrence must be set after import. MCP: calling recurring-tasks with only `{"start_date": ...}` errors ("inputs.deal_size expected number"); works only with no inputs or with deal_size added. Quarterly/yearly first-due dates contradict the playbook's timing. |
| 13 | Show up in ChatGPT answers? | PASS | PASS | 4, 12 (right) | LPA, Ad Copy, performance-os, Research Agent (LPA/Ad Copy/perfos noise; Correlation would fit) | AEO steps: 20 buyer questions monthly, quotable pages, third-party mentions, share of answers (04); ChatGPT ads only on Free/Go (12). |
| 14 | Landing pages convert at 1%. | PASS | PASS | 4, 7 (right) | LPA first, Ad Copy, performance-os (fits) | Below 2% rule (rule of thumb): message match, form length, speed, then Landing Page Analyzer; measure visit-to-form and form-to-SQL separately; test design from 07. |
| 15 | $400K behind on pipeline mid-quarter. | PASS | PASS | 6, 8 (right) | Ad Budget Optimizer, Driver breakdown (fits) | fill.py on the gap: 13.3 SAOs, 22.2 SQLs, 88.9 MQLs, $30,769 at defaults. Order: stage rates, budget-limited capture, reset goal in writing if the gap is over 20% of the quarter's goal (rule of thumb); explain in the weekly. |

**Totals:** skill 15/15 PASS. MCP 14/15 PASS (Q12 fails on input validation). playbook_guide picked the right sections for all 15; its tool list fits 10 of 15 well, the rest include noise or miss an obvious tool (Q1, Q3, Q6, Q8, Q13).

## Earlier review findings: verified

| Finding | Status | Evidence |
| --- | --- | --- |
| Blended cost per MQL = 1/(capture share/capture cost + creation share/creation cost) everywhere; $230,769 at defaults | Fixed | defaults.md:40,50; 06-budget.md:25-27; fill.py:119; playbook.ts:173; tracker row 20 `=1/(B11/B13+B12/B14)`. Evaluated: $346.15, budget $230,769.23, 462 + 205 MQLs. playbook-parity.mts: 5/5 cases match. |
| Tracker: budget by channel; plan vs actual spend, cost per SAO, pipeline | Partly fixed | Budget by channel present (plan only). Spend and pipeline have plan, actual and variance. Cost per SAO has an actual column only; plan cost per SAO sits in the plan block, with no monthly plan column or variance. |
| Sourced and influenced pipeline never added | Fixed | Separate column O, own total; note row says so. |
| Totals compare actuals only with months that have actuals | Fixed | `SUMIF(C,"<>",B)` and `SUMIF(M,"<>",L)` in the Total row. |
| Revenue-goal row and rule (revenue_goal only) | Fixed | Pipeline goal = `=B3/B4` → $3,000,000 from $600,000 at 20%; same via MCP. |
| experiment-database.csv formulas parse as CSV | Fixed | 20 columns on every row; ICS `=ROUND(AVERAGE(G:I),1)` → 6.7/6.3/5.7; error `=IF(P="","",P-L)` evaluates. |
| fill.py calibrate by Confidence and Impact with win rate | Fixed | Test CSV of 7 rows (6 finished): bands 1-4/5-7/8-10 for both, win rate counts significant and in the predicted direction; MCP experiments_csv gives the same text. |
| Recurring tasks have description and first due date | Fixed | Both columns present (fill.py:352, playbook.ts:390). Dates wrong for Q6, Q7, Y2 (Still open). |
| Filled slide-template.pptx has company numbers and product-led labels | Fixed | Flowly product-led run: slides 2, 3, 6, 8 show $6,000,000, 500 SAOs, $1,153,846, Signups/PQLs. |
| No template link breaks outside the repo | Fixed | All deliverable template links are absolute GitHub URLs; no relative links in filled output; all in-repo playbook links and anchors resolve. |
| Planning doc has a Priorities table with a Principle column | Fixed | planning-doc.md:70-77. |
| Defaults used listed in plain words | Fixed in fill.py, not in MCP | Planning doc risk line uses plain labels; MCP header lists raw keys (`mql_to_sql, cost_per_mql_capture`). |
| Every section's Tools block links the Library | Fixed | 12/12 link https://www.redavio.com (the library home); tool slugs match src/lib/library.ts. |
| No unlabelled benchmark numbers | Mostly fixed | Two thresholds lack "rule of thumb" (Still open, nice). |
| No contradictions: QBR timing, annual plan timing, lead follow-up, pacing tolerance, SQL = meeting scheduled | Mostly fixed | Section text agrees (08, 09, decks; 02 and 11 on follow-up; 06/10 ±10% vs 15% alert; 03/defaults/fill.py on SQL). Remaining: recurring-tasks.csv QBR wording and first-due dates. |

## Still open

**Must**

1. redavio-web/src/app/mcp/route.ts:448 — `deal_size` is required in the zod schema, so `playbook_deliverable` recurring-tasks with `{"start_date": ...}` fails validation; make `deal_size` optional in the schema and enforce it in the handler for the deliverables that need it.
2. fill.py:349 (and playbook.ts:384) — quarterly and yearly first-due dates contradict the playbook: Q7 QBR and Q6 next quarter's plan fall after the quarter ends (08:24, 09:69-70 say last 2 weeks of the quarter), Y2 annual plan falls at the start of the next year (08:26, 09:77 say draft 8 weeks before); set per-task offsets (e.g. QBR = quarter end − 14 days, Y2 = year end − 8 weeks, postmortems = end + 14 days).

**Should**

3. deliverables/recurring-tasks.csv:27 — "Run the QBR (within 2 weeks of quarter end)" reads as after the end; change to "in the last 2 weeks of the quarter" to match 08:24 and 09:70.
4. fill.py:319-329 (and playbook.ts:345-355) — add a monthly "Planned cost per SAO" column and a cost-per-SAO variance, so cost per SAO has plan vs actual like spend and pipeline.
5. playbook/06-budget.md:60 vs fill.py:310-317 — 06 says actuals are entered by channel, but the tracker only has channel plan; add actual spend, SAOs and pipeline per channel (or capture vs creation), or change the sentence.
6. playbook/05-demand-creation.md:19 vs fill.py:321 — 05 says creation pipeline is counted from self-reported source in the tracker; there is no self-reported column; add "Self-reported pipeline, creation (medium confidence)" next to influenced, or reword.
7. deliverables/experiment-database.csv:1 — 07:23-28 says to record score reasoning, baseline, minimum detectable effect, sample size, stop date and decision rule "in the database"; add those columns.
8. deliverables/planning-doc.md:74-75 — Priorities rows hardcode "SQL", "MQL, SQL and SAO"; use {{SQL}}/{{MQL}} so product-led plans say Signup/PQL. Same for fill.py:51-57 / playbook.ts:113-117 labels in the risk line ("MQL to SQL rate", "cost per MQL").
9. redavio-web/src/app/mcp/route.ts:495 — "Defaults used" lists raw keys; map through LABELS for plain words, as fill.py does.
10. playbook/02-align-to-the-business.md:42 vs playbook/11-cross-channel-and-working-with-others.md:30 — "20 recent MQLs" vs "20 recent leads Sales rejected", while 11 calls it "the same check"; pick one wording.
11. redavio-web/src/lib/playbook.ts:31-36 — guide tool hand-offs: add perfos to section 03 (offline conversion setup, Q1), add "last click"/"cut linkedin" keywords to section 05 so its last-click rule is returned (Q4), and drop adcopy/landing from section 04's default hand-offs unless the question is about pages or copy (noise on Q3, Q6, Q13).
12. SPEC.md §3 / redavio-web/src/lib/library.ts:133-378 — no Library page for the playbook in the item list (confirm it isn't only in Sanity); needed before publishing.

**Nice**

13. deliverables/defaults.md:19 — product-led runs use sales-led defaults ($300 per signup, 25% signup to PQL); add product-led defaults or warn in the filled planning doc when motion is product-led and rates are defaulted.
14. deliverables/planning-doc.md:7 — when the pipeline goal is derived from a revenue goal, say so ("revenue goal ÷ win rate"), and mark period and start date "(default)" when defaulted.
15. deliverables/regular-updates.md:9 — weekly update audience ("your manager, Sales leadership, Finance") differs from 08:22 ("Marketing lead, Sales leader, CEO at a startup"); align.
16. playbook/07-experimentation.md:47 ("drop anything scored under 5") and playbook/09-operating-rhythm.md:113 ("more than four channels") — label as rules of thumb.
17. fill.py:419-427 (and playbook.ts:425-430) — calibrate drops scores between bands (e.g. 4.5, 7.5) and averages signed lift across metrics where lower is better (cost per SAO); use bands 1-<5/5-<8/8-10 and compare lift in the predicted direction.
