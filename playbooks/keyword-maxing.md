# SEO keyword maxing: free keyword research with Claude (fan-out for Google + AI search)

One prompt in Claude finds your real competitors, fans every topic out into the questions people actually ask, and turns
them into a topical map plus 5 page briefs. Free: it uses web search, Google's own free boxes and the AI answers you can
already open. Search volumes only appear when a real tool returns them. Checked Nov 14, 2026.

## Why "fan-out"

Google says AI Mode "uses our query fan-out technique, breaking down your question into subtopics and issuing a multitude
of queries simultaneously on your behalf" ([Google, I/O 2025, May 20, 2025](https://blog.google/products/search/google-search-ai-mode-update/)).
Its Search Central page says AI Overviews and AI Mode may both use it, and that there are "no additional requirements to
appear in AI Overviews or AI Mode, nor other special optimizations necessary"
([AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)).

So the job is classic SEO, done thoroughly: find the sub-questions behind each topic, and answer each one well on a page
that belongs to a clear topic cluster. That serves people searching Google, and it serves the searches Google's own
systems run.

## What you need

- **Claude** with web search on (any plan that has it).
- The free **keyword-maxing** skill: `dist/keyword-maxing.zip` in the free repo. In Claude: **Customize › Skills › + Add ›
  Upload skill**. No skills on your plan? Attach the skill's `SKILL.md` to a chat and say "follow this".
- Optional: **Claude in Chrome**, so Claude can read Google's boxes itself. Without it you paste what you see.
- Optional, for real search volumes: the free **dataforseo-seo-tool** skill (cents per check), a **Google Keyword Planner**
  export, or your **Search Console** queries.

## The one prompt

```text
Run the keyword maxing playbook for [mysite.com]. We sell [what] to [who] in [country / city]. Competitors I know: [optional]. Use web search. No search volumes unless a real tool returns them.
```

## What Claude does (and the prompt for each step if you'd rather go one at a time)

**1. Reads your site** (homepage, services, blog, sitemap) and lists what you already cover.

**2. Finds your real competitors**: the sites that rank for your buyers' searches, split into business rivals,
publishers / "best of" lists and forums, and what the top rivals cover that you don't.

```text
Search the web for 6 searches my buyers would type for [what I sell]. List every domain in the top results, split into business rivals, publishers/lists and forums. For the top 3 rivals, list the topics and page types they have that [mysite.com] doesn't.
```

**3. Picks 5–10 seed topics** in the buyer's words.

**4. Fans out every seed** into the sub-questions behind it, from free sources, each one logged with where it came from:

