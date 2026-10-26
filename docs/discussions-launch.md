# GitHub Discussions — launch plan

Enabling is a repo-settings click (Settings → General → Features → Discussions).
Once enabled, configure these categories (Settings → Discussions → pencil icons),
then post the welcome below in **Announcements**.

## Categories

| Category | Format | Purpose |
|---|---|---|
| 📣 Announcements | Announcement (maintainers post, all comment) | Releases, roadmap shifts, State of GEO drops |
| 💬 General | Open discussion | Anything GEO/AI-visibility |
| 🙏 Q&A | Question/Answer (mark answers) | "How do I…" support — deflects issues |
| 💡 Ideas | Open discussion | Feature proposals before they become issues |
| 🏆 Show & tell | Open discussion | Score improvements, before/after, badges |

Keep **Issues for confirmed bugs only**; route everything else here (add a note
in the issue templates later).

## Welcome post (paste in Announcements)

Title: `Welcome — let's make the web readable for AI engines`

```markdown
Welcome to GEO Optimizer Discussions 👋

This project started as a simple question — *can an AI engine actually read,
understand, and cite your site?* — and grew into a 100-point audit engine,
a CLI with 14 commands, an MCP server, and [GeoReady](https://skywalkerqqq.github.io/geo-optimizer-skill).
400+ stars later, it deserves a place to talk that isn't a bug tracker.

**Where things go:**
- 🙏 **Q&A** — "how do I raise my llms.txt score?", CI setup, MCP quirks. Ask anything.
- 💡 **Ideas** — propose checks, commands, integrations. The roadmap
  ([docs/ROADMAP.md](https://github.com/skywalkerqqq/geo-optimizer-skill/blob/main/docs/ROADMAP.md))
  is shaped by what practitioners actually need.
- 🏆 **Show & tell** — post your before/after GEO scores, your
  [score badge](https://github.com/skywalkerqqq/geo-optimizer-skill#show-your-geo-score),
  what moved the needle. Real-world evidence beats theory.
- 🐛 Confirmed bugs → [Issues](https://github.com/skywalkerqqq/geo-optimizer-skill/issues), as always.

**Three things worth trying today:**
1. `uvx --from geo-optimizer-skill geo audit --url https://yoursite.com` — zero-install audit
2. `geo citations --brand "You" --domain yoursite.com` — does AI actually cite you? (BYO key)
3. The live [State of GEO benchmark](https://skywalkerqqq.github.io/geo-optimizer-skill/state-of-geo/) — where the audited web stands

Be kind, bring data, cite your sources — it's what we ask of the models, after all.
```
