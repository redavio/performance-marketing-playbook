# 7. Experimentation program

## Why it matters

Your accounts only get better as fast as you learn. A program with a backlog, a scoring method, a test log and readouts turns guesses into results you can repeat, and stops the team from rerunning ideas that already failed.

## Ask first

- What is the one metric each test must move? Pick the deepest funnel stage you have enough volume to read (see [03-measurement](03-measurement.md)).
- How much traffic or how many conversions does the thing you want to test get per week?
- Can you split traffic cleanly? (Platform experiments, a testing tool on the site, or geo splits.)
- Who approves a test that touches an ad account, a landing page or a form?
- Where will the backlog and test log live? Use one table for both: [experiment-database.csv](../deliverables/experiment-database.csv).

## Do this

1. **Set up the experiment database.** Copy [experiment-database.csv](../deliverables/experiment-database.csv) into Sheets, Airtable or Notion. One row per idea. It holds the backlog, the scores, the design and the result.
2. **Fill the backlog.** Write each idea as a hypothesis: "If we change X for audience Y, metric Z will move, because of evidence E." Good sources: search terms, sales call notes, voice of customer, competitor ads, past test results, and the attribute analyzers listed under Tools. Aim for 20 ideas before you score (rule of thumb).
3. **Score every idea with ICS.** Three scores, each 1 to 10:
   - **Impact:** how much the main metric moves if it wins, and how much spend or traffic it touches.
   - **Confidence:** how strong the evidence is. Your own past test or data = high. A competitor does it = medium. A hunch = low.
   - **Simplicity:** how little time, money and help from others it needs. Copy change = 9. New landing page with Design and Dev = 3.
   - **ICS score = (Impact + Confidence + Simplicity) / 3.** Run the highest scores first. Write one line of reasoning per score so you can check it later.
4. **Design the test before you launch it.** Write down, in the database:
   - The metric, the baseline rate and the **minimum detectable effect**: the smallest change worth detecting. If you can only detect a 50% lift, a real 10% lift will look like "no result".
   - The **sample size** per variant, from a calculator. Defaults: 95% significance, 80% power (convention, see the CXL guide below). Example, computed with the standard formula: a 3% conversion rate and a 20% relative lift (3.0% to 3.6%) needs about 14,000 visitors per variant. Check yours in a calculator.
   - The **run time** = sample size / weekly traffic, rounded up to full weeks. Minimum 2 full weeks to cover weekday swings (rule of thumb).
   - The stop date and the decision rule: "Ship B if it beats A at 95% on the main metric with no drop in SQL rate."
5. **If the sample is out of reach, change the test, not the rules.** Test a bigger change, pool similar campaigns, or use a higher-volume metric (click-through rate or MQLs instead of SAOs) and confirm downstream quality later.
6. **Use the platform's split tools.** Google Ads experiments and drafts, Microsoft Ads experiments, LinkedIn A/B tests, or a site testing tool. One change per test.
7. **Do not peek and stop.** Look for breakage in week one, then leave it until the stop date. Stopping the moment it looks significant inflates false wins (see Evan Miller below).
8. **Read the result.** Record: winner or no difference, the measured lift and its range, and what happened to the next funnel stage. "No difference" is a result. Log it.
9. **Ship, then log.** Roll out winners, archive losers, and write the one-line lesson.
10. **Back-test the scores every quarter.** The test log puts each test's predicted Impact and Confidence next to its actual result. Compare:
    - Tests you scored Impact 8+ : how many actually moved the metric?
    - Tests you scored Confidence 8+ : what share won?
    - If high-confidence tests win no more often than low ones, your evidence is weaker than you think. Score Confidence lower next quarter. Do the same for Impact.
11. **Share readouts.** One slide per finished test in the monthly report ([08-reporting-and-communication](08-reporting-and-communication.md)). Postmortem any large test.

## If you see X, do Y

- **Test can't reach sample size in 6 weeks (rule of thumb):** make the change bigger or move to a higher-volume metric.
- **Big early lift in week one:** keep running. Early swings shrink.
- **Variant wins on MQLs but SQL rate drops:** do not ship. Check lead quality with Sales.
- **Most tests come back flat:** your changes are too small. Test bolder ideas: offer, audience, landing page, not button color.
- **A winner fades a month later:** check for seasonality or novelty, then retest.
- **Backlog keeps growing but nothing runs:** cap work in progress at 2 to 3 live tests per channel (rule of thumb) and drop anything scored under 5.

## Metrics

- Tests launched and finished per month (test velocity).
- Win rate: share of finished tests that beat control.
- Total measured lift shipped this quarter on the main metric.
- Score accuracy: win rate by Confidence band, and measured lift by Impact band.
- Time from idea to readout.

## Common mistakes

- Running tests with no planned sample size or stop date.
- Changing two things at once, then not knowing which worked.
- Calling a winner on clicks when the goal is pipeline.
- Overlapping tests on the same traffic.
- Scoring every idea 7, 7, 7. Force a spread.
- Never checking past scores, so the team never gets better at picking tests.

## Call an expert when

- You need geo holdouts, lift studies or matched-market tests to prove cause (see [03-measurement](03-measurement.md)).
- Traffic is low and you are considering sequential or Bayesian methods.
- Results conflict between the platform and your CRM.
- A test changes bidding strategy on large spend.

## Tools and sources

**Related tools**

- [Ad Copy Analyzer](https://www.redavio.com/attribute-engine-ad-copy) (Exists): finds which ad copy attributes drive performance. A strong source of test ideas with real evidence behind them.
- [Landing Page Analyzer](https://www.redavio.com/attribute-engine-landing-pages) (Exists): the same for landing pages.
- All Redavio tools are listed in the [Library](https://www.redavio.com) and run through the [Redavio MCP server](https://www.redavio.com/mcp-server). Your AI can call both analyzers there and turn findings into backlog rows.

**Outside sources**

- [Evan Miller sample size calculator](https://www.evanmiller.org/ab-testing/sample-size.html): quick sample size from baseline rate and minimum detectable effect.
- [Optimizely sample size calculator](https://www.optimizely.com/sample-size-calculator/): same inputs with plain explanations of each one.
- [How Not To Run an A/B Test (Evan Miller)](https://www.evanmiller.org/how-not-to-run-an-ab-test.html): why peeking and stopping early produces false wins.
- [CXL: A/B testing statistics](https://cxl.com/blog/ab-testing-statistics/): significance, power and sample size explained for marketers.
- [Google Ads: campaign drafts](https://support.google.com/google-ads/answer/6318732): how to test campaign changes without touching the live campaign.
