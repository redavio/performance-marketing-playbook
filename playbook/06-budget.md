# 6. Budget

## Why it matters

Budget is the biggest lever you control. Work it back from the pipeline goal so the number is defensible, then move each dollar to where the next one returns the most.

## Ask first

- What is the pipeline goal (and revenue goal, if any) for the period?
- What is the average deal size?
- Do you have your own stage conversion rates and cost per MQL, or will you start from the [defaults](../deliverables/defaults.md)?
- Is the budget fixed by Finance, or are you proposing one?
- How long is the sales cycle? Spend this quarter becomes pipeline and revenue later.
- Which channels are live, and which are tests?

## Do this

1. **Back into the budget from the goal.** Use this math (same in the [budget tracker](../deliverables/budget-tracker.csv), the skill and the MCP server). Example with the defaults: $3,000,000 pipeline goal, $30,000 deal, 12 months.

   | Step | Formula | Default example |
   | --- | --- | --- |
   | SAOs needed | Pipeline goal ÷ deal size | $3,000,000 ÷ $30,000 = 100 |
   | SQLs needed | SAOs ÷ SQL to SAO rate | 100 ÷ 60% = 167 |
   | MQLs needed | SQLs ÷ MQL to SQL rate | 167 ÷ 25% = 667 |
   | Blended cost per MQL | Capture cost × capture share + creation cost × creation share | $300 × 60% + $450 × 40% = $360 |
   | Budget | MQLs × blended cost per MQL | 667 × $360 = $240,000 |
   | Capture / creation | Budget × each share | $144,000 / $96,000 |
   | Expected revenue | Pipeline goal × win rate | $3,000,000 × 20% = $600,000 |
   | Cost per SAO | Budget ÷ SAOs | $2,400 |
   | Pipeline-to-spend | Pipeline goal ÷ budget | 12.5 to 1 |

   Figures are rounded for display; the tracker keeps full precision ($240,000 comes from 666.7 MQLs). If you have a revenue goal instead, set pipeline goal = revenue goal ÷ win rate first. Monthly plan = each number ÷ months in the period: here $20,000 a month and about 8 SAOs.

2. **Sanity-check the result.** Compare cost per SAO to what your unit economics allow (see [Align to the business](02-align-to-the-business.md)). If it does not fit, change the goal, raise conversion rates or lower cost per MQL. Do not quietly cut the budget and keep the goal.

3. **Split capture and creation.** Default 60% capture, 40% creation (rule of thumb). Capture (paid search) harvests demand that exists and is limited by search volume. Creation (LinkedIn, ABM, sponsorships) builds demand and pays back later. Shift toward creation as branded search and direct traffic grow, which signals capture is near its ceiling. Credit creation's pipeline where you can (self-reported source, influenced pipeline) and label it lower confidence. See [Measurement](03-measurement.md).

4. **Allocate by marginal return.** The question is not which channel has the best average cost per SAO, but where the next $1,000 buys the most. Signs a campaign can take more: high impression share lost to budget, cost per SAO well under target, a steady trend. Signs it is saturated: cost per SAO rising as spend rises, impression share already high. Default moves:
   - Move money in steps of 20% or less per campaign, then wait one to two weeks to read the result (rule of thumb).
   - Take from the campaign with the worst cost per SAO at the margin, give to the one with headroom and good cost per SAO.
   - Keep 10% of budget for tests (rule of thumb). See [Experimentation](07-experimentation.md).
   Google's Performance Planner shows forecast curves for search campaigns. The [Ad Budget Optimizer](https://www.redavio.com/budget-optimizer) recommends these moves and applies them on Google and Microsoft Ads after you approve.

5. **Pace weekly.** Each Monday compare spend month to date against plan month to date (monthly plan × share of the month gone). Defaults:
   - Within ±10% of plan: leave it.
   - More than 10% over: lower daily budgets on the campaigns with the worst marginal return.
   - More than 10% under: check for limits (low bids, narrow targeting, disapproved ads) before adding budget.
   Platforms do not spend evenly. Google can overspend a daily budget on busy days while holding the monthly total, so judge pacing on the month, not single days.