- Google **autocomplete** (type the seed + "for", "vs", "best", "cost"…). Google: predictions "reflect real searches
  that have been done on Google", but they aren't the most common queries or volumes
  ([Google Search Help](https://support.google.com/websearch/answer/7368877)).
- Google's **People also ask** (when it shows), **People also search for**, and the headings of the **AI Overview**.
- **ChatGPT, Gemini and Google AI Mode**: ask the buyer's exact question; log the subtopics in the answer, the follow-up
  questions and every source it cites (those sources are also where you want to be mentioned).
- **Reddit and Quora** threads (`site:reddit.com "[seed]"`), in the buyer's own words.
- The H2s of the competitor pages that rank.

```text
Fan out the seed "[seed]": collect the sub-questions from Google autocomplete, People also ask / People also search for, Reddit and Quora threads, and the competitor pages that rank. Log the source of every one. Don't add questions you didn't see; mark your own ideas "idea (unverified)".
```

**5. Cleans the long-tail list**: merges duplicates, tags intent (informational, commercial, transactional, local) and
counts how many sources surfaced each question.

**6. Builds the topical map**: one pillar page per seed, one spoke page per cluster of questions a single page can
answer, internal links between them, and your existing URLs marked covered / thin / missing. Keep it focused: Google's
own checklist asks "Does your site have a primary purpose or focus?"
([helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)).

**7. Prioritises** every page 0–3 on intent fit, competitor gap, fan-out breadth, a free difficulty proxy (who holds
Google's page 1: forums and thin pages = easier, big brands with a page built for it = harder) and your first-hand edge.

**8. Optional real numbers** (only from a real source, otherwise the cell says "no data"):

| source | cost | what you get | the catch |
|---|---|---|---|
| DataForSEO (free **dataforseo-seo-tool** skill) | cents per check | volume + difficulty per keyword | $1 free credit, then a $50 minimum top-up |
| Google Keyword Planner | free tool | Google's own volume estimates | Google's help: you must complete Google Ads account setup, including billing info. Low-spend accounts "may see a limited data view" (ranges like 100–1K) |
| Google Search Console | free | the searches your site already shows up for | only your own verified site |

Our real DataForSEO check (Nov 13, 2026): seed "ai blog writer", US → 61 keyword ideas; the seed itself 260 searches a
month, difficulty 27; cost $0.0144.

**9. Hands you the output**: `keyword-maxing.csv` (cluster, page type, question, intent, sources + URLs, gap, difficulty
proxy, priority, volume only with its source), the topical map, and 5 page briefs (main question, its fan-out, the
answer in the first two sentences, outline, what the top 3 results miss, first-hand proof, sources, internal links).

## Our run (Nov 14, 2026, wordrocket.ai)

We ran the one prompt on our own site in Claude.ai (web search on, the skill's `SKILL.md` attached to the chat). We declined Claude's request to use Chrome, so the
Google boxes and the AI Mode answer came from our own Chrome session and were pasted in, exactly as step 4 allows.

- **Competitors:** eesel.ai showed up for every seed; behind it Surfer, Koala, RightBlogger, PostNext, SEOwind and a long
  tail of WordPress plugins.
- **What we were missing:** almost all of our 49 sitemap URLs were prompt-engineering pages and free tools. No page for
  "AI blog writer", WordPress publishing, pricing or getting cited by AI.
- **Fan-out for "ai blog writer":** autocomplete (with images free · free · github · us · with images · tool · jobs · for
  seo · for wordpress), 8 "People also search for" searches (including "eesel ai blog writer"), no People also ask box,
  and Google AI Mode naming Frase, Surfer SEO, KoalaWriter and Writesonic (not us), citing pilotscribe.com, Okara,
  theStacc and two subreddits, and asking 3 follow-ups (your platform, your budget and volume, hands-off or hands-on).
- **Output:** an 87-row CSV, every row with its source and every volume "no data"; a topical map of 3 pillar pages and 23
  spokes; 5 page briefs. Top 5: AI blog writer for WordPress · Koala AI alternatives · AI blog writer with your own API
  key · AI blog writer pricing · how to get your blog cited by ChatGPT.
- **Real numbers for the seed:** DataForSEO the day before (US): 61 ideas, "ai blog writer" 260 searches a month,
  difficulty 27, $0.0144.

## The honest notes

- **AI answers change** by person, place and day. Treat them as a sample and log the date.
- **Not every Google box shows on every search.** On our seed, Google showed autocomplete, an AI Overview / AI Mode answer
  and "People also search for", but no People also ask box. Log what you see.
- **The difficulty proxy is a judgment, not a metric.** Say so when you share it.
- **No search volume without a source.** If a chat hands you volumes and no tool ran, they're made up.
- **Don't automate Google.** A handful of manual searches is fine; if you get a CAPTCHA, stop.

## Then write the pages

Write each brief with the free **ranking-principles** skill (answer first, add what the top results don't have, show
first-hand proof, cite sources), yourself, with any writer, or with **WordRocket** (our own tool, Claude connector
`https://wordrocketapi.com`). Re-run the fan-out every 2–3 months.

---

18 free SEO skills: [github.com/WordRocket/claude-seo-skills](https://github.com/WordRocket/claude-seo-skills) ·
Sources: [Google I/O 2025 AI Mode post](https://blog.google/products/search/google-search-ai-mode-update/) ·
[AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) ·
[How autocomplete works](https://support.google.com/websearch/answer/7368877) ·
[Creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) ·
[Use Keyword Planner](https://support.google.com/google-ads/answer/7337243) ·
[SEJ on Keyword Planner's limited data view (2016)](https://www.searchenginejournal.com/googles-keyword-planner-tool-providing-limited-data-low-spending-advertisers/170837/) ·
[DataForSEO pricing](https://dataforseo.com/pricing). Made by WordRocket (wordrocket.ai), our own tool. Not affiliated
with Google, OpenAI or DataForSEO. Results vary.
