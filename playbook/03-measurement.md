# 3. Measurement

## Why it matters

Ad platforms optimize toward whatever you tell them is a conversion. If that is a form fill, they find form fillers, not buyers. Good measurement sends real pipeline back to the platforms and tells you which numbers are proven and which are only credited.

## Ask first

- What are your CRM's stage names, and how do they map to MQL, SQL, SAO and closed won?
- Does every form capture the click ID (GCLID for Google, MSCLKID for Microsoft) and UTM parameters, and store them on the CRM record?
- Is consent in place for the tags and data you send? Check with whoever owns privacy.
- Which conversion is each campaign optimizing to today?
- Do you ask "How did you hear about us?" on the demo form?
- Who owns the CRM (RevOps, Sales Ops, you)?

## Do this

1. **Map the funnel stages.** Names vary by CRM, so map yours to these:

   | Stage | Means | Example |
   | --- | --- | --- |
   | MQL | A lead marketing hands to Sales | Hand-raiser: demo or contact request. Non-hand-raiser: content download, webinar |
   | SQL | Sales has qualified it | Meeting scheduled |
   | SAO | Sales accepts it as an opportunity; it enters pipeline | Opportunity created |
   | Closed won | Signed | Contract signed |

   Product-led: MQL becomes signup, SQL becomes product-qualified lead (PQL). Track hand-raisers and content leads as separate MQL types; they convert at very different rates. The rates between stages drive the [budget math](06-budget.md).

2. **Set up tracking.** In order:
   - One tag manager on every page. Google tag and Microsoft UET at minimum, plus LinkedIn and any other platform you buy.
   - UTM rules written down: source, medium, campaign, content. Use lowercase. Store first-touch and latest-touch UTMs on the contact.
   - Hidden form fields that save the click ID and UTMs to the CRM record.
   - A free-text "How did you hear about us?" field on the demo form. No dropdown; dropdowns lead the answer.
   - Test every form end to end once a month. Broken tracking is the most common silent failure.

3. **Put a value on each conversion.** Value = deal size × the chance that stage closes. At the [defaults](../deliverables/defaults.md) ($30,000 deal, 25% MQL to SQL, 60% SQL to SAO, 20% win rate):

   | Stage | Value |
   | --- | --- |
   | MQL | $30,000 × 25% × 60% × 20% = $900 |
   | SQL | $30,000 × 60% × 20% = $3,600 |
   | SAO | $30,000 × 20% = $6,000 |
   | Closed won | $30,000 (or the actual contract value) |

   Use real stage rates once you have three months of data. A content-download MQL may be worth a fraction of a demo MQL; value them separately.

