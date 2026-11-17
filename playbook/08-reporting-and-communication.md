# 8. Reporting and communication

## Why it matters

Leaders fund what they understand. Short, regular updates tied to the pipeline goal keep budget, trust and Sales on your side, and postmortems make sure each quarter teaches the next one.

## Ask first

- Who reads each update, and what decision do they make with it? (CEO: keep funding. CFO: spend vs plan. Sales: lead volume and quality.)
- What is the goal everyone agreed to? Use the pipeline goal and funnel stages from the [planning doc](../deliverables/planning-doc.md) and [02-align-to-the-business](02-align-to-the-business.md).
- Which numbers are the source of truth: CRM for pipeline, ad platforms for spend? Settle this once (see [03-measurement](03-measurement.md)).
- Where do updates go: email, Slack, a doc, a meeting?

## Do this

1. **Build every update on one base deck.** Start from [slide-template.md](../deliverables/slide-template.md) so numbers, charts and stage names look the same everywhere.
2. **Lead with the goal, not the channels.** Every update opens with: pipeline (SAOs) vs goal, spend vs budget, cost per SAO. Channel detail comes after.
3. **Send the five regular pieces below on schedule.** Same day, same format, every time.

| Piece | Who it's for | What goes in it | When it goes out | Template |
| --- | --- | --- | --- | --- |
| **Weekly update** | Marketing lead, Sales leader, CEO at a startup | Results vs goal (MQL, SQL, SAO, spend), what changed, what's next, asks. Under one page. | Every Monday by noon, covering the prior Monday to Sunday | [regular-updates.md](../deliverables/regular-updates.md) |
| **Monthly report** | Leadership, Finance, Sales | Month vs plan by funnel stage and channel, capture vs creation, budget plan vs actual, test readouts, next month's plan and budget shifts | By the 5th business day of the month | [regular-updates.md](../deliverables/regular-updates.md), numbers from [budget-tracker.csv](../deliverables/budget-tracker.csv) |
| **QBR** | Leadership, Finance, Sales leadership | The quarter's review plus next quarter's plan: results vs goal to date, what worked, what didn't and why, tests and lessons, next quarter's goal, budget and top bets | In the last 2 weeks of the quarter, so next quarter's plan is agreed before it starts | [planning-and-review-decks.md](../deliverables/planning-and-review-decks.md) |
| **Quarterly plan** | Marketing lead, Finance | Goal, back-math from pipeline to budget, channel split, top 3 to 5 initiatives, test plan | Agreed in the QBR | [planning-doc.md](../deliverables/planning-doc.md), [budget-tracker.csv](../deliverables/budget-tracker.csv) |
| **Annual plan** | CEO, CFO, board | Annual pipeline and revenue goal, unit economics, budget by quarter and channel, capture vs creation split, hiring and tools | Drafted 8 weeks before the year starts, final 4 weeks before (rule of thumb) | [planning-and-review-decks.md](../deliverables/planning-and-review-decks.md), [planning-doc.md](../deliverables/planning-doc.md) |

4. **Write postmortems for the year, the quarter, and any test, launch or campaign.**
   - Who it's for: the team, plus whoever funded the work.
   - What goes in it: the goal, what happened (numbers vs goal), why (the drivers of the gap), what we'll keep, stop and start, and owners for each follow-up.
   - When: within 2 weeks after the end. The quarter postmortem follows the QBR and closes out the final weeks' numbers; the year postmortem does the same for the annual plan. Their lessons feed the next cycle.
   - Template: [planning-and-review-decks.md](../deliverables/planning-and-review-decks.md).
   - Keep them blameless. Look for causes in the plan, data and process, not in people.
5. **Explain gaps with drivers.** When a number misses, break it into its parts: was it spend, cost per click, conversion rate or stage conversion? Say which lever moved and which one you will pull next.
6. **Separate capture from creation.** Report each on its own measures ([Measurement](03-measurement.md#measuring-capture-vs-creation)), side by side. Label creation's [influenced pipeline](03-measurement.md#influenced-pipeline) lower confidence.
7. **End every piece with asks.** Budget, help from Design or Dev, a decision. If there are none, say "no asks".
8. **Use the same numbers in every surface.** The weekly, monthly and QBR numbers must reconcile. Pull them from one tracker.

## If you see X, do Y

- **Leaders ask the same question every week:** add the answer to the template permanently.
- **CRM and platform numbers disagree:** report CRM for pipeline and note the gap once. Fix tracking in [03-measurement](03-measurement.md).
- **A bad month:** send it on time anyway, with the cause and the fix. Late bad news costs more trust than bad news.
- **Nobody reads the weekly:** cut it to five lines and send it where they already work.
- **Sales says leads are bad:** add MQL to SQL rate by channel to the weekly and review it with them.

## Metrics

Every regular piece shows these, in this order:

- SAOs and pipeline vs goal, month and quarter to date.
- Spend vs budget, and pacing.
- Cost per SAO and pipeline-to-spend ratio.
- MQL, SQL and SAO counts with stage conversion rates.
- Capture vs creation split of spend and credited pipeline.
- Tests finished and their results.

## Common mistakes

- Leading with clicks, impressions or platform-reported conversions instead of pipeline.
- A different format every week, so nobody can compare.
- Reporting what happened without why or what's next.
- Skipping postmortems when things went well. Wins need explaining too.
- Judging creation channels on last click.
- Changing a goal mid-quarter without saying so in writing.

## Call an expert when

- The board or CFO wants a model of pipeline by channel with confidence ranges.
- You need multi-touch attribution or proof of cause to defend a budget.
- Finance and Marketing disagree on what counts as pipeline. Bring in RevOps.

## Tools and sources

**Related tools**

- Driver breakdown (Planned): shows which drivers explain a gap to goal. Built for postmortems and the "why" in each update.
- [Marketing Correlation Analyzer](https://www.redavio.com/marketing-correlation) (Exists): checks which channels move together, useful when explaining creation's effect on capture.
- All Redavio tools are listed in the [Library](https://www.redavio.com) and run through the [Redavio MCP server](https://www.redavio.com/mcp-server). Your AI can pull tool results straight into a report draft.

**Outside sources**

- [Google SRE book: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/): the clearest guide to blameless postmortems. Written for engineering, works for campaigns.
- [Atlassian: Incident postmortems](https://www.atlassian.com/incident-management/postmortem): a practical postmortem process and template.
- [Exit Five](https://www.exitfive.com/): B2B marketing community, good for seeing how other teams report to leadership.
- [Looker Studio](https://lookerstudio.google.com/): free dashboards that connect to Google Ads and Sheets for the weekly numbers.
