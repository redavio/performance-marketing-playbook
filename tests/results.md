# Test results

Run 2026-11-17. Route A = SKILL.md followed as written (sections from its table, fill.py for numbers). Route B = local Redavio MCP server (playbook_guide, playbook_deliverable), answer written only from what the tools returned. Routing = the sections playbook_guide returned for the question as asked, without a `section` follow-up.

Parity checks done first: every section returned by playbook_guide contains the repo file's text exactly (all 12), and playbook_deliverable output is byte-identical to `fill.py plan` for planning-doc, budget-tracker, regular-updates, planning-and-review-decks, recurring-tasks and experiment-database (3M / 30K, and product-led), apart from the tool's header and source lines.

| # | Route A | Route B | Routing right? | Agree? |
| --- | --- | --- | --- | --- |
| 1 | PASS | PASS | Partial: 2, 3, 5 (5 is off topic; 1, 4, 6 missing) | Mostly |
| 2 | PASS | PASS | Yes: 6, 3 | Yes |
| 3 | PASS | PASS | Yes: 4, 5, 6 | Yes |
| 4 | PASS | PASS | Partial: 5 only (3, 11 missing) | Yes |
| 5 | PASS | PASS | Yes: 3 | Yes |
| 6 | PASS | PASS (weak) | Partial: 4 only (3 missing) | Mostly |
| 7 | PASS | PASS | Yes: 2, 3 (11 would help) | Yes |
| 8 | PASS | PASS | Partial: 8, 9, 12 (12 off topic) | Yes |
| 9 | PASS | PASS | Yes: 8 | Yes |
| 10 | PASS | PASS | Partial: 2 only (3 missing) | Yes |
| 11 | PASS | PASS | Yes: 7, 1, 4 | Yes |
| 12 | PASS | PASS | Yes: 9 | Yes |
| 13 | PASS | PASS | Partial: 4 only (12 missing) | Mostly |
| 14 | PASS | PASS | Partial: 2, 4 (7 missing) | Mostly |
| 15 | PASS (weak) | FAIL | No: 3 only (6 and 8 missing) | No |

Totals: Route A 15/15, Route B 14/15. Routing right 7, partial 7, wrong 1.

## Summary per question

