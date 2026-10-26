#!/usr/bin/env python3
"""
SEO Audit Chart Generator
Generates all charts needed for the SEO audit HTML report as base64-encoded PNG images.
Output is a JSON file with chart names as keys and base64 strings as values.

Usage:
  python generate_charts.py \
    --output /path/to/charts.json \
    --site-name "My Site" \
    --competitors "Comp A,Comp B,Comp C,Comp D" \
    --traffic "1200,8500,5200,3100,2400" \
    --da "22,48,41,35,29" \
    --pagespeed-mobile "58" \
    --pagespeed-desktop "81" \
    --issue-counts "5,8,6"
"""

import argparse
import base64
import json
import io
import sys

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import numpy as np
except ImportError:
    print("Installing matplotlib...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "matplotlib", "numpy", "--break-system-packages", "-q"])
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import numpy as np

# ── Color palette ──────────────────────────────────────────────────────────────
NAVY   = "#1A3C6E"
TEAL   = "#0D9488"
AMBER  = "#F59E0B"
RED    = "#EF4444"
GREEN  = "#22C55E"
LGRAY  = "#F0F4F8"
WHITE  = "#FFFFFF"
COLORS = [TEAL, "#2563EB", "#7C3AED", AMBER, RED]

def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', dpi=130, facecolor=WHITE)
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return encoded


def traffic_comparison_chart(site_name, competitors, traffic_values):
    """Horizontal bar chart comparing estimated organic traffic."""
    labels = [site_name] + competitors
    values = traffic_values
    bar_colors = [TEAL] + [COLORS[i % len(COLORS)] for i in range(1, len(competitors) + 1)]
    # Sort descending
    paired = sorted(zip(values, labels, bar_colors), reverse=True)
    values_s, labels_s, colors_s = zip(*paired)

    fig, ax = plt.subplots(figsize=(9, max(3, len(labels) * 0.7 + 1)))
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(LGRAY)

    bars = ax.barh(labels_s, values_s, color=colors_s, height=0.55, zorder=3)
    ax.set_xlabel("Estimated Monthly Organic Visits", fontsize=10, color="#444")
    ax.set_title("Organic Traffic Comparison", fontsize=13, fontweight='bold', color=NAVY, pad=12)
    ax.xaxis.grid(True, color='#ddd', linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#ccc')
    ax.spines['bottom'].set_color('#ccc')
    ax.tick_params(colors='#555', labelsize=9)

    for bar, val in zip(bars, values_s):
        ax.text(bar.get_width() + max(values_s) * 0.01, bar.get_y() + bar.get_height() / 2,
                f"{val:,}", va='center', ha='left', fontsize=9, color='#333')

    plt.tight_layout()
    return fig_to_base64(fig)


def da_comparison_chart(site_name, competitors, da_values):
    """Horizontal bar chart comparing Domain Authority scores."""
    labels = [site_name] + competitors
    bar_colors = [TEAL] + [COLORS[i % len(COLORS)] for i in range(1, len(competitors) + 1)]
    paired = sorted(zip(da_values, labels, bar_colors), reverse=True)
    values_s, labels_s, colors_s = zip(*paired)

    fig, ax = plt.subplots(figsize=(9, max(3, len(labels) * 0.7 + 1)))
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(LGRAY)

    bars = ax.barh(labels_s, values_s, color=colors_s, height=0.55, zorder=3)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Domain Authority (0–100)", fontsize=10, color="#444")
    ax.set_title("Domain Authority Comparison", fontsize=13, fontweight='bold', color=NAVY, pad=12)
    ax.xaxis.grid(True, color='#ddd', linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#ccc')
    ax.spines['bottom'].set_color('#ccc')
    ax.tick_params(colors='#555', labelsize=9)

    for bar, val in zip(bars, values_s):
        ax.text(min(bar.get_width() + 1.5, 98), bar.get_y() + bar.get_height() / 2,
                str(int(val)), va='center', ha='left', fontsize=9, color='#333')

    plt.tight_layout()
    return fig_to_base64(fig)


def pagespeed_chart(mobile_score, desktop_score):
    """Grouped bar chart for PageSpeed scores."""
    categories = ['Mobile', 'Desktop']
    scores = [mobile_score, desktop_score]

    def score_color(s):
        if s >= 90: return GREEN
        if s >= 50: return AMBER
        return RED

    colors = [score_color(s) for s in scores]

    fig, ax = plt.subplots(figsize=(5, 3.5))
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(LGRAY)

    bars = ax.bar(categories, scores, color=colors, width=0.45, zorder=3)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Score (0–100)", fontsize=10, color="#444")
    ax.set_title("PageSpeed Scores", fontsize=13, fontweight='bold', color=NAVY, pad=12)
    ax.yaxis.grid(True, color='#ddd', linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#ccc')
    ax.spines['bottom'].set_color('#ccc')
    ax.tick_params(colors='#555', labelsize=10)

    # Threshold lines
    ax.axhline(y=90, color=GREEN, linestyle='--', linewidth=1, alpha=0.7)
    ax.axhline(y=50, color=AMBER, linestyle='--', linewidth=1, alpha=0.7)
    ax.text(1.45, 91, 'Good (90+)', fontsize=7, color=GREEN)
    ax.text(1.45, 51, 'Needs Work (50+)', fontsize=7, color=AMBER)

    for bar, val in zip(bars, scores):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.5,
                str(int(val)), ha='center', va='bottom', fontsize=13, fontweight='bold', color='#333')

    plt.tight_layout()
    return fig_to_base64(fig)


def issue_priority_matrix(critical, warning, low):
    """Horizontal stacked bar showing issue distribution by priority."""
    categories = ['SEO Issues Found']
    crit_vals = [critical]
    warn_vals = [warning]
    low_vals  = [low]

    fig, ax = plt.subplots(figsize=(8, 2.2))
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(WHITE)

    b1 = ax.barh(categories, crit_vals, color=RED, height=0.4, label=f'Critical ({critical})', zorder=3)
    b2 = ax.barh(categories, warn_vals, left=crit_vals, color=AMBER, height=0.4, label=f'Warning ({warning})', zorder=3)
    b3 = ax.barh(categories, low_vals, left=[c + w for c, w in zip(crit_vals, warn_vals)],
                 color=GREEN, height=0.4, label=f'Low ({low})', zorder=3)

    ax.set_xlim(0, critical + warning + low + 2)
    ax.set_title("Issue Priority Distribution", fontsize=12, fontweight='bold', color=NAVY, pad=8)
    ax.legend(loc='lower right', fontsize=9, framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#ccc')
    ax.set_yticks([])
    ax.tick_params(colors='#555', labelsize=9)

    plt.tight_layout()
    return fig_to_base64(fig)


def reviews_comparison_chart(site_name, competitors, review_data):
    """
    Bar chart comparing review counts and ratings.
    review_data: list of (count, rating) tuples — one per site (target first)
    """
    labels = [site_name] + competitors
    counts = [r[0] for r in review_data]
    ratings = [r[1] for r in review_data]

    x = np.arange(len(labels))
    width = 0.38

    fig, ax1 = plt.subplots(figsize=(9, 4))
    fig.patch.set_facecolor(WHITE)
    ax1.set_facecolor(LGRAY)

    bar_colors = [TEAL] + [COLORS[i % len(COLORS)] for i in range(1, len(competitors) + 1)]
    bars = ax1.bar(x - width / 2, counts, width, color=bar_colors, label='Review Count', zorder=3, alpha=0.85)

    ax2 = ax1.twinx()
    ax2.plot(x + width / 2, ratings, 'o-', color=AMBER, linewidth=2, markersize=7, label='Avg Rating', zorder=4)
    ax2.set_ylim(0, 5.5)
    ax2.set_ylabel("Avg Star Rating", fontsize=10, color=AMBER)
    ax2.tick_params(colors=AMBER, labelsize=9)

    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, fontsize=9, rotation=15, ha='right')
    ax1.set_ylabel("Review Count", fontsize=10, color="#444")
    ax1.set_title("Reviews & Ratings Comparison", fontsize=13, fontweight='bold', color=NAVY, pad=12)
    ax1.yaxis.grid(True, color='#ddd', linewidth=0.7, zorder=0)
    ax1.set_axisbelow(True)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='upper right')

    plt.tight_layout()
    return fig_to_base64(fig)


def seo_health_gauge(score):
    """Semicircular gauge chart for overall SEO health score."""
    fig, ax = plt.subplots(figsize=(5, 3), subplot_kw=dict(polar=False))
    fig.patch.set_facecolor(WHITE)
    ax.set_aspect('equal')
    ax.axis('off')

    # Background arc (gray)
    theta = np.linspace(np.pi, 0, 200)
    r = 1.0
    ax.plot(r * np.cos(theta), r * np.sin(theta), color='#E5E7EB', linewidth=18, solid_capstyle='round')

    # Colored arc (score portion)
    score_theta = np.linspace(np.pi, np.pi - (score / 100) * np.pi, 200)
    if score >= 70:
        arc_color = GREEN
    elif score >= 40:
        arc_color = AMBER
    else:
        arc_color = RED

    ax.plot(r * np.cos(score_theta), r * np.sin(score_theta),
            color=arc_color, linewidth=18, solid_capstyle='round')

    ax.text(0, 0.15, str(int(score)), ha='center', va='center',
            fontsize=38, fontweight='bold', color=NAVY)
    ax.text(0, -0.2, 'SEO Health Score', ha='center', va='center',
            fontsize=11, color='#555')
    ax.text(0, -0.45, '/ 100', ha='center', va='center',
            fontsize=11, color='#999')

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-0.6, 1.2)
    plt.tight_layout()
    return fig_to_base64(fig)


# ── Main ───────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description='Generate SEO audit charts as base64 PNG')
    p.add_argument('--output', required=True, help='Output JSON file path')
    p.add_argument('--site-name', default='Target Site')
    p.add_argument('--competitors', default='Competitor 1,Competitor 2,Competitor 3,Competitor 4')
    p.add_argument('--traffic', default='1000,5000,3000,2000,1500',
                   help='Comma-separated traffic estimates: target,c1,c2,c3,c4')
    p.add_argument('--da', default='20,45,38,30,25',
                   help='Comma-separated DA scores: target,c1,c2,c3,c4')
    p.add_argument('--pagespeed-mobile', type=float, default=55)
    p.add_argument('--pagespeed-desktop', type=float, default=78)
    p.add_argument('--issue-counts', default='4,7,5',
                   help='critical,warning,low issue counts')
    p.add_argument('--reviews', default='',
                   help='Comma-separated count:rating pairs e.g. "120:4.5,340:4.8,89:4.2"')
    p.add_argument('--seo-score', type=float, default=42,
                   help='Overall SEO health score 0-100')
    return p.parse_args()


def main():
    args = parse_args()

    comps = [c.strip() for c in args.competitors.split(',')]
    traffic = [float(v) for v in args.traffic.split(',')]
    da = [float(v) for v in args.da.split(',')]
    issues = [int(v) for v in args.issue_counts.split(',')]

    charts = {}

    print("Generating traffic comparison chart...")
    charts['traffic_chart'] = traffic_comparison_chart(
        args.site_name, comps,
        [traffic[0]] + traffic[1:len(comps)+1]
    )

    print("Generating DA comparison chart...")
    charts['da_chart'] = da_comparison_chart(
        args.site_name, comps,
        [da[0]] + da[1:len(comps)+1]
    )

    print("Generating PageSpeed chart...")
    charts['pagespeed_chart'] = pagespeed_chart(args.pagespeed_mobile, args.pagespeed_desktop)

    print("Generating issue priority matrix...")
    charts['issue_matrix'] = issue_priority_matrix(*issues[:3])

    print("Generating SEO health gauge...")
    charts['seo_gauge'] = seo_health_gauge(args.seo_score)

    if args.reviews:
        print("Generating reviews comparison chart...")
        review_data = []
        for pair in args.reviews.split(','):
            count, rating = pair.strip().split(':')
            review_data.append((int(count), float(rating)))
        while len(review_data) < len(comps) + 1:
            review_data.append((0, 0.0))
        charts['reviews_chart'] = reviews_comparison_chart(
            args.site_name, comps[:len(review_data)-1], review_data
        )

    with open(args.output, 'w') as f:
        json.dump(charts, f)

    total_kb = sum(len(v) for v in charts.values()) // 1024
    print(f"\n✓ Generated {len(charts)} charts → {args.output} ({total_kb} KB total)")


if __name__ == '__main__':
    main()
