# {{company}}: performance marketing plan

Period: {{period}}. Motion: {{motion}}. Values marked "(default)" are rules of thumb from [defaults.md](https://github.com/redavio/performance-marketing-playbook/blob/main/deliverables/defaults.md); replace them with your own numbers when you have them.

## 1. Goals

- Pipeline goal: **{{pipeline_goal}}** in new SAOs ({{monthly_pipeline}} a month).
- Expected closed-won revenue: **{{revenue}}** at a {{win_rate}} win rate.
- Average deal size: {{deal_size}}. Sales cycle: {{sales_cycle_days}}.

## 2. Funnel stages and what it takes

| Stage | Needed this period | Per month | Conversion to next stage |
| --- | --- | --- | --- |
| {{MQLs}} | {{mqls}} | {{monthly_mqls}} | {{mql_to_sql}} to {{SQL}} |
| {{SQLs}} ({{sql_meaning}}) | {{sqls}} | {{monthly_sqls}} | {{sql_to_sao}} to SAO |
| SAOs (pipeline) | {{saos}} | {{monthly_saos}} | {{win_rate}} to closed won |
| Closed won | {{closed_won}} | {{monthly_closed_won}} | |

Stage names in {{crm}} may differ. Map yours to these before the first report.

## 3. Unit economics

- Blended cost per {{MQL}}: {{blended_cost_per_mql}} (capture {{cost_per_mql_capture}}, creation {{cost_per_mql_creation}}).
- Cost per SAO: {{cost_per_sao}}.
- Pipeline to spend: {{pipeline_to_spend}}.
- Add CAC, payback and LTV once Finance shares gross margin and retention. See [Align to the business](https://github.com/redavio/performance-marketing-playbook/blob/main/playbook/02-align-to-the-business.md).

## 4. Who we sell to

- ICP: {{icp}}.
- Competitors: {{competitors}}.
- Voice of customer: add the top 3 reasons customers buy and the top 3 objections, in their words, from sales calls and reviews.

## 5. Channel mix

| | Share | Budget | Channels | Judged on |
| --- | --- | --- | --- | --- |
| Demand capture | {{capture_share}} | {{capture_budget}} | Paid search, SEO, AEO, review sites, website CRO | Pipeline, cost per SAO, short window |
| Demand creation | {{creation_share}} | {{creation_budget}} | Paid social, YouTube and CTV, display and retargeting, ABM, sponsorships, syndication | Target-account engagement, self-reported source, velocity, longer window |

Expected {{MQLs}}: capture {{capture_mqls}}, creation {{creation_mqls}}.

Budget by channel (equal split within each group unless you set shares; change them in the tracker):

| Channel | Type | Share | Budget | Per month |
| --- | --- | --- | --- | --- |
{{channel_rows}}

## 6. Budget

- Total: **{{budget}}** ({{monthly_budget}} a month), worked back from the pipeline goal.
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
| Offline conversions for {{SQL}} and SAO live in every ad platform | Data driven | | |
| Agree {{MQL}}, {{SQL}} and SAO definitions with Sales | Strategic alignment | | |
| Weekly update and budget tracker running | Operational excellence | | |
| First three tests from the experiment database | Rapid experimentation | | |

## 10. Risks and asks

- Risk: rule-of-thumb defaults used for: {{defaults_used}}. Replace them with your last 3 months of actuals by the first QBR.
- Ask: Sales agrees the SAO definition and updates stages within two business days.
