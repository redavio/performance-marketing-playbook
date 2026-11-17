# 10. Operations and AI

## Why it matters

One person can run several channels well only if the routine work runs itself: data flows on its own, alerts catch problems, and AI drafts the analysis. Done carelessly, the same automation can spend money nobody approved. This section covers both sides.

## Ask first

- Which recurring tasks in [09-operating-rhythm](09-operating-rhythm.md) take the most time? Automate those first.
- Where does each number live: ad platforms, CRM, analytics, a sheet? Which tools already connect?
- Which AI assistant does the team use, and does it support MCP servers (for example Claude or ChatGPT)?
- Who is allowed to approve a change to an ad account? Write the names down.
- What access does each tool really need: read only, or read and write?

## Do this

1. **Write the approval rule first.** No person, script, rule or agent changes an ad account (budget, bid, target, status, keyword, audience) without a named human approving that specific change. AI and automations propose; a person approves; then the change is applied and logged. Put this in the [planning doc](../deliverables/planning-doc.md).
2. **Connect your data.** Get spend, clicks and conversions from each ad platform and stages from the CRM into one place, on a daily schedule. Options, simplest first:
   - Native connectors (CRM to ad platform, Looker Studio to Google Ads).
   - No-code workflow tools like Zapier or n8n.
   - The platform APIs (Google Ads API, Microsoft Advertising API) when you need full control.
3. **Set alerts before anything else.** They cover the daily checks. Defaults (rule of thumb; tune after a month):
   - No conversions recorded on any channel for 24 hours: tracking alert.
   - Spend pacing more than 15% over or under plan month to date.
   - A campaign spends more than 2x your target cost per MQL with zero conversions.
   - Offline conversion upload or CRM sync failed.
   - Ads disapproved.
   Send alerts where you already look (email or Slack), one open alert per issue, not one per hour.
4. **Automate the reports.** Draft the weekly update and monthly report from the tracker on a schedule. A person reviews and sends them ([08-reporting-and-communication](08-reporting-and-communication.md)).
5. **Connect your AI through MCP.** The Model Context Protocol is an open standard that lets an AI assistant call outside tools. Add an MCP server's address in your assistant's connector settings and it can use that server's tools in chat.
6. **Add the Redavio MCP server.** One address, [redavio.com/mcp](https://www.redavio.com/mcp), gives your AI every Redavio tool, such as the ad copy and landing page analyzers, plus this playbook's own tools (playbook_guide and playbook_deliverable). Your AI does the reasoning; the tools fetch, measure and return results. Example asks:
   - "Using the playbook, what should a team with $50K a month and no offline conversions do first?"
   - "Fill the budget tracker for a $3M pipeline goal and a $30K deal size."
   - "Run the Landing Page Analyzer on our top five pages and add test ideas to the backlog."
7. **Use agents for analysis, not unattended action.** A good agent: runs on a schedule, reads the data through tools, decides what is worth raising, and writes a short proposal with the numbers it used. It does not apply changes. Start with one: a weekly agent that reviews search terms and proposes negatives for you to approve.
8. **Apply changes through a tool with an approval step.** For budgets, the [Ad Budget Optimizer](https://www.redavio.com/budget-optimizer) recommends changes on Google and Microsoft Ads and applies them only after you approve. It has its own MCP server for connected accounts, so your AI can show you the recommendations, but the change still waits for your click.
9. **Keep access tight.** Read-only access by default. Separate credentials per tool. Remove access when a person or vendor leaves. Never paste API keys into a chat.
10. **Log every change.** Who, what, when, from what value to what value, and why. Platform change history covers the platform; keep your own log for changes made by tools and agents.

## If you see X, do Y

- **An automation or agent changed an account without approval:** turn it off, revert from change history, and remove its write access until it has an approval step.
- **Alerts fire every day and get ignored:** raise thresholds or merge alerts. An ignored alert is worse than none.
- **The AI gives a number you can't trace:** ask it which tool returned the number. If none did, don't use it.
- **A workflow breaks silently:** add an alert for "no data arrived today" on every scheduled pull.
- **You want to automate a task you've never done by hand:** do it by hand for a month first.

## Metrics

- Hours per week spent on routine tasks, before and after automation.
- Time from a problem starting to an alert firing.
- Share of alerts that led to an action (aim for most; the rest are noise).
- Changes applied with a recorded approval: should be 100%.
- Data freshness: hours since the last successful pull for each source.

## Common mistakes

- Letting platform auto-apply recommendations run on its own. Review them like any other change.
- Building automation on top of broken tracking. Fix [03-measurement](03-measurement.md) first.
- Giving every tool write access "to be safe".
- Trusting AI-written numbers without checking where they came from.
- Ten half-built automations instead of three that work.

## Call an expert when

- You need custom API work, data warehouse pipelines or offline conversion uploads at scale.
- An agent needs write access to anything that spends money.
- Security or legal reviews are required to connect a tool to company data.

## Tools and sources

**Related tools**

- [Redavio MCP server](https://www.redavio.com/mcp) (Exists): one address that gives your AI every Redavio tool, including this playbook's tools.
- [Ad Budget Optimizer](https://www.redavio.com/budget-optimizer) (Exists, free): budget recommendations on Google and Microsoft Ads, applied only after you approve. Has its own MCP server for connected accounts.
- [Research Agent](https://www.redavio.com/research-agent) (Exists): a scheduled brief on the news that matters, delivered without you asking.
- [Google Sheet to CMS Landing Page](https://www.redavio.com/google-sheet-to-cms-landing-page) (Exists): builds landing pages in bulk from a sheet.

**Best outside sources**

- [What is the Model Context Protocol?](https://modelcontextprotocol.io/docs/getting-started/intro): the official introduction to MCP and which assistants support it.
- [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices): what to check before connecting a server to company data.
- [Google Ads Scripts](https://developers.google.com/google-ads/scripts/docs/start): custom alerts and reports inside Google Ads without a full API project.
- [Microsoft Advertising API overview](https://learn.microsoft.com/en-us/advertising/guides/): when and how to connect Microsoft Ads programmatically.
- [n8n docs](https://docs.n8n.io/) and [Zapier help](https://help.zapier.com/hc/en-us): no-code workflows to move data between tools and send alerts.
