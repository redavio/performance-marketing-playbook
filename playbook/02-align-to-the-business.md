# 2. Align to the business

## Why it matters

Paid acquisition is judged on pipeline and revenue, not clicks. If you do not know the goal, the deal size and what a customer is worth, you cannot tell good spend from bad.

## Ask first

- What is the pipeline goal for the year or quarter? Is there a revenue goal too?
- What is the average deal size (first-year contract value)?
- What is the win rate, and how long is the sales cycle from opportunity to close?
- Is the motion sales-led (demo, then sales) or product-led (signup, then usage, then sales or self-serve)?
- What CAC payback does Finance expect? What gross margin should you use?
- Who defines MQL and SQL, and does Sales agree with those definitions?
- Who are the buyers and the users, and what words do they use for the problem?
- Who are the top three competitors?

## Do this

1. **Write down the goal and two numbers.** Pipeline goal and average deal size are required. Everything else has a default in [defaults.md](../deliverables/defaults.md). Example: $3,000,000 pipeline a year at $30,000 per deal means 100 sales-accepted opportunities (SAOs).
2. **Pick your motion.**
   - Sales-led: the conversion you optimize is a demo or contact request, then SQL and SAO.
   - Product-led: swap MQL for signup and SQL for product-qualified lead (PQL). Optimize for activated signups, not raw signups.
   - Mixed: run both funnels and report them separately. Do not blend a signup and a demo into one "lead".
3. **Work out unit economics.** Agree definitions with Finance before you report them.
   - CAC = sales and marketing cost to win new customers ÷ new customers won. Also track paid-media cost per closed-won deal as your own narrower number. Say which one you mean.
   - CAC payback (months) = CAC ÷ (monthly revenue per customer × gross margin).
   - LTV = monthly revenue per customer × gross margin ÷ monthly churn rate.
   - Targets: LTV at least 3× CAC (David Skok, For Entrepreneurs). CAC payback under 12 months for SMB, under 18 for mid-market, under 24 for enterprise (Bessemer, Scaling to $100 Million).
4. **Set guardrails.** Write them in the [planning doc](../deliverables/planning-doc.md). Defaults (rule of thumb):
   - Maximum paid cost per closed-won deal: the amount that keeps CAC payback inside the target once sales cost is added. Paid cost per closed-won = cost per SAO ÷ win rate. At the defaults: $2,857 ÷ 20% = $14,286 per deal. On a $30,000 first-year deal ($2,500 a month) at an assumed 80% gross margin, paid media alone pays back in about 7 months. Ask Finance how many months that leaves for sales cost. If there is no room, the goal, deal size or budget needs to change. See [Budget](06-budget.md) for where the $2,857 comes from.
   - Monthly spend never exceeds plan by more than 10% without approval. That is the ±10% plan tolerance in [Budget](06-budget.md).
   - No new channel without a written test plan. See [Experimentation](07-experimentation.md).
5. **Agree stage definitions with Sales.** In one meeting, write down what counts as MQL, SQL, SAO and closed won, who moves a record between stages, and how fast Sales follows up. A rule of thumb: demo requests get a reply the same business day, other MQLs within one business day. Map your CRM's stage names to these. See [Measurement](03-measurement.md).
6. **Collect voice of customer.** Before writing ads, read or listen to at least 10 sales calls, win/loss notes or customer interviews (rule of thumb). Record the problem in their words, the trigger that made them look, the alternatives they considered and the objections. Use the exact phrases in ads and landing pages. See [Demand capture](04-demand-capture.md) and [Demand creation](05-demand-creation.md).
7. **Write positioning in one paragraph.** Who it is for, the problem, the category, the main alternative and why you win. If Product Marketing owns this, use theirs.
8. **Set the Sales rhythm.** A weekly 30-minute check with a sales leader: lead quality, follow-up speed, lost reasons. Monthly: pipeline from marketing vs goal. See [Cross-channel and working with others](11-cross-channel-and-working-with-others.md).

## If you see X, do Y

- **No pipeline goal exists:** propose one from last year's closed-won revenue ÷ win rate, plus the growth target, and get it approved before spending more.
- **Sales says leads are bad:** pull 20 recent MQLs and review them together. Fix the definition or the targeting, not the argument.
- **CAC payback is over target:** cut the lowest-return spend first (see [Budget](06-budget.md)) before cutting whole channels.
- **Product-led and signups look great but revenue does not move:** optimize to activation or PQL, not signup.
- **Finance and marketing report different CAC:** agree one formula and label every report with it.
- **Deal size varies a lot by segment:** plan and report by segment. A blended average hides where money is made.

## Metrics

- Pipeline created vs goal (monthly and quarter to date).
- SAOs, SQLs and MQLs vs plan.
- Cost per SAO and cost per closed-won deal.
- CAC, CAC payback and LTV:CAC, quarterly.
- Win rate and sales cycle for marketing-sourced deals vs all deals.
- Speed to lead for hand-raisers.

## Common mistakes

- Optimizing to cost per lead. Cheap leads that never become SAOs are the most expensive kind.
- Using a deal size that includes multi-year value when the plan assumes first-year.
- Agreeing stage definitions by email and never writing them down.
- Writing ads from internal language instead of customer language.
- Blending sales-led and product-led funnels into one number.

## Call an expert when

- Finance cannot give you gross margin or churn, so LTV is a guess.
- Multiple products or segments have very different deal sizes and cycles.
- Sales and marketing cannot agree on stage definitions after two meetings. That needs a RevOps owner.
- The motion is moving from sales-led to product-led, or the reverse.

## Tools and sources

**Related tools**

- [Research Agent](https://www.redavio.com/research-agent) (Exists): a brief on competitor and market news.
- [Marketing Correlation Analyzer](https://www.redavio.com/marketing-correlation) (Exists): checks whether two metrics move together, such as lead volume and SAOs.
- Driver breakdown (Planned): which drivers explain a gap to goal.
- All Redavio tools are listed in the [Library](https://www.redavio.com) and run through the [Redavio MCP server](https://www.redavio.com/mcp-server).

**Outside sources**

- [David Skok, SaaS Metrics 2.0](https://www.forentrepreneurs.com/saas-metrics-2/): the standard guide to CAC, LTV and payback.
- [Bessemer, Scaling to $100 Million](https://www.bvp.com/atlas/scaling-to-100-million): CAC payback targets by customer segment.
- [Exit Five: 8 steps to survive annual planning](https://exitfive.com/newsletter/8-steps-to-survive-annual-planning/): agreeing targets with Sales and Finance and presenting in financial terms.
- [Pavilion](https://www.joinpavilion.com/): community for go-to-market leaders; good for sales and marketing alignment.
- [SaaStr](https://www.saastr.com/): sales-led and product-led go-to-market from founders.
