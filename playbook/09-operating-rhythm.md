# 9. Operating rhythm

## Why it matters

Most paid accounts fail from neglect, not bad strategy: broken tracking nobody noticed, budget that ran out on the 20th, search terms nobody read. A fixed rhythm catches problems while they are small and leaves time for tests and planning.

## Ask first

- Who owns paid acquisition day to day? Every task needs one named owner.
- How much time do you have? The daily list takes about 15 minutes, the weekly about 2 hours (rule of thumb).
- Which task tool does the team use: ClickUp, Asana or Notion? Import [recurring-tasks.csv](../deliverables/recurring-tasks.csv) there.
- Who in Sales, RevOps and Finance do you need on a regular schedule?

## Do this

1. **Name the owner roles.** This playbook uses five:
   - **Paid acquisition owner:** runs the accounts. Owns most tasks.
   - **Marketing lead:** owns the goal, the plans and the QBR.
   - **RevOps:** owns CRM stages, offline conversions and tracking data.
   - **Finance:** owns budget sign-off and invoice reconciliation.
   - **Sales leader:** gives lead quality feedback.
   One person can hold several roles at a small company.
2. **Import the task list.** Every task below is a row in [recurring-tasks.csv](../deliverables/recurring-tasks.csv). CSV imports into ClickUp and Asana do not set recurrence. Import the CSV, then set recurrence and assignee on each task, or ask your AI to create them as recurring tasks through its connector.
3. **Run the tasks below.** Do the daily ones first thing, before you change anything.

### Daily

| # | Task | Owner |
| --- | --- | --- |
| D1 | Check alerts and confirm conversions recorded yesterday on every channel | Paid acquisition owner |
| D2 | Check spend pacing vs budget by channel | Paid acquisition owner |
| D3 | Scan for flagrant spend (a campaign or keyword that has spent past your alert threshold with no conversions) | Paid acquisition owner |
| D4 | Review and approve or reject pending change recommendations | Paid acquisition owner |

### Weekly

| # | Task | Owner |
| --- | --- | --- |
| W1 | Review search terms: add negatives, promote converting terms to keywords | Paid acquisition owner |
| W2 | Review results vs goal by funnel stage and channel | Paid acquisition owner |
| W3 | Check live tests: end any that hit sample size, launch the next from the backlog | Paid acquisition owner |
| W4 | Review ads and assets: disapprovals, low performers, fatigue | Paid acquisition owner |
| W5 | Review lead quality and MQL to SQL rate with Sales | Sales leader |
| W6 | Log every change made this week in the change log | Paid acquisition owner |
| W7 | Send the weekly update (Monday by noon) | Paid acquisition owner |

### Monthly

| # | Task | Owner |
| --- | --- | --- |
| M1 | Update the budget tracker with plan vs actual | Paid acquisition owner |
| M2 | Reconcile platform spend with invoices | Finance |
| M3 | Check offline conversions and CRM stages match what the ad platforms received | RevOps |
| M4 | Rebalance budget across channels and campaigns by marginal return | Paid acquisition owner |
| M5 | Groom the experiment backlog and re-score ideas with ICS | Paid acquisition owner |
| M6 | Review competitors and the news brief: new ads, offers, pricing, platform changes | Paid acquisition owner |
| M7 | Refresh audiences and lists: target accounts, customer exclusions, retargeting | Paid acquisition owner |
| M8 | Send the monthly report (by the 5th business day) | Paid acquisition owner |

### Quarterly

| # | Task | Owner |
| --- | --- | --- |
| Q1 | Audit each account: structure, settings, tracking, conversion setup | Paid acquisition owner |
| Q2 | Back-test ICS scores against test results in the test log | Paid acquisition owner |
| Q3 | Replace default conversion rates and costs with your last 3 months of actuals | RevOps |
| Q4 | Plan or run one proof-of-cause check (brand vs non-brand, geo or account holdout) | Paid acquisition owner |
| Q5 | Write the quarter postmortem (within 2 weeks after quarter end) | Paid acquisition owner |
| Q6 | Build next quarter's plan and budget | Marketing lead |
| Q7 | Run the QBR (in the last 2 weeks of the quarter, so next quarter's plan is agreed before it starts) | Marketing lead |

### Yearly

| # | Task | Owner |
| --- | --- | --- |
| Y1 | Write the annual postmortem (within 2 weeks after year end) | Marketing lead |
| Y2 | Build the annual plan and budget with Finance (draft 8 weeks before the year starts, final 4 weeks before; rule of thumb) | Marketing lead |
| Y3 | Review tracking and attribution end to end | RevOps |
| Y4 | Review tools, vendors and contracts before renewals | Marketing lead |
| Y5 | Clean up user access on every ad account and tool | Paid acquisition owner |

4. **Block the time.** Put daily, weekly and monthly work on the calendar as recurring blocks. Protect them.
5. **Automate what you can.** Alerts cover D1 to D3; reports can draft W2, W7 and M8. See [10-operations-and-ai](10-operations-and-ai.md).
6. **Close the loop.** The weekly feeds the monthly ([08-reporting-and-communication](08-reporting-and-communication.md)); the monthly feeds the QBR; the QBR feeds the next plan ([06-budget](06-budget.md)).

## If you see X, do Y

- **Daily check finds no conversions yesterday:** treat it as a tracking break until proven otherwise. Check tags and the CRM sync before touching bids or budget.
- **You keep skipping weekly tasks:** cut accounts or channels until the rhythm fits. An unwatched channel wastes money.
- **Monthly rebalance moves more than 20% of budget** (rule of thumb): make it in steps over 2 to 3 weeks so bidding can adjust.
- **Quarter starts with no agreed plan:** keep last quarter's budget flat until the QBR signs off.
- **A task has no owner:** it will not happen. Assign it today.

## Metrics

- Share of recurring tasks done on time, by cadence.
- Days from a problem starting to it being caught (tracking break, overspend).
- Weekly update and monthly report sent on time.
- Changes logged vs changes made.

## Common mistakes

- Changing bids or budgets daily. Most bidding needs days of data to react; look daily, act weekly.
- Skipping the search term review because performance "looks fine".
- No change log, so nobody can explain a jump in cost.
- Doing quarterly planning after the quarter has started.
- One person holding every task with no backup during vacations.

## Call an expert when

- The daily and weekly lists take more than double the time above. The account structure probably needs fixing.
- Tracking breaks more than once a quarter.
- You run more than four channels (rule of thumb) and can't keep the rhythm alone.

## Tools and sources

**Related tools**

- [Ad Budget Optimizer](https://www.redavio.com/budget-optimizer) (Exists, free): recommends budget changes on Google and Microsoft Ads and applies them after you approve. Covers D2, D4 and M4.
- [Research Agent](https://www.redavio.com/research-agent) (Exists): a scheduled brief on the news that matters. Covers M6.
- All Redavio tools are listed in the [Library](https://www.redavio.com) and run through the [Redavio MCP server](https://www.redavio.com/mcp-server).

**Outside sources**

- [Google Ads: About change history](https://support.google.com/google-ads/answer/19888): who changed what and when. Use it for W6 and when cost jumps.
- [Google Ads: Set up automated rules](https://support.google.com/google-ads/answer/2472779): email alerts or simple rules when conditions are met.
- [Exit Five](https://www.exitfive.com/): B2B marketers comparing how they run weekly and quarterly routines.
- [SaaStr](https://www.saastr.com/): B2B SaaS operating advice, useful for annual planning and board reporting.
