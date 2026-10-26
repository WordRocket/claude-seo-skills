# Ultimate SEO Prompt Library

Copy-paste these prompts directly into Claude. Replace all [BRACKETED] sections with your business info.
After running the Business Context prompt (Prompt 0) once, you don't need to repeat that context — just run
the numbered prompts in order.

---

## PROMPT 0 — SEO Brain Setup (Run This First, Once)

```
You are now my dedicated SEO consultant with 14+ years of experience in local and national SEO. 
I am going to give you everything you need to know about my business. From this point forward, 
all SEO recommendations must be based on this specific context — not generic advice.

Here is my business context:

Business name: [YOUR BUSINESS NAME]
Website URL: [YOUR WEBSITE URL]
Primary service: [e.g. emergency plumber, roofing contractor, HVAC repair, personal injury lawyer]
Secondary services: [list all services]
Primary location: [City, State/Country]
Service areas: [list all cities/suburbs you serve]
Target keywords: [e.g. "plumber New York", "emergency plumber Manhattan", "water heater repair NYC"]

Google Business Profile URL: [paste your GBP URL or say "not set up"]
Monthly GBP views: [from GBP Insights]
Monthly calls from GBP: [from GBP Insights]
Current review count: [number] with average rating: [X.X stars]

Top competitors (name + website + GBP URL):
1. [Competitor 1]
2. [Competitor 2]
3. [Competitor 3]

Google Search Console access: [yes/no]
SEO tool available: [Ahrefs / Semrush / Ubersuggest / none — and whether you're logged in on Chrome]
Monthly organic clicks (from GSC): [number or "unknown"]
Current rankings I care about: [paste from GSC or say "unknown"]

My biggest SEO problem right now: [describe — e.g. "I rank position 6–10 for my main keyword but get no calls"]
What I've already tried: [describe]
My #1 goal: [e.g. "rank top 3 for plumber New York and get 30+ calls/month"]

When you give me any recommendation, please always include:
- What to do (specific and actionable)
- Why it matters (tied to competitor data)
- Impact: High / Medium / Low
- Time to see results
- Difficulty: Easy / Medium / Hard

Ready? Acknowledge that you have my context and suggest which workflow to start with first.
```

---

## PROMPT 1 — GBP Competitor Deep Audit

```
You are a senior local SEO analyst. Open Chrome and go to maps.google.com.

Search for: [SERVICE] [CITY]
Example: "plumber New York" or "roofing contractor Austin"

Step 1 — Identify top 5 organic competitors:
Find the top 5 Google Business Profile listings that appear in organic results (not ads/sponsored).
Skip any directories (Yelp, Angi, HomeAdvisor, Thumbtack), national chains, or franchise aggregators.
Label them Competitor 1 through Competitor 5.

Step 2 — For each competitor, collect:

BUSINESS IDENTITY:
- Full business name (does it contain the target keyword?)
- Primary GBP category
- All visible secondary categories
- Listed address (street address vs just city? apartment or commercial address?)
- Is it marked as a service-area business?
- Operating hours (open 24/7? emergency availability flagged?)

REVIEW AUTHORITY:
- Total review count
- Average star rating
- Estimate of reviews received in the last 30 days (look at review dates)
- Estimate of reviews received in the last 60 days
- Do reviews mention specific service keywords? (e.g. "drain", "water heater", "leak")
- Do reviews mention specific neighbourhoods or cities?
- Are staff names mentioned in reviews?
- Any recurring complaints or negative themes?
- Does the owner respond to reviews? Estimate response rate and average response time.

PROFILE COMPLETENESS:
- Is a business description present? Approximate word count? Does it contain keywords?
- Are services listed in the Services section?
- Is the Q&A section populated?
- Is a website linked?

MEDIA & FRESHNESS:
- Approximate number of photos (many/some/few)
- Photo quality: real job photos? branded vehicles? stock images?
- Any videos present?
- When was the most recent photo uploaded? (days/weeks ago)
- Is the business posting Google updates/posts? When was the last post?

ATTRIBUTES:
- List every visible attribute tag (wheelchair accessible, veteran-owned, free estimates, LGBTQ+ friendly, 24/7, etc.)

Step 3 — Patterns & Insights:
After collecting data for all 5 competitors:
- What do ALL top 3 have in common?
- What do 2 out of 3 share?
- Who ranks despite having weaker signals? (proximity outlier?)
- What is the dominant ranking factor in THIS specific market? (reviews? proximity? category? posting activity?)

Step 4 — Outputs:
Present:
1. A competitor data table (one row per business, columns = all signals above)
2. Pattern summary (bullet points)
3. Top 7 ranking levers for this niche+city, ranked by impact, with evidence citing specific competitors
4. Priority action list: the 3 things I should do in the next 24 hours based on this data
```

