# The 10-minute AI ranking setup

Three steps to help Google's AI answers and ChatGPT find you, show you and pick you. Each takes a few minutes.
Nothing here guarantees a ranking: AI answers change by person and by day. These are the switches most sites have
never flipped. (Checked November 7, 2026; links go to the official docs.)

## Step 1: Let the AI search crawlers in (3 minutes)

AI search can only show what its crawler is allowed to read. OpenAI says it plainly:

> "Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers."
> ([OpenAI: crawlers](https://developers.openai.com/api/docs/bots))

**Check yours:** open `yourdomain.com/robots.txt`. A `Disallow: /` under any of these hides you from that AI search:

```text
User-agent: OAI-SearchBot
User-agent: PerplexityBot
User-agent: Claude-SearchBot
User-agent: Googlebot
User-agent: Bingbot
Allow: /
```

What each name controls:
- `OAI-SearchBot` = ChatGPT search. `GPTBot` = OpenAI model training: allowing or blocking it is your call and is
  separate from search.
- `PerplexityBot` = Perplexity's answers. `Claude-SearchBot` = Claude's search; `ClaudeBot` is training only.
- `Google-Extended` only controls Gemini training and grounding. Blocking it does **not** remove you from Google Search
  or AI Overviews, which use Googlebot.
- `Bingbot` feeds Bing, and Microsoft Copilot grounds its answers with Bing searches.

**On Cloudflare?** Open AI Crawl Control and keep **Search** on Allow. Don't want AI training? Pick "Disallow AI
Training", never "Block": Block also stops Googlebot, Bingbot and Applebot.
([Cloudflare, Sep 15, 2026](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers)) Changes can take about a
day to be picked up.

## Step 2: Own the exact question (4 minutes)

Broad questions are crowded. Specific ones are winnable.

Our own test (ChatGPT, November 4, 2026):
- **Broad:** "best AI tool that writes SEO blog posts and publishes them to WordPress automatically" → WordRocket #2.
- **Specific:** "best AI blog writer where I can use my own OpenRouter API key and auto publish SEO articles to
  WordPress" → WordRocket **#1**.

Do this:
1. Write down the exact sentence your best customer would type, with the detail that makes you different (the city,
   the feature, the price point, the "with my own API key").
2. Ask ChatGPT, Perplexity and Google AI Mode that sentence. Note who shows up and **why** the answer says they're
   good.
3. Make sure one page on your site answers that exact question in its first two sentences, in plain words, with the
   facts the AI quoted about your competitors (features, prices, who it's for).
4. Ask again in a week. Keep a log: date, question, tool, your position (the free SEO tracker has a sheet for it).

## Step 3: Google's Preferred Sources button (3 minutes)

**What it does.** Readers can tap a button on your site to add you as a *preferred source* in Google. Since May 27,
2026, those readers see your links labeled **"Preferred"** when you appear in AI Mode and AI Overviews, and your
content is more likely to appear in their Top Stories. Google says people are twice as likely to click through to a
Preferred Source. ([Google blog](https://blog.google/products-and-platforms/products/search/original-high-quality-content-search/) ·
[Search Central doc](https://developers.google.com/search/docs/appearance/preferred-sources))

**Who qualifies.** Sites that publish fresh content, at domain level (example.com) or subdomain level
(blog.example.com). A folder such as example.com/blog doesn't. For the AI label, Search Console › Settings › Search
generative AI must be set to Include (the default).

**Add it.** Two lines of code. First, in the `<head>` of your pages:

```html
<script async src="https://news.google.com/swg/js/v1/publisher.js"></script>
```

Then where you want the button (footer, sidebar, end of each post):

```html
<div google-add-preferred-source-btn></div>
```

**No code access?** Use a plain link in a newsletter, your bio or a button image:
`https://www.google.com/preferences/source?q=yourdomain.com`

**WordPress:** paste the first line with a header/footer plugin (e.g. WPCode › Header & Footer), and the second in a
Custom HTML block in your footer widget.

**Then ask for it.** The button only helps when people tap it: mention it in your newsletter, at the end of posts and
to your regular readers and customers.

## What you don't need

- **An llms.txt file for Google.** Google says it won't help or hurt you in Google Search.
- **Special "AI schema" or a second AI version of your pages.** Google: "There are no additional requirements to
  appear in AI Overviews or AI Mode." ([AI features and your website](https://developers.google.com/search/docs/appearance/ai-features))

---

More checks: the free **AI search visibility checklist** (20 checks with sources). Free skills **generative-ai-search**
(your AI Overview / AI Mode data from Search Console + the articles to write next) and **borrowed-authority** (the
questions where Reddit, LinkedIn and YouTube already rank or get cited): [github.com/WordRocket/claude-seo-skills](https://github.com/WordRocket/claude-seo-skills) ·
Made by WordRocket, our own tool. Results vary.
