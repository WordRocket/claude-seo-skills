# Keyword maxing: sources, prompts, layers, CSV and brief template (checked Nov 14, 2026)

## Primary sources (what each one says, so you quote it right)

| claim | source | the words |
|---|---|---|
| AI Mode splits a question into subtopics and runs many searches | Google, [AI in Search: Going beyond information to intelligence](https://blog.google/products/search/google-search-ai-mode-update/) (Google I/O 2025, Elizabeth Reid, VP, Head of Search, May 20, 2025) | "AI Mode uses our query fan-out technique, breaking down your question into subtopics and issuing a multitude of queries simultaneously on your behalf." Deep Search "can issue hundreds of searches". |
| AI Overviews and AI Mode may both use fan-out; no special optimization | Google Search Central, [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) | both "may use a 'query fan-out' technique — issuing multiple related searches across subtopics and data sources"; "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary." |
| Autocomplete = real searches, not volumes | Google Search Help, [How Google autocomplete predictions work](https://support.google.com/websearch/answer/7368877) | predictions "reflect real searches that have been done on Google"; autocomplete "doesn't simply display the most common queries on a given topic". |
| Focus beats breadth | Google Search Central, [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | "Does your site have a primary purpose or focus?" · "Are you producing lots of content on many different topics in hopes that some of it might perform well in search results?" · no preferred word count ("No, we don't.") |
| Keyword Planner needs a set-up Google Ads account | Google Ads Help, [Use Keyword Planner](https://support.google.com/google-ads/answer/7337243) | "You must complete your account setup by entering your billing information" to use its basic features. |
| Low-spend accounts may get ranges | Search Engine Journal, [Google's Keyword Planner providing limited data to low-spending advertisers](https://www.searchenginejournal.com/googles-keyword-planner-tool-providing-limited-data-low-spending-advertisers/170837/) (Aug 15, 2016) | Google's notice: "Advertisers with lower monthly spend may see a limited data view in the Keyword Planner." (Google hasn't published the threshold.) |
| DataForSEO keyword ideas cost cents | [dataforseo.com/pricing](https://dataforseo.com/pricing) + our own request, Nov 13, 2026 | Labs: $0.012 per task + $0.00012 per result. Seed "ai blog writer", US, limit 20: 61 ideas, 260 searches/mo, difficulty 27, cost $0.0144. |

## Prompts to paste

**Run the whole playbook (Claude):**
```text
Run the keyword maxing playbook for [mysite.com]. We sell [what] to [who] in [country / city]. Competitors I know: [optional]. Use web search. No search volumes unless a real tool returns them.
```

**The buyer's question in ChatGPT / Gemini / Google AI Mode** (the user runs it if Claude can't, then pastes the answer
and the sources):
```text
[The exact question a buyer would type, e.g. "What's the best AI blog writer for a small business that wants Google traffic?"]
```
Then log: the subtopics in the answer, the follow-up questions it suggests, every cited source (domain + URL), the date.

**Reddit / Quora (web search):** `site:reddit.com "[seed]"` · `site:quora.com "[seed]"` · `site:reddit.com [seed] vs`

**Autocomplete modifiers:** `[seed]` · `[seed] for` · `[seed] vs` · `how to [seed]` · `best [seed]` · `[seed] cost` ·
`is [seed]` · `[seed] free` · `[seed] for [audience]` (a handful, typed by hand in the browser).

## The fan-out layers (check every seed against them)
| layer | example for "ai blog writer" |
|---|---|
| what is / how it works | how does an ai blog writer work |
| how to | how to write a blog post with ai that ranks |
| cost / free | is there a free ai blog writer |
| best / top | best ai blog writer for seo |
| vs / comparison | [tool A] vs [tool B] |
| alternatives | [big brand] alternatives |
| for [audience] | ai blog writer for small business / agencies |
| problems / risks | will google penalize ai content |
| examples / templates | ai blog post examples |
| is it worth it / reviews | are ai blog writers worth it |
| local (local businesses only) | [service] in [city], [service] near me |

The examples show the shape only: in a real run every row must come from a source you saw.

## CSV columns (`keyword-maxing.csv`)
```text
cluster,page_type,keyword_or_question,intent,funnel,sources,source_urls,evidence_count,competitors_covering,gap,difficulty_proxy,priority,volume,keyword_difficulty,metric_source,existing_url,status
```
- `page_type`: pillar · spoke · section (answered inside another page)
- `sources`: any of PAA · related · autocomplete · ChatGPT · Gemini · AI Mode · Reddit · Quora · competitor · Search
  Console · idea (unverified), separated by `|`
- `gap`: yes · thin · no · `difficulty_proxy`: 0–3 (3 = easiest) · `priority`: 0–15
- `volume`, `keyword_difficulty`: only from `metric_source` (DataForSEO / Keyword Planner / Search Console + date);
  otherwise `no data`
- `status`: covered · thin · missing

## Page brief template
```text
Page: [title idea]  ·  type: pillar / spoke  ·  cluster: [name]  ·  priority [n]/15
Main question: [the buyer's words]
Also answers (fan-out): [3–8 sub-questions, each with its source]
Intent / funnel: [ ]
First two sentences must say: [the direct answer]
Outline (H2 = sub-question): [ ]
What the top 3 results miss: [from reading them]
First-hand proof to add: [data, screenshots, photos, a real example, a price, a test]
Sources to cite: [primary sources]
Internal links: pillar [URL] · spokes [URL], [URL]
Schema: [only if it matches what's on the page]
Call to action: [ ]
```