---

## PROMPT 2 — GBP Category Optimisation

```
Based on the competitor data you just collected (or open Chrome → maps.google.com → search [SERVICE] [CITY]):

1. For the top 3–5 organic GBP listings (no directories), extract:
   - Primary category for each
   - Every secondary category for each
   
2. Create a category frequency table:
   - Which primary category appears most often? → This is my recommended primary category
   - Which secondary categories appear in ALL top 3? → Non-negotiable to add
   - Which appear in 2 out of 3? → Highly recommended
   - Which appear in only 1? → Consider if applicable

3. Compare to my current categories (if I've told you them) and flag any gaps.

4. Output a prioritised list:
   - PRIMARY CATEGORY: [exact category name to use]
   - NON-NEGOTIABLE SECONDARY CATEGORIES: [list]
   - RECOMMENDED SECONDARY CATEGORIES: [list]
   - OPTIONAL: [list]

5. If I'm logged into my Google account in Chrome:
   - Navigate to business.google.com/locations
   - Find my business: [BUSINESS NAME]
   - Update the primary category to your recommendation
   - Add all non-negotiable and recommended secondary categories
   - Save and confirm the changes were saved successfully
   - Report back exactly what was changed
```

---

## PROMPT 3 — GBP Attributes Audit

```
Open Chrome. For each of the top 3–5 ranking GBP listings for [SERVICE] [CITY]:
1. Click on the listing
2. Scroll through the profile and note every visible attribute tag
   (examples: wheelchair accessible, veteran-owned, women-led, LGBTQ+ friendly, free estimates,
   appointments required, credit cards accepted, free parking, 24/7 availability, online booking)

Create a table:
| Attribute | Competitor 1 | Competitor 2 | Competitor 3 | I Have It | Applicable to Me |
|-----------|-------------|-------------|-------------|-----------|-----------------|

For each attribute my competitors have that I'm missing:
- Note whether it's likely applicable to my business (based on what you know about it)
- Note likely ranking impact (High if all top 3 have it, Medium if 2 have it, Low if only 1 has it)

Output: 
1. The gap analysis table
2. An "Add immediately" list of attributes I should add to my profile
3. A note on any attributes that are likely NOT applicable to me (don't add fake attributes)

If I'm logged into Google in Chrome:
- Navigate to my GBP and add all applicable missing attributes
- Report what was added
```

---

## PROMPT 4 — Review Velocity & Teardown

```
Open Chrome. Visit the Google Business Profile for each of these competitors:
[COMPETITOR 1 GBP URL]
[COMPETITOR 2 GBP URL]  
[COMPETITOR 3 GBP URL]

For each competitor, collect:
1. Total review count
2. Average star rating
3. Count of reviews posted in the last 30 days (scroll reviews sorted by "Newest")
4. Count of reviews posted in the last 60 days
5. Count of reviews posted in the last 90 days
6. Are service-specific keywords mentioned in reviews? List the most common ones.
7. Are location/neighbourhood names mentioned in reviews?
8. Are staff names mentioned?
9. What is the recurring positive theme? (speed, cleanliness, pricing, expertise?)
10. What is any recurring complaint? (this is my USP opportunity)
11. Does the owner respond? What is their response rate (estimate)?
12. Average response time to reviews?

Then calculate:
- My current review count: [MY COUNT] | My average rating: [MY RATING]
- Review gap to Competitor 1: [X reviews behind]
- At my current collection rate of [MY RATE]/month, I'll catch up in [X months]
- To close the gap in 90 days, I need [X reviews/week]

Output:
1. Review data table (one row per competitor + one row for me)
2. Review velocity gap analysis with catch-up math
3. My weekly review target to dominate within 90 days
4. Recommended review ask script (what to say to customers post-job, naturally prompting service keywords + location)
5. Email/SMS follow-up template for review requests
6. Insight on what keyword + location combos to encourage in review asks
```

---

## PROMPT 5 — Review Response Strategy & Automation

