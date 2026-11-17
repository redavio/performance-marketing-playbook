# Default inputs

Every deliverable starts from these. Each one is a rule of thumb, not a benchmark: replace it with your own number as soon as you have three months of data. The planning doc and budget tracker print which values are defaults so nobody mistakes them for yours.

## Required (you enter these)

| Input | Example | Notes |
| --- | --- | --- |
| Pipeline goal | $3,000,000 per year | The dollar value of new SAOs you need. Add a revenue goal too if you have one. |
| Average deal size | $30,000 | First-year contract value of a closed-won deal. |

## Optional (defaults shown)

| Input | Default | Notes |
| --- | --- | --- |
| Revenue goal | Pipeline goal × win rate | If you enter it, the tracker works back from revenue instead. |
| Period | 12 months | Use 3 for a quarterly plan. |
| Motion | Sales-led | Product-led swaps MQL for signup and SQL for product-qualified lead (PQL). |
| MQL → SQL | 25% | Hand-raisers (demo, contact) usually convert far higher than content leads; split them once you can. |
| SQL → SAO | 60% | Meetings held that Sales accepts as opportunities. |
| SAO → Closed won (win rate) | 20% | |
| Sales cycle | 90 days | SAO to closed won. Sets how far ahead pipeline must be built. |
| Capture / creation split | 60% / 40% of budget | Shift toward creation as branded search and direct traffic grow. |
| Cost per MQL, capture | $300 | Blended across paid search and other capture channels. |
| Cost per MQL, creation | $450 | Blended across paid social, ABM and other creation channels. Creation MQLs are fewer and slower; its pipeline is credited with lower confidence. |
| Channels | Google Ads, Microsoft Ads, LinkedIn Ads | Add or remove freely. |
| CRM | HubSpot | Any CRM works; map your own stage names. |
| Competitors | none entered | Listed in the planning doc and used for competitor search terms. |
| ICP | none entered | Company size, industry, buyer titles. |

## The math (same in the skill, the MCP server and the sheet)

Working back from the goal:

1. SAOs needed = pipeline goal ÷ average deal size
2. SQLs needed = SAOs ÷ (SQL → SAO)
3. MQLs needed = SQLs ÷ (MQL → SQL)
4. Blended cost per MQL = capture cost × capture share + creation cost × creation share
5. Budget = MQLs needed × blended cost per MQL
6. Capture budget = budget × capture share; creation budget = budget × creation share
7. Expected revenue = pipeline goal × win rate (or, if a revenue goal is given, pipeline goal = revenue goal ÷ win rate first)
8. Cost per SAO = budget ÷ SAOs; pipeline-to-spend ratio = pipeline goal ÷ budget

Monthly plan = each number ÷ months in the period, so plan vs actual can be tracked month by month.

Rounding is for display only. The tracker, the skill and the MCP server keep full precision in the math and round half up when they show a number, so 666.7 MQLs × $360 = $240,000 even though the doc shows 667.
