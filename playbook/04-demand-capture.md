# 4. Demand capture

## Why it matters

Demand capture puts you in front of people who are already looking for what you sell. It is the fastest path to pipeline and the easiest to measure, so it is where most budgets should start (see [06-budget.md](06-budget.md)).

## Ask first

- Is tracking clean down to SAO and closed won, with offline conversions flowing back to the ad platforms? If not, fix that first ([03-measurement.md](03-measurement.md)).
- How many people search for your category, your brand and your competitors each month?
- Which conversion counts: demo request, signup, or something lower? Which stage will you bid to?
- What do your best customers call the problem, in their own words? ([02-align-to-the-business.md](02-align-to-the-business.md))
- Do you have a landing page for each offer, or does everything go to the homepage?

## Do this

1. **Judge capture on pipeline.** Primary measure: pipeline and revenue, and cost per qualified opportunity (SAO). Use a short window: the sales cycle from click to SAO, not to closed won.
2. **Prove cause with two checks.** Brand vs non-brand: report them apart, because brand gets credit for demand other channels created. Geo holdouts: pause a channel in a few matched regions and compare SAOs.
3. **Start in this order:** paid search on your highest-intent terms, conversion rate fixes on the pages that traffic lands on, then SEO, review sites and AI answers, which compound but take months.

### Paid search (Google and Microsoft)

