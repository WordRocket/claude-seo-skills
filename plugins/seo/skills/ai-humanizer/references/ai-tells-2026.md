# What gives AI writing away (sourced, Nov 2026)

## The short version

1. Wikipedia volunteers keep a public field guide to AI writing, "Signs of AI writing" (WikiProject AI Cleanup),
   last edited Nov 6, 2026. It says these are signs, not proof.
2. The famous AI words are real and measured: in 15M+ PubMed abstracts, "delves" ran 28x its expected 2024 rate,
   and at least 13.5% of 2024 abstracts were processed with an LLM (Kobak et al., Science Advances, 2025).
3. The em dash is no longer a reliable tell. Wikipedia moved it to "historical indicators (2022 to September 2026)".
   Claude Opus 5.5 uses 0.015 per 1,000 words, down 99% from Opus 5 (Graphite, Oct 1, 2026).
4. The 2026 tells are phrases, not punctuation: "matters because" (357x the human rate in GPT-6 Astra), "this matters"
   (116x in Opus 5.5), "dependable" (59x Astra, 23x Opus 5.5), "rather than simply/merely", "not simply" (Graphite).
5. Readers punish text they THINK is AI: 48% less trustworthy, 57% less authentic (Raptive, 3,000 US adults, 2025),
   even when a human wrote it. 56% of Americans would like a news article less if they learned AI wrote it (Pew 2025).
6. People who use ChatGPT a lot spot it: a majority vote of 5 such "experts" misclassified only 1 of 300 articles
   (Russell et al., ACL 2025). Most people can't: 53% of Americans aren't confident they can tell (Pew 2025).


## Part A1. Wikipedia: "Signs of AI writing" (WikiProject AI Cleanup)

- URL: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (shortcuts WP:AISIGNS, WP:AITELLS)
- Last revision checked: Nov 6, 2026, 22:56 UTC (revid 1384165696, via the MediaWiki API). Read from the raw wikitext.
- Framing: a "field guide" for Wikipedia; the list is "descriptive, not prescriptive". Signs are "only potential signs
  of a problem, not the problem itself". It warns that AI detectors have "non-trivial error rates" and that human
  judgment is unreliable (cites a 2025 study: no better than chance; a German theses study: 57% recognition for AI
  texts, 64% for human texts).
- "As of October 2026" the most common signs on Wikipedia: Markdown, AI edit summaries, hedging disclaimers about
  sources, vague "connected/associated with" wording, undue emphasis on identification by primary sources.
- Caution for our use: the page asks editors not to just scrub surface signs because "that could just make detection
  harder". Our angle is different (your own writing, in your own voice), but the reel should not promise "undetectable".

### Main categories and concrete examples (page order)

