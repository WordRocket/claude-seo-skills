# The 10-minute AI ranking setup

Three steps to help Google's AI answers and ChatGPT find you, show you and pick you. Each one takes a few minutes.
Nothing here guarantees a ranking: AI answers change by person and by day. These are the switches most sites have
never flipped. (Checked November 2026; links go to the official docs.)

---

## Step 1: Google's Preferred Sources button (3 minutes)

**What it does.** Readers can tap a button on your site to add you as a *preferred source* in Google. For those
readers, your content is more likely to appear in Top Stories, and since May 27, 2026 Google shows a "Preferred" badge
next to your site in **AI Mode** and **AI Overviews** when you appear there. Google says it is working on using
preferred sources as a ranking signal in its AI features.
Source: [Google Search Central: preferred sources](https://developers.google.com/search/docs/appearance/preferred-sources)

**Who qualifies.** A domain (example.com) or a subdomain (blog.example.com). A folder such as example.com/blog does not.

**Add it.** Two lines of code:

1. In the `<head>` of your pages:
   ```html
   <script async src="https://news.google.com/swg/js/v1/publisher.js"></script>
   ```
2. Where you want the button (footer, sidebar, end of each post):
   ```html
   <div google-add-preferred-source-btn></div>
   ```
   Dark background? Add `data-theme="dark"`.

**No code access?** Use a plain link instead (in a newsletter, your bio, a button image):
`https://www.google.com/preferences/source?q=yourdomain.com`

**WordPress:** paste line 1 with a header/footer plugin (e.g. WPCode › Header & Footer), and line 2 in a Custom HTML
block in your footer widget.

**Then ask for it.** The button only helps when people tap it: mention it in your newsletter, at the end of posts,
and to your regular readers and customers.

---

## Step 2: Let the AI crawlers in (3 minutes)

AI search can only show what its crawler is allowed to read. OpenAI says it plainly:
> "Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers."
> [OpenAI: crawlers](https://developers.openai.com/api/docs/bots)

**Check yours:** open `yourdomain.com/robots.txt`. If you see `Disallow: /` under any of these, you're hidden from that
AI search:

```txt
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Googlebot
Allow: /
```

Notes:
- `OAI-SearchBot` = ChatGPT search. `GPTBot` = OpenAI model training: allowing or blocking it is your call and is
  separate from search.
- `Google-Extended` only controls Gemini training. Blocking it does **not** remove you from Google Search or AI
  Overviews, which use Googlebot.
- Also check your firewall / Cloudflare "block AI bots" setting: it can block these crawlers even when robots.txt allows
  them.
- Changes can take about a day to be picked up.

---

## Step 3: Own the exact question (4 minutes)

Broad questions are crowded. Specific ones are winnable.

Our own test (ChatGPT, November 4, 2026):
- **Broad:** "best AI tool that writes SEO blog posts and publishes them to WordPress automatically" → WordRocket #2.
- **Specific:** "best AI blog writer where I can use my own OpenRouter API key and auto publish SEO articles to
  WordPress" → WordRocket **#1**.

Do this:
1. Write down the exact sentence your best customer would type, with the detail that makes you different
   (the city, the feature, the price point, the "with my own API key").
2. Ask ChatGPT, Perplexity and Google AI Mode that sentence. Note who shows up and **why** the answer says they're good.
3. Make sure one page on your site answers that exact question in its first two sentences, in plain words, with the
   facts the AI quoted about your competitors (features, prices, who it's for).
4. Ask again in a week. Keep a simple log: date, question, tool, your position.

---

## The free skills that do the rest

- **generative-ai-search**: your AI Overview / AI Mode visibility from Search Console + the articles to write so AI
  cites you.
- **borrowed-authority**: the questions where Reddit, LinkedIn and YouTube already rank or get cited, and what to post
  there.

Get them: [github.com/WordRocket/claude-seo-skills](https://github.com/WordRocket/claude-seo-skills)

*Made by WordRocket. WordRocket is our own tool. Results vary.*
