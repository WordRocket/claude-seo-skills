#!/usr/bin/env python3
"""
Core/Spam Update Recovery — Chart Generator
Generates all charts needed for the recovery report as base64-encoded PNG images.
Output is a JSON file with chart names as keys and base64 strings as values.

Usage:
  python generate_charts.py \
    --output /path/to/charts.json \
    --site-name "ranksite.ai" \
    --months "Jan,Feb,Mar,Apr,May,Jun,Jul" \
    --traffic "12000,11500,7200,6800,7900,9600,11200" \
    --update-months "Mar,May,Jun" \
    --update-labels "Mar Core,May Core,Jun Spam" \
    --recovery-score 62 \
    --factor-names "Content freshness,Topical authority,E-E-A-T,Local/structured pages,Off-platform signals,Backlinks,Technical/CWV" \
    --factor-scores "80,75,70,85,55,60,65" \
    --before-trough-now "12000,6800,11200"
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
    import numpy as np
except ImportError:
    print("Installing matplotlib...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "matplotlib", "numpy", "--break-system-packages", "-q"])
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np

# ── Color palette (matches skill design system) ─────────────────────────────
NAVY   = "#1A2E4A"
TEAL   = "#0D9488"
AMBER  = "#F59E0B"
RED    = "#EF4444"
GREEN  = "#22C55E"
PURPLE = "#7C3AED"
LGRAY  = "#F0F4F8"
WHITE  = "#FFFFFF"


def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', dpi=130, facecolor=WHITE)
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return encoded


def traffic_timeline_chart(site_name, months, traffic, update_months, update_labels):
    """Line chart of traffic over time with vertical markers on update rollout months."""
    fig, ax = plt.subplots(figsize=(11, 4.5))
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(LGRAY)

    x = np.arange(len(months))
    ax.plot(x, traffic, color=TEAL, linewidth=2.5, marker='o', markersize=5, zorder=4)
    ax.fill_between(x, traffic, min(traffic) * 0.9, color=TEAL, alpha=0.08, zorder=2)

    # Mark trough
    trough_idx = int(np.argmin(traffic))
    ax.scatter([x[trough_idx]], [traffic[trough_idx]], color=RED, s=90, zorder=5, edgecolor=WHITE, linewidth=1.5)
    ax.annotate("Trough", (x[trough_idx], traffic[trough_idx]),
                textcoords="offset points", xytext=(0, -22), ha='center', fontsize=9, color=RED, fontweight='bold')

    # Update rollout markers
    label_map = dict(zip(update_months, update_labels)) if update_labels else {}
    for um in update_months:
        if um in months:
            idx = months.index(um)
            ax.axvline(x=idx, color=PURPLE, linestyle='--', linewidth=1.3, alpha=0.7, zorder=3)
            lbl = label_map.get(um, um)
            ax.text(idx, max(traffic) * 1.04, lbl, rotation=90, fontsize=8, color=PURPLE,
                    ha='right', va='top', fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(months, fontsize=9)
    ax.set_ylabel("Organic Traffic", fontsize=10, color="#444")
    ax.set_title(f"{site_name} — Organic Traffic vs. Google Update Timeline", fontsize=13, fontweight='bold', color=NAVY, pad=14)
    ax.yaxis.grid(True, color='#ddd', linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#ccc')
    ax.spines['bottom'].set_color('#ccc')
    ax.tick_params(colors='#555', labelsize=9)
    ax.set_ylim(bottom=0)

    plt.tight_layout()
    return fig_to_base64(fig)


def recovery_factor_scorecard(factor_names, factor_scores):
    """Horizontal bar chart scoring the site against known recovery factors (0-100)."""
    paired = sorted(zip(factor_names, factor_scores), key=lambda p: p[1])
    names_s, scores_s = zip(*paired)

    def score_color(s):
        if s >= 75: return GREEN
        if s >= 50: return AMBER
        return RED

    colors = [score_color(s) for s in scores_s]

    fig, ax = plt.subplots(figsize=(9, max(3, len(names_s) * 0.6 + 1)))
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(LGRAY)

    bars = ax.barh(names_s, scores_s, color=colors, height=0.55, zorder=3)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Strength Score (0–100)", fontsize=10, color="#444")
    ax.set_title("Recovery Factor Scorecard", fontsize=13, fontweight='bold', color=NAVY, pad=12)
    ax.xaxis.grid(True, color='#ddd', linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#ccc')
    ax.spines['bottom'].set_color('#ccc')
    ax.tick_params(colors='#555', labelsize=9)

    for bar, val in zip(bars, scores_s):
        ax.text(min(bar.get_width() + 1.5, 97), bar.get_y() + bar.get_height() / 2,
                str(int(val)), va='center', ha='left', fontsize=9, color='#333', fontweight='bold')

    plt.tight_layout()
    return fig_to_base64(fig)


def before_trough_now_chart(labels, values):
    """Simple 3-bar comparison: before drop / trough / now."""
    colors = [NAVY, RED, TEAL]
    fig, ax = plt.subplots(figsize=(5.5, 4))
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(LGRAY)

    bars = ax.bar(labels, values, color=colors, width=0.5, zorder=3)
    ax.set_ylabel("Organic Traffic", fontsize=10, color="#444")
    ax.set_title("Before → Trough → Now", fontsize=13, fontweight='bold', color=NAVY, pad=12)
    ax.yaxis.grid(True, color='#ddd', linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#ccc')
    ax.spines['bottom'].set_color('#ccc')
    ax.tick_params(colors='#555', labelsize=10)

    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(values) * 0.02,
                f"{val:,.0f}", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#333')

    # % recovered annotation
    if values[1] != values[0]:
        pct_of_loss_recovered = (values[2] - values[1]) / max(abs(values[0] - values[1]), 1) * 100
        ax.text(0.5, 0.92, f"{pct_of_loss_recovered:.0f}% of the drop recovered so far",
                transform=ax.transAxes, ha='center', fontsize=9.5, color=TEAL, fontweight='bold')

    plt.tight_layout()
    return fig_to_base64(fig)


def recovery_gauge(score):
    """Semicircular gauge chart for overall recovery trajectory score."""
    fig, ax = plt.subplots(figsize=(5, 3), subplot_kw=dict(polar=False))
    fig.patch.set_facecolor(WHITE)
    ax.set_aspect('equal')
    ax.axis('off')

    theta = np.linspace(np.pi, 0, 200)
    r = 1.0
    ax.plot(r * np.cos(theta), r * np.sin(theta), color='#E5E7EB', linewidth=18, solid_capstyle='round')

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
    ax.text(0, -0.2, 'Recovery Trajectory Score', ha='center', va='center',
            fontsize=11, color='#555')
    ax.text(0, -0.45, '/ 100', ha='center', va='center',
            fontsize=11, color='#999')

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-0.6, 1.2)
    plt.tight_layout()
    return fig_to_base64(fig)


def parse_args():
    p = argparse.ArgumentParser(description='Generate core/spam update recovery charts as base64 PNG')
    p.add_argument('--output', required=True)
    p.add_argument('--site-name', default='Your Site')
    p.add_argument('--months', required=True, help='Comma-separated month labels, chronological')
    p.add_argument('--traffic', required=True, help='Comma-separated traffic values, same length as --months')
    p.add_argument('--update-months', default='', help='Comma-separated subset of --months where an update rolled out')
    p.add_argument('--update-labels', default='', help='Comma-separated labels matching --update-months, e.g. "May Core,Jun Spam"')
    p.add_argument('--recovery-score', type=float, default=50)
    p.add_argument('--factor-names', required=True, help='Comma-separated recovery factor names')
    p.add_argument('--factor-scores', required=True, help='Comma-separated 0-100 scores matching --factor-names')
    p.add_argument('--before-trough-now', required=True, help='Comma-separated 3 values: before,trough,now')
    return p.parse_args()


def main():
    args = parse_args()

    months = [m.strip() for m in args.months.split(',')]
    traffic = [float(v) for v in args.traffic.split(',')]
    update_months = [m.strip() for m in args.update_months.split(',')] if args.update_months else []
    update_labels = [m.strip() for m in args.update_labels.split(',')] if args.update_labels else []
    factor_names = [f.strip() for f in args.factor_names.split(',')]
    factor_scores = [float(v) for v in args.factor_scores.split(',')]
    btn = [float(v) for v in args.before_trough_now.split(',')]

    charts = {}

    print("Generating traffic timeline chart...")
    charts['timeline_chart'] = traffic_timeline_chart(args.site_name, months, traffic, update_months, update_labels)

    print("Generating recovery factor scorecard...")
    charts['scorecard_chart'] = recovery_factor_scorecard(factor_names, factor_scores)

    print("Generating before/trough/now chart...")
    charts['btn_chart'] = before_trough_now_chart(['Before drop', 'Trough', 'Now'], btn)

    print("Generating recovery gauge...")
    charts['gauge_chart'] = recovery_gauge(args.recovery_score)

    with open(args.output, 'w') as f:
        json.dump(charts, f)

    total_kb = sum(len(v) for v in charts.values()) // 1024
    print(f"\n✓ Generated {len(charts)} charts → {args.output} ({total_kb} KB total)")


if __name__ == '__main__':
    main()
