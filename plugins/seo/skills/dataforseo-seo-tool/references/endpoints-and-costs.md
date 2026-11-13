# DataForSEO: the 4 requests, what they cost, where the numbers are (checked Nov 13, 2026)

Every request is a `POST` to `https://api.dataforseo.com/v3/<endpoint>` with a JSON **array** of tasks as the body (one
task per request here). The connector builds this for you; in the API Playground the user pastes the body. If a field
isn't where this file says, look it up in DataForSEO's docs (docs.dataforseo.com/v3) instead of guessing.

## Price formulas (estimate before every call)

| API | formula | examples |
|---|---|---|
| DataForSEO Labs (keyword suggestions, competitors, ranked keywords) | $0.012 per task + $0.00012 per result returned | limit 10: $0.0132 · limit 20: $0.0144 · limit 100: $0.024 · limit 1,000: $0.132 |
| Google Organic SERP, live mode | $0.002 per SERP of 10 results | depth 10: $0.002 · depth 100: $0.0155 in our run (less than 10 × $0.002, so pages after the first cost less: use the `cost` field and the pricing page for the exact rate) |
| Backlinks | $0.024 per task + $0.000036 per row | summary (1 row): $0.024 · a list of 100 rows: about $0.028 · 1,000 rows: about $0.06 |

- The SERP API's standard queue ($0.0006) and priority queue ($0.0012) are cheaper per 10 results but not instant: post
  a task, then fetch it later. This skill uses live mode so the answer comes back in the same chat.
- Backlinks has had no monthly minimum since Jul 1, 2026 (the $100/mo commitment was removed): it runs on the normal
  pay-as-you-go balance. Our backlinks call worked that way.
- The guardrail: ask before anything estimated over $0.25 (a single call, a batch, or the session total). Example: 20
  rank checks at depth 100 ≈ 20 × $0.0155 ≈ $0.31, so ask first.

## 1. Keyword research: `dataforseo_labs/google/keyword_suggestions/live`

```json
[{
  "keyword": "ai blog writer",
  "location_name": "United States",
  "language_code": "en",
  "order_by": ["keyword_info.search_volume,desc"],
  "limit": 20
}]
```

Where the numbers are: `tasks[0].result[0].total_count` (how many ideas exist) and `tasks[0].result[0].items[]`, each
with `keyword`, `keyword_info.search_volume` (monthly average), `keyword_info.cpc`,
`keyword_properties.keyword_difficulty` (0–100) and, when present, `search_intent_info.main_intent`.
Labs data is by country; for one city, use a rank check (job 2) with a city location.

## 2. Rank tracking: `serp/google/organic/live/advanced`

```json
[{
  "keyword": "ai blog writer",
  "location_name": "United States",
  "language_code": "en",
  "device": "desktop",
  "depth": 100
}]
```

Where the numbers are: `tasks[0].result[0].items[]`, each with a `type` (`organic`, `ai_overview`, `people_also_ask`,
`local_pack`, …). For `organic` items: `rank_group` (position among the organic results: use this as "position"),
`rank_absolute` (position among everything on the page), `domain`, `url`, `title`. `result[0].item_types` lists the
features on the page. Match the site's domain (with and without `www.`) to find it; no match = "not in the top 100".
City-level checks: set `location_name` to the city (e.g. `"Austin,Texas,United States"`; check the exact name in
DataForSEO's locations list).

## 3. Competitors: `dataforseo_labs/google/competitors_domain/live`

```json
[{
  "target": "wordrocket.ai",
  "location_name": "United States",
  "language_code": "en",
  "exclude_top_domains": true,
  "order_by": ["intersections,desc"],
  "limit": 10
}]
```

Where the numbers are: `tasks[0].result[0].total_count` (how many competing domains exist) and `items[]`, each with
`domain`, `intersections` (keywords both sites rank for) and `avg_position`. Skip the target's own row if it shows up.

## 4. Backlinks: `backlinks/summary/live`

```json
[{
  "target": "wordrocket.ai",
  "include_subdomains": true,
  "exclude_internal_backlinks": true,
  "backlinks_status_type": "live"
}]
```

Where the numbers are: `tasks[0].result[0]` → `rank` (DataForSEO's own score), `backlinks`, `referring_domains`,
`referring_main_domains`, `backlinks_spam_score`, `first_seen`.

## Every response
- `cost` at the top (the whole request) and `tasks[i].cost` (each task): that's the actual charge to report.
- `tasks[i].status_code` 20000 = OK. Anything else: read `status_message`, fix the input once, tell the user.

## Worked example: our real run (Nov 13, 2026, API Playground, the creator's own account)

| job | what we asked | what came back | cost |
|---|---|---|---|
| Keyword research | "ai blog writer", US, English, limit 20 by volume | 20 of 61 ideas. Top: ai blog writer 260/mo (difficulty 27), best ai blog writer 70 (27), eesel ai blog writer 70 (0), ai blog post writer 50 (22), seo ai blog writer 40 (28), free ai blog writer 30 (43) | $0.0144 |
| Rank tracking | "ai blog writer", US, desktop, depth 100 | 110 items: 99 organic + an AI Overview + related searches. wordrocket.ai not in the top 100. Top 3: Crocoblock, Reddit (r/Blogging), ClickUp | $0.0155 |
| Competitors | wordrocket.ai, US, no giant sites, limit 10 | 829 competing domains. Top shared keywords: promptbase.com 27, feedough.com 26, quillbot.com 26, generateprompt.ai 25, docsbot.ai 23 | $0.0132 |
| Backlinks | wordrocket.ai, subdomains on, live links | rank 38, 1,248 backlinks, 333 referring domains (317 main domains), spam score 17, first seen 2023-05-25 | $0.024036 |
| **Total** | | | **$0.067136** |

The gap it found: the site wasn't in Google's top 100 for the keyword it should own, so that page went to the writer
next. A difficulty of 0 with real volume (as for some rows above) is DataForSEO's estimate: check the live results before
calling a keyword easy.

## Sources
- Pricing: pay as you go, no subscriptions, $50 minimum top-up, balance never expires: https://dataforseo.com/pricing
- Free $1 credit for API testing on registration (Help Center, updated Oct 21, 2026): https://dataforseo.com/help-center/how-does-your-free-unlimited-trial-work
- Labs pricing, $0.012 per task + $0.00012 per item (live): https://dataforseo.com/pricing/dataforseo-labs/dataforseo-google-api
- Google Organic SERP pricing, standard $0.0006, priority $0.0012, live $0.002 per SERP of 10 results: https://dataforseo.com/pricing/google-serp/google-organic-serp-api
- Backlinks pricing, $0.024 per task + $0.000036 per row: https://dataforseo.com/pricing/backlinks/backlinks
- Pricing update, Jul 1, 2026 (Backlinks $100/mo commitment removed): https://dataforseo.com/update/pricing-update-in-dataforseo-apis
- MCP connector URL and setup in Claude: https://dataforseo.com/model-context-protocol
- Remote MCP server with OAuth (lists Claude Pro as the prerequisite): https://dataforseo.com/help-center/connecting-the-remote-dataforseo-mcp-server-using-oauth
- API Playground: https://app.dataforseo.com/api-playground
- Semrush SEO plan $139/mo billed monthly: https://www.semrush.com/pricing/seo-ai-search/ · Ahrefs Lite $129/mo billed monthly: https://ahrefs.com/pricing (both checked Nov 13, 2026; list prices, not like-for-like)
