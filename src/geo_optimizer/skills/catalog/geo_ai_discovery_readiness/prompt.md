# GEO AI Discovery Readiness

## Mission

Evaluate whether a site is realistically ready from an AI discovery perspective by interpreting bot access, AI discovery endpoints, and related GEO discovery evidence.

## Required Inputs

- `target_url`
- `audit_evidence_input` — either a full `AuditResult` or a normalized audit summary that preserves the relevant discovery evidence

## Execution Protocol

1. Start from the authoritative GEO audit surface so the assessment is grounded in real crawlability and AI discovery findings, not a generic crawler checklist.
2. Use the bot-access surface to interpret whether citation-critical and other tracked AI bots can reliably reach the site through `robots.txt`.
3. Use the AI discovery surface to interpret whether discovery endpoints are present and complete enough to support AI-facing discovery workflows.
4. Keep the interpretation focused on practical AI discoverability: explain whether AI systems can find the site, understand where discovery resources live, and avoid obvious discovery blockers.
5. If the main need is implementation planning rather than readiness interpretation, route to the foundation-repair workflow instead of expanding this skill into a repair plan.

## Output Contract

- `ai_discovery_readiness_summary`: concise judgment of the current AI discovery posture as it relates to GEO goals.
- `prioritized_ai_discovery_gaps`: ordered list of the most meaningful AI discovery weaknesses, each tied to the evidence surface it comes from.
- `ai_discovery_signal_strengths`: clear summary of the discovery signals that already support AI-facing discovery well.
- `ai_discovery_improvement_priorities`: short list of the highest-leverage discovery improvements to address first.
- `next_step_recommendation`: one explicit next workflow recommendation, typically foundation repair or a broader GEO audit follow-up.

## Guardrails

- Do not duplicate the full GEO audit output.
- Do not reduce the answer to raw `robots.txt` or endpoint check output.
- Do not drift into a broad repair plan or generic SEO crawlability advice.
- Keep every claim tied to existing engine surfaces, MCP tools, or repository docs.
