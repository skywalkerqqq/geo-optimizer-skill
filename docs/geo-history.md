# GEO History

`geo history` shows the saved GEO score trend for a URL from the local tracking database.

---

## What It Does

- Reads saved snapshots from `~/.geo-optimizer/tracking.db`
- Shows score trend over time with deltas vs previous snapshot
- Surfaces best score, worst score, and regression status
- Works well with `geo audit --save-history`, `geo audit --regression`, and `geo track`

---

## Usage

```bash
# Show saved trend for a URL
geo history --url https://yoursite.com

# JSON output
geo history --url https://yoursite.com --format json

# Limit to the latest 20 snapshots
geo history --url https://yoursite.com --limit 20
```

---

## Flags

| Flag | Required | Description |
|------|----------|-------------|
| `--url` | Yes | URL whose saved trend should be displayed |
| `--format` | No | `text` (default) or `json` |
| `--limit` | No | Maximum snapshots to show (default: `12`) |
| `--retention-days` | No | Retention window applied before reading history (default: `90`) |
| `--output` | No | Write the report to a file |

---

## Example Output

```text
GEO HISTORY — SCORE TREND

URL: https://example.com/
Snapshots: 4 | Retention: 90 days
Latest: 81/100 (GOOD) | Delta vs previous: +6
Best: 81/100 | Worst: 63/100

2026-04-13   81/100  GOOD        +6  ████████████████████
2026-04-06   75/100  GOOD        +8  ██████████████████
2026-03-30   67/100  FOUNDATION  +4  ████████████████
2026-03-23   63/100  FOUNDATION   —  ███████████████
```

---

## Related Commands

- [`geo audit`](geo-audit.md): save snapshots with `--save-history` or gate CI with `--regression`
- [`geo track`](geo-track.md): run a new audit, persist it, and optionally generate an HTML report
- [`CI/CD Integration`](ci-cd.md): use regression detection in pipelines
