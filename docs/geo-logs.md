# geo logs

Analyze server access logs for AI crawler activity.

## Usage

```bash
geo logs --file /var/log/nginx/access.log
geo logs --file access.log --format json
```

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `--file` | required | Path to server access log |
| `--format` | text | Output format: `text` or `json` |

## Supported log formats

- **Apache/Nginx combined** — standard `combined` log format
- **JSON lines** — CloudFront, Vercel, custom (fields: `user_agent`, `path`, `timestamp`)

## Bot detection

Uses the `AI_BOTS` registry (27 bots). Case-insensitive User-Agent matching.

## Python API

```python
from geo_optimizer.core.log_analyzer import analyze_log_file

result = analyze_log_file("/var/log/nginx/access.log")
```
