# Where to save it so every chat uses it (official help pages, read Nov 7, 2026)


### ChatGPT

**Custom instructions** (https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions , "Updated 10 days ago")
- Web and Desktop: **Settings > Personalization**, make sure **Enable customization** is ON, type in the **Custom
  Instructions** field.
- iOS and Android: **Settings > Customize ChatGPT**, **Enable customization** ON, **Custom Instructions** field.
- Character limit: **Free and Go: 1,500 characters. Plus, Pro, Enterprise, Business, Education: 5,000 characters.**
  (Raised from 1,500 for paid plans on Jul 15, 2026, per the release notes.)
- Available on all plans, on web, desktop, iOS and Android.
- Scope: "applied immediately to all chats", "including existing conversations". This changed on Nov 7, 2025; before
  that, edits only applied to new chats (release notes). Small contradiction on the same help page: its FAQ still says
  updates are "reflected only in future conversations" (that answer is about what old chat history shows).
- Overrides: **Project instructions** "apply only within that project and override your global custom instructions"
  (https://help.openai.com/en/articles/10169521-projects-in-chatgpt). Temporary chats can be started
  **Unpersonalized** (no memories or custom instructions).

**Personality presets ("Base style and tone")** (https://help.openai.com/en/articles/11899719-customizing-your-chatgpt-personality , updated ~19 days ago)
- Web: profile icon > **Personalization** > dropdown **Base style and tone**. (The page says the icon is "bottom-right".)
  iOS/Android: profile icon > Settings > Personalization > Base style and tone.
- Options: **Default, Professional, Friendly, Candid, Quirky, Efficient, Cynical.** "Nerdy" was retired (release notes,
  March 2026).
- Applies across all chats, including existing ones.
- Important for us: a personality does NOT set the style of things you ask it to write. For an email, post or résumé,
  ChatGPT "will match the tone and style to your instructions and the context". So the humanizer goes in Custom
  Instructions, not in the personality.

**Characteristics** (https://help.openai.com/en/articles/20001038-characteristics-in-chatgpt , updated ~18 days ago)
- Web: profile icon > **Personalization** > **Characteristics**. Four sliders, each "+" or "-": **Warm,
  Enthusiastic, Headers & Lists, Emojis**. Applies to "this chat and new chats going forward".
- Useful pairing with the humanizer: Headers & Lists "-" and Emojis "-".

**Memory** (https://help.openai.com/en/articles/8590148-memory-in-chatgpt , updated ~7 days ago)
- **Settings > Personalization > Memory.** Controls vary by plan: Memory, Reference saved memories, Reference chat
  history, Memory summary, Manage, Saved memories.
- Memory is separate from custom instructions: custom instructions are "direct guidance"; memory builds up from chats
  and other sources. No storage limit for what chat history can reference. Not a reliable place for a style guide.

### Claude (claude.ai)

**Instructions (the old "personal preferences")** (https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features , updated ~2 weeks ago)
- Click your initials (lower left) > **Settings** > **Your Claude** (older layout: **Account**) > **Instructions**
  (older layout: **Instructions for Claude**).
- "Any instructions you add here will be applied to all of your conversations with Claude."
- No character limit is stated on the page. The help center no longer uses the phrase "personal preferences" except in
  one incognito FAQ. Incognito chats still use these profile settings
  (https://support.claude.com/en/articles/12260368-use-incognito-chats).
- Layout note: the "new Claude experience" (Cowork in every conversation) started rolling out Sep 16, 2026, which is
  why there are two Settings layouts.

**Styles: being retired, replaced by Skills (big change for the reel)**
- The old Styles article (10181068) was renamed **"Styles are moving to skills"** (dated Jun 1, 2026) and now returns
  404. Archived copy: https://web.archive.org/web/20260710101210/https://support.claude.com/en/articles/10181068-styles-are-moving-to-skills
  - Custom styles are migrated to skills automatically, **disabled by default**: turn them on in **Customize > Skills**.
  - Use one in a chat with a slash command: **/{style-name}-style** (e.g. "concise pirate" becomes /concise-pirate-style).
  - Concise, Explanatory and Formal default styles are removed; Learning lives on as a skill. The styles menu is
    removed once the migration finishes.
  - Or put the same tone and format guidance in your Instructions, which "apply to all your conversations".
- The current personalization article lists only Instructions, Project instructions and Skills (no Styles) and says
  "Use skills when you want to customize how Claude formats and delivers its responses."
- Old "create a style from writing samples" steps, for reference only (archived Dec 19, 2025 copy:
  https://web.archive.org/web/20251219114512id_/https://support.claude.com/en/articles/10181068-configuring-and-using-styles ):
  "Search and tools" menu > **Use style** > **Create & edit styles** > **Create custom style** > **Add Writing Example**
  (upload pdf/doc/txt or paste) > **Create style**. Or "Describe style instead" > "Use custom instructions (advanced)".
  Styles were picked per conversation and could be switched mid-chat. Do not show this flow in the reel as current.

**Skills (the current way to save a writing style you invoke on demand)**
(https://support.claude.com/en/articles/12512180-use-skills-in-claude , https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- Plans: Free, Pro, Max, Ultra, Team, Enterprise. Needs code execution: **Settings > Capabilities > Code execution and
  file creation** ("Create and edit files" in the updated layout).
- Add your own: **Customize > Skills > "+" > "+ Create skill" > "Upload a skill"**, upload a ZIP with the skill folder
  at its root containing **skill.md** (YAML front matter: `name` max 64 characters, `description` max 200 characters).
  Toggle it on. On a Mac in Cowork you can also "Record a skill" (Pro, Max, Ultra, Team).
- A skill is used when Claude judges it relevant (from its description) or when you call it; the docs suggest asking
  explicitly if it isn't picked up.

**Project instructions** (https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects , updated today)
- **claude.ai/projects > "+ New Project"** > on the project page click **"Set project instructions"** > **"Save
  instructions"**. Used "for all the chats within the project".
- Projects are available on all plans; Free users can make up to 5. (The personalization article still says project
  instructions are "paid plans only", a contradiction between two official pages.)

### B3. Scope in one line each
- **ChatGPT custom instructions:** yes, every chat, new and existing, as long as "Enable customization" is on; a project's
  instructions override them inside that project; an "Unpersonalized" temporary chat skips them.
- **Claude:** Instructions apply to all conversations. Styles were per conversation (picked from the menu); after the
  move to skills, a migrated style is turned on per conversation with its /{name}-style command. For "every chat", use
  Instructions (or a Project for one area of work).

---