1. Fix tracking first (map stages, click IDs, conversion values, daily offline uploads), optimize to valued MQLs until volume allows SQL/SAO, ask for pipeline goal + deal size and run the math to test the $50K/month. A also cites section 1's "data driven first" order and the $50K/$20K call-an-expert thresholds; B doesn't have those.
2. fill.py and the tool agree: 100 SAOs, 167 SQLs, 667 MQLs, $240,000/yr ($20,000/mo), capture $144,000 / creation $96,000, $2,400 per SAO, 12.5x. Offer all seven deliverables.
3. Default 60% capture / 40% creation, LinkedIn as the first creation channel, Microsoft at 10-20% of search, move money by marginal return in steps of 20% or less.
4. Don't judge creation on last click; show the holdout, self-reported source and branded search trend; propose a lift test. A adds section 11's "branded search falls a month later" warning.
5. Data-driven in the ad platforms for bidding, linear in the CRM for pipeline, self-reported next to both; attribution isn't proof of cause.
6. Brand vs non-brand checks and geo holdouts; call an expert to design the holdout. A adds section 3's "at least one cause test a year" and lift tests.
7. Pull recent MQLs and review them with Sales, fix the definition or targeting, split hand-raisers from content leads, bid to SQL/SAO through offline conversions.
8. Weekly template (results vs goal, what changed, what's next, tests, asks; Monday by noon); both need pipeline goal + deal size before the filled template can be produced.
9. 12-slide QBR outline from planning-and-review-decks (postmortem then next-quarter plan), within 2 weeks of quarter end.
10. Yes: swap MQL to signup and SQL to PQL, optimize to activation, run fill.py / the tool with `motion: product-led`.
11. ICS from the experiment database: pricing on demo page 6.7, competitor split 6.3, LinkedIn video 5.7; rescore with own evidence, check sample size, judge the video on creation measures.
12. Section 9 daily/weekly/monthly/quarterly/yearly lists, recurring-tasks CSV (31 tasks) to import into ClickUp. ClickUp was not written to in this test.
13. AEO steps: ask the 20 buyer questions monthly, quotable pages, third-party mentions, share of answers. A also offers a small ChatGPT ads test (section 12); B doesn't.
14. Start with paid landing pages, one page per offer, cut form fields, test one big change, judge on SAOs per visit. A adds section 7's sample size and run-time rules.
15. A: explain the gap with drivers, forecast plan / actual / period end, apply the section 6 rules, and use fill.py to size the catch-up (at $30K deals: 13.3 SAOs, 88.9 MQLs, $32,000 at defaults). B got only measurement and has nothing on catching up.

## Fails and weak spots

- Q15 (B FAIL): playbook_guide sent "$400K behind on pipeline halfway through the quarter" to section 3 only; it needs 6 (forecast, pacing, reallocation) and 8 (explain gaps with drivers, bad-month rule).
- Q15 (A weak): no section has a rule for a mid-quarter pipeline shortfall (how to size the catch-up, whether to add spend given the stage lag, when to reset the goal in writing). The only trigger, "two months under 80% of pipeline plan", sits in the annual plan deck and has no response steps in 06-budget.md.
- Q1: playbook_guide picked 5 (demand creation, from the word "brand") instead of 1 (fix data driven first) and 4/6 (the $20K search and $50K/month call-an-expert thresholds).
- Q4: playbook_guide returned 5 only; 11 (cut LinkedIn, branded search falls; "Finance wants to cut creation first") and 3 (never judge creation on last click) are missing. No "Redavio tools to call next" line, though section 5 lists Marketing Correlation Analyzer.
- Q6: playbook_guide returned 4 only; 3 has the full proof-of-cause list. Tools line suggests Landing Page Analyzer, Ad Copy Analyzer and Ad Budget Optimizer, none of which bear on incrementality; Marketing Correlation Analyzer (with "correlation is not proof") fits.
- Q7: the playbook contradicts itself: 02 says review 20 recent MQLs with Sales, 11 says pull ten rejected leads.
- Q8: playbook_guide adds section 12 (off topic) and suggests Research Agent. playbook_deliverable refuses regular-updates without pipeline_goal and deal_size, so an unfilled weekly template can't be had from the tool (fill.py has the same requirement).
- Q9: section 1 step 5 says open the QBR with the four principle scores, but the QBR outline in planning-and-review-decks.md has no slide for them. No tools line.
- Q10: product-led planning doc labels the second stage "PQLs (meeting scheduled)", carrying the sales-led SQL description over. defaults.md has no product-led rates or cost per signup (sales-led 25% and $300 are reused), and the plan has no activation stage although 02 says optimize to activation. playbook_guide returned 2 only; 3 has the product-led stage mapping.
- Q12: no "Redavio tools to call next" line, although section 9 maps Ad Budget Optimizer to D2/D4/M4 and Research Agent to M6.
- Q13: playbook_guide returned 4 only; 12 (ChatGPT ads, AI answers as a channel) is missing. Tools line suggests Landing Page/Ad Copy Analyzers and Ad Budget Optimizer; section 4's own pick for AEO is Marketing Correlation Analyzer (AI mentions vs direct traffic).
- Q14: playbook_guide returned 2 and 4 but not 7 (sample size, run time). No rule for "landing pages convert at X%" (is it low, which rate is meant, what to check first); the only sample-size example is a 3% baseline.
- Q3: tools line lists Ad Budget Optimizer twice.
- playbook_guide with `section` set still appends sections matched from the question (a junk question falls back to 2 and 3), so it doesn't return only the section asked for.
