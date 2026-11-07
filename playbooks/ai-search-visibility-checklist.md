# The AI search visibility checklist

20 checks so ChatGPT, Perplexity, Claude, Copilot and Google's AI Overviews and AI Mode can find your pages, show them
and quote them. Every line links to the official doc or the study behind it. Checked November 7, 2026. Nothing here
guarantees a mention: AI answers change by person and by day. These are the switches most sites never check.

## Google AI Overviews and AI Mode

1. **Key pages indexed and allowed a snippet.** That's Google's only requirement: "There are no additional
   requirements to appear in AI Overviews or AI Mode." Check with URL Inspection.
   ([AI features](https://developers.google.com/search/docs/appearance/ai-features))
2. **Search Console › Settings › Search generative AI says "Include"** (the default).
   ([help](https://support.google.com/webmasters/answer/16908024))
3. **Open the Generative AI performance report** in Search Console to see how often AI Overviews and AI Mode showed
   your links (live for all sites since Aug 31, 2026). ([help](https://support.google.com/webmasters/answer/16984139))
4. **No nosnippet or tiny max-snippet** on pages you want quoted: they limit AI features too.
   ([robots meta tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag))
5. **Know what Google-Extended does:** blocking it only stops Gemini training and grounding. It doesn't remove you
   from Google Search or AI Overviews. ([Google crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers))
6. **Skip llms.txt for Google.** Google says it won't help or hurt you there. Make one only if another tool asks.
   ([AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide#mythbusting))
7. **Add the "Add as preferred source" button** (domain or subdomain sites that publish fresh content). Readers who
   tap it see your links labeled "Preferred" in AI Mode and AI Overviews; Google says people are twice as likely to
   click a Preferred Source. ([preferred sources](https://developers.google.com/search/docs/appearance/preferred-sources))

## ChatGPT, Perplexity and Claude

8. **Allow OAI-SearchBot** in robots.txt. OpenAI: sites opted out "will not be shown in ChatGPT search answers".
   Changes take about a day. ([OpenAI crawlers](https://developers.openai.com/api/docs/bots))
9. **Decide on GPTBot separately.** Blocking it only opts you out of OpenAI model training, not ChatGPT search.
10. **Allow PerplexityBot:** it's what surfaces and links sites in Perplexity answers.
    ([Perplexity crawlers](https://docs.perplexity.ai/guides/bots))
11. **Allow Claude-SearchBot and Claude-User.** ClaudeBot is training only.
    ([Anthropic crawlers](https://support.claude.com/en/articles/8896518))

## Microsoft Copilot and Bing

12. **Verify the site in Bing Webmaster Tools** and open its AI Performance report. Copilot grounds its answers with
    Bing searches. ([Bing blog, Feb 2026](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview))
13. **Turn on IndexNow** so Bing and other engines hear about new or updated pages right away (Google isn't part of
    it). ([indexnow.org](https://www.indexnow.org/faq))
14. **Local business? Claim Bing Places for Business** as well as your Google Business Profile. ([Bing](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview))

## Your host and firewall

15. **Check Cloudflare (or your host's bot settings).** In AI Crawl Control, keep **Search** on Allow. Don't want AI
    training? Pick "Disallow AI Training", never "Block": Block also stops Googlebot, Bingbot and Applebot.
    ([Cloudflare, Sep 15, 2026](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers))

## The page itself

16. **Key facts in plain text:** services, prices, hours, areas. Not only inside images or video.
17. **Answer first, then the follow-up questions.** Only about 38% of AI Overview citations also rank in Google's top 10
    for the same search, because AI pulls from related searches too. ([Ahrefs, Mar 2026](https://ahrefs.com/blog/ai-overview-citations-top-10/))
18. **Add sources, short real quotes and real numbers.** In the GEO study (KDD 2024) they lifted visibility in AI answers
    by up to 40%; keyword stuffing didn't help. ([arxiv.org/abs/2311.09735](https://arxiv.org/abs/2311.09735))
19. **Normal structured data that matches the visible text.** No special "AI schema" is needed.
    ([AI features](https://developers.google.com/search/docs/appearance/ai-features))
20. **Get mentioned off your site** (YouTube, Reddit, lists in your niche). In Ahrefs' study of 75,000 brands,
    mentions tracked AI visibility far more closely than backlinks (correlation, not proof).
    ([Ahrefs](https://ahrefs.com/blog/ai-brand-visibility-correlations/))

## Copy-paste robots.txt (allow AI search, your call on training)

Check what's in your file first: a `Disallow: /` under any of these hides you from that search.

```text
User-agent: OAI-SearchBot
User-agent: PerplexityBot
User-agent: Claude-SearchBot
User-agent: Googlebot
User-agent: Bingbot
Allow: /
```

---

Free skills: **generative-ai-search** (your AI Overview and AI Mode data, and what to write next) and
**borrowed-authority** at [github.com/WordRocket/claude-seo-skills](https://github.com/WordRocket/claude-seo-skills) ·
Made by WordRocket (wordrocket.ai), our own tool. Results vary.
