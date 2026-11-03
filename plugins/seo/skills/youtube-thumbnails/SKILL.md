---
name: "youtube-thumbnails"
description: "Level-10 YouTube thumbnails (\"prompt maxing\"): Claude studies the top-performing videos in your niche in your own Chrome (100K+ views, outliers that beat their channel's usual views), screenshots and analyses their thumbnails into a research doc, turns your video title into thumbnail concepts and one finished image prompt built on that research, then generates the thumbnail with GPT Image 2 through the kie.ai API (your key) and checks it. Use whenever the user wants a YouTube thumbnail, better thumbnails, higher CTR, \"design my thumbnail\", \"what thumbnails work in my niche\", a thumbnail prompt, or to connect kie.ai / GPT Image 2 to Claude. Delivers thumbnail-research.md, the prompts, and 1–3 generated thumbnails (1280×720)."
---

# YouTube thumbnails, prompt-maxed

"Make me a thumbnail" (level 1) gets a generic image. Level 10 is research first: find what already earns clicks in
the niche, copy the *patterns* (never the images), then generate from a prompt built on that research with a strong
image model. You do every step; the user only gives the niche, the title and (for generation) their kie.ai key.

Outputs (in `thumbnails/` in the working folder, or as downloads on Claude.ai):
1. `thumbnail-research.md`: the reference videos and the patterns that win in this niche.
2. `prompts.md`: 3 concepts for the title and the final image prompt for each.
3. `thumb-<n>.png`: the generated thumbnails (when the kie.ai key is set), checked against the research.

---

## Step 0: Inputs (ask once)
- Niche or channel URL, and the exact video title.
- Optional: a photo of the creator for face thumbnails (image-to-image), brand colours, words that must appear.
- To generate: a kie.ai API key. In Claude Code the user sets it themselves: `export KIE_API_KEY=...` (never paste it
  into chat, never print it). On Claude.ai without code access: skip generation, hand over the prompt to paste into the
  kie.ai playground (kie.ai/gpt-image-2).

## Step 1: Find the winners (Claude in Chrome)
Search YouTube for 3–5 searches a viewer of this video would type (the title's topic, the niche's main terms).
For each search, open the results and the top channels' Videos tab sorted by Popular. Keep 15–30 videos that are:
- 100K+ views (lower the bar for tiny niches and say so), published in the last ~18 months;
- outliers: views well above that channel's typical video (a strong sign of a high click-through rate, which YouTube
  does not show publicly; say "outlier", never claim a CTR number).
Record: title, channel, views, age, URL, and a screenshot of the thumbnail.

## Step 2: Analyse the thumbnails → `thumbnail-research.md`
For every reference, note: words on the image (count, size, colour), face (yes/no, emotion, where it looks), the main
object, background, contrast, composition (left/right split, arrow, before/after), brand logos. Then write the
patterns that repeat in the outliers, each with how many of the references show it, for example
"3–4 huge words, yellow + white on dark: 11 of 18". End with 5 rules for this niche and 3 things everyone does that
you could do differently to stand out.

## Step 3: Concepts + the final prompt → `prompts.md`
For the user's title write 3 concepts (one line each: the idea + why it should earn the click, tied to the patterns).
The thumbnail must ADD to the title, not repeat it (2–4 words max on the image). For each concept write the image
prompt for GPT Image 2:
- format: "YouTube thumbnail, 16:9, 1280x720"; the scene, subject, expression, lighting, background;
- the exact on-image text in quotes, its font style, colour, size and position (GPT Image 2 renders text well);
- contrast and focal point rules from the research; nothing small, nothing busy;
- with a creator photo: use image-to-image and say what to keep (face, hair, clothes) and what to change.
Never copy another creator's thumbnail, logo, face or artwork. Brand logos only when the video is about that brand.

## Step 4: Generate (kie.ai · GPT Image 2)
In Claude Code, with `KIE_API_KEY` set:
```
python3 [skill_dir]/scripts/kie_generate.py --prompt-file thumbnails/prompt-1.txt --out thumbnails/thumb-1.png --resolution 2K
```
(add `--image <url>` for image-to-image with the creator's photo). It creates the task, polls until it's done and
downloads the image. kie.ai's listed price for GPT Image 2 is about $0.03 (1K) to $0.08 (4K) per image (check
kie.ai/gpt-image-2 for current prices); confirm with the user before generating more than 3.

## Step 5: Check and iterate
Look at each result at full size and at phone size (~170 px wide): is the main subject readable, is the text spelled
right and legible, does it match the research rules? Fix the prompt and regenerate the best concept once if needed.
Give the user the finished files, the prompt that made each one, and which concept you'd test first.

## Rules
- Study, don't copy: patterns only, never another creator's image, face, logo or exact layout.
- Never invent view counts or claim CTRs; outliers are "views far above the channel's usual".
- The API key stays in the environment; never echo it or write it to a file.
- Be honest about the face: if the creator wants their own face, use their real photo (image-to-image).
