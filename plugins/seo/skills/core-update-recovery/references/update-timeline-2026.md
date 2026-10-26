# Google Core & Spam Update Timeline (2025–2026) — Reference

Pulled from live research as of July 2026. **Always re-verify with a fresh web
search before writing a report** — Google may have shipped a newer update
since this file was last touched, and this file itself should be updated
whenever the skill runs and finds something newer.

## Confirmed rollouts

| Update | Dates | Duration | Notes |
|---|---|---|---|
| June 2025 Core | Jun 30 – Jul 17, 2025 | ~17 days | |
| December 2025 Core | Dec 11 – Dec 29, 2025 | ~18 days | |
| Jan 2026 (unconfirmed, "Mt. AI") | ~Jan 2026 | — | Not officially confirmed by Google; hit sites scaling low-quality AI/commodity content hard. Glenn Gabe (GSQi) coined "Mt. AI" for the surge-then-crash pattern. Sites hit here mostly had NOT recovered as of the May core update. |
| March 2026 Spam Update | Mar 24–25, 2026 | <20 hrs | Shortest confirmed spam update on record. Cleared bad actors just before the core update. |
| March 2026 Core | Mar 27 – Apr 8, 2026 | ~13 days | 55% of tracked sites (Ahrefs/Semrush) saw measurable ranking change. Rewarded "information gain" (original data, first-hand experience, unique methodology). LCP > 3s pages saw ~23% more traffic loss than faster peers. |
| May 2026 Core | May 21 – Jun 2, 2026 | ~11 days 21 hrs | Overlapped Google I/O. Larger/more typical than March. Multiple volatility spikes (May 23, May 30, Jun 2), not one smooth curve — date your impact to the specific spike. Heavy YMYL (gambling, finance, health) volatility. Reddit gained more top-3/top-1 SERP real estate across all niches (biggest in Pets/Education/Sports/E-commerce, smallest in Real Estate/Healthcare/News); YouTube thinned out of regular link results in the same window. Unique domains ranking in top 10/top 3 both increased — SERPs got less monopolized. |
| June 2026 Spam Update | Jun 24–26, 2026 | ~2 days | SpamBrain-based, targets scaled/AI-driven spam signals. No official new policy or named system disclosed — treat "S-CTS" / embedding-based detection claims as speculation, not confirmed mechanism. Reassessment can take months, not days. Coincides with a cluster of AI-surface signals across June (May policy expansion → GSC AI-traffic reporting → AI Overviews opt-out toggle June 17 → this spam update). |

**Pattern**: updates are landing every 2–4 months and the gap between them is
shrinking. Full algorithmic "credit" for genuine improvements tends to show
up at the *next* core update, not immediately — Google has repeatedly said
recovery is usually measured in weeks-to-months, and the biggest jumps
typically land alongside a future update, not a slow drift.

## What Google says, verbatim in substance (paraphrased, not quoted)

- There is no specific fixed action list to "recover" from a core update; a
  drop doesn't necessarily mean something is broken.
- Improving content beats deleting it — pruning is a last resort for pages
  built for search engines rather than people.
- Recovery is not instant; some sites see partial movement between core
  updates via smaller unannounced adjustments, but the largest re-scoring
  tends to land with the next core update.
- AI-generated content isn't penalized as a category — thin, derivative,
  unedited output is penalized regardless of who/what wrote it.

## What's consistently correlated with recovery / gains (cross-source synthesis)

1. **Topical authority / depth over breadth** — narrow, expert coverage of a
   niche outperforms broad-but-shallow. Interconnected content clusters beat
   isolated articles.
2. **Information gain** — original data, first-hand experience, proprietary
   insight, unique methodology. Pages that just re-summarize the SERP lose.
3. **E-E-A-T site-wide, not just page-level** — Google's systems evaluate
   this across the whole site now; a weak spot in one area can drag down
   otherwise-strong content. Author credentials, consistent expertise
   signals, and trust markers matter more than any single page's polish.
4. **Freshness / maintenance** — updating and re-publishing existing ranking
   pages with more current, relevant material is a repeatedly-cited recovery
   lever, not just new content velocity.
5. **Consolidation over sprawl** — merging overlapping/duplicate pages into
   one comprehensive resource (with 301s + internal link updates) beats
   letting thin variants compete with each other.
6. **Local/location pages** — count as part of topical + entity authority
   when they're genuinely useful (not templated NAP dumps); part of "closer
   to primary information, more useful as an endpoint" pattern Google
   rewarded in March/May 2026.
7. **Technical quality as a tiebreaker** — Core Web Vitals (esp. LCP <2.5s)
   don't cause recovery by themselves but measurably worsen outcomes for
   otherwise-comparable content. Not the main lever, but don't ignore it.
8. **Off-platform / cross-channel signals** — YouTube, Reddit, and other
   community/video presence correlate with entity authority and citations in
   AI Overviews/AI Mode, which increasingly ride the same underlying quality
   systems as classic Search. Caveat from practitioner data: manufactured
   Reddit seeding shows weak ROI — the threads that get cited skew old (avg.
   ~900 days) and low-upvote; authentic, sustained presence beats a sprint.
9. **Strategic backlinks from reputable, topically-relevant sites** — still
   valuable as an authority signal, but multiple sources explicitly warn that
   "just build more backlinks" is not a fix for a content-quality-driven
   core update hit. Links reinforce genuine authority; they don't substitute
   for it.
10. **Don't touch anything mid-rollout.** Reacting to day-to-day volatility
    during a live rollout risks turning a recoverable dip into a real one.
    Diagnose only after a clean post-completion window (Google-recommended:
    ~1 week after official completion).

## Diagnostic method (use this to date and classify a traffic drop)

- Pull a **multi-week time series**, not a single before/after snapshot —
  rollouts move in multiple distinct volatility spikes.
- Shape tells you the cause: a **flat line → sharp step at a dated event →
  new flat line** = algorithm event. A **gradual downward slope** = content
  quality decay (not a single update). A **line that keeps falling past the
  rollout window** = possible manual action or ongoing spam-cleanup, check
  GSC Manual Actions report.
- Cross-reference the exact date(s) of movement against the confirmed
  rollout windows above. If the drop doesn't line up with a confirmed
  update window, look for: Search Console glitches, seasonality, a
  competitor surge, or a technical issue (deploy, robots.txt, canonical
  errors) around that date instead.
- Check whether CTR moved independently of position — position dropping with
  flat CTR means "we still convert visitors, we rank lower"; that's a pure
  ranking/authority signal. CTR dropping with flat position means a
  SERP-features issue (someone else got the AI Overview/snippet).
