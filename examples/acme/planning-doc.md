# Acme Analytics: performance marketing plan

Period: 12 months from Jan 2027 (default). Motion: sales-led. Values marked "(default)" are rules of thumb from [defaults.md](https://github.com/redavio/performance-marketing-playbook/blob/main/deliverables/defaults.md); replace them with your own numbers when you have them.

## 1. Goals

- Pipeline goal: **$3,000,000** in new SAOs ($250,000 a month).
- Expected closed-won revenue: **$600,000** at a 20% (default) win rate.
- Average deal size: $30,000. Sales cycle: 90 days (default).

## 2. Funnel stages and what it takes

| Stage | Needed this period | Per month | Conversion to next stage |
| --- | --- | --- | --- |
| MQLs | 667 | 56 | 25% (default) to SQL |
| SQLs (meeting scheduled) | 167 | 14 | 60% (default) to SAO |
| SAOs (pipeline) | 100 | 8.3 | 20% (default) to closed won |
| Closed won | 20 | 1.7 | |

Stage names in HubSpot (default) may differ. Map yours to these before the first report.

## 3. Unit economics

- Cost per MQL from capture channels: $300 (default). Capture cost per SAO: $2,000.
- Cost per SAO including creation: $2,857.
- Pipeline to spend: 10.5x.
- Add CAC, payback and LTV once Finance shares gross margin and retention. See [Align to the business](https://github.com/redavio/performance-marketing-playbook/blob/main/playbook/02-align-to-the-business.md).

## 4. Who we sell to

- ICP: US software companies, 200-2,000 employees; VP Finance and Controllers.
- Competitors: Northwind, Contoso.
- Voice of customer: add the top 3 reasons customers buy and the top 3 objections, in their words, from sales calls and reviews.

## 5. Channel mix

| | Share | Budget | Channels | Judged on |
| --- | --- | --- | --- | --- |
| Demand capture | 70% (default) | $200,000 | Paid search, SEO, AEO, review sites, website CRO | Pipeline, cost per SAO, short window |
| Demand creation | 30% (default) | $85,714 | Paid social, YouTube and CTV, display and retargeting, ABM, sponsorships, syndication | Target-account engagement, self-reported source, velocity, longer window |

The goal is worked back through demand capture only: all 667 MQLs are planned from capture channels. Demand creation (30% (default) of budget) is not counted toward the goal and is assigned no MQLs or pipeline. Some non-hand-raiser leads may come from it; treat them as a bonus. Judge it on target-account engagement, self-reported source and influenced pipeline.

Budget by channel (equal split within each group unless you set shares; change them in the tracker):

| Channel | Type | Share | Budget | Per month |
| --- | --- | --- | --- | --- |
| Google Ads | capture | 50% of capture | $100,000 | $8,333 |
| Microsoft Ads | capture | 50% of capture | $100,000 | $8,333 |
| LinkedIn Ads | creation | 100% of creation | $85,714 | $7,143 |

## 6. Budget

- Total: **$285,714** ($23,810 a month), worked back from the pipeline goal.
- Track plan vs actual monthly in the budget tracker (budget-tracker.csv).
- Rebalance monthly by marginal return. See [Budget](https://github.com/redavio/performance-marketing-playbook/blob/main/playbook/06-budget.md).

## 7. Measurement

- Primary conversion: SAO, sent back to ad platforms as an offline conversion with its value.
- Capture proof of cause: brand vs non-brand checks, geo holdouts.
- Creation proof of cause: lift tests, holdout accounts.
- See [Measurement](https://github.com/redavio/performance-marketing-playbook/blob/main/playbook/03-measurement.md).

## 8. First 90 days

1. Weeks 1-2: tracking and offline conversions working end to end; stage names mapped.
2. Weeks 3-4: capture channels live on the core terms; budget tracker filled.
3. Month 2: first creation programs live; self-reported "how did you hear about us" field on every form.
4. Month 3: first tests from the experiment database (experiment-database.csv); first QBR.

## 9. Priorities

| Initiative | Principle | Owner | Due |
| --- | --- | --- | --- |
| Offline conversions for SQL and SAO live in every ad platform | Data driven | | |
| Agree MQL, SQL and SAO definitions with Sales | Strategic alignment | | |
| Weekly update and budget tracker running | Operational excellence | | |
| First three tests from the experiment database | Rapid experimentation | | |

## 10. Risks and asks

- Risk: rule-of-thumb defaults used for: MQL to SQL rate, SQL to SAO rate, win rate, sales cycle, creation share of budget, cost per MQL from capture channels. Replace them with your last 3 months of actuals by the first QBR.
- Ask: Sales agrees the SAO definition and updates stages within two business days.
