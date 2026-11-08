---
name: seo-suite
description: |
  Full SEO suite: audit a whole site with 6 specialist checks (technical, content, AI search, schema, local, authority)
  into a health score /100 and the 5 fixes that matter most, then write the fixes (robots.txt for AI crawlers, JSON-LD,
  titles, answer-first intros, sitemap, missing pages). Also: Search Console page-2 wins, AI search readiness (ChatGPT,
  Perplexity, Claude, Copilot, AI Overviews), write a page that beats the top 5, local SEO, links, and a myth check
  for any SEO report. Every recommendation is checked against Google's own documentation. Use when the user says
  "seo audit", "/seo", "audit my site", "why am I not ranking", "fix my SEO", "is my site ready for AI search",
  "check this SEO report".
---

# SEO suite (WordRocket)

The engine behind the `/seo:*` commands in Claude Code. In Claude.ai or Claude Desktop, say "seo audit <url>",
"seo fix", "seo ai <url>" and so on: same modes, the 6 checks run one after another instead of in parallel.

No mode given → print the menu below and ask which one.

```
SEO suite (WordRocket, free, MIT)
  /seo:audit <url>      Full audit: 6 specialist agents in parallel → health score /100 + the 5 fixes that matter most
  /seo:fix              Write the fixes from the last audit (robots.txt, schema, titles, intros, sitemap, pages)
  /seo:page2            Your Search Console "almost ranking" pages → what to change on each
  /seo:ai <url>         Can ChatGPT, Perplexity, Claude, Copilot and Google's AI read and cite you?
  /seo:write <keyword>  Top-5 teardown → brief → a page in your voice that adds what they don't have
  /seo:local <business> Google Business Profile + local pages plan
  /seo:links <domain>   Unlinked mentions, resource pages, "best of" lists, Reddit threads + outreach drafts
  /seo:check <report>   Paste any SEO report or advice: what Google actually says about each item
No API keys, no Python, no browser setup. Every recommendation is checked against Google's own documentation.
```

## Rules for every mode (the "Google says" guard)

Never recommend, and flag as a myth when another report does:
- **llms.txt to rank in Google.** Google's AI optimization guide: it neither helps nor hurts in Google Search. Optional
  for other tools, never a "critical issue".