| Section | Concrete examples on the page |
|---|---|
| **Content** | |
| Undue emphasis on significance, legacy, trends | "stands/serves as", "is a testament/reminder", "a pivotal/crucial/vital role/moment", "underscores/highlights its importance", "reflects broader", "setting the stage for", "key turning point", "evolving landscape", "indelible mark", "deeply rooted" |
| Canned emphasis on notability / media coverage | "independent coverage", lists of outlet types, "maintains an active social media presence" |
| Undue emphasis on identification by primary/tertiary sources (newer) | "identifies him as", "is listed in", "his professional profile lists" |
| Superficial analyses | trailing "-ing" phrases: "highlighting/underscoring/emphasizing...", "ensuring...", "reflecting/symbolizing...", "contributing to...", "fostering...", "valuable insights", "align/resonate with" |
| Vague connection | "in connection with", "connected to", "associated with" instead of stating the relationship |
| Vague attributions (weasel words) | "Industry reports", "Observers have cited", "Experts argue", "Some critics argue", "several sources" when only one or two are cited |
| Outline-like conclusions | "Despite its... faces several challenges", "Despite these challenges", "Challenges and Legacy", "Future Outlook" |
| "Awards and recognition" section | "X and Y" headers, near ubiquitous in AI articles |
| **Language and grammar** | |
| High density of "AI vocabulary" | Words to watch: Additionally (starting a sentence), align with, boasts (= has), bolstered, crucial, deep dive, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, landscape (abstract), meticulous/meticulously, pivotal, robust, showcase, tapestry (abstract), testament, underscore (verb), valuable, vibrant. "One word is coincidental; many in one edit is a strong tell" (paraphrase). |
| ...by era (page's own breakdown) | 2023 to mid-2024 (GPT-4): delve, tapestry, testament, pivotal, underscore, intricate, garner, meticulously, vibrant... Mid-2024 to mid-2025 (GPT-4o): align with, enhance, fostering, highlighting, showcasing... Mid-2025 to mid-2026 (GPT-5): emphasizing, enhance, highlighting, showcasing. Mid-2026 on (GPT-6): challenge, clearer, dependable, echoed, foster, leverage, matters, multifaceted, practical, prioritize, quietly, steady, universally, plus more periods/commas and 8 to 20 word sentences. Grok: causal, empirical, correlate, still "underscore". Note: the GPT-6 list cites a review site (intellectualead.com), the weakest source on the page. |
| Avoidance of basic copulatives | "serves as / stands as / marks / represents" instead of "is"; "boasts / features / offers" instead of "has"; "refers to". Cites a >10% drop in "is"/"are" in academic writing in 2023 (Geng & Trotta, arXiv 2404.08627). |
| Negative parallelisms | "Not just X, but also Y" / "Not only... but..."; "Not X, but Y" / "It's not..., it's..." / "no..., no..., just..."; "Y rather than X" (common in recent output) |
| Lists/titles treated as proper nouns | "[Title] is the chronological list of..." |
| Rule of three | "adjective, adjective, adjective" or "short phrase, short phrase, and short phrase", used to make shallow analysis look complete |
| **Style** | Title case in headings; overused boldface (and stray asterisks); inline-header vertical lists; wrong heading levels; emoji at the start of headings or list items; curly quotes/apostrophes instead of straight ones |
| **Communication meant for the user** | "I hope this helps", "Of course!", "Certainly!", "You're absolutely right!", "Would you like...", "is there anything else", "let me know", "here is a..." |
| Hedging disclaimers | 2023-24: "it's important to note/remember", "it is crucial to differentiate". 2024-25: "not widely available/documented", "maintains a low profile". Mid-2026: "should be treated as... rather than...", "based on available information", "does not by itself establish", "should not be confused with" |
| Placeholders | date and URL placeholders left in text |
| **Markup** | Markdown in wikitext (asterisk bold, # headings, `---` dividers, triple backticks), leaked citation code like `contentReference[oaicite:1]` (called unambiguous) |
| **Citations / edit summaries / misc** | broken links, invalid DOIs/ISBNs, `utm_source=` links, canned "I preserved/retained..." edit summaries, sudden style shifts |
| **Signs of HUMAN writing** (useful for voice rules) | simple "is/has" ("there is a", "it has a"); plain verbs: "wrote" not "authored", "moved" not "relocated", "used" not "utilized", "tried" not "attempted", "died" not "passed away"; definitive statements ("one of the best", "is the only", "was the first"); qualifiers ("very", "perhaps", "tends to"); wordy bits like "in order to", "the fact that" |
| **Ineffective indicators** (do NOT treat as tells) | perfect grammar; mixed casual/formal register; "bland" or "fancy" prose without the specific words; transition words alone ("Additionally", "Notably"); unsourced content; correct wikitext |
| **Historical indicators** (older models, less common now) | Promotional tone 2023 to 2025 ("boasts a", "vibrant", "rich", "nestled", "in the heart of", "groundbreaking", "renowned", "diverse array"); knowledge-cutoff disclaimers 2022 to 2023 ("as of my last knowledge update", "up to my last training update"); section summaries ("In summary", "In conclusion", "Overall"); prompt refusals ("As an AI language model..."); **overuse of em dashes (2022 to September 2026)**; abrupt cut-offs; outdated access-dates; elegant variation (too many synonyms) |

### The em dash entry, exactly what it says (WP:AIDASH)
- LLMs used em dashes far more than nonprofessional human writers, "in a formulaic, pat way", often with spaces around
  them. Most useful combined with other signs.
- Some companies made newer chatbots suppress them, "most notably OpenAI's GPT-5.1" (cites Ars Technica, Nov 14, 2025).
- Cites The Economist (Jul 30, 2026): of current models, only Claude used em dashes more than professional writers, and
  ChatGPT used them less. (Economist is paywalled; I could not open it. Second-hand via Wikipedia.)
- Since September 2026 the latest models are "more and more often" found hard-coded to use no em dashes at all; the page
  says this made punctuation less varied, so heavy commas/periods are becoming their own sign. That last claim is
  tagged [citation needed] on the page.
- Curly quotes, title case and emoji are not dated on the page; they are listed as current "Style" signs.

---


## Part A2. Data on overused words, em dashes, and trust

### Overused words (peer-reviewed)
1. **Kobak, González-Márquez, Horvát, Lause, "Delving into LLM-assisted writing in biomedical publications through
   excess vocabulary", Science Advances 11(27), Jul 2, 2025.** https://www.science.org/doi/10.1126/sciadv.adt3813
   (full text read via Europe PMC, PMC12219543)
   - Corpus: "more than 15 million biomedical abstracts from 2010 to 2024" (PubMed).
   - "at least 13.5% of 2024 PubMed abstracts were processed with LLMs" (lower bound); up to 40% in some subcorpora.
   - Excess-frequency ratios in 2024: **delves r = 28.0, underscores r = 13.8, showcasing r = 10.7**. Common words with
     the biggest excess: potential (δ = 0.052), findings (0.041), crucial (0.037).
   - 379 excess style words in 2024; 66% verbs, 14% adjectives. During COVID the excess words were almost all content
     words ("respiratory", "remdesivir"); in 2024 they were almost all style words.
2. **Juzek & Ward, "Why Does ChatGPT 'Delve' So Much?", COLING 2025.** https://aclanthology.org/2025.coling-main.426 ,
   arXiv 2412.11385. Found 21 "focal words" (incl. delve, intricate, underscore) whose rise in scientific abstracts is
   likely from LLM use. Found no evidence it comes from architecture or training data; tests were "consistent with RLHF
   playing a role". In their experiment, readers grew wary of "delve" in an abstract's first sentence.
3. **Russell, Karpinska, Iyyer, "People who frequently use ChatGPT for writing tasks are accurate and robust detectors
   of AI-generated text", ACL 2025.** https://aclanthology.org/2025.acl-long.267/ . 300 non-fiction articles; majority
   vote of five "expert" annotators "misclassifies only 1 of 300 articles". They rely on "AI vocabulary" plus
   formality, originality and clarity.

### 2026 tells and em dash measurements (industry research, not peer-reviewed)
4. **Graphite (Druck, Paredes, Smith), "AI Tells", Sep 16, 2026.** https://graphite.io/five-percent/research/ai-tells
   - 10,000 pre-ChatGPT human articles (Common Crawl) vs 90,000 AI articles (10,000 each from GPT-4.1, GPT-5,
     GPT-5.6 Sol, GPT-6 Astra, Claude Opus 4, 4.6, 5, Gemini 2.5 Pro, 3.1 Pro) on the same topics. A "tell" = used at
     least 2x as often as humans. 12,877 tells found; 65% unique to one model family.
   - Em dashes: GPT-6 Astra about 1/8 of the human rate (88% below pre-ChatGPT humans); Claude Opus 5 about the human
     rate; Gemini 3.1 Pro "nearly stopped".
   - Ratios vs humans. Astra: "matters because" 357x, "rather than relying" 187x, "not simply" 157x, "another
     dimension" 117x, "together these" 95x, "dependable" 59x, "practical" 26x. Opus 5: "rather than merely" 160x,
     "matters because" 132x, "less like a _ and more like" 105x, "rather than simply" 43x, "what comes next" 28x,
     "deliberate" 26x. Gemini 3.1 Pro: "is not just a _ it is" 153x, "ultimately this" 78x, "furthermore the" 43x,
     "absolutely essential" 32x, "profound" 25x.
   - Style: AI sentence lengths vary much less than humans'; AI words average 5.2 to 5.7 characters vs 4.9 for humans;
     humans use exclamation marks over 100x as often as current models and use far more parenthetical asides.
   - Conclusion: well-known tells are fading but "tells shift between versions rather than disappearing".
5. **Graphite, "AI Tells: Opus 5.5 Update", Oct 1, 2026.** https://graphite.io/five-percent/research/ai-tells-opus-5-5-update
   - Em dashes: **Opus 5.5 = 0.015 per 1,000 words vs Opus 5 = 2.92 (minus 99%)**.
   - Tells: 2,548 for Opus 5.5 vs 2,666 for Opus 5 (minus 4%); Opus 4 had 3,746. Top: "this matters" 116x, "is more than a _ it" 98x, "why _
     matters" 92x, "looking ahead the" 40x, "rather than simply" 32x, "adds another layer" 27x, "what comes next" 24x,
     "dependable" 23x, "steady" 11x, "thoughtful" 9x, "meaningful" 8x.
   - Opus 5.5's word distribution is 19% closer to human writing than Opus 5's; "mannered prose" score 10.57 vs human
     6.65 (about 1.6x).
6. **Pangram Labs, "9 Signs of AI Writing, Backed by Data"** (AI-detector vendor, page undated, © 2026).
   https://www.pangram.com/signs-of-ai-writing . Per 10,000 words, human vs AI: Markdown 8 vs 90 (bold 2 vs 65), AI
   phrases 3 vs 30, em dashes 2 vs 17 (by family: OpenAI 45, Anthropic 32, Gemini 3 Pro 3, below human), bullet lists
   3 vs 28, triads 5 vs 19, "not just X but Y" 1 vs 3, "Certainly! Here's" 0 vs 94. Some multipliers on the page don't
   match its own numbers and it uses two different human em dash baselines (2 and 5); method not disclosed. Use only as
   supporting color.
7. **OpenAI, ChatGPT release notes** (read live): Nov 2025 entry says "GPT-5.1 models follow your custom instructions
   and style preferences more reliably". The em dash coverage of Sam Altman's post (Ars Technica, Nov 14, 2025) I could
   not open directly (site blocks fetches); it is cited on Wikipedia.
   https://help.openai.com/en/articles/6825453-chatgpt-release-notes

### Do readers trust content they think is AI?
8. **Pew Research Center, "How Americans View AI and Its Impact on People and Society", Sep 17, 2025.** 5,023 US
   adults, Jun 9 to 15, 2025. https://www.pewresearch.org/science/2025/09/17/how-americans-view-ai-and-its-impact-on-people-and-society/
   - 76% say it is extremely or very important to be able to tell if pictures, videos and text were made by AI or people.
   - 53% are not too or not at all confident they can tell.
   - Same survey (short read): if they learned AI wrote a news article they felt informed by, 56% would like it less,
     7% more, 36% no difference. Political speech: 71% less.
     https://www.pewresearch.org/short-reads/2025/09/17/from-political-speeches-to-songs-how-would-americans-react-if-they-found-out-ai-was-involved/
9. **Raptive, "The 'AI stink' is real, and it's costing brands"** (ad company; commissioned survey, 3,000 nationally
   representative US adults; published Jul 2025, page updated Aug 22, 2025).
   https://raptive.com/blog/the-ai-stink-is-real-and-its-costing-brands/
   - When people suspected content was AI: 48% less trustworthy, 57% less authentic, 60% lower emotional connection.
     Ads next to it: purchase consideration minus 14%, willingness to pay a premium minus 14%.
   - The effect follows perception, "regardless of whether it was really AI-generated or not" (Anna Blender, SVP).
   - Caveat: vendor study; the page doesn't give the survey firm, questions or baseline.
10. **Schilke & Reimann, "The transparency dilemma: How AI disclosure erodes trust", Organizational Behavior and Human
    Decision Processes, 2025** (DOI 10.1016/j.obhdp.2025.104405). 13 experiments, 5,000+ participants (per University
    of Arizona News, May 29, 2025). People who disclose AI use are trusted less; being exposed by others is worse.
    https://news.arizona.edu/employee-news/being-honest-about-using-ai-work-makes-people-trust-you-less-research-finds
11. Not verified, don't use: Search Engine Land's Feb 2026 "AI writing tics" engagement study (1,000+ content pages;
    secondary write-ups say em dashes had a slight POSITIVE link to engagement). The page returned 403 to me.

---

