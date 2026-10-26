# astro-geoready

Make your Astro site **GEO-ready at build time**. Generates the text
scaffolding AI engines use to discover and understand your site, straight from
the route list Astro already knows — no crawling, no HTTP:

| File | Purpose |
|---|---|
| `/llms.txt` | Markdown index of your pages, grouped by section — the orientation file AI systems read first |
| `/.well-known/ai.txt` | AI crawler guidance file (sitemap + llms.txt pointers) |
| `/ai/summary.json` | Machine-readable site summary |

These are the same files the open-source
[GEO Optimizer](https://github.com/skywalkerqqq/geo-optimizer-skill) audit
scores under **llms.txt (18 pts)** and **AI Discovery (6 pts)**. Generate them
here, verify them with `geo audit`.

## Install

```bash
npm install astro-geoready
```

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import geoReady from 'astro-geoready';

export default defineConfig({
  site: 'https://yoursite.com',   // required — absolute URLs need it
  integrations: [
    geoReady({
      siteName: 'Your Site',
      description: 'One line about what your site is.',
    }),
  ],
});
```

Run `astro build` — the files land in `dist/` and deploy with everything else.

## Options

| Option | Default | Notes |
|---|---|---|
| `siteName` | site hostname | H1 of llms.txt |
| `description` | `''` | Blockquote line in llms.txt + summary.json |
| `llmsTxt` | `true` | Generate `/llms.txt` |
| `aiDiscovery` | `true` | Generate `/.well-known/ai.txt` + `/ai/summary.json` |
| `overwrite` | `false` | **Never overwrites existing files by default** — your hand-curated `public/llms.txt` always wins |
| `maxPerSection` | `20` | Max links per llms.txt section |

## Notes

- An llms.txt is an orientation file, not a confirmed ranking factor — it helps
  AI systems understand your site faster; it does not guarantee citations.
- The generated file is a solid starting point; a hand-curated one (better
  titles, descriptions per link) is still stronger. Generate, then refine.
- Verify the result: `uvx --from geo-optimizer-skill geo audit --url https://yoursite.com`
  or the free audit at [skywalkerqqq.github.io/geo-optimizer-skill](https://skywalkerqqq.github.io/geo-optimizer-skill).

MIT © [skywalkerqqq](https://github.com/skywalkerqqq)