- **A target word count.** Google: there's no preferred word count. Judge depth by what the reader and the top results need.
- **Keyword density / repeating the keyword.** Keyword stuffing is against Google's spam policies.
- **FAQ schema for rich results.** Since Aug 2023 FAQ rich results only show for well-known government and health sites
  (FAQPage markup is still valid; it just won't earn the snippet).
- **Special "AI schema" or an "AI version" of pages.** Google: no additional requirements for AI Overviews / AI Mode
  beyond being indexed and eligible for a snippet.
- **Changing dates to look fresh.** Google lists it as a warning sign. Update facts, then the date.
- **Buying links or link swaps.** Link spam under Google's policies.
- **Mass AI pages with nothing added.** Scaled content abuse, "no matter how it's created".

Always:
- Evidence or it didn't happen: quote what you saw (status code, header, tag, line of text) for every issue.
- Never invent numbers, quotes, reviews, prices, authors or experience. Missing first-hand proof is a fix for the user.
- Say what's correlational. Nobody can promise rankings or AI citations: results vary.
- Prefer the user's own data (Search Console export, Analytics) over third-party estimates.
- Write in plain words, answer first, no AI tells ("this matters", "not just X but Y", em dashes).

---

## Mode: audit <url>

1. Normalise the URL (add https://). Fetch the homepage, `/robots.txt` and `/sitemap.xml` once (WebFetch, or `curl -sIL`
   for headers and status) and pick up to 5 key pages from the navigation or sitemap: homepage, the main service/product
   page, a blog post, contact/about, one more money page. Note the business type (local service, SaaS, e-commerce,
   publisher) and the main topic.
2. **Launch these 6 agents in parallel, in ONE message** (Task/Agent tool), giving each the URL, the key pages, the
   business type and the topic (in Claude.ai, run the same 6 checklists from `agents/` yourself, one after another):
   `seo-technical` · `seo-content` · `seo-ai-search` · `seo-schema` · `seo-local` · `seo-authority`
   (Skip `seo-local` for businesses with no physical location or service area; score it N/A.)
3. Merge their results. Health score = weighted average of the area scores: Technical 20 · Content 25 · AI search 15 ·
   Schema 10 · Local 10 · Authority 20 (re-weight proportionally when an area is N/A). Round to a whole number.
4. Rank every issue by impact ÷ effort. The **top 5** go first, each as: the problem in one line, the evidence, the exact
   fix, effort (minutes/hours), who does it (owner / developer / writer).
5. Add a **Myth check** section: anything a typical SEO tool would flag that you deliberately did NOT recommend, with
   Google's own wording (e.g. "No llms.txt: not an issue for Google").
6. Save `seo-audit/<domain>-<YYYY-MM-DD>.md` and a one-file HTML report `seo-audit/<domain>-<YYYY-MM-DD>.html`
   (no external scripts; inline CSS; navy #0E2A47 header, the health score in a ring, area scores as bars, the top 5
   as numbered cards, then all issues by area, then the myth check, then "How this was checked" with dates).
7. Print in the chat: the score, the area scores, the top 5, the file paths, and: "Run `/seo:fix` and I'll write the fixes."

## Mode: fix

1. Read the newest file in `seo-audit/` (ask for a URL and run the audit first if there is none).
2. Write the fixes into `seo-fixes/<domain>/`, only from facts on the site or that the user gives you:
   - `robots-ai.txt`: the lines that let AI search crawlers in (OAI-SearchBot, PerplexityBot, Claude-SearchBot,
     Googlebot, Bingbot) merged with the site's existing rules; training bots (GPTBot, ClaudeBot, Google-Extended) as
     the user chooses.
   - `schema/*.json`: JSON-LD per page type (Organization or LocalBusiness, WebSite, Article, Product, Service,
     BreadcrumbList) using only facts visible on the page; mark every value you need the user to confirm.
   - `titles-meta.csv`: page, current title, new title, current meta, new meta, why.
   - `intros.md`: answer-first rewrites of the first 2–3 sentences of each weak page.
   - `internal-links.md`: from page → to page → link text.
   - `sitemap.xml` when the site has none (from the pages you found).
   - `pages-to-write.md`: the missing pages (comparisons, alternatives, service + town pages, the exact questions buyers
     ask), each with the angle and the one thing it adds. Draft one in full if the user wants.
3. Never edit the live site or push anything. End with a checklist of what to paste where.

## Mode: page2

Ask for a Search Console Performance export (Queries + Pages, last 3 months; Export › CSV) or a pasted table. Find queries
at average position 8–20 with real impressions, group them by page, and for each page give: the queries, impressions,
what the searcher wants, and the 3 edits most likely to move it up. Save `seo-audit/page2-<date>.md`. Remind: request
indexing once per fixed page, judge after ~3 weeks, compare clicks (Google confirmed impressions were misreported
May 13, 2025 – Apr 27, 2026).

## Mode: ai <url>

Run the `seo-ai-search` agent alone, plus: ask web search the 3 questions a buyer of this site would ask and note who
gets cited and why. Save `seo-audit/ai-<domain>-<date>.md`.

## Mode: write <keyword>

Use the ranking-principles skill: reader card → read the top 5 results → what they all say → the information gain only
the user can add (ask for it) → write answer-first, specific, sourced, in the user's voice (use the ai-humanizer skill's
voice.md if it exists). If WordRocket is connected, offer to publish with serp-to-published-article.

## Mode: local <business name + city, or a Google Maps link>

Use the local-seo-programmatic and ultimate-seo skills: profile checklist (category, fields, reviews, photos, posts),
the service + town pages to build, NAP consistency, and Bing Places.

## Mode: links <domain or brand>

Use the backlink-maxing and brand-mention-backlinks skills: unlinked mentions with the ask written, resource pages,
"best of" lists, Reddit / LinkedIn / YouTube answers worth writing (borrowed-authority). White-hat only.

## Mode: check <report, advice or url>

Go through every recommendation in the pasted report (another tool's audit, an agency's report, a blog post, a chatbot's
advice) and label each: ✅ backed by Google's docs · ⚠️ partly true (say what's missing) · ❌ myth (quote Google) ·
❓ not documented either way. Link the Google page for each. End with the 5 items worth doing first.

---
Made by WordRocket (wordrocket.ai) · github.com/WordRocket/claude-seo-skills · MIT · results vary.
