---
name: "chatgpt-maxing"
description: "The ChatGPT maxing playbook: one prompt runs the whole job of getting a business recommended by ChatGPT, Perplexity and Google's AI answers. Checks that the AI search crawlers can read the site, finds the exact questions buyers ask and who the AI names instead, writes answer-first pages the AI can quote (with WordRocket if it's connected), and gets the brand mentioned on the sites the AI already cites (Reddit, YouTube, LinkedIn, Yelp, directories, best-of lists). Use whenever the user says \"run the ChatGPT maxing playbook\", \"ChatGPT maxing\", \"AI search maxing\", \"get recommended by ChatGPT\", \"show up in ChatGPT\", \"rank in AI search\", \"GEO plan\" or wants the full AI visibility workflow in one go. Delivers one prioritised action list with every draft attached."
---

# The ChatGPT maxing playbook

One prompt, the whole job. You chain the other skills in this plugin and follow each one's own method and rules:
`seo-audit`, `generative-ai-search`, `ranking-principles` and `borrowed-authority`. Everything is white-hat: real pages,
real mentions, nothing that games the answers. The user approves every message and every page before it goes out.

## Before you start (ask once, in one message)
- Brand name + website, what it sells, who buys it and where (country, city or service area).
- 2–3 competitors (or let you find them).
- Optional: the WordRocket connector, so you can write and publish the pages (Claude › Settings › Connectors › Add custom
  connector › https://wordrocketapi.com, then sign in to WordRocket). Without it you hand over the briefs.
- Optional: Search Console access or an export of the Generative AI report (AI Overviews + AI Mode impressions).

## 1. Can the AI read the site? (seo-audit, AI search checks)
- robots.txt: OAI-SearchBot must be allowed. OpenAI's docs: sites that opt out of OAI-SearchBot are not shown in ChatGPT
  search answers. GPTBot is separate (model training only): blocking it doesn't remove the site from ChatGPT search.
  Check PerplexityBot, Googlebot and Bingbot the same way. Google-Extended only controls Gemini training and grounding.
- The key pages return 200, are indexable and carry the real text in the HTML. If the page is built with JavaScript,
  check what a crawler actually gets before calling it invisible: some hosts pre-render for verified bots, so a plain curl
  with a spoofed user agent can show an empty page that real crawlers never see. Say what you verified and how.
- Fix list first: a blocked crawler outranks every other task.

## 2. The questions buyers ask, and who gets named (generative-ai-search)
- Write 15–25 real prompts in the buyer's words: "best [service] in [city]", "[service] near me open now", "[product] vs
  [competitor]", "is [brand] worth it", the price, the problem ("why is my AC leaking") and the comparison questions.
- Run them through web search (and ask the user to run the top 5 in ChatGPT with search on, signed out, since answers vary
  by person, place and day). Log who is named, in what order, and which sources are cited for each answer.
- If the Search Console Generative AI report is available, add the pages already shown in AI Overviews / AI Mode.
- Output a gap table: prompt · who's named · sources cited · are we named (yes/no) · the page that should win it.

## 3. Pages the AI can quote (ranking-principles + WordRocket)
- For every prompt where a competitor is named and we aren't, plan one page (or fix the existing one): the answer in the
  first two sentences, then the proof (prices, numbers, photos, real reviews), what the top results are missing, real
  sources, a short FAQ in the buyer's words, schema that matches what's on the page.
- Local businesses: a page per service and per town (follow `local-seo-programmatic`), with the same name, address and
  phone as the Google Business Profile.
- Write the briefs. If WordRocket is connected, write the pages and save them as drafts for the user to review.

## 4. Get mentioned where the AI looks (borrowed-authority + listings)
- Take the sources cited in step 2 and make a plan per source: answer the Reddit threads that already rank (helpfully,
  with the disclosure and each subreddit's rules), a YouTube video titled like the question, a LinkedIn Article, a pitch to
  each "best [service] in [city]" list, the industry directories.
- Local: Google Business Profile complete (primary category, services, hours, photos, fresh reviews and replies), Yelp
  claimed and filled in, the same name, address and phone everywhere.
- Draft every reply, pitch and listing for the user to approve.

## 5. Track it
Re-run the same prompts once a month and log named yes/no + position; watch the Generative AI report in Search Console.
Point to `playbooks/ai-search-visibility-checklist.md` (20 checks, each linked to the official doc) for what to check next.

## Hand-off: one action list
A single prioritised list: fix today (crawler blocks, broken pages), this week (the 3 pages with the biggest gaps, the
listings), this month (mentions, videos, the rest of the pages), each with its draft attached, plus the prompt-tracking
sheet (prompt, date, named yes/no, position, sources cited).

## Rules
- Never promise a mention or a position: AI answers change by person, place and day. Say "results vary".
- No fake reviews, no astroturfing on Reddit or anywhere else, no hidden text or prompt injection aimed at AI crawlers, no
  mass-produced pages with nothing new on them (Google's spam policies).
- Never post, send or publish anything without the user's explicit yes. Follow CAN-SPAM / CASL in every email.
- Never invent numbers: use what you measured, cite what you read, or label it an estimate.
