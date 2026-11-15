"""
Radar chart thumbnail for the "AI Safety and Ethics" section of the interests page.

Source: "Investigating Political and Demographic Associations in Large Language Models
Through Moral Foundations Theory" (AIES 2025), Table 2 (page 9 of Moral-LLMs.pdf).

The paper does not report absolute mean scores per group, only the mean difference M
between aggregated LLM responses and the human responses of Graham, Haidt & Nosek (2009).
So the chart plots M directly: larger values mean the LLMs agreed with that foundation
more strongly than humans of the same alignment, and negative values mean they agreed less.

Sign convention (checked against the RQ4 rows of Table 2): in "Human v. X", M = X - Human.
E.g. Purity, liberal: Explicit - Inherent = 0.027 - 1.695 = -1.668, which matches the
reported "Inherent v. Explicit" value.

Usage:
    pip install matplotlib numpy
    python moral_foundations_radar.py                       # persona prompting (default)
    python moral_foundations_radar.py --condition explicit  # explicit liberal/conservative prompting
"""

import argparse

import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------------------------
# Data transcribed from Table 2 (mean difference M, LLM minus human).
# Significance stars from the table are kept in comments.
# ---------------------------------------------------------------------------
TABLE2_M = {
    # RQ1: Human v. Inherent (model given no political alignment, compared to each human group)
    "inherent": {
        "liberal": {
            "Ingroup": 0.950,  # ***
            "Fairness": 0.293,  # ***
            "Purity": 1.695,  # ***
            "Authority": 1.297,  # ***
            "Harm": 0.176,  # *
        },
        "conservative": {
            "Ingroup": 0.664,  # ***
            "Fairness": 0.966,  # ***
            "Purity": 0.654,  # ***
            "Authority": 0.480,  # ***
            "Harm": 0.729,  # ***
        },
    },
    # RQ2: Human v. Explicit (model told to answer as a liberal / conservative)
    "explicit": {
        "liberal": {
            "Ingroup": 0.195,  # **
            "Fairness": 0.093,  # n.s.
            "Purity": 0.027,  # n.s.
            "Authority": -0.290,  # ***
            "Harm": 0.217,  # **
        },
        "conservative": {
            "Ingroup": 0.796,  # ***
            "Fairness": 0.625,  # ***
            "Purity": -0.490,  # ***
            "Authority": 0.439,  # ***
            "Harm": 0.798,  # ***
        },
    },
    # RQ3: Human v. Persona (model told to role-play a liberal / conservative persona)
    "persona": {
        "liberal": {
            "Ingroup": 0.164,  # ***
            "Fairness": 0.066,  # n.s.
            "Purity": 0.151,  # ***
            "Authority": 0.540,  # ***
            "Harm": 0.287,  # ***
        },
        "conservative": {
            "Ingroup": 1.134,  # ***
            "Fairness": 0.287,  # ***
            "Purity": 1.379,  # ***
            "Authority": 1.384,  # ***
            "Harm": 0.560,  # ***
        },
    },
}

# Order around the circle, clockwise from the top. Fairness sits at the top and Harm at the
# upper right so that no label overlaps the plot border.
FOUNDATIONS = ["Fairness", "Harm", "Ingroup", "Authority", "Purity"]

# Colours match the paper's figures (blue = liberal, red = conservative)
COLOURS = {"liberal": "#1f77b4", "conservative": "#d62728"}

TITLES = {
    "inherent": "Moral Foundations of Unprompted LLMs vs. Humans",
    "explicit": "Moral Foundations of Explicitly Prompted LLMs vs. Humans",
    "persona": "Moral Foundations of LLM Personas vs. Humans",
}


def radar(condition: str, out: str) -> None:
    data = TABLE2_M[condition]
    n = len(FOUNDATIONS)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]  # close the loop

    # Radial range covers every value in Table 2 so all conditions share one scale
    all_vals = [v for cond in TABLE2_M.values() for grp in cond.values() for v in grp.values()]
    rmin = np.floor(min(all_vals) * 2) / 2 - 0.25  # -0.75
    rmax = np.ceil(max(all_vals) * 2) / 2  # 2.0

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"polar": True})
    ax.set_theta_offset(np.pi / 2)  # first foundation at the top
    ax.set_theta_direction(-1)  # clockwise
    ax.set_ylim(rmin, rmax)

    for group in ["liberal", "conservative"]:
        vals = [data[group][f] for f in FOUNDATIONS]
        vals += vals[:1]
        ax.plot(angles, vals, color=COLOURS[group], linewidth=2.5, marker="o",
                label=f"{group.capitalize()} LLM responses")
        ax.fill(angles, vals, color=COLOURS[group], alpha=0.15)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(FOUNDATIONS, fontsize=14)
    ax.tick_params(axis="x", pad=12)
    ticks = [t for t in np.arange(-0.5, rmax + 0.01, 0.5)]
    ax.set_yticks(ticks)
    ax.set_yticklabels([f"{t:+.1f}" if t else "0" for t in ticks], fontsize=9, color="grey")
    ax.set_rlabel_position(180 / n)  # put radial labels between two spokes

    ax.set_title(TITLES[condition], fontsize=14, pad=52)
    # Reading guide, centred under the title. Positioned relative to the top of the plot (in
    # points) so it stays between the title and the top spoke label at any figure size.
    ax.annotate("Outward = valued more than humans", xy=(0.5, 1), xycoords="axes fraction",
                xytext=(0, 48), textcoords="offset points", ha="center", va="top",
                fontsize=10, style="italic", color="dimgrey")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=2, frameon=False, fontsize=10)

    fig.tight_layout()
    fig.savefig(out, dpi=300, bbox_inches="tight")
    print(f"Saved {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--condition", choices=TABLE2_M.keys(), default="persona")
    parser.add_argument("--out", default=None, help="output file (default: moral_radar_<condition>.png)")
    args = parser.parse_args()
    radar(args.condition, args.out or f"moral_radar_{args.condition}.png")
