---
name: serp-to-published-article
description: >
  Full SERP-to-published-article pipeline using WordRocket and WordPress.
  Use this skill whenever the user gives you a keyword and wants to:
  rank for it, write an SEO article about it, outrank competitors, publish
  a blog post, create content for their WordPress site, run the content
  pipeline, or says things like "write and publish an article for [keyword]",
  "help me rank for [keyword]", "run the content pipeline for [keyword]",
  "SERP analysis for [keyword]", or "use WordRocket to write about [topic]".
  Trigger immediately when the user provides a keyword and any intent to
  create, write, or publish content around it.
---

# SERP-to-Published Article Skill

You are running a fully automated SEO content pipeline. When this skill is triggered, complete all steps below **without stopping to ask for confirmation between steps**. Run the full workflow from keyword to published post.

---

## Step 0 — Collect Configuration

If the user has not already provided the following, ask for them all at once in a single message before starting:

- **KEYWORD** — the exact search term to rank for
- **WORDPRESS SITE ID** — from WordRocket dashboard → Settings → Sites
- **CLIENT PROFILE ID** — from WordRocket → Client Profiles (optional; leave blank if none)
- **COUNTRY** — two-letter code (CA, US, GB, AU, etc.)
- **SITE URL** — their website (e.g. https://yoursite.com)
- **AUDIENCE** — who the article is for (1–2 sentences)
- **TONE** — professional / casual / friendly / formal
- **WORD COUNT** — target (recommend 3000–3500 for competitive keywords)
- **TAGS** — comma-separated list of tags for the WordPress post

Once you have all values, confirm them back in a single summary line and proceed immediately to Step 1.

---

## Step 1 — SERP Analysis

Search Google for the keyword. Identify the top 5 ranking URLs.

For each of the top 5 articles, fetch and read the full page. Extract:

- Full H1 title and its structural pattern
- All H2 and H3 headings (the complete outline)
- Primary keyword and secondary/LSI keywords visible in title, headings, and body
- Approximate word count and reading level
- Tone (technical, conversational, plain English, etc.)
- Data tables, statistics, comparison elements, or unique content assets
- GEO signals — city names, local regulatory bodies, regional data
- Any factual errors, outdated claims, or missing local angles

Present a structured summary of all 5 articles (a table works well) before moving to Step 2.

---

## Step 2 — Competitive Analysis

Synthesise across all 5 articles and produce:

**TITLE PATTERNS**
What structures do ranking titles use? (e.g. `[Keyword]: [Year] Guide`, `How to [Action]`, `[Number] Ways to...`) Which pattern is most common at the top?

**MUST-INCLUDE KEYWORDS**
Secondary and LSI keywords appearing in 3+ of the top 5. These are non-negotiable inclusions.

**TABLE-STAKES OUTLINE SECTIONS**
H2/H3 topics that appear in the majority of articles — every competing article covers these, so must you.

**CONTENT GAPS**
Topics, angles, data points, or perspectives that are missing or underrepresented across all 5. These are differentiation opportunities.

**COMPETITOR WEAKNESSES**
Outdated content, factual errors, thin sections, missing local angle, poor structure, or generic advice. Note specifically — you will exploit these.

**TONE BENCHMARK**
What reading level and writing style dominates this SERP?

---

## Step 3 — Build the Content Brief

Produce the following. This is what goes into WordRocket's `additional_instructions`.

```
WINNING TITLE: [one title using the best-performing pattern, incorporating keyword + year + value prop]

PRIMARY KEYWORD: [exact keyword]

SECONDARY KEYWORDS (8–12):
[list them]

OPTIMAL OUTLINE:
[full H2/H3 structure — minimum 8 H2s — covering table-stakes topics AND content gaps]

TONE & STYLE GUIDANCE:
[2–3 sentences: reading level, analogies, what to avoid, how to sound authoritative without being dry]

KEY FACTS & STATISTICS TO INCLUDE:
[cite any real data found in research — stats, regulatory figures, market data — with source name]

COMPETITOR WEAKNESSES TO EXPLOIT:
[specific errors or gaps found in Step 2 that this article should directly fix or fill]

WHAT NOT TO DO:
[specific claims to avoid, terms that don't apply to this market, outdated info to skip]

GEO OPTIMIZATION SIGNALS:
[city names, local regulators, regional terminology, local lenders/providers to name-drop naturally]
```

---

## Step 4 — Generate Article via WordRocket

Call `generate_article` with the following settings. Pass the full content brief from Step 3 as `additional_instructions` and the H2/H3 outline as `custom_outline`.

```
keyword:               [KEYWORD]
client_profile_id:     [CLIENT PROFILE ID — omit if blank]
word_count:            [WORD COUNT]
template:              blog
tone:                  [TONE]
include_toc:           true
include_faq:           true
include_images:        true
include_cover_image:   true
num_inline_images:     3
enable_research:       true
research_model:        perplexity/sonar-reasoning-pro
geo_optimization:      true
include_html_element:  true
include_internal_links: true
image_style:           photorealistic
image_aspect_ratio:    3:2
text_on_images_policy: headline
intended_audience:     [AUDIENCE]
custom_outline:        [H2/H3 outline from Step 3]
additional_instructions: [full content brief from Step 3]
```

Capture the `job_id` and `content_id` returned. Proceed to Step 5.

---

## Step 5 — Poll Until Article Complete

Call `get_job_status` every 30 seconds using the `job_id`.

Keep polling until `status = "done"`. Typical time: 5–15 minutes for a 3,000+ word research article with images.

Do not proceed to Step 6 until status is confirmed `done`.

---

## Step 6 — Verify Images

Call `get_article_images` using the `content_id`.

Check:
- `slot_index: 0` (cover image) → must be `status: done` before publishing
- At least 2 of the 3 inline images (slots 1–3) → should be `status: done`

If the cover image is not done, wait and re-check every 30 seconds.

If one inline image is still `running` after 5 additional minutes, proceed to publish anyway — do not hold the workflow indefinitely. Flag it in the final report.

---

## Step 7 — Publish to WordPress

Call `publish_wordpress` with:

```
article_id:  [content_id from Step 4]
site_id:     [WORDPRESS SITE ID]
status:      publish
post_type:   post
tags:        [TAGS array]
```

---

## Step 8 — Final Report

Report back with all of the following:

| Field | Value |
|-------|-------|
| Article title | [exact title used] |
| Live URL | [permalink] |
| Post ID | [post_id] |
| Word count | [word_count] |
| Featured image | Set ✅ / Not set ⚠️ |
| SEO meta | Set ✅ / Not set ⚠️ |
| Inline images embedded | [inline_images_count] |
| Tags applied | [tags] |
| Warnings | [any warnings from publish diagnostics] |

If `inline_images_count = 0` in the diagnostics, flag this clearly:
> ⚠️ Inline images were not embedded in the post. Go to WordRocket → My Content → open the article → click "Sync to WordPress" to push them, or set them manually in the WordPress editor.

---

## Troubleshooting Reference

| Problem | Fix |
|---------|-----|
| WordRocket connector not found | Settings → Connectors → ensure `wordrocketapi.com` is added with Always Allow |
| Job returns `failed` | Re-run Step 4 once — usually a research model timeout |
| All images stuck on `running` > 15 min | WordRocket dashboard → My Content → Regenerate Images |
| `inline_images_count: 0` after publish | WordRocket → My Content → Sync to WordPress |
| No featured image on live post | WordPress → Posts → open post → set Featured Image from Media Library |
| Published to wrong site | Verify `WORDPRESS SITE ID` matches the target site in WordRocket → Settings → Sites |

---

## Notes on Image Generation

WordRocket generates 4 images total: 1 cover + 3 inline. The cover is the most important — it becomes the featured image in WordPress and is what readers see in social previews.

Image prompts are auto-generated based on the article content. They will be photorealistic (3:2 ratio) with headline text overlaid on the cover. If you want a specific visual style, add it to `additional_instructions` before Step 4 (e.g. "Generate images in a clean editorial style with Canadian landmarks where relevant").
