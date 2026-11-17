# {{company}}: slide template

The base deck every presentation uses: the weekly update (if slides are asked for), the monthly report, the QBR, the annual plan and postmortems. The PowerPoint file [slide-template.pptx](https://github.com/redavio/performance-marketing-playbook/blob/main/deliverables/slide-template.pptx) has these layouts (fill.py writes a copy with your plan numbers filled in); it opens in Google Slides. Your AI can also build the deck in Google Slides from this outline through its own connector.

## Rules

- One message per slide, written as the title in a full sentence ("Pipeline is 12% behind plan because LinkedIn cost per lead doubled"), not a label ("Pipeline").
- Numbers come from the budget tracker. Every chart says the period and the source.
- Green, amber, red for status vs plan: green at or above 100% of plan to date, amber 80-99%, red below 80% (rule of thumb).
- No more than 3 bullets per slide. Detail goes in an appendix.

## Layouts

1. **Title:** deck name, {{company}}, period, presenter.
2. **Headline:** one sentence and 3-4 large numbers (pipeline vs plan, SAOs, spend, cost per SAO).
3. **Funnel vs plan:** table of {{MQLs}} → {{SQLs}} → SAOs → closed won with plan, actual, variance and status color.
4. **Trend:** one chart (e.g. pipeline by month vs plan), title states the takeaway.
5. **Drivers:** two columns, "Levers we control" and "Outside forces".
6. **Capture vs creation:** two columns, each with its own measures.
7. **Tests:** table of test, result, decision.
8. **Plan:** goal, budget ({{budget}} for the period in this plan), priorities.
9. **Asks and risks.**
10. **Appendix:** detail tables.

## Numbers for {{company}}

Put these plan numbers on the slides; fill actuals from the budget tracker.

| Slide | Plan numbers |
| --- | --- |
| 1. Title | {{company}}, {{period}} |
| 2. Headline | Pipeline {{pipeline_goal}}, SAOs {{saos}}, spend {{budget}}, cost per SAO {{cost_per_sao}} |
| 3. Funnel vs plan | {{MQLs}} {{mqls}}, {{SQLs}} {{sqls}}, SAOs {{saos}}, pipeline {{pipeline_goal}}, closed won {{closed_won}}, spend {{budget}} |
| 4. Trend | Pipeline plan {{monthly_pipeline}} a month |
| 6. Capture vs creation | Capture budget {{capture_budget}}, creation budget {{creation_budget}} |
| 8. Plan | Goal {{pipeline_goal}} pipeline, {{revenue}} expected closed won; budget {{budget}}; {{mqls}} {{MQLs}} → {{sqls}} {{SQLs}} → {{saos}} SAOs |