```
Open Chrome. Visit the top 3 competitor GBP listings for [SERVICE] [CITY].

For each competitor:
1. How many total reviews? How many has the owner responded to? (estimate response rate %)
2. What is the average response time? (check timestamps on reviews and responses)
3. What is the tone of their responses? (formal/casual/template-sounding/personalised)
4. Do their responses include service keywords or location names? (this is a ranking signal)
5. How long are their responses on average?

Now look at my own GBP (if I've shared it): [MY GBP URL or "not set up yet"]
- How many unanswered reviews do I have?
- What is my current response rate?

Output:
1. Competitor response strategy comparison table
2. My recommended response playbook:
   - Target response time: [X hours/days to beat competitors]
   - Tone: [based on what works in my market]
   - Length: [based on what top performers do]
   - Keywords to naturally include in responses
3. 5 template responses I can use/adapt for common review types:
   - Positive 5-star review
   - Positive review mentioning a specific service
   - Neutral 3-4 star review
   - Negative 1-2 star review (professional de-escalation)
   - Review mentioning a staff member by name

If I'm logged in to Google in Chrome:
- Open my GBP review management page
- For each unanswered review, generate and post a personalised response using the playbook above
- Include keywords naturally (service name + location) in each response
- Report how many reviews were responded to
```

---

## PROMPT 6 — GBP Post Strategy

```
Open Chrome. For each of the top 3 ranking competitors for [SERVICE] [CITY]:
[COMPETITOR 1 GBP URL]
[COMPETITOR 2 GBP URL]
[COMPETITOR 3 GBP URL]

For each competitor:
1. Click on their "Updates" or "Posts" section
2. Note: how many recent posts are visible?
3. What types of posts are they publishing? (offer/event/update/product)
4. What is their posting frequency? (daily/weekly/monthly/sporadic)
5. When was their most recent post?
6. What topics do they post about? (seasonal tips, before/after jobs, promotions, reviews, team intros?)
7. What is the typical call to action? (call now / get a quote / book online)
8. Approximate post length (short caption vs. long description)

Now identify: 
- Which competitors are most active with posting?
- What content style seems most engaging (based on photo type, caption style)?
- Are there seasonal or timely themes to capitalise on right now (based on today's date: [TODAY'S DATE])?

Generate 10 ready-to-publish GBP posts for my business: [BUSINESS NAME] based in [CITY], specialising in [PRIMARY SERVICE].

Each post should include:
- Headline (8 words max, with keyword)
- Body (2–3 sentences, natural keyword inclusion, location mention)
- Call to action (specific: "Call [NAME] today at [PHONE]" or "Book online at [URL]")
- Post type recommendation (update/offer/event)
- Recommended publish date/timing (space them out weekly)

Make the posts sound like a real local business owner wrote them — not a marketing agency.
```

---

## PROMPT 7 — Keyword Gap Audit

```
Open Chrome. Navigate to [semrush.com OR ahrefs.com] — I am logged in.

Go to the Keyword Gap (Semrush) or Content Gap (Ahrefs) tool.

Enter:
- My domain: [MY WEBSITE URL]
- Competitor 1: [COMPETITOR 1 URL]
- Competitor 2: [COMPETITOR 2 URL]
- Competitor 3: [COMPETITOR 3 URL]

Filter the results to show ONLY keywords where:
- At least one competitor ranks in position 1–20
- My domain does NOT rank at all (not in top 100)
- Keyword contains at least one of these local/commercial intent signals:
  [city name], [neighbourhood names], near me, best, top, emergency, affordable, cheap, 
  licensed, certified, same day, 24 hour, free estimate, quote

Export or capture all results.

For each keyword, record:
- Keyword
- Monthly search volume
- Keyword difficulty (KD)
- Which competitor ranks and at what position
- Search intent (commercial service / local / informational)

Calculate an Opportunity Score for each: (search volume / KD) × commercial intent multiplier
(commercial = 3, local = 2, informational = 1)

Output:
1. Full keyword gap list as a table, sorted by Opportunity Score (highest first)
2. Group by: 
   - "Create new page" (no existing page on my site targeting this)
   - "Optimise existing page" (I have a relevant page but it's not ranking)
3. Top 20 priority keywords with specific page creation/optimisation recommendations
4. Save as a spreadsheet if possible
```

---

## PROMPT 8 — Money Page Audit (GSC Quick Wins)

