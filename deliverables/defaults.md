# Default inputs

Every deliverable starts from these. Each one is a rule of thumb, not a benchmark: replace it with your own number as soon as you have three months of data. The planning doc and budget tracker mark which values are defaults so nobody mistakes them for yours.

## Required (you enter these)

| Input | Example | Notes |
| --- | --- | --- |
| Pipeline goal | $3,000,000 per year | The dollar value of new SAOs you need. Or enter a revenue goal instead (below). |
| Average deal size | $30,000 | First-year contract value of a closed-won deal. |

## Optional (defaults shown)

| Input | Default | Notes |
| --- | --- | --- |
| Revenue goal | none | Closed-won revenue. If you give no pipeline goal, pipeline goal = revenue goal ÷ win rate. If you give both, the pipeline goal is used and the revenue goal is shown for reference. |
| Period | 12 months | Use 3 for a quarterly plan. |
| Start date | The next Monday | Sets month names in the tracker and first due dates in the task list. |
| Motion | Sales-led | Product-led swaps MQL for signup and SQL for product-qualified lead (PQL). The default rates below are sales-led; replace them with your own signup-to-PQL and PQL-to-opportunity rates. |
| MQL → SQL | 25% | SQL = meeting scheduled. Hand-raisers (demo, contact) usually convert far higher than content leads; split them once you can. |
| SQL → SAO | 60% | Meetings that Sales accepts as opportunities. |
| SAO → Closed won (win rate) | 20% | |
| Sales cycle | 90 days | SAO to closed won. Sets how far ahead pipeline must be built. |
| Cost per MQL from capture channels | $300 | Blended across paid search, review sites and other capture channels. |
| Creation share of budget | 30% of the total | Added on top of what capture needs. Creation is never counted toward the pipeline goal: no MQLs or pipeline are assigned to it in the plan. Grow the share as target-account engagement, branded search and self-reported source show it working. |
| Channels | Google Ads, Microsoft Ads, LinkedIn Ads | Add or remove freely. A channel with search, SEO, AEO, G2, Capterra or review in its name counts as capture; the rest count as creation. |
| Channel shares | Equal within each group | Optional share of its group's budget per channel, e.g. Google Ads 80% and Microsoft Ads 20% of capture. |
| CRM | HubSpot | Any CRM works; map your own stage names. |
| Competitors | none entered | Listed in the planning doc and used for competitor search terms. |
| ICP | none entered | Company size, industry, buyer titles. |

## The math (same in the skill, the MCP server and the sheet)

The pipeline goal is worked back through demand capture only. Demand creation (LinkedIn, Meta, YouTube, ABM, sponsorships) builds demand that shows up later and elsewhere, so the plan never assumes it produces MQLs or pipeline. It gets a set share of budget on top and is judged on its own measures (see the measurement section).

1. SAOs needed = pipeline goal ÷ average deal size
2. SQLs needed = SAOs ÷ (SQL → SAO)
3. MQLs needed from capture = SQLs ÷ (MQL → SQL)
4. Capture budget = MQLs needed × cost per MQL from capture channels
5. Total budget = capture budget ÷ (1 − creation share)
6. Creation budget = total budget × creation share
7. Each channel's budget = its group's budget × its share
8. Expected closed-won revenue = pipeline goal × win rate
9. Cost per SAO = total budget ÷ SAOs (capture cost per SAO = capture budget ÷ SAOs); pipeline to spend = pipeline goal ÷ total budget

Monthly plan = each number ÷ months in the period, so plan vs actual can be tracked month by month. Variances compare actuals only with the months that have actuals.

Example at the defaults: $3,000,000 ÷ $30,000 = 100 SAOs → 167 SQLs → 667 MQLs from capture. Capture budget = 667 × $300 = $200,000. Total = $200,000 ÷ 0.7 = $285,714, so creation gets $85,714 and no MQLs are assigned to it.

Rounding is for display only. The tracker, the skill and the MCP server keep full precision and round half up when they show a number.
