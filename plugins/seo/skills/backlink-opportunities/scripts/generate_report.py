#!/usr/bin/env python3
"""
Backlink Opportunities Report Generator
Reads backlink_findings.json and outputs a beautiful, prioritized HTML report.
"""

import json
import argparse
import sys
from datetime import datetime

TIER_CONFIG = {
    "quick_win":   {"emoji": "🔥", "label": "Quick Win",    "color": "#ef4444", "bg": "#fef2f2", "border": "#fca5a5", "order": 1},
    "high_value":  {"emoji": "🎯", "label": "High Value",   "color": "#7c3aed", "bg": "#f5f3ff", "border": "#c4b5fd", "order": 2},
    "volume_play": {"emoji": "📈", "label": "Volume Play",  "color": "#0284c7", "bg": "#f0f9ff", "border": "#7dd3fc", "order": 3},
    "long_game":   {"emoji": "🌊", "label": "Long Game",    "color": "#059669", "bg": "#f0fdf4", "border": "#6ee7b7", "order": 4},
}

TYPE_LABELS = {
    "guest_post":    "Guest Post / Write For Us",
    "resource_page": "Resource Page",
    "link_insertion":"Link Insertion / Niche Edit",
    "directory":     "Directory / Listing",
    "podcast":       "Podcast Guest",
    "skyscraper":    "Skyscraper Target",
    "other":         "Other",
}


def dr_badge(dr):
    if dr is None or dr == 0:
        return '<span class="dr-badge dr-unknown">DR ?</span>'
    if dr >= 70:
        c = "#7c3aed"
    elif dr >= 50:
        c = "#0284c7"
    elif dr >= 30:
        c = "#059669"
    elif dr >= 15:
        c = "#d97706"
    else:
        c = "#6b7280"
    return f'<span class="dr-badge" style="background:{c}">{dr}</span>'


def tier_badge(tier):
    cfg = TIER_CONFIG.get(tier, TIER_CONFIG["long_game"])
    return (f'<span class="tier-badge" style="background:{cfg["bg"]};'
            f'color:{cfg["color"]};border:1px solid {cfg["border"]}">'
            f'{cfg["emoji"]} {cfg["label"]}</span>')


def type_label(t):
    return TYPE_LABELS.get(t, t.replace("_", " ").title())


def render_outreach_templates(opportunities):
    guest = [o for o in opportunities if o.get("type") == "guest_post"][:3]
    resource = [o for o in opportunities if o.get("type") == "resource_page"][:2]
    insertion = [o for o in opportunities if o.get("type") == "link_insertion"][:2]

    blocks = []

    if guest:
        blocks.append("""
<div class="template-card">
  <div class="template-title">📧 Guest Post Pitch Template</div>
  <div class="template-body">
Subject: Guest Post Pitch — [Your Topic Idea] for [Their Site Name]<br><br>
Hi [Editor Name],<br><br>
I came across [Their Site Name] while researching [niche] resources and loved your piece on [specific article]. 
Your audience seems really interested in [topic], and I'd love to contribute.<br><br>
I'm [brief 1-line credibility: your role/site/experience]. I'd like to pitch a guest post titled:<br>
&nbsp;&nbsp;→ "[Headline idea that delivers clear value]"<br><br>
Here's a quick outline: [3 bullet points of what the article covers]<br><br>
I can have a draft to you within [X] days and will promote it to my own audience of [X] readers/followers.<br><br>
Happy to send samples of my previous work. Does this sound like a fit?<br><br>
Best,<br>[Your name + site]
  </div>
</div>""")

    if resource:
        blocks.append("""
<div class="template-card">
  <div class="template-title">🔗 Resource Page Addition Template</div>
  <div class="template-body">
Subject: Suggestion for your [Niche] resources page<br><br>
Hi [Name],<br><br>
I noticed your resource page at [URL] — it's a great roundup of [niche] tools and guides.<br><br>
I wanted to suggest adding [Your Site Name] ([your URL]). We offer [1-sentence value prop that complements what's already on their page].<br><br>
It might be a useful addition for your readers looking for [specific benefit].<br><br>
Either way, keep up the great work — your resources page is genuinely one of the better ones I've found.<br><br>
Best,<br>[Your name]
  </div>
</div>""")

    if insertion:
        blocks.append("""
<div class="template-card">
  <div class="template-title">✏️ Link Insertion / Niche Edit Template</div>
  <div class="template-body">
Subject: Quick suggestion for your article on [Topic]<br><br>
Hi [Name],<br><br>
I just read your post "[Article Title]" at [URL] — solid piece, especially the section on [specific section].<br><br>
I noticed you mention [related topic] but don't link out to any resources there. We have a [guide/tool/article] 
at [your URL] that goes deep on exactly that — I think it would add real value for your readers.<br><br>
Would you be open to adding it? Happy to return the favour if there's ever anything I can help with on our end.<br><br>
Thanks,<br>[Your name + site]
  </div>
</div>""")

    return "\n".join(blocks)


