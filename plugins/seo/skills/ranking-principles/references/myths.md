# Checklist habits Google says don't help (or backfire)

| Habit | What Google says | Source |
|---|---|---|
| Writing to a word count ("2,000 words") | "(No, we don't.)" have a preferred word count. "There's no magical word count target, minimum or maximum." Reviews: focus on "quality and originality … not the length." | people-first page; SEO Starter Guide; reviews guidance |
| Keyword density / repeating the keyword | "Excessively repeating the same words … is tiring for users, and keyword stuffing is against Google's spam policies." (GEO paper: keyword stuffing scored below baseline, 10% worse on Perplexity.) | Starter Guide; spam policies; GEO paper |
| Meta keywords tag | "Google Search doesn't use the keywords meta tag." | Starter Guide |
| Keywords in the domain or URL | "hardly any effect beyond appearing in breadcrumbs." | Starter Guide |
| Counting headings / perfect H1-H2 order | Order "doesn't matter" to Search; "no magical, ideal amount of headings." | Starter Guide |
| "E-E-A-T is a ranking factor" | "Thinking E-E-A-T is a ranking factor: No, it's not." (Signals that reflect it are used.) | Starter Guide; people-first page |
| Adding an FAQ section for the rich result | Since Aug 2023 FAQ rich results "will only be shown for well-known, authoritative government and health websites." Unused markup "has no visible effects." | https://developers.google.com/search/blog/2023/08/howto-faq-changes |
| HowTo markup | How-to rich results deprecated (Sept 13, 2023). | same post |
| Faking freshness (new date, no real change) | A listed warning sign; mass add/remove to look fresh: "(No, it won't)". | people-first page |
| Mass AI or programmatic pages | Scaled content abuse; 45% less low-quality, unoriginal content after March 2024. | spam policies; Google Keyword blog 2024 |
| Rewriting / summarizing the top results | "Mainly summarizing what others have to say without adding much value" is a warning sign; Lowest when almost all MC is paraphrased with no added value. | people-first page; QRG 4.6.6 |
| Fake author personas, AI headshots, made-up credentials | "A form of deception"; rated Lowest. | people-first page; QRG 4.5.3 |
| AI as the byline | "Probably not the best way" to disclose AI help. | Feb 2023 FAQ |
| llms.txt / special AI files / special schema for AI Overviews | "You don't need to create new machine readable files, AI text files, or markup"; no special schema. | AI features doc |
| Chunking pages into bite-sized pieces for LLMs, or a 2nd version for AI | "we don't want you to do that" (Danny Sullivan, Jan 2026). | Search Off the Record, via SER |
| Chasing trends or a niche you know nothing about for traffic | Both are listed warning signs. | people-first page |
| Publishing third-party content on a strong host to borrow its rankings | Site reputation abuse, "regardless of whether there is first-party involvement." | Nov 2024 post |
| Fearing a "duplicate content penalty" for your own URL variants | "It's not something that will cause a manual action. Copying others' content, however, is a different story." | Starter Guide |
| Quick fixes after a core update (removing an element "bad for SEO") | "Avoid doing 'quick fix' changes." | core updates page |
| Persuasive "authoritative" tone as a GEO trick | No significant improvement (third-party lab data, not Google). | GEO paper |

---

## Numbers you can quote

1. **45%** less low-quality, unoriginal content in Google results after the March 2024 core update + spam policies (Google said it expected 40%). Google, Apr 26, 2024 update to https://blog.google/products/search/google-search-update-march-2024/
2. **+30–40%** visibility in generative-engine answers from adding cited sources, quotations and statistics; keyword stuffing scored **below** baseline (10% worse on Perplexity); Cite Sources lifted the 5th-ranked page **+115.1%**. Aggarwal et al., GEO, KDD 2024, https://arxiv.org/abs/2311.09735
3. Only **38%** of AI Overview citations rank in Google's top 10 for the same query (863K keywords, 4M cited URLs; ~76% in July 2025 with an older method). Ahrefs, Mar 2, 2026, https://ahrefs.com/blog/ai-overview-citations-top-10/
4. **44.2%** of ChatGPT citations come from the first 30% of a page; cited text uses definitive language 36.2% vs 20.2%. Kevin Indig / Gauge, SEJ, Feb 17, 2026, https://www.searchenginejournal.com/the-science-of-how-ai-pays-attention/567597/ (correlational, ChatGPT only)
5. Searchers clicked a traditional result in **8%** of visits with an AI summary vs **15%** without, and a link inside the summary in **1%**; 53% of 10+ word searches got a summary. Pew Research Center, Jul 22, 2025, https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/

Runner-up: branded web mentions correlate **0.664** with AI Overview visibility vs **0.218** for backlinks (Ahrefs, 75K brands, May 26, 2025).

---