```
Open Chrome. Navigate to Google Search Console: search.google.com/search-console

Make sure you're viewing the property for: [MY WEBSITE URL]

Go to Search Results report. Set date range to last 3 months.

Export all queries with:
- Average position between 4 and 15
- More than 20 impressions

For each page in this position range (group by URL / page):
1. What is the primary keyword driving impressions to this page?
2. Current average position
3. Current clicks vs impressions (CTR)
4. Estimated click increase if moved to position 1–3

Now open each of the top 10 opportunity pages in Chrome and audit:
- Title tag: does it contain the target keyword? Is it under 60 characters? Is it compelling?
- Meta description: present? Contains keyword? Has a CTA?
- H1: exists? Contains keyword? Only one H1?
- Word count: how does it compare to the top 3 ranking pages for that keyword?
- Internal links: how many internal links point to this page? (check via site: search or GSC)
- Page speed: use pagespeed.web.dev — is the score above 70 on mobile?
- Schema: does the page have appropriate schema markup?
- SERP features: do the top 3 results have FAQ sections, tables, or rich snippets this page lacks?

For each page, output:
1. Current status summary
2. Specific 5-item quick-win checklist
3. Estimated traffic uplift if all 5 wins are implemented
4. Priority: Critical (fix this week) / Important (fix this month) / Nice to have

Final output: Priority action table sorted by traffic upside potential.
Present this as the "gold mine list" — these are pages that are almost ranking and just need a push.
```

---

## PROMPT 9 — On-Page SEO Competitor Audit

```
Open Chrome. Search Google for: [TARGET KEYWORD] — e.g. "roofer New York"

Identify the top 5 organic results that are direct business competitors
(skip Yelp, directories, Reddit, Wikipedia, national brands unless they're your actual competition).

For each competitor page, open it in Chrome and collect:

TITLE & META:
- Full title tag (does it contain the keyword? Is it under 60 chars?)
- Meta description (present? Keyword included? Has a CTA?)

CONTENT:
- H1 tag (how many H1s? What does the H1 say? Does it contain the keyword?)
- H2 subheadings (do they cover relevant subtopics?)
- Word count (approximate — is this a thin page or comprehensive?)
- Does the content mention the city/location naturally throughout?
- Is there a clear unique value proposition?
- Is there video content embedded?
- Images: do they have descriptive alt text? Are they relevant job photos?

TECHNICAL SIGNALS:
- Page load time (use Chrome DevTools Network tab or report from pagespeed.web.dev)
- Is the page mobile-friendly? (check on mobile viewport in DevTools)
- Does the page have schema markup? (view source for JSON-LD or check with schema.org/validator)
- What schema types are used? (LocalBusiness, Service, Review, FAQ, etc.)
- Is there an OG image for social sharing?
- Internal linking: does the page link to other relevant service pages?

Create a comparison table: my page vs each competitor, all signals as columns.

Then output:
1. "5 things competitors are doing RIGHT that I should replicate on my page"
2. "5 mistakes competitors are making that I can exploit" (e.g. "Competitor 2 has 7 H1 tags — use exactly 1")
3. A specific 10-item on-page optimisation checklist for MY page at [MY PAGE URL]
4. Recommended title tag (new, optimised version)
5. Recommended meta description (new, optimised version)
6. Recommended H1 (new, optimised version)
7. Schema markup gaps to fix
```

---

## PROMPT 10 — Backlink Intelligence & Link Acquisition

```
Open Chrome. Navigate to [ahrefs.com OR semrush.com] — I am logged in.

We are going to analyse backlinks for the top 3 ranking competitors for the keyword: [TARGET KEYWORD]
My domain to exclude from analysis: [MY DOMAIN]

For each competitor ([COMPETITOR 1 URL], [COMPETITOR 2 URL], [COMPETITOR 3 URL]):

Step 1 — Get raw backlink profile:
- Total backlinks (raw number)
- Total referring domains (raw)

Step 2 — Apply quality filters:
- Filter 1: Dofollow links only (remove nofollow)
- Filter 2: One link per domain (unique domains only)
- Record count after each filter

Step 3 — Identify high-quality links (apply both criteria):
- Referring domain DR ≥ 40
- Referring domain gets ≥ 2,000 monthly organic visits
- Record this "true quality link" count

Step 4 — DR tier breakdown:
For the dofollow + unique domain filtered list, how many links fall in:
- DR 70+ 
- DR 50–69
- DR 30–49
- DR 10–29
- DR 0–9

Step 5 — Spam score assessment:
What percentage of the backlinks appear to be from PBNs, link farms, or unrelated foreign sites?
Flag if spam % > 30% (high risk competitor — do not replicate their strategy).

Step 6 — Link opportunity list:
For the high-quality links (DR 40+, 2K+ traffic), list the top 20 referring domains with:
- Domain name
- DR score
- Monthly traffic
- Type of site (local directory, news site, industry blog, association, partner, etc.)
- The anchor text used

Step 7 — Calculate my target:
Based on where the top 3 competitors sit, what is my target to rank in top 3?
- Target DR for my domain overall
- Links needed in each DR tier
- Realistic timeline to acquire them

Generate a premium PDF report with all this data. Include:
- Executive summary
- Competitor backlink comparison table
- DR tier distribution chart (describe as table if chart not possible)
- Red flags / spam alerts
- My target link profile
- Top 20 outreach targets (the domains linking to competitors — prioritised by DR + traffic)
- Outreach email template: "You link to [competitor] — would you also link to us?"
```

