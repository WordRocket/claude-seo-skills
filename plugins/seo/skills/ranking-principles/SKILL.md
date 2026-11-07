---
name: ranking-principles
description: |
  Teaches Claude HOW Google and AI answers judge content, instead of SEO checklists ("keyword in the H1, 2,000 words,
  add an FAQ"). 12 principles from Google's own guidance (people-first content page, Oct 2026; rater guidelines, Sept
  2025) and the research on what ChatGPT and AI Overviews cite. Use it to write a page, brief a writer, or audit an
  existing page: "use ranking principles to write a page about X", "audit this page with ranking principles", "why
  isn't this page ranking?", "make this post better than the top results", "write content AI will cite".
---

# Ranking principles

AI writes bad SEO content for one reason: it copies the steps from SEO guides (keyword in the title, 2,000 words, an
FAQ at the end) and misses the thinking behind them. Google itself says it has no preferred word count. This skill
gives Claude the thinking instead: who the page is for, what it adds, and why someone would trust it and quote it.

Read `references/principles.md` (the 12 principles, each with its source and how to apply it) before you write or
audit. `references/myths.md` lists the checklist habits Google says don't help, with sources and quotable numbers.

---

## Mode 1: Write a page (or a brief)

1. **Reader card (ask once, then write it down):** who is searching, the words they'd type, what they want done
   (know / do / buy / visit), and what they'll do after reading. One reader, one problem.
2. **Look at what already ranks:** read the top 5 results for the main search (web search or the browser) and the
   follow-up questions people ask around it. List what they ALL say. That's the commodity part.
3. **Find the information gain:** write down at least one thing none of them have: the user's own numbers, a test, a
   real example, a local detail, a cost breakdown, a mistake and its fix. If the user has nothing first-hand, ask for
   it. Never invent experience, data or quotes.
4. **Write with the 12 principles:** answer in the first 2–3 sentences; be specific (numbers, names, places, dates,
   each with a source or the user's method); cite primary sources where the claim is made; start each section with a
   plain sentence that makes sense quoted alone; show who wrote it and how; cut every paragraph any page could contain.
5. **Hand over:** the page (or the brief), then a short table: principle → what the page does for it → what's still
   missing (usually first-hand proof only the user can add).

## Mode 2: Audit a page

1. Read the page (URL or pasted text) and the top 5 results for its main search.
2. Score each of the 12 principles 0–2 (0 missing, 1 partly, 2 done) with one line of evidence quoted from the page.
3. Flag checklist habits from `references/myths.md` (word-count padding, keyword repetition, FAQ added only for rich
   results, fake freshness, summaries of the top results with nothing added).
4. Give the 5 fixes that matter most, in order, each written as a concrete edit ("Move the price range from paragraph
   6 to the first two lines", "Add the photos from your last 3 jobs with the dates"). Total score /24.

## Mode 3: Teach a writer or another skill

Turn the principles into a one-page brief for this topic: reader card, the commodity list, the information gain to
add, the answer-first opening, the sources to cite, the proof to collect. Works as the input for a writer, for
WordRocket, or for the serp-to-published-article skill.

---

## Rules (say what's true, nothing more)
- Never claim a principle is a "ranking factor". Google says E-E-A-T, word count, heading count and keyword placement
  aren't; signals that reflect quality are what matter.
- Never say Google uses an "information gain score". Say: Google patented one (2022, not confirmed in use) and its own
  docs ask for content "beyond the obvious".
- AI citation studies are correlational, except the GEO paper (KDD 2024), which used a 2023 lab setup. Never promise
  that a tactic makes ChatGPT or AI Overviews cite a page.
- For AI Overviews and AI Mode, Google says there are no extra requirements: no special files (llms.txt), no special
  schema, no second "AI version" of a page.
- Never invent a number, quote, author, credential, test or customer story. Missing proof is a fix for the user to
  make, not a gap for you to fill.
- Results vary. Nobody honest can promise rankings.

Sources: Google Search Central, "Creating helpful, reliable, people-first content" (updated Oct 5, 2026); Search Quality
Rater Guidelines (Sept 11, 2025); SEO Starter Guide; Aggarwal et al., "GEO: Generative Engine Optimization", KDD 2024;
Ahrefs AI Overview citation study (Mar 2026); Indig/Gauge in Search Engine Journal (Feb 2026). Full list with links in
`references/principles.md` and `references/myths.md`. Made by WordRocket (wordrocket.ai).
