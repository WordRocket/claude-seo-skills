# SEO suite for Claude Code (free) + 15 SEO skills

Turn Claude Code into your SEO team. One command audits your whole site with **6 specialist agents in parallel**,
gives you a **health score and the 5 fixes that matter most** (with proof for each), and then **writes the fixes**.
Every recommendation is checked against **Google's own documentation**, so it won't tell you to add llms.txt to rank
in Google or to write 2,000 words. No API keys, no Python, no browser setup.

Free, open source (MIT). Made by [WordRocket](https://wordrocket.ai).

## Install (Claude Code, one minute)
```bash
claude plugin marketplace add WordRocket/claude-seo-skills
claude plugin install seo@claude-seo-skills
```
Or inside Claude Code: `/plugin marketplace add WordRocket/claude-seo-skills`, then `/plugin install seo@claude-seo-skills`.

## The commands
| command | what it does |
|---|---|
| `/seo:audit <url>` | 6 agents at once (technical · content · AI search · schema · local · authority) → health score /100, the 5 fixes that matter most, a one-file HTML report, and a **myth check** (what it deliberately didn't recommend, with Google's words) |
| `/seo:fix` | writes the fixes from the last audit into `seo-fixes/`: robots.txt for AI search crawlers, JSON-LD schema, titles + metas, answer-first intros, redirects, sitemap, the pages you're missing. Never touches your live site |
| `/seo:ai <url>` | can ChatGPT search, Perplexity, Claude, Copilot and Google's AI features **reach and read** you? Tests real crawler access, firewall blocks and pages that are empty without JavaScript (common on Lovable, Bolt and v0 sites) |
| `/seo:page2` | from your Search Console export: the pages Google almost ranks and the 3 edits that move each one up |
| `/seo:write <keyword>` | top-5 teardown → brief → a page in your voice that adds what they don't have |
| `/seo:local <business>` | Google Business Profile checklist + the service and town pages to build |
| `/seo:links <domain>` | unlinked mentions, resource pages, best-of lists, Reddit/YouTube answers + outreach drafts (white-hat only) |
| `/seo:check <report>` | paste any SEO report or advice: ✅ backed by Google · ⚠️ partly · ❌ myth · ❓ undocumented, with links |
| `/seo:help` | the menu |

In Claude.ai / Claude Desktop, upload `dist/seo-suite.zip` and say "seo audit yoursite.com": same checks, one after another.

## Skills (also work on their own, in Claude.ai or Claude Code)

| skill | ask Claude something like | you get |
|---|---|---|
| **seo-suite** ✨ new | "seo audit *[my site]*" · "seo fix" · "is my site ready for AI search?" | the engine behind the /seo commands: 6 checks, health score, top 5 fixes, the fix files, myth check |
| **ranking-principles** ✨ new | "Use ranking principles to write a page about *[topic]*" · "Audit this page with ranking principles" | Claude stops copying SEO checklists and thinks like Google's own guidance: 12 principles (answer first, add what the top results don't have, first-hand proof, cite sources…) to write, brief or audit any page, with sources |
| **ai-humanizer** ✨ new | "Learn my voice from these 3 emails" · "Humanize this" | your voice profile, drafts rewritten without the 2026 AI tells ("this matters", "rather than simply", reflex lists of three…), and a paste-ready prompt for ChatGPT custom instructions or Claude Instructions |
| **backlink-maxing** | "Run the SEO backlink maxing playbook for *[my site]*" | the whole white-hat link job in one prompt: unlinked mentions → links, guest posts + resource pages + listicles, cited on Reddit/LinkedIn/YouTube, link-worthy articles (with WordRocket), every outreach draft |
| **chatgpt-maxing** | "Run the ChatGPT maxing playbook for *[my business]*" | get recommended by ChatGPT, Perplexity and Google's AI answers in one prompt: AI crawler check (OAI-SearchBot), the questions buyers ask + who gets named instead, answer-first pages (with WordRocket), mentions on the sites AI cites (Reddit, YouTube, Yelp, best-of lists), a monthly prompt tracker |
| **ultimate-seo** | "Do SEO for my plumbing business in Austin" | 14 workflows: Google Business Profile audit, reviews, keyword gaps, money pages, on-page, technical, schema, page speed |
| **seo-audit** | "Audit example.com and its competitors" | a full HTML audit: competitors, keywords, on-page + technical issues, 30/60/90-day plan |
| **local-seo-programmatic** | "I want to rank in every town around Dallas" | a scored local audit + the city pages to build, with a brief for each one |
| **generative-ai-search** | "Why am I not in Google's AI Overviews?" | your AI Overview / AI Mode visibility from Search Console + the fan-out articles to write so AI cites you |
| **backlink-opportunities** | "Find backlinks my competitors have" | guest posts, resource pages, directories, link insertions, scored and ready to pitch |
| **brand-mention-backlinks** | "Who mentions my brand without linking?" | every unlinked mention, the contact, and an outreach email for each |
| **core-update-recovery** | "My traffic dropped after the Google update" | the drop matched to Google's update dates + a recovery plan |
| **visual-search-opportunities** | "I get image impressions but no clicks" | the image + video searches you can win, with briefs |
| **borrowed-authority** | "Get me on page 1 this week without touching my website" | the searches where Reddit, LinkedIn and YouTube already rank or get cited by AI, the platform-native posts to put there, and a 30-day rank + AI-citation tracker |
| **youtube-thumbnails** | "Design the thumbnail for my video: *[title]*" | Claude studies the top thumbnails in your niche in Chrome, writes the research, turns your title into prompts and makes the thumbnail with GPT Image 2 via kie.ai (your key) |
| **serp-to-published-article** | "Write and publish an article for *best crm for roofers*" | top-5 SERP teardown → brief → article written and published to WordPress (needs WordRocket) |