4. **Send offline conversions back.** Upload SQL, SAO and closed won from the CRM to Google and Microsoft Ads against the click ID, with the values above. On Google, use enhanced conversions for leads or offline conversion imports (Google is moving these imports to its Data Manager API; check the current method in Google Ads Help). Do the same for LinkedIn and other platforms through their conversion integrations. Default: upload daily. Then set campaigns to optimize to SQL or SAO value once each campaign has enough volume (rule of thumb: about 30 conversions in 30 days per campaign; see [Demand capture](04-demand-capture.md)); until then, optimize to MQL with values so the platform still prefers hand-raisers. The deep paid search setup is in [performance-os](https://github.com/redavio/performance-os).

5. **Choose attribution models for each job.** No model proves cause. Each answers a different question.

   | Model | Gives credit to | Use it for |
   | --- | --- | --- |
   | First touch | The first recorded touch | Which channels bring new people in. Good for judging demand creation's reach. |
   | Last touch | The last touch before conversion | Which channels close the gap to a form fill. Biased toward branded search and direct. |
   | Linear | Every touch equally | A neutral view of everything that touched a deal. Good default for multi-touch reports. |
   | Position-based | Most credit to the first and lead-creation touches, the rest spread between | When both discovery and conversion matter. HubSpot now offers an "Empirical" model in place of its U- and W-shaped models. |
   | Data-driven | Credit learned from your own conversion paths | Bidding inside an ad platform. Google Ads now supports only data-driven and last click. |
   | Self-reported | What the buyer says on the form | Channels software cannot see: podcasts, communities, word of mouth, LinkedIn content. |

   Default: data-driven inside each ad platform for bidding; linear in the CRM for the pipeline report; self-reported alongside both. When software and self-reported disagree, show both rather than picking one.

6. **Separate attribution from proof of cause.** Attribution shares out credit for deals that happened. It cannot say whether a deal would have happened without the ad. To prove cause, hold something out and compare:
   - Brand vs non-brand checks: pause or cut branded search in some regions or weeks and watch whether total branded conversions fall or just move to organic.
   - Geo holdouts: turn a channel off in matched regions and compare pipeline with regions where it stayed on.
   - Lift tests: platform lift studies, such as LinkedIn's conversion lift testing.
   - Holdout accounts: for ABM, keep a random set of target accounts unexposed and compare their progress.

   Run at least one cause test a year on your largest channel (rule of thumb). See [Experimentation](07-experimentation.md).

7. **Measure capture and creation differently,** as set out below.

### Measuring capture vs creation

Demand capture meets people who are already looking. Demand creation reaches buyers before they look, so they search for you later. Judge each on its own terms:

| | Demand capture (paid search, SEO, AEO) | Demand creation (paid social, YouTube and CTV, display, ABM, sponsorships, syndication) |
| --- | --- | --- |
| Primary measure | Pipeline and revenue, cost per qualified opportunity | Target-account reach and engagement, pipeline velocity, self-reported "how did you hear about us" |
| Window | Short | Longer; never judged on last click |
| Proof of cause | Brand vs non-brand checks, geo holdouts | Lift tests, holdout accounts |

See [Demand capture](04-demand-capture.md), [Demand creation](05-demand-creation.md) and [Cross-channel](11-cross-channel-and-working-with-others.md).

### Influenced pipeline

Influenced pipeline is an opportunity created at a target account that had a paid creation touch, such as an ad engagement, in the 90 days before the opportunity was created (the 90-day window is a rule of thumb). Count it separately from sourced pipeline (opportunities tracked to a click or a self-reported source). Never add the two together: the same deal would be counted twice. Label it lower confidence.

## If you see X, do Y

- **Platform conversions far above CRM MQLs:** look for duplicate tags, spam and newsletter forms counted as leads. Fix before changing bids.
- **Branded search looks like your best channel:** run a brand vs non-brand check before moving budget into it.
- **Creation shows almost no last-touch pipeline:** judge it on self-reported answers, target-account engagement and a lift test, not last touch.
- **Click IDs missing on many CRM records:** check hidden fields and redirects that strip URL parameters.
- **Too few SAOs to optimize to:** optimize to SQL or valued MQLs and move down the funnel as volume grows.

## Metrics

- MQL, SQL, SAO and closed won by channel and month.
- Stage conversion rates and time between stages.
- Share of CRM records with a click ID or UTM (aim for most paid leads).
- Pipeline value by attribution model, side by side.
- Self-reported source mix.
- Cost per SAO and pipeline-to-spend ratio.

## Common mistakes

- Optimizing ad platforms to all form fills, including newsletter signups.
- Reporting one attribution model as the truth.
- Uploading only closed won, which arrives too late and too rarely for bidding.
- Judging demand creation on last click and cutting it.
- Changing stage definitions without telling anyone, which breaks every trend line.

## Call an expert when

- Offline conversion uploads fail or match rates are low.
- You need server-side tagging or consent mode set up.
- You want a geo holdout or lift test and do not know how to size it.
- The CRM has no clean stage history to build conversion rates from.

## Tools and sources

**Related tools**

- [Marketing Correlation Analyzer](https://www.redavio.com/marketing-correlation) (Exists): checks whether two metrics move together, such as LinkedIn spend and branded search. Correlation is a lead to test, not proof.
- [performance-os](https://github.com/redavio/performance-os) (Exists, open source): conversion and offline conversion setup for Google and Microsoft Ads.
- Account Influence Analyzer (Planned): which ABM touches move accounts through stages, measured by lift.
- Driver breakdown (Planned): which drivers explain a gap to goal.
- All Redavio tools are listed in the [Library](https://www.redavio.com) and run through the [Redavio MCP server](https://www.redavio.com/mcp-server).

**Outside sources**

- [Google Ads Help: About attribution models](https://support.google.com/google-ads/answer/6259715): which models Google Ads still supports and how data-driven works.
- [Google Ads Help: About offline conversion imports](https://support.google.com/google-ads/answer/2998031): sending CRM stages back to Google, and the current upload method.
- [HubSpot: Create attribution reports](https://knowledge.hubspot.com/reports/create-attribution-reports): the CRM models available and how to build the report.
- [Refine Labs: Hybrid attribution framework](https://www.refinelabs.com/article/hybrid-attribution-framework): combining self-reported and software attribution for demand creation.
- [LinkedIn: Ad campaign experimentation](https://training.marketing.linkedin.com/ad-campaign-experimentation): setting up and reading lift tests.
- [Dreamdata B2B Benchmarks](https://dreamdata.io/b2b-benchmarks): B2B ad and journey benchmarks to compare against.
