# 9 free SEO skills for Claude

Turn Claude into your SEO team. Each skill does the actual work with real data from the web (search results, your
Search Console, Google Maps, free backlink tools) and gives you a client-ready report you can act on today.

Free, open source (MIT). Made by [WordRocket](https://wordrocket.ai).

| skill | ask Claude something like | you get |
|---|---|---|
| **ultimate-seo** | "Do SEO for my plumbing business in Austin" | 14 workflows: Google Business Profile audit, reviews, keyword gaps, money pages, on-page, technical, schema, page speed |
| **seo-audit** | "Audit example.com and its competitors" | a full HTML audit: competitors, keywords, on-page + technical issues, 30/60/90-day plan |
| **local-seo-programmatic** | "I want to rank in every town around Dallas" | a scored local audit + the city pages to build, with a brief for each one |
| **generative-ai-search** | "Why am I not in Google's AI Overviews?" | your AI Overview / AI Mode visibility from Search Console + the fan-out articles to write so AI cites you |
| **backlink-opportunities** | "Find backlinks my competitors have" | guest posts, resource pages, directories, link insertions, scored and ready to pitch |
| **brand-mention-backlinks** | "Who mentions my brand without linking?" | every unlinked mention, the contact, and an outreach email for each |
| **core-update-recovery** | "My traffic dropped after the Google update" | the drop matched to Google's update dates + a recovery plan |
| **visual-search-opportunities** | "I get image impressions but no clicks" | the image + video searches you can win, with briefs |
| **serp-to-published-article** | "Write and publish an article for *best crm for roofers*" | top-5 SERP teardown → brief → article written and published to WordPress (needs WordRocket) |

## Install

### Claude Code (one minute)
```bash
claude plugin marketplace add WordRocket/claude-seo-skills
claude plugin install seo@claude-seo-skills
```
Then just ask, or call one directly: `/seo:seo-audit`, `/seo:local-seo-programmatic`, …

### Claude.ai / Claude Desktop
1. Download the skills you want from [`dist/`](dist/) (one zip per skill).
2. In Claude: **Customize › Skills › + › Upload a skill** and pick the zip. (Older layouts: Settings › Capabilities › Skills.)
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