---

## PROMPT 11 — Technical SEO Audit

```
Run a technical SEO audit on my website: [MY WEBSITE URL]

Use Chrome and web fetch to check each of the following. For items you can't verify directly,
note them as "manual verification needed" with instructions.

CRAWLABILITY:
- Fetch [MY URL]/robots.txt — is anything important being blocked?
- Fetch [MY URL]/sitemap.xml — does it exist? Are all key service pages included?
- Check if the site is indexed: search "site:[MY DOMAIN]" in Google and report results

SECURITY & PROTOCOL:
- Is the site on HTTPS? Any HTTP pages that redirect incorrectly?
- Check for mixed content warnings (HTTP resources on HTTPS pages)

MOBILE:
- Open in Chrome mobile view (DevTools) — does it render properly?
- Is text readable without zooming? Are buttons tap-friendly?

PAGE SPEED (fetch from pagespeed.web.dev/analysis?url=[MY URL]):
- Mobile performance score
- Desktop performance score  
- Largest Contentful Paint (LCP) — target: under 2.5 seconds
- Cumulative Layout Shift (CLS) — target: under 0.1
- Interaction to Next Paint (INP) — target: under 200ms
- Specific issues flagged by PageSpeed

ON-PAGE STRUCTURE (check homepage + main service page):
- Title tags: present on all pages? Unique? Under 60 chars? Keyword included?
- Meta descriptions: present? Under 160 chars? Include keyword + CTA?
- H1: exactly one per page? Contains primary keyword?
- Image alt text: all images have descriptive alt text?
- Internal linking: are key service pages linked from the homepage and other pages?
- Canonical tags: are they set correctly?

SCHEMA (fetch page source or check with validator.schema.org):
- What schema markup exists?
- What's missing? (LocalBusiness, Service, Review, FAQ recommended)

STRUCTURED DATA (Google's perspective):
- Fetch https://search.google.com/test/rich-results?url=[MY URL] — any errors?

Output: Prioritised fix list
| Issue | Severity | Fix | Difficulty | Impact |
Sort by: Critical → Important → Nice-to-have
Include: "Easy wins" section — issues that take under 30 minutes to fix
```

---

## PROMPT 12 — Content Strategy & Blog Keyword Research

```
Open Chrome. Navigate to [ahrefs.com OR semrush.com] — I am logged in.

I want to build a content calendar of blog posts targeting keywords my potential customers search
before hiring a [PRIMARY SERVICE] in [CITY].

Step 1 — Go to Keywords Explorer / Keyword Magic Tool
Enter seed keyword: [PRIMARY SERVICE] (e.g. "roofing", "plumbing", "HVAC")
Filter to: Questions section

Step 2 — Apply filters:
- Search volume: minimum 50/month
- Keyword difficulty: under 40 (preferably under 20 for quick wins)
- Include keywords about: costs, how to choose, what to look for, signs you need, best, top rated
- EXCLUDE: keywords about doing it yourself (install, DIY, how to fix yourself)
- EXCLUDE: keywords aimed at business owners (how to start, how to market)
- INCLUDE: keywords with local intent where possible

Step 3 — Filter for opportunity:
Show me keywords where at least one site ranking in top 5 has DR under 20
(these are the easiest to rank for — low DR sites are beatable)

Step 4 — Google Trends check:
For the top 10 keywords identified, check interest over time and seasonal patterns.
Are any of them trending right now or about to peak seasonally?
Note: publish 6–8 weeks before seasonal peak for best results.

Step 5 — Output a content calendar:
12 blog post recommendations, each with:
- Post title (SEO-optimised, natural language)
- Target keyword
- Monthly search volume
- Keyword difficulty
- Recommended word count (based on top 3 ranking posts for that keyword)
- Seasonal timing recommendation
- Priority: High / Medium / Low (based on commercial intent + volume + difficulty)
- Brief outline (5-point structure for the article)

Sort by priority. The first 3 should be posts I can publish this month.
```