## Free playbooks
[**The AI humanizer prompt**](playbooks/ai-humanizer-prompt.md) ✨ new: copy-paste it into ChatGPT (Settings › Personalization › Custom instructions) or Claude (Settings › Your Claude › Instructions). Full version + a short one for ChatGPT Free, every rule sourced.

[**The 10-minute AI ranking setup**](playbooks/rank-in-ai-10-minutes.md) ([PDF](playbooks/rank-in-ai-10-minutes.pdf)): letting the AI search crawlers in, owning the exact question your buyer asks, and Google's Preferred Sources button (the two lines of code).

[**The AI search visibility checklist**](playbooks/ai-search-visibility-checklist.md) ([PDF](playbooks/ai-search-visibility-checklist.pdf)) ✨ new: 20 checks for ChatGPT, Perplexity, Claude, Copilot and Google's AI Overviews / AI Mode, each with the official source.

[**Page-2 quick wins**](playbooks/page-2-quick-wins.md) ([PDF](playbooks/page-2-quick-wins.pdf)) ✨ new: find the pages Google almost ranks in Search Console, the fixes that move them up, and a Claude prompt for your export.

[**Ranking principles cheat sheet**](playbooks/ranking-principles-cheat-sheet.md) ([PDF](playbooks/ranking-principles-cheat-sheet.pdf)) ✨ new: the 12 principles Google and AI answers judge pages by, on one page, plus the habits Google says don't help.

[**The 30-day SEO plan**](playbooks/30-day-seo-plan.md) ([PDF](playbooks/30-day-seo-plan.pdf)) ✨ new: one task a day for a month, from page-2 fixes to AI answers to links, and what to measure.

[**The SEO tracker**](playbooks/seo-tracker.xlsx) (Excel / Google Sheets) ✨ new: page-2 shortlist with automatic check dates, an AI answers log and the 30-day plan.

[**50 backlink tactics, ranked S tier to C tier**](playbooks/50-backlink-tactics.md) ([PDF](playbooks/50-backlink-tactics.pdf)): what to run first, with the Claude prompt for each.

## Install

### Claude Code (one minute)
```bash
claude plugin marketplace add WordRocket/claude-seo-skills
claude plugin install seo@claude-seo-skills
```
Then just ask, or call one directly: `/seo:seo-audit`, `/seo:local-seo-programmatic`, …

### Claude.ai / Claude Desktop
1. Download the skills you want from [`dist/`](dist/) (one zip per skill).
2. In Claude: **Customize › Skills › + Create skill › Upload a skill** and pick the zip. (Older layouts: Settings › Capabilities › Skills.)
3. Make sure **Code execution and file creation** is on (Settings › Capabilities). The reports are built as files.

### Works best with
- **Claude in Chrome**, so Claude can read pages that need a browser (Google Business Profiles, Search Console, free backlink checkers).
- **Python 3** with `matplotlib` and `numpy` for the charts in the audit and recovery reports (`pip install matplotlib numpy`).

## Want the fixes written for you?
Every skill ends with a plan: pages to build, articles to write. Connect **WordRocket** and Claude can write those
articles with research, images and FAQs, and publish them straight to your WordPress site.

Claude › Settings › Connectors › **Add custom connector** › `https://wordrocketapi.com`, then sign in to
[WordRocket](https://wordrocket.ai). The skills work without it; you just get the plan instead of the published pages.

## Notes
- Every skill is told to use real data and never invent numbers. Still check anything you publish.
- Not affiliated with Anthropic or Google.
- MIT licensed: use them for your own sites and your clients.
