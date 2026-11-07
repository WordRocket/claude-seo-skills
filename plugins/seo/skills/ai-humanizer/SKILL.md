---
name: ai-humanizer
description: |
  Makes AI writing sound like YOU, not a chatbot. Learns your voice from 3–5 samples, rewrites drafts to remove the
  2026 AI tells (phrases like "this matters", "rather than simply", "not just X but Y", reflex lists of three, not only
  em dashes), and gives you a paste-ready prompt for ChatGPT custom instructions or Claude Instructions so every chat
  writes like you. Use when the user says: "make this sound human", "humanize this", "this sounds like AI", "learn my
  voice", "write like me", "set up my writing style in ChatGPT/Claude", or pastes text that reads robotic.
---

# AI humanizer

Readers trust text less when they think AI wrote it (Raptive 2025: 48% less trustworthy, 57% less authentic, even when
a human wrote it). And the old tricks are out of date: AI models nearly stopped using em dashes in 2026 (Graphite
measured Claude Opus 5.5 at 0.015 per 1,000 words, down 99%), so a prompt that only bans em dashes misses what gives
AI away now: stock phrases and patterns. This skill fixes both: it writes in the user's voice and hunts the real tells.

References: `references/humanizer-prompt.md` (the prompt, full + compact, with the source of every rule),
`references/ai-tells-2026.md` (the tells, with data), `references/where-to-save.md` (exact menu paths and limits).

---

## Mode 1: Learn my voice (do this once)

1. Ask for 3–5 things the user wrote themselves and likes: emails, posts, a page, messages. Not AI-edited text.
2. Read them and write a short voice profile into `voice.md`: typical sentence length and how much it varies, the
   words and phrases they actually use, how they open and close, punctuation habits (parentheses, exclamation marks,
   dashes), formality, humour, what they never say. Quote 4–6 short lines from the samples as anchors.
3. Build their personal prompt: take the full version in `references/humanizer-prompt.md`, put 2–3 of their best short
   samples in the `<examples>` slot, and add 3–5 voice rules from the profile. Keep it under 5,000 characters (ChatGPT
   paid, Claude) and also give the compact version under 1,500 for ChatGPT Free/Go. Show the character count.
4. Tell them where to paste it (from `references/where-to-save.md`):
   - ChatGPT (web/desktop): Settings › Personalization › Custom instructions (applies to all chats).
   - Claude: Settings › Your Claude › Instructions (applies to all conversations).
   - For one client or project only: a ChatGPT Project's instructions, or a Claude Project's instructions.

## Mode 2: Humanize this text

1. Keep every fact, number, name and link. Add none.
2. Rewrite in the user's voice (use `voice.md` if it exists; otherwise ask for one sample or use plain, direct prose).
3. Run the final check from the prompt: scan for every AVOID item in `references/ai-tells-2026.md` and the prompt,
   rewrite each hit, vary punctuation (a parenthesis or "!" is fine, em dashes go), mix sentence lengths, read it as
   the user and fix any line they wouldn't say out loud.
4. Return the rewritten text, then a short list of what you changed and why (pattern → fix), so the user learns it.

## Mode 3: Check for AI tells

Scan the text and list every tell found, quoted, with the category (stock phrase, "not just X but Y", reflex triad,
tacked-on "-ing" clause, vague attribution, chatbot filler, heading/bold/bullet overuse, uniform sentence length, em
dashes) and a one-line fix for each. End with a 0–10 "sounds like a person" score and the 3 fixes that matter most.

---

## Rules
- Signs are signs, not proof (Wikipedia's own warning). Never claim text will "pass" or "beat" an AI detector.
- Never invent facts, quotes, sources, experiences or numbers to make text sound more human.
- The goal is the user's voice, not a generic "human" voice: when in doubt, copy their samples' rhythm and words.
- If the text is for others to read as the user's own work, the user decides how to disclose AI help.

Sources: Wikipedia, "Signs of AI writing" (WikiProject AI Cleanup, rev. Nov 6, 2026); Graphite, "AI Tells" (Sept 16,
2026) and the Opus 5.5 update (Oct 1, 2026); Kobak et al., Science Advances (2025); Raptive (2025); Pew Research Center
(2025); Anthropic and OpenAI prompting guides; OpenAI and Anthropic help centers (menu paths, Nov 2026). Links in the
references. Made by WordRocket (wordrocket.ai).