1. **Structure:** separate campaigns for brand, non-brand and competitor terms, so each gets its own budget and target. Group ad groups by theme, one theme per landing page.
2. **Match types and negatives:** start non-brand on phrase and exact. Add broad match only once smart bidding has conversion data. Build shared negative lists (jobs, login, free, support, students) on day one.
3. **Bidding:** start on Maximize Conversions. Move to a target CPA once you have steady volume (rule of thumb: 30 conversions in 30 days). Once offline conversions send back SAOs with values, bid to value.
4. **Query mining:** review the search terms report ([Google Ads Help](https://support.google.com/google-ads/answer/2472708)) weekly. Add negatives for junk, promote converting queries to keywords.
5. **Microsoft:** copy the Google build to Microsoft Ads. Start it at a small share of search spend (rule of thumb: 10 to 20%) and scale on cost per SAO.
6. **Primary metric:** cost per SAO, split brand vs non-brand.
7. **Go deeper:** the full setup, audit checklist and weekly loop are in [performance-os](https://github.com/redavio/performance-os).
8. **Best sources:** [Search Engine Land](https://searchengineland.com/) for news and how-to; [PPC Land](https://ppc.land/) for fast coverage of platform changes.

### SEO

1. Map keywords to pages: one page per buyer problem, use case, integration and competitor comparison ("X vs Y", "X alternatives").
2. Write for the buyer first. Google's own guidance is to make helpful, people-first content ([Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)).
3. Fix technical basics once: indexing, speed, internal links, clean titles.
4. Reuse paid search data: queries that convert in ads are the pages to write first.
5. **Primary metric:** organic signups and demo requests from non-brand pages, then the SAOs they produce.
6. **Best sources:** [Ahrefs blog](https://ahrefs.com/blog/) for keyword and link research; [Backlinko](https://backlinko.com/blog) for clear how-to guides.

### AEO and GEO (showing up in AI answers)

1. Ask ChatGPT, Gemini, Claude, Perplexity and Google's AI Mode the 20 questions your buyers ask. Record whether you are named, and who is named instead. Repeat monthly.
2. Publish clear, quotable pages: plain definitions, comparison tables, pricing, and honest "who it's for" sections. AI answers draw on pages and on third parties.
3. Get mentioned where models read: review sites, community threads, analyst lists, partner pages.
4. Watch direct and branded search traffic alongside mentions. AI answers often send visits you cannot track by click.
5. **Primary metric:** share of answers that name you for your core questions.
6. **Best sources:** [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features); [Search Engine Roundtable](https://www.seroundtable.com/) for daily changes.

### Review sites (G2, Capterra)

1. Claim and complete your profiles. Pick the right categories; that is where buyers compare.
2. Ask happy customers for reviews every quarter, through Customer Success. A steady flow beats a one-time push.
3. Test paid placements only after you have enough recent reviews to win the comparison.
4. Track self-reported "how did you hear about us" mentions of the site, plus SAOs from it.
5. **Primary metric:** SAOs and influenced pipeline from review-site traffic.
6. **Best sources:** [G2 for vendors](https://sell.g2.com/); [Exit Five](https://www.exitfive.com/) for how B2B teams use review sites in practice.

### Website conversion rate optimization

1. Start with the pages paid traffic lands on. One page per offer and audience, matching the ad's promise.
2. Cut form fields to what Sales truly needs. Add a calendar booking step after the form.
3. Test one big change at a time (offer, headline, proof, form) and log it in the [experiment database](../deliverables/experiment-database.csv) ([07-experimentation.md](07-experimentation.md)).
4. Judge tests on SAOs per visit, not form fills alone. A cheaper lead that Sales rejects is not a win.
5. **Primary metric:** visit to SAO rate on paid landing pages.
6. **Best sources:** [CXL](https://cxl.com/blog/) for testing method; [Unbounce conversion benchmark report](https://unbounce.com/conversion-benchmark-report/) for landing page benchmarks by industry.

## If you see X, do Y

- **Brand cost per SAO looks great, non-brand looks bad:** report them apart. Do not move non-brand budget into brand; brand is capped by demand.
- **Lots of leads, few SAOs:** check search terms and lead quality with Sales before raising bids. Bid to SQL or SAO with offline conversions.
- **Impression share lost to budget on converting non-brand terms:** shift budget in (see [06-budget.md](06-budget.md)).
- **Branded search falls:** look at demand creation, not search bids ([11-cross-channel-and-working-with-others.md](11-cross-channel-and-working-with-others.md)).
- **Competitors named in AI answers, you are not:** add comparison pages and earn third-party mentions before buying anything.
- **Landing page converts well in tests but SAOs don't move:** check which leads Sales accepted, and whether tracking counts duplicates.

## Metrics

- Pipeline and revenue from capture, brand vs non-brand.
- Cost per SAO and pipeline-to-spend ratio.
- Conversion rate by stage: click to MQL, MQL to SQL, SQL to SAO.
- Impression share on brand (rule of thumb: keep it above 90%) and lost share on top non-brand terms.
- Share of AI answers naming you; organic non-brand signups; review count and recency.

## Common mistakes

- Judging capture on MQLs or form fills instead of SAOs.
- Mixing brand and non-brand in one campaign or one number.
- Broad match and automated bidding with no offline conversions to steer them.
- Sending all paid traffic to the homepage.
- Treating AI answers as a ranking problem only. Mentions elsewhere matter.

## Call an expert when

- Spend is past roughly $20K a month in search (rule of thumb) and cost per SAO is rising.
- You need offline conversion uploads or value-based bidding set up.
- An SEO migration or site rebuild is planned.
- A geo holdout test needs designing.

## Tools and sources

**Related tools**

- [Paid search playbook (performance-os)](https://github.com/redavio/performance-os) (Exists, open source): deep paid search how-to, from build to audit.
- [Ad Budget Optimizer](https://www.redavio.com/budget-optimizer) (Exists, free): budget changes on Google and Microsoft Ads, applied after you approve.
- [Ad Copy Analyzer](https://www.redavio.com/attribute-engine-ad-copy) (Exists): which copy attributes drive performance.
- [Landing Page Analyzer](https://www.redavio.com/attribute-engine-landing-pages) (Exists): which page attributes drive conversion.
- [Google Sheet to CMS Landing Page](https://www.redavio.com/google-sheet-to-cms-landing-page) (Exists): landing pages in bulk, one per offer or keyword theme.
- [Marketing Correlation Analyzer](https://www.redavio.com/marketing-correlation) (Exists): for example, do AI mentions and direct traffic move together.
- All are reachable by your AI through the [Redavio MCP server](https://www.redavio.com/mcp).

**Best outside sources**

- [Search Engine Land](https://searchengineland.com/): search news and how-to.
- [Google Ads Help](https://support.google.com/google-ads): official setup docs, such as [enhanced conversions](https://support.google.com/google-ads/answer/9888656) and [offline conversions with GCLID](https://support.google.com/google-ads/answer/7012522).
- [Microsoft Advertising Learning Lab](https://learninglab.about.ads.microsoft.com/): free Microsoft Ads training.
- [Ahrefs blog](https://ahrefs.com/blog/): SEO research and AI search studies.
- [CXL](https://cxl.com/blog/): conversion research and testing method.
