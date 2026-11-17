# 11. Cross-channel and working with others

## Why it matters

Channels affect each other, so judging each one alone gives wrong answers: cut LinkedIn and branded search falls a month later. And none of this works without Sales, RevOps and Finance agreeing on the numbers.

## Ask first

- Which channels create demand and which capture it in your mix? ([04-demand-capture.md](04-demand-capture.md), [05-demand-creation.md](05-demand-creation.md))
- Is there one funnel definition (MQL, SQL, SAO, closed won) that Sales, RevOps and Finance all use? ([03-measurement.md](03-measurement.md))
- Who owns the CRM fields, the lead routing and the "how did you hear about us" question?
- Which agencies and vendors touch your accounts or data, and what do they report on?

## Do this

1. **Map how channels feed each other.** Default model: creation (social, video, ABM, sponsorships, AI-answer mentions) raises branded search, direct traffic and AI-answer traffic; capture collects it. Write this into the [planning doc](../deliverables/planning-doc.md).
2. **Watch the leading signals weekly:** branded search volume, direct traffic, self-reported source, and named mentions in AI answers. When creation spend changes, these should move within weeks.
3. **Test the links, don't assume them.** Run a holdout (pause creation in some regions or accounts) and compare branded search and SAOs. Use correlation to find candidates, a lift test to confirm.
4. **One plan, one report.** All channels in one [budget tracker](../deliverables/budget-tracker.csv) against one pipeline goal, split capture vs creation. One weekly update ([regular-updates.md](../deliverables/regular-updates.md)), with capture and creation side by side, each on its own measures ([Measurement](03-measurement.md#measuring-capture-vs-creation)).
5. **Credit by confidence, not by channel.** High: SAOs tracked from click. Medium: self-reported source. Lower: [influenced pipeline](03-measurement.md#influenced-pipeline). Show all three; never add them into one number that double counts.
6. **Sales:** agree the target account list, what counts as an accepted opportunity, and lead follow-up time (rule of thumb: demo requests the same business day, other MQLs within one business day). Meet weekly on lead quality. Close the loop: rejected leads come back with a reason.
7. **RevOps:** own tracking together. Hidden form fields for click IDs and UTMs, offline conversion uploads, stage dates on every opportunity. Write changes down before they ship.
8. **Finance:** share the budget math ([06-budget.md](06-budget.md)) and agree monthly flex rules up front: how far you can move spend between channels without asking. Report cost per SAO and pipeline-to-spend ratio, the numbers they trust.
9. **Agencies and vendors:** you own the accounts, the data and the goals. Give them the pipeline goal, not a click goal. Ask for change logs and admin access you control. Review them monthly on SAOs and pipeline, not their own dashboards. Never let a vendor's report be the only source of truth.

## If you see X, do Y

- **Branded search drops after a creation cut:** that was creation's effect. Restore it or plan for lower capture pipeline.
- **Every channel claims the same deal:** switch the report to confidence tiers (step 5).
- **Sales says leads are bad:** pull 20 recent MQLs, including ones Sales rejected, and review them together (the same check as in [Align to the business](02-align-to-the-business.md)). Fix targeting, routing or follow-up time, whichever is actually broken.
- **Finance wants to cut creation first:** show the holdout result and branded search trend ([08-reporting-and-communication.md](08-reporting-and-communication.md)).
- **An agency reports wins you can't find in the CRM:** reconcile to CRM SAOs before the next invoice.

## Metrics

- Branded search volume, direct traffic and AI-answer mentions, against creation spend.
- Pipeline by confidence tier.
- Lead follow-up time and SQL to SAO rate (Sales health).
- Plan vs actual budget and pipeline by month.

## Common mistakes

- Cutting creation because brand search "does the work".
- Each channel owner reporting their own platform numbers.
- Changing CRM stages or forms without telling marketing.
- Letting an agency own the ad accounts.

## Call an expert when

- You need a geo or account holdout designed and read.
- Your CRM can't tie opportunities to campaigns; RevOps help is needed.
- You're replacing or adding an agency and need a scope and scorecard.

## Tools and sources

**Related tools**

- [Marketing Correlation Analyzer](https://www.redavio.com/marketing-correlation) (Exists): do creation spend, AI mentions, branded search and direct traffic move together.
- Account Influence Analyzer (Planned): which ABM touches move accounts through stages, measured by lift.
- [Ad Budget Optimizer](https://www.redavio.com/budget-optimizer) (Exists, free): budget changes on Google and Microsoft Ads after you approve.
- All Redavio tools are listed in the [Library](https://www.redavio.com) and run through the [Redavio MCP server](https://www.redavio.com/mcp-server).

**Outside sources**

- [Refine Labs blog](https://www.refinelabs.com/blog): how creation drives capture, and self-reported attribution.
- [LinkedIn B2B Institute](https://business.linkedin.com/marketing-solutions/b2b-institute): research on B2B brand building and long-term effects.
- [Exit Five](https://www.exitfive.com/): working with Sales, Finance and agencies, from operators.
- [SaaStr](https://www.saastr.com/blog/): sales and marketing alignment in SaaS.