def build_html(data: dict) -> str:
    target = data.get("target_site", {})
    competitors = data.get("competitors", [])
    opps = sorted(data.get("opportunities", []),
                  key=lambda o: (TIER_CONFIG.get(o.get("tier","long_game"),{}).get("order",9), -o.get("priority_score",0)))
    link_bait = data.get("link_bait_ideas", [])
    summary = data.get("summary", {})
    total = summary.get("total_opportunities", len(opps))
    qw = summary.get("quick_wins", sum(1 for o in opps if o.get("tier")=="quick_win"))
    hv = summary.get("high_value", sum(1 for o in opps if o.get("tier")=="high_value"))
    vp = summary.get("volume_plays", sum(1 for o in opps if o.get("tier")=="volume_play"))
    lg = summary.get("long_game", sum(1 for o in opps if o.get("tier")=="long_game"))
    now = datetime.now().strftime("%B %d, %Y")

    # Build competitor rows
    comp_rows = ""
    for c in competitors:
        comp_rows += f"""
      <tr>
        <td><a href="https://{c.get('domain','')}" target="_blank">{c.get('domain','—')}</a></td>
        <td>{dr_badge(c.get('dr'))}</td>
        <td>{c.get('referring_domains', '—'):,}</td>
        <td>{', '.join(d.get('domain','') for d in c.get('top_linking_domains',[])[:3]) or '—'}</td>
      </tr>"""

    # Build opportunity rows
    opp_rows = ""
    for o in opps:
        site_url = o.get("site_url", "")
        page_url = o.get("page_url", site_url)
        domain = site_url.replace("https://","").replace("http://","").split("/")[0]
        action = o.get("action","—")
        contact = o.get("contact","")
        contact_html = f'<br><small style="color:#6b7280">📬 {contact}</small>' if contact else ""
        notes = o.get("notes","")
        opp_rows += f"""
      <tr>
        <td>
          <a href="{page_url}" target="_blank" style="font-weight:600">{domain}</a>
          {contact_html}
        </td>
        <td>{tier_badge(o.get('tier',''))}</td>
        <td>{type_label(o.get('type',''))}</td>
        <td style="text-align:center">{dr_badge(o.get('site_dr'))}</td>
        <td style="text-align:center"><b style="color:#0284c7">{o.get('priority_score',0):.1f}</b></td>
        <td>{action}</td>
        <td style="font-size:0.8rem;color:#6b7280">{notes}</td>
      </tr>"""

    # Build link bait cards
    bait_cards = ""
    for idx, idea in enumerate(link_bait):
        bait_cards += f"""
    <div class="bait-card">
      <div class="bait-num">#{idx+1}</div>
      <div>
        <div class="bait-title">{idea.get('title','')}</div>
        <div class="bait-meta">{idea.get('format','')} &nbsp;|&nbsp; Effort: {idea.get('effort','')}</div>
        <div class="bait-rationale">{idea.get('rationale','')}</div>
      </div>
    </div>"""

    outreach = render_outreach_templates(opps)
    site_dr = target.get('dr')
    dr_display = dr_badge(site_dr) if site_dr else '<span class="dr-badge dr-unknown">DR ?</span>'
    site_url = target.get('url', '—')
    niche = target.get('niche', '—')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Backlink Opportunity Report — {site_url}</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #f8fafc; color: #1e293b; line-height: 1.6; }}
  a {{ color: #0284c7; text-decoration: none; }} a:hover {{ text-decoration: underline; }}

  .header {{ background: linear-gradient(135deg, #1e293b 0%, #334155 100%); color: white; padding: 2.5rem 3rem; }}
  .header h1 {{ font-size: 1.75rem; font-weight: 700; margin-bottom: 0.25rem; }}
  .header .sub {{ opacity: 0.7; font-size: 0.95rem; }}
  .header .meta {{ display: flex; gap: 2rem; margin-top: 1.25rem; flex-wrap: wrap; }}
  .header .meta-item {{ display: flex; flex-direction: column; }}
  .header .meta-label {{ font-size: 0.7rem; text-transform: uppercase; opacity: 0.6; letter-spacing: 0.05em; }}
  .header .meta-value {{ font-size: 1rem; font-weight: 600; }}

  .container {{ max-width: 1200px; margin: 0 auto; padding: 2rem 1.5rem; }}

  .stat-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1rem; margin-bottom: 2rem; }}
  .stat-card {{ background: white; border-radius: 12px; padding: 1.25rem 1.5rem; border: 1px solid #e2e8f0; }}
  .stat-card .stat-num {{ font-size: 2.25rem; font-weight: 800; }}
  .stat-card .stat-label {{ font-size: 0.8rem; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em; }}
  .stat-card.qw .stat-num {{ color: #ef4444; }}
  .stat-card.hv .stat-num {{ color: #7c3aed; }}
  .stat-card.vp .stat-num {{ color: #0284c7; }}
  .stat-card.lg .stat-num {{ color: #059669; }}

  .section {{ background: white; border-radius: 12px; padding: 1.75rem; border: 1px solid #e2e8f0; margin-bottom: 1.5rem; }}
  .section-title {{ font-size: 1.15rem; font-weight: 700; margin-bottom: 1.25rem; display: flex; align-items: center; gap: 0.5rem; }}

  table {{ width: 100%; border-collapse: collapse; font-size: 0.875rem; }}
  th {{ background: #f8fafc; padding: 0.6rem 0.8rem; text-align: left; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; border-bottom: 2px solid #e2e8f0; }}
  td {{ padding: 0.75rem 0.8rem; border-bottom: 1px solid #f1f5f9; vertical-align: top; }}
  tr:hover td {{ background: #f8fafc; }}

  .dr-badge {{ color: white; font-size: 0.7rem; font-weight: 700; padding: 2px 7px; border-radius: 999px; white-space: nowrap; }}
  .dr-unknown {{ background: #94a3b8; }}
  .tier-badge {{ font-size: 0.75rem; font-weight: 600; padding: 3px 10px; border-radius: 999px; white-space: nowrap; }}

  .roadmap {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }}
  .roadmap-col {{ border-radius: 10px; padding: 1.25rem; }}
  .roadmap-col.m30 {{ background: #fef2f2; border: 1px solid #fca5a5; }}
  .roadmap-col.m60 {{ background: #f5f3ff; border: 1px solid #c4b5fd; }}
  .roadmap-col.m90 {{ background: #f0fdf4; border: 1px solid #6ee7b7; }}
  .roadmap-col h3 {{ font-size: 0.9rem; font-weight: 700; margin-bottom: 0.75rem; }}
  .roadmap-col ul {{ list-style: none; }}
  .roadmap-col ul li {{ font-size: 0.85rem; padding: 0.3rem 0; padding-left: 1.25rem; position: relative; }}
  .roadmap-col ul li::before {{ content: "→"; position: absolute; left: 0; opacity: 0.5; }}

  .bait-card {{ display: flex; gap: 1rem; padding: 1rem; border: 1px solid #e2e8f0; border-radius: 10px; margin-bottom: 0.75rem; }}
  .bait-num {{ font-size: 1.5rem; font-weight: 800; color: #cbd5e1; min-width: 2rem; }}
  .bait-title {{ font-weight: 700; font-size: 0.95rem; margin-bottom: 0.2rem; }}
  .bait-meta {{ font-size: 0.75rem; color: #0284c7; margin-bottom: 0.4rem; }}
  .bait-rationale {{ font-size: 0.85rem; color: #475569; }}

  .template-card {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 1.25rem; margin-bottom: 1rem; }}
  .template-title {{ font-weight: 700; font-size: 0.9rem; margin-bottom: 0.75rem; color: #1e293b; }}
  .template-body {{ font-family: monospace; font-size: 0.8rem; color: #475569; line-height: 1.7; white-space: pre-wrap; background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e2e8f0; }}

  .legend {{ display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem; }}
  .legend-item {{ display: flex; align-items: center; gap: 0.4rem; font-size: 0.8rem; }}

  @media (max-width: 768px) {{
    .roadmap {{ grid-template-columns: 1fr; }}
    .header {{ padding: 1.5rem; }}
    table {{ font-size: 0.8rem; }}
  }}
</style>
</head>
<body>

<div class="header">
  <h1>🔗 Backlink Opportunity Report</h1>
  <div class="sub">AI-powered link building strategy — real opportunities from real tools</div>
  <div class="meta">
    <div class="meta-item"><span class="meta-label">Target Site</span><span class="meta-value">{site_url}</span></div>
    <div class="meta-item"><span class="meta-label">Niche</span><span class="meta-value">{niche}</span></div>
    <div class="meta-item"><span class="meta-label">Current DR</span><span class="meta-value">{site_dr if site_dr else "Unknown"}</span></div>
    <div class="meta-item"><span class="meta-label">Report Date</span><span class="meta-value">{now}</span></div>
    <div class="meta-item"><span class="meta-label">Total Opportunities</span><span class="meta-value">{total}</span></div>
  </div>
</div>

<div class="container">

  <!-- Stats -->
  <div class="stat-grid">
    <div class="stat-card"><div class="stat-num">{total}</div><div class="stat-label">Total Opportunities</div></div>
    <div class="stat-card qw"><div class="stat-num">{qw}</div><div class="stat-label">🔥 Quick Wins</div></div>
    <div class="stat-card hv"><div class="stat-num">{hv}</div><div class="stat-label">🎯 High Value</div></div>
    <div class="stat-card vp"><div class="stat-num">{vp}</div><div class="stat-label">📈 Volume Plays</div></div>
    <div class="stat-card lg"><div class="stat-num">{lg}</div><div class="stat-label">🌊 Long Game</div></div>
    <div class="stat-card"><div class="stat-num">{len(link_bait)}</div><div class="stat-label">💡 Link Bait Ideas</div></div>
  </div>

  <!-- Competitor Analysis -->
  <div class="section">
    <div class="section-title">🏆 Competitor Backlink Analysis</div>
    <table>
      <thead>
        <tr>
          <th>Domain</th>
          <th>DR</th>
          <th>Referring Domains</th>
          <th>Top Linking Domains (sample)</th>
        </tr>
      </thead>
      <tbody>
        {comp_rows if comp_rows else '<tr><td colspan="4" style="text-align:center;color:#94a3b8;padding:2rem">No competitor data collected</td></tr>'}
      </tbody>
    </table>
  </div>

  <!-- Priority Opportunities -->
  <div class="section">
    <div class="section-title">📋 Prioritized Backlink Opportunities</div>
    <div class="legend">
      <div class="legend-item">{tier_badge("quick_win")} Do this week</div>
      <div class="legend-item">{tier_badge("high_value")} Month 1-2</div>
      <div class="legend-item">{tier_badge("volume_play")} Scale up</div>
      <div class="legend-item">{tier_badge("long_game")} 3-6 months</div>
    </div>
    <div style="overflow-x:auto">
    <table>
      <thead>
        <tr>
          <th>Site</th>
          <th>Tier</th>
          <th>Type</th>
          <th>DR</th>
          <th>Score</th>
          <th>Action</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>
        {opp_rows if opp_rows else '<tr><td colspan="7" style="text-align:center;color:#94a3b8;padding:2rem">No opportunities found — check the JSON input</td></tr>'}
      </tbody>
    </table>
    </div>
  </div>

  <!-- 30/60/90 Day Roadmap -->
  <div class="section">
    <div class="section-title">🗓️ 30 / 60 / 90 Day Roadmap</div>
    <div class="roadmap">
      <div class="roadmap-col m30">
        <h3>🔥 Days 1–30: Quick Wins</h3>
        <ul>
          <li>Submit to all relevant directories (Crunchbase, Product Hunt, G2, niche dirs)</li>
          <li>Email resource page owners with your URL</li>
          <li>Pitch top {min(qw,5)} Quick Win guest post sites</li>
          <li>Claim any unlinked brand mentions</li>
          <li>Apply to 3–5 podcasts in your niche</li>
        </ul>
      </div>
      <div class="roadmap-col m60">
        <h3>🎯 Days 31–60: High Value</h3>
        <ul>
          <li>Publish first link bait content piece</li>
          <li>Follow up on Month 1 pitches</li>
          <li>Pitch {hv} High Value sites with tailored pitches</li>
          <li>Reach out for link insertions in existing articles</li>
          <li>Start building relationships with top-tier editors</li>
        </ul>
      </div>
      <div class="roadmap-col m90">
        <h3>🌊 Days 61–90: Scale & Long Game</h3>
        <ul>
          <li>Scale volume plays (batch-submit to 20+ sites)</li>
          <li>Publish second link bait piece targeting competitor links</li>
          <li>Pitch Long Game targets with warm relationship</li>
          <li>Re-audit: run competitors through Ahrefs again for new link sources</li>
          <li>Target DR uplift: expect +3–8 DR points by end of 90 days</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Link Bait Ideas -->
  {'<div class="section"><div class="section-title">💡 Link Bait Content Strategy</div>' + bait_cards + '</div>' if link_bait else ''}

  <!-- Outreach Templates -->
  <div class="section">
    <div class="section-title">📧 Outreach Email Templates</div>
    {outreach if outreach else '<p style="color:#94a3b8">No template opportunities identified.</p>'}
  </div>

  <div style="text-align:center;padding:2rem;color:#94a3b8;font-size:0.8rem">
    Generated by Claude Backlink Opportunity Skill · {now} · Data sourced from live tools (Ahrefs, Open Link Profiler, Semrush, Moz)
  </div>

</div>
</body>
</html>"""

    return html


def main():
    parser = argparse.ArgumentParser(description="Generate backlink opportunity HTML report")
    parser.add_argument("--input", required=True, help="Path to backlink_findings.json")
    parser.add_argument("--output", required=True, help="Path for output HTML report")
    args = parser.parse_args()

    try:
        with open(args.input, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in input file: {e}", file=sys.stderr)
        sys.exit(1)

    html = build_html(data)
    with open(args.output, "w") as f:
        f.write(html)

    opp_count = len(data.get("opportunities", []))
    print(f"✅ Report generated: {args.output}")
    print(f"   {opp_count} opportunities | {len(data.get('link_bait_ideas',[]))} link bait ideas")


if __name__ == "__main__":
    main()