6. **Forecast with the lag.** SAOs from this month's spend close one sales cycle later (90 days by default). Each month, update the forecast with actual stage rates and cost per MQL from the last three months. Report three numbers: plan, actual to date, and forecast for the period end.

7. **Plan annually, revise quarterly.**
   - Annual: set the goal, run the math, split capture and creation, name the tests. Present it with the [annual plan deck](../deliverables/planning-and-review-decks.md).
   - Quarterly: rerun the math with real rates, move budget between channels by marginal return, and reset the test reserve. Present it in the QBR. See [Reporting and communication](08-reporting-and-communication.md).
   - Build pipeline one sales cycle ahead: Q1 revenue needs Q4 pipeline.

8. **Use the budget tracker.** Open [budget-tracker.csv](../deliverables/budget-tracker.csv) (or the Google Sheet your AI builds from it).
   - Enter pipeline goal and deal size. Replace defaults with your numbers as you get them; defaults are marked so nobody mistakes them for yours.
   - It returns SAOs, SQLs, MQLs and budget by channel, split capture and creation, by month.
   - Each month, enter actual spend, MQLs, SQLs, SAOs and pipeline by channel. It shows plan vs actual and the gap.
   - Review it in the weekly update and rerun it each quarter.

## If you see X, do Y

- **Cost per SAO above plan two months in a row:** check stage rates first. If MQL to SQL dropped, the problem is lead quality, not budget.
- **Capture campaigns limited by budget with good cost per SAO:** move money there from the weakest campaign.
- **Capture spend rising but SAOs flat:** you are past saturation. Hold spend and fund creation or tests.
- **Underspending all month:** look for bid targets set too tight or narrow targeting before raising budgets.
- **Finance cuts the budget:** rerun the math and show the new pipeline the budget buys. Agree a new goal in writing.
- **Creation shows no pipeline after one quarter:** check self-reported answers and target-account engagement before cutting; its window is longer.

## Metrics

- Spend vs plan, month to date and quarter to date.
- Cost per MQL, SQL and SAO by channel.
- Pipeline-to-spend ratio.
- Impression share lost to budget (search).
- Marginal cost per SAO after each budget move.
- Forecast vs actual pipeline at period end.

## Common mistakes

- Setting budget from last year's spend plus a percentage, with no link to the goal.
- Moving budget to the best average channel instead of the best marginal one.
- Big budget swings every few days, so no change can be read.
- Judging this quarter's spend on this quarter's revenue, ignoring the sales cycle.
- Keeping default rates after you have real ones.

## Call an expert when

- Spend is above roughly $50,000 a month and you are moving it by hand (rule of thumb).
- You need a forecast model beyond the funnel math, such as diminishing-returns curves or media mix modeling.
- Finance wants a budget defended at board level.
- Results swing a lot and you cannot tell noise from a real change.

## Tools and sources

**Related tools**

- [Ad Budget Optimizer](https://www.redavio.com/budget-optimizer) (Exists, free): recommends budget moves and applies them on Google and Microsoft Ads after you approve.
- [Marketing Correlation Analyzer](https://www.redavio.com/marketing-correlation) (Exists): checks whether spend and pipeline move together.
- [performance-os](https://github.com/redavio/performance-os) (Exists, open source): paid search budget rebalancing and pacing in depth.
- Driver breakdown (Planned): which drivers explain a gap to goal.
- All Redavio tools are reachable by your AI through the [Redavio MCP server](https://www.redavio.com/mcp).

**Outside sources**

- [Google Ads Help: About Performance Planner](https://support.google.com/google-ads/answer/9230124): forecasting what more or less spend would do on Google.
- [Exit Five: 8 steps to survive annual planning](https://exitfive.com/newsletter/8-steps-to-survive-annual-planning/): building and getting a plan approved, with strategic and experimental budget buckets.
- [Bessemer, Scaling to $100 Million](https://www.bvp.com/atlas/scaling-to-100-million): CAC payback targets to check your budget against.
- [David Skok, SaaS Metrics 2.0](https://www.forentrepreneurs.com/saas-metrics-2/): how acquisition spend links to payback and LTV.
- [Search Engine Land: PPC budget planning](https://searchengineland.com/ppc-budget-planning-aligning-business-goals-ad-spend-performance-458150): aligning paid search spend with business goals.
