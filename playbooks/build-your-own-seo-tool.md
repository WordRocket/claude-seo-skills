# Build your own SEO tool for under 7 cents (DataForSEO + Claude)

Keyword research, a rank check, competitor research and a backlink check, run from a Claude chat on DataForSEO's
pay-as-you-go API. On Nov 13, 2026 we ran all four for our own site and DataForSEO charged **$0.067** in total. No
subscription: you pay per request. Below: the setup, the 4 prompts to paste, the real bill, and the honest catches.
Prices checked Nov 13, 2026; check [dataforseo.com/pricing](https://dataforseo.com/pricing) before you rely on them.

## What you need

- **A DataForSEO account.** New accounts get a **$1 free credit** for testing. After that, top-ups start at **$50** and
  the balance never expires. ([Help Center](https://dataforseo.com/help-center/how-does-your-free-unlimited-trial-work), [pricing](https://dataforseo.com/pricing))
- **Claude with custom connectors.** DataForSEO's setup guide lists a Claude Pro plan as the prerequisite.
- Optional: the free **dataforseo-seo-tool** skill (it estimates every cost first and builds the report for you).
- Optional: the **WordRocket** connector, to write the pages the report says you're missing (WordRocket is our own tool).

## Setup (5 minutes)

1. Create your account at [dataforseo.com](https://dataforseo.com).
2. In Claude: **Customize › Connectors › Add custom connector**. Name: DataForSEO. URL:
   `https://mcp.dataforseo.com/v3/mcp`. Add it, then approve the authorization screen (you sign in to DataForSEO; no API
   key goes into Claude). ([DataForSEO's guide](https://dataforseo.com/model-context-protocol))
3. Optional: add the skill: **Customize › Skills › + Add › Upload skill** and pick `dataforseo-seo-tool.zip` from the
   free repo's `dist/` folder.
4. Open a new chat, make sure the DataForSEO connector is on, and paste prompt 1.

**No connector?** Sign in at app.dataforseo.com, open **API Playground**, pick the endpoint, paste the request (the free
skill writes it for you), press Send. Every response shows its `cost`. Paste the response into Claude and ask for the
report. Never paste your API password into a chat.

| job | endpoint |
|---|---|
| Keyword research | `dataforseo_labs/google/keyword_suggestions/live` |
| Rank tracking | `serp/google/organic/live/advanced` |
| Competitors | `dataforseo_labs/google/competitors_domain/live` |
| Backlinks | `backlinks/summary/live` |

## The 4 prompts

Swap the [brackets] for your own keyword, site and country.

**1. Keyword research**

```text
Use DataForSEO (Labs keyword suggestions, live) for the seed keyword "[ai blog writer]", location [United States], language English. Limit 20, sorted by search volume. Tell me the estimated cost before you call it. Show a table: keyword, monthly search volume, keyword difficulty. Mark the 5 best targets for [my site and what it sells]. Then tell me the actual cost from the response. Don't invent any numbers.
```

**2. Rank tracking**

```text
Use DataForSEO (Google organic SERP, live advanced) for "[ai blog writer]", [United States], English, desktop, depth 100. Estimate the cost first. Tell me where [mysite.com] ranks (position and URL) or say it's not in the top 100, list the top 10 domains and the SERP features (AI Overview, People Also Ask, local pack). Then the actual cost.
```

**3. Competitors**

```text
Use DataForSEO (Labs competitors domain, live) for [mysite.com], [United States], English, exclude top domains, limit 10, sorted by shared keywords. Estimate the cost first. Table: domain, shared keywords, and whether each one looks like a real competitor. Then the actual cost.
```

**4. Backlinks**

```text
Use DataForSEO (Backlinks summary, live) for [mysite.com], including subdomains, live links only. Estimate the cost first. Give me backlinks, referring domains, rank, spam score and first seen, in plain words. Then the actual cost.
```

**Then put it together**

```text
Put the four results into one report: keywords, where I rank, top competitors, backlink summary, and the 3 biggest gaps (each with the number behind it and the page or fix that closes it). Add a table of what each call cost. Only use numbers from the responses above.
```

## What it really cost (Nov 13, 2026)

Four requests from our own account, for our own site and the keyword "ai blog writer" (US, English). The cost is the
`cost` field DataForSEO returned.

| job | what came back | cost |
|---|---|---|
| Keyword research | 20 of 61 ideas with volume and difficulty (top one: 260 searches a month, difficulty 27) | $0.0144 |
| Rank tracking | Google's top 100 (US, desktop): 99 organic results plus an AI Overview. Our site wasn't in it | $0.0155 |
| Competitors | 829 competing domains, top 10 returned | $0.0132 |
| Backlinks | 1,248 backlinks from 333 referring domains | $0.024 |
| **Total** | | **$0.067** |

**The price list behind it:** DataForSEO Labs $0.012 per task + $0.00012 per result
([pricing](https://dataforseo.com/pricing/dataforseo-labs/dataforseo-google-api)) · Google organic SERP, live mode,
$0.002 per 10 results; our depth-100 call was billed $0.0155
([pricing](https://dataforseo.com/pricing/google-serp/google-organic-serp-api)) · Backlinks $0.024 per task + $0.000036
per row ([pricing](https://dataforseo.com/pricing/backlinks/backlinks)), with no monthly minimum since Jul 1, 2026, when
the $100/mo commitment was removed ([update](https://dataforseo.com/update/pricing-update-in-dataforseo-apis)).

## The honest notes

- **The free dollar covers this test about 14 times** ($0.067 each). After that, the smallest top-up is $50 (it never
  expires).
- **Not like-for-like with Semrush or Ahrefs.** Semrush's SEO plan is $139/mo and Ahrefs Lite is $129/mo (list prices,
  billed monthly, checked Nov 13, 2026). They include dashboards, history, site audits and tracking projects. Here you get
  raw data on demand and Claude builds the view.
- **Costs grow with limits.** 20 keyword ideas cost $0.0144; 1,000 cost about $0.13. Twenty rank checks at depth 100
  cost about $0.31. Ask Claude for the estimate first (the free skill does it automatically and asks before anything
  over $0.25).
- **It's DataForSEO's data.** Search volumes are monthly estimates; a ranking is one check at one place and time, and it
  changes day to day.
- **Never let a chat top up or change billing.** Do that yourself in your DataForSEO account.

## Then write the gap pages

Our run found our own site missing from Google's top 100 for the keyword it should own: that's the next page. Brief each
gap with the free **ranking-principles** skill, then write it yourself, with any writer, or with **WordRocket** (our own
tool, connector `https://wordrocketapi.com`). Re-run the rank check monthly.

---

17 free SEO skills: [github.com/WordRocket/claude-seo-skills](https://github.com/WordRocket/claude-seo-skills) ·
Sources: [DataForSEO pricing](https://dataforseo.com/pricing) ·
[MCP connector](https://dataforseo.com/model-context-protocol) ·
[Remote MCP with OAuth](https://dataforseo.com/help-center/connecting-the-remote-dataforseo-mcp-server-using-oauth) ·
[Semrush pricing](https://www.semrush.com/pricing/seo-ai-search/) · [Ahrefs pricing](https://ahrefs.com/pricing). Made
by WordRocket (wordrocket.ai), our own tool. Not affiliated with DataForSEO. Results vary.
