# Page-2 quick wins: move up the pages Google almost ranks

The fastest SEO win usually isn't a new article. It's the pages Google already shows, just too low to get clicked.
Move them up a few spots and the traffic comes from pages you already have. Google's own Search Central blog says the
queries you already appear for are "easier to optimize" (Apr 6, 2022). Checked November 2026; links go to the sources.

## Why a few spots make the difference

- On mobile, the #1 result gets **35.95%** of clicks when there's no AI Overview, and **8.51%** when there is one.
  ([Advanced Web Ranking, Q2 2026](https://www.advancedwebranking.com/blog/ctr-google-2026-q2), Sep 29, 2026)
- In an older, pre-AI study of 4 million results, only **0.63%** of searchers clicked anything on page 2.
  ([Backlinko](https://backlinko.com/google-ctr-stats), 2019 data)
- When Google showed an AI summary, people clicked a regular result on **8%** of visits, against **15%** with no
  summary. ([Pew Research Center](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/), Jul 22, 2025; 900 US adults)

So the page that answers clearly, near the top, is the one that gets quoted and clicked.

## Step 1: Find your shortlist (10 minutes)

1. Open **Google Search Console › Performance › Search results**. The default view is the last 3 months.
2. Click **Average position** above the chart to turn it on.
3. In the table, stay on the **Queries** tab. Use the filter icon above the table to keep rows with **Position greater
   than 7** (or sort by Position and scroll to 8–20).
4. Sort by **Impressions**. The top of the list is your shortlist: people search for it, Google thinks you're
   relevant, and you sit just below the clicks.
5. Click a query, then the **Pages** tab, to see which page Google shows for it.
6. Copy the top 10 into the free SEO tracker (Page 2 shortlist sheet).

**Skip:** queries that don't match what the page is for, and queries with a handful of impressions. One page often
ranks for several shortlist queries: fix the page once.

## Step 2: Fix each page (about 30 minutes each)

1. **Answer first.** The query's answer in the first two or three sentences, in plain words.
2. **The searcher's words in the title and main heading.** Google's Starter Guide: put them in "prominent locations on
   the page, such as the title and main heading". Once, naturally. Repeating them is keyword stuffing.
3. **Cover what the top 3 cover, then add one thing they don't:** your prices, a real example, a test, a table, your
   own photos. That last part is what makes the page worth ranking.
4. **Link to it** from 2 or 3 related pages on your site, with link text that says what the page is about.
5. **Update the facts, then the date.** Google's own helpful content page lists "changing the date of pages to make
   them seem fresh when the content has not substantially changed" as a warning sign.
6. **Request indexing once:** URL Inspection › Request indexing. Google: indexing "typically takes only a day or so",
   up to a week or two, and asking again doesn't speed it up.

## Step 3: Check after 3 weeks

- Google suggests waiting "a few weeks to assess whether your work had beneficial effects" (SEO Starter Guide).
- Compare the same length of time before and after the fix (21 days vs the 21 days before). Watch **clicks** first.
- Moved up but still no clicks? Look at the title and snippet: is it the answer people want?
- Didn't move? Run the ranking-principles audit on the page and compare it with the top 3 again.

## The Claude prompt (paste your export)

In Search Console, export the Performance report (Export › CSV or Google Sheets), then give the Queries and Pages files
to Claude:

```text
Here is my Search Console export (last 3 months). Find the queries with an average position between 8 and 20 and at least [50] impressions. Group them by the page that ranks. For each page, give me: the queries, total impressions, what the searcher wants, and the 3 edits most likely to move it up (answer first, what to add that the top results don't have, which internal links to add). Order the pages by impressions. Don't invent numbers.
```

With the free **seo-audit** or **ranking-principles** skill on, add: "Then audit the first page with ranking
principles."

---

Free skills (seo-audit, ranking-principles + 12 more): [github.com/WordRocket/claude-seo-skills](https://github.com/WordRocket/claude-seo-skills) ·
Sources: [Search Console Performance report](https://support.google.com/webmasters/answer/7576553) ·
[Request indexing](https://support.google.com/webmasters/answer/9012289) ·
[SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) ·
[Creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). Made by
WordRocket (wordrocket.ai), our own tool. Nobody honest can promise rankings: results vary.