---

## PROMPT 13 — Schema Markup Audit & Implementation

```
Check what schema markup my competitors are using for the keyword: [TARGET KEYWORD]
and what I'm missing on my page: [MY PAGE URL]

For the top 3 ranking pages:
1. View source or use a schema validator to identify all JSON-LD schema types present
2. List: what structured data does each competitor implement?

For my page:
1. Check current schema markup
2. Identify gaps

Now generate complete, ready-to-implement JSON-LD code blocks for:

1. LocalBusiness schema (include: name, url, telephone, address, geo coordinates, 
   openingHoursSpecification, priceRange, aggregateRating if I have reviews)
   Business details: [NAME, ADDRESS, PHONE, HOURS, RATING]

2. Service schema (one for each primary service):
   Services: [LIST SERVICES]

3. FAQ schema (use these 5 common questions about my service — or generate the most asked ones):
   [OPTIONALLY LIST YOUR FAQs OR SAY "generate the top 5 questions customers ask about [SERVICE]"]

4. BreadcrumbList schema for the page structure

5. AggregateRating schema using my Google reviews:
   Rating: [X.X] | Review count: [N]

For each schema block:
- Provide the complete JSON-LD code
- Tell me where to add it (in the <head> of the page)
- Confirm it will pass Google's Rich Results Test
```

---

## PROMPT 14 — Core Web Vitals & Page Speed Fix

```
Fetch the Google PageSpeed Insights report for my website:
URL: https://pagespeed.web.dev/analysis?url=[MY WEBSITE URL]

Analyse both mobile and desktop scores.

For each of the Core Web Vitals:

LCP (Largest Contentful Paint) — target: under 2.5s
- What element is causing the LCP? (usually hero image or main heading)
- Specific fix recommendations

CLS (Cumulative Layout Shift) — target: under 0.1
- What elements are shifting? (images without dimensions, late-loading ads/embeds?)
- Specific fix recommendations

INP (Interaction to Next Paint) — target: under 200ms
- What JavaScript is causing slow responsiveness?
- Specific fix recommendations

Also check:
- Total Blocking Time (TBT)
- Speed Index
- Time to First Byte (TTFB)

Generate a fix list:
| Issue | Current Score | Target | Fix | Difficulty | Dev or DIY? |

Prioritise: fixes that will move the needle most for mobile (Google primarily uses mobile scores).

For each fix, explain it in plain English — I may need to explain these to a web developer.
```

---

## BONUS PROMPT — Competitor Spy (Run Daily/Weekly)

```
Open Chrome. Run a quick competitive intelligence check for my business: [BUSINESS NAME] in [CITY].

Check my top 3 competitors:
1. [COMPETITOR 1 GBP URL + WEBSITE]
2. [COMPETITOR 2 GBP URL + WEBSITE]
3. [COMPETITOR 3 GBP URL + WEBSITE]

In the last 7 days:
- Have they posted any new GBP updates? What did they post?
- Have they gotten new reviews? How many? What's being said?
- Have they responded to reviews? 
- Any new pages or content on their website?
- Any new offers or promotions visible on their GBP?
- Any changes to their business hours or attributes?

Compare to me:
- Did I post on GBP this week? [yes/no]
- Did I get new reviews? [count]
- Did I respond to all reviews?

Output:
1. Competitor activity summary (what they're up to)
2. Opportunities I'm missing (they're doing something I'm not)
3. 3 specific actions I should take this week to stay ahead
```

---

## BONUS PROMPT — Outreach Email Generator (Backlink Acquisition)

```
Based on the backlink target list from Prompt 10, generate personalised outreach emails for the 
top 10 link opportunities.

For each target domain, the email should:
- Reference that they link to [SPECIFIC COMPETITOR] (makes it relevant and non-spammy)
- Briefly introduce my business and why I'm a relevant resource for their audience
- Make a specific ask (guest post / resource page addition / testimonial exchange / partnership)
- Be under 150 words (busy website owners don't read essays)
- Sound like a human wrote it, not a marketing agency

Target domains:
[PASTE THE LIST FROM PROMPT 10]

My business details:
- Name: [NAME]
- URL: [URL]
- Location: [CITY]
- What makes me credible: [e.g. "10 years in business, 200+ 5-star reviews, licensed and insured"]

Output: 10 personalised email drafts, one per target domain, ready to send (or copy into a mail merge).
```
