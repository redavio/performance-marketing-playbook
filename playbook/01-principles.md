# 1. Principles

## Why it matters

Four principles sit under every section of this playbook. Use them to decide what to work on, to check a plan before it ships, and to explain your approach to your boss.

| Principle | What it means in practice |
| --- | --- |
| Strategic alignment | Work ties to business goals: pipeline and revenue targets, unit economics, budget, voice of customer, positioning, and Sales. |
| Operational excellence | Work runs efficiently and is automated where it can be: recurring routines, connected tools (APIs, MCP servers), alerts, clean handoffs. |
| Rapid experimentation | You are always testing, with a backlog, a scoring method, a test log and readouts. |
| Data driven | Clean tracking, a value on each conversion, data joined across sources, and proof of cause where it matters. |

These are plain names on purpose. Rename them if your company already has its own words for the same ideas. Keep the meaning.

## Ask first

- Which of the four is weakest today? That is usually where the next quarter's work should go.
- Does every initiative on your list tie to at least one principle? If not, why is it on the list?
- Who else needs to use them: Sales, RevOps, Finance, an agency? Agree the names with them once.

## Do this

1. **Score yourself.** Rate each principle 1 to 5 against the checks below. Write one sentence of evidence for each score.
   - Strategic alignment: you can state the pipeline goal, average deal size and CAC payback target from memory, and Sales agrees with your stage definitions. See [Align to the business](02-align-to-the-business.md).
   - Operational excellence: daily and weekly checks run on a calendar, spend and tracking alerts exist, and nothing depends on one person remembering. See [Operating rhythm](09-operating-rhythm.md) and [Operations and AI](10-operations-and-ai.md).
   - Rapid experimentation: there is a written backlog, at least one test is live, and finished tests have a readout. See [Experimentation](07-experimentation.md).
   - Data driven: conversions flow from the CRM back to the ad platforms, each conversion has a value, and you know which numbers are proven and which are only attributed. See [Measurement](03-measurement.md).
2. **Fix the lowest score first.** Default order when everything is weak: data driven (you cannot judge anything without tracking), then strategic alignment, then operational excellence, then rapid experimentation.
3. **Tag every initiative.** Add a "Principle" column to your initiative list, the Priorities table in the planning doc, and the experiment database. Give each item one primary tag and at most one secondary tag. Example:

   | Initiative | Primary | Secondary |
   | --- | --- | --- |
   | Send closed-won deals back to Google and Microsoft Ads | Data driven | Strategic alignment |
   | Set daily alerts for spend and broken tracking | Operational excellence | |
   | Test a pricing-page offer against a demo offer | Rapid experimentation | Data driven |
   | Agree MQL and SQL definitions with Sales | Strategic alignment | |

4. **Check the balance each quarter.** Count initiatives by primary tag. If one principle has none, ask whether that is a choice or a gap. A rule of thumb: no principle should go a full quarter with zero initiatives.
5. **Use them in reviews.** Add a principles scorecard slide to the QBR: the four scores and how they moved. See [Reporting and communication](08-reporting-and-communication.md) and the [planning and review decks](../deliverables/planning-and-review-decks.md).
6. **Put the tags in your files.** The Priorities table in the [planning doc](../deliverables/planning-doc.md) has a Principle column, and so do the [experiment database](../deliverables/experiment-database.csv) and [recurring tasks](../deliverables/recurring-tasks.csv). Keep the names identical across them so you can filter.

## If you see X, do Y

- **Lots of tests, no tie to pipeline:** stop and score each test's link to the pipeline goal before starting more. That is a strategic alignment gap.
- **Good strategy, everything done by hand:** automate the checks you repeat weekly before adding new work.
- **Reports full of numbers nobody trusts:** pause optimization and fix tracking first.
- **Every initiative tagged with all four:** you are not choosing. Force one primary tag.
- **A leader asks "why are we doing this?":** answer with the principle and the goal it serves in one sentence. If you cannot, drop it.

## Metrics

- The four self-scores, 1 to 5, tracked quarterly.
- Share of initiatives by primary principle.
- Share of initiatives that shipped versus planned, by principle.

## Common mistakes

- Treating principles as a poster. They are a filter for what to do and what to drop.
- Renaming them every quarter, which breaks filtering and history.
- Tagging after the fact to justify work already chosen.
- Starting with experiments before tracking works. You cannot read a test you cannot measure.

## Call an expert when

- You score 1 or 2 on data driven and do not know where tracking breaks.
- Leadership disagrees on the goal you are aligning to. That is a business decision, not a marketing one.
- You cannot tell which of the four is weakest.

## Tools and sources

**Related tools**

- [Marketing Correlation Analyzer](https://www.redavio.com/marketing-correlation) (Exists): checks whether two metrics move together. Useful for the data driven score.
- [Ad Budget Optimizer](https://www.redavio.com/budget-optimizer) (Exists, free): applies budget changes on Google and Microsoft Ads after you approve. An operational excellence quick win.
- [performance-os](https://github.com/redavio/performance-os) (Exists, open source): the deep paid search how-to, organized the same way.
- All Redavio tools are listed in the [Library](https://www.redavio.com) and run through the [Redavio MCP server](https://www.redavio.com/mcp-server).

**Outside sources**

- [Exit Five](https://www.exitfive.com/): B2B marketing community and newsletter; good for how other B2B teams run their programs.
- [Exit Five: 8 steps to survive annual planning](https://exitfive.com/newsletter/8-steps-to-survive-annual-planning/): tying marketing work to finance's numbers, which is strategic alignment in practice.
- [Lenny's Newsletter](https://www.lennysnewsletter.com/): growth and experimentation practice from operators.
- [SaaStr](https://www.saastr.com/): B2B SaaS go-to-market and how marketing is judged by founders and boards.
