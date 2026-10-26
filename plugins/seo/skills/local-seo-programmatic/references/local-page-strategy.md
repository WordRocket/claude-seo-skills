# Local Page Strategy — Location Targeting Methodology

## Why Programmatic Local Pages Work

Google's local algorithm rewards relevance and proximity. When someone searches "roofing contractor Plano TX", a page titled "Roofing Contractor in Plano, TX" with content about that specific city almost always outranks a generic "service areas" page listing 40 cities.

Each location page is a targeted relevance signal. Done right (not thin, not duplicate), a network of 20–30 city pages can dominate an entire metro area.

---

## Step 1: Define the Location Hierarchy

Structure locations in 3 tiers based on a business's service area:

### Tier 1 — Primary Market (1–3 locations)
The city or cities the business is headquartered in or most wants to rank for. These get the most comprehensive pages (1,000–1,500 words, full FAQ, testimonials, embedded map).

### Tier 2 — Secondary Markets (5–15 locations)
Major suburbs or nearby cities within the service area. Strong pages (700–1,000 words), dedicated URL, unique content.

### Tier 3 — Tertiary Targets (10–30 locations)
Smaller towns, neighborhoods, or ZIP code areas. Shorter pages (500–700 words) that still have unique local signals — not just find/replace pages.

**Rule of thumb:** If a location has a distinct community identity and people would plausibly search "[service] in [location]", it deserves its own page.

---

## Step 2: Find Locations to Target

Use these data sources to build the location list:

### Competitor reverse engineering
Look at what your top 3 competitors are targeting. Their site structure tells you exactly what's worth building:
```
site:competitor.com inurl:dallas
site:competitor.com /locations/
```

### Google Trends by region
`get_interest_by_region` for the primary service keyword — sub-regions with notable interest are strong targets even if the business hasn't thought of them.

### "Near [city]" search queries
Search `[service] near [primary city]` and look at the "People also search for" and map results — those are your tier 2 and 3 targets.

### Population/commuter patterns
For service businesses, follow where people live and work. Major suburbs of a metro area almost always have high search demand for local services.

---

## Step 3: Decide on URL Structure

Pick ONE pattern and stick to it across all location pages. Never mix patterns.

**Option A: Service-first** (best when the service is the primary brand differentiator)
```
/hvac-repair-dallas/
/hvac-repair-plano/
/hvac-repair-frisco/
```

**Option B: Location-first** (best for hyper-local businesses or those with strong local identity)
```
/dallas-hvac-repair/
/plano-hvac-repair/
```

**Option C: Hub-and-spoke** (best for businesses with multiple service lines)
```
/locations/dallas/
/locations/plano/
  — then internally link from /locations/dallas/ to /dallas-hvac-repair/, /dallas-ac-installation/, etc.
```

Choose based on what competitors rank with and what matches the existing site structure.

---

## Step 4: What Makes a Local Page Actually Rank

Every location page needs these signals to rank. Generic "we serve Dallas too" pages don't work.

### Non-negotiables
- Location in title tag, H1, and first paragraph
- Unique introductory paragraph mentioning the city by name (not copy-pasted from another page)
- The business's address or service confirmation for that area
- At least one local-specific mention: a neighborhood, a landmark, a local event, local weather patterns if relevant to the service (e.g. "Dallas summers push HVAC systems hard")

### Strong additions (prioritize these)
- FAQ section targeting "[service] in [city]" questions — mine from Google's "People Also Ask"
- Testimonial or review from a customer in that city (even just a quote attributed to "[First Name], [City]")
- Embedded Google Map of the area
- List of specific neighborhoods or ZIP codes served within that city
- Service-specific content relevant to that location (e.g. local building codes, permit requirements, common problems in that climate)

### What to avoid
- Identical pages with just the city name swapped out — Google detects and penalizes this
- Thin pages under 400 words
- Pages with no internal links pointing to them (orphan pages)
- Location pages that aren't linked from the main navigation or a locations hub

---

## Step 5: Content Brief Template

For each location page, capture these fields before writing:

```
TARGET URL: /[service]-[city]/
PRIMARY KEYWORD: [service] [city] [state]
SECONDARY KEYWORDS: 
  - [service] near [city]
  - [service] company [city]
  - [service] contractor [city] [state]
  - best [service] [city]
  - [service] cost [city]
PAGE TITLE TAG: [Service] in [City], [State] | [Business Name]
H1: [Service] in [City], [State]
RECOMMENDED WORD COUNT: [based on top 3 competitors — match or beat the longest]
TIER: [1 / 2 / 3]
LOCAL SIGNALS TO INJECT:
  - Neighborhoods: [list]
  - Landmarks: [list]  
  - Local context: [e.g. "known for hot humid summers" / "older housing stock means X is common"]
  - ZIP codes: [list if tier 1 or 2]
KEY SECTIONS:
  1. Intro (why we serve [city], what we do there)
  2. Our [Service] Services in [City]
  3. Areas We Serve Within [City] (neighborhoods)
  4. Why Local Homeowners/Businesses Choose Us
  5. FAQ — [City]-specific questions
  6. Service Coverage Map
  7. CTA — get a quote / call us
INTERNAL LINKS FROM THIS PAGE:
  - → [main service page]
  - → [nearby city pages]
INTERNAL LINKS TO THIS PAGE:
  - From: [hub page / homepage / related blog posts]
```

---

## Step 6: Prioritization Order

Build pages in this order for maximum early impact:

1. **Tier 1** pages first — highest volume, most competitive, but ranking here validates the strategy
2. **Tier 2** pages next — faster to rank, good traffic, builds topical authority
3. **Tier 3** pages last — lower individual volume but collectively important, and competition is usually weak

Within each tier, prioritize locations where competitors have pages but they're thin or low quality — you can outrank them quickly with better content.
