# Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| 4.x     | :white_check_mark: |
| 3.x     | :x:                |
| < 3.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in GEO Optimizer, please report it responsibly.

**Do NOT open a public GitHub issue for security vulnerabilities.**

### How to Report

1. **Email**: Send details to [skywalkerqqq@users.noreply.github.com](mailto:skywalkerqqq@users.noreply.github.com)
2. **Subject**: `[SECURITY] GEO Optimizer — Brief description`
3. **Include**:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### What to Expect

- **Acknowledgment**: Within 48 hours
- **Assessment**: Within 7 days
- **Fix timeline**: Critical vulnerabilities patched within 14 days
- **Credit**: You will be credited in the release notes (unless you prefer anonymity)

### Scope

The following areas are in scope:

| Area | Examples |
|------|---------|
| **SSRF** | Bypassing `validate_public_url()`, DNS rebinding, redirect attacks |
| **XSS** | Injection via HTML formatter output, SVG badge, web app |
| **Path Traversal** | Bypassing `validate_safe_path()` in schema injection |
| **DoS** | Bypassing response size limits, sitemap bomb, rate limiter bypass |
| **Injection** | Template injection in schema templates, JSON-LD injection |

### Out of Scope

- Vulnerabilities in dependencies (report to the upstream project)
- Social engineering attacks
- Denial of service via legitimate high traffic
- Issues in the legacy `scripts/` directory (removed in v3.4.0)

## Security Architecture

GEO Optimizer implements multiple defense layers:

- **Anti-SSRF**: DNS pinning (`_PinnedIPAdapter`), manual redirect validation, blocked networks (RFC 1918, loopback, link-local, cloud metadata)
- **Input validation**: `validate_public_url()` for URLs, `validate_safe_path()` for file paths
- **Output encoding**: HTML escaping in formatters, `</` escape in JSON-LD tags
- **Size limits**: `MAX_RESPONSE_SIZE` (10 MB), `MAX_TOTAL_URLS` (10,000), `_MAX_BODY_BYTES` (4 KB POST body)
- **Rate limiting**: Per-IP rate limiter on web API endpoints
