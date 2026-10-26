"""One-off migration: replace English copy in manifesto.html with __I18N_*__
placeholders, matching the dict keys in ``manifest_i18n._M_EN``.

Strategy: build a long→short sorted list of (literal, key) pairs, replace
each English literal with its token exactly once. Ambiguous collisions (same
literal mapped to multiple keys) are reported as a warning. After the pass,
the dict literal is the single source of truth and English strings no longer
appear in the rendered template (assuming every literal was unique enough).

Run from the repo root via:
    python -m geo_optimizer.web._manifest_migrate
"""

import collections
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
TPL = ROOT / "templates" / "manifesto.html"

sys.path.insert(0, str(ROOT.parent))  # so `geo_optimizer.web.manifest_i18n` resolves
from geo_optimizer.web.manifest_i18n import PAGES  # noqa: E402

M_EN = PAGES["manifesto.html"]["en"]


def find_overlaps(strings: list[str]):
    """Return groups of (string, occurrences_in_template) for each key whose
    literal exists in the template."""
    pass


def main():
    html = TPL.read_text(encoding="utf-8")

    # 1) Sort by length DESC so longer (more specific) literals are replaced
    #    first. This avoids collisions like "GitHub" being replaced before
    #    "GitHub Star".
    keys_by_len = sorted(
        ((k, v) for k, v in M_EN.items() if isinstance(v, str) and v),
        key=lambda kv: len(kv[1]),
        reverse=True,
    )

    total_replaced = 0
    misses = []
    ambiguous = []
    for key, en_value in keys_by_len:
        token = "__I18N_" + key.upper() + "__"
        if en_value not in html:
            misses.append((key, en_value[:60]))
            continue
        # Track how many times it would be replaced; if it duplicates we
        # warn (template has the same English literal twice or more — fine
        # but worth a note).
        count = html.count(en_value)
        if count > 1:
            ambiguous.append((key, en_value[:60], count))
        html = html.replace(en_value, token)
        total_replaced += count

    print(f"replaced: {total_replaced}")
    print(f"missed ({len(misses)}):")
    for k, v in misses:
        print(f"  MISSING {k}: {v!r}")
    print(f"ambiguous repeats ({len(ambiguous)}):")
    for k, v, c in ambiguous:
        print(f"  REPEAT {c}x {k}: {v!r}")

    TPL.write_text(html, encoding="utf-8")
    print("wrote", TPL)


if __name__ == "__main__":
    main()
