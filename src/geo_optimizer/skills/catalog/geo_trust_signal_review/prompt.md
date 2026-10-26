# GEO Trust Signal Review

## Mission

Evaluate whether a site or page exposes a strong enough trust-signal layer for GEO-related reliability, source confidence, and AI-facing trust interpretation.

## Required Inputs

- `target_url`
- `audit_evidence_input` — either a full `AuditResult` or a normalized audit summary that preserves the relevant trust evidence

## Execution Protocol

1. Start from the authoritative GEO audit surface so the assessment is grounded in real trust and entity findings, not a generic trust checklist.
2. Use the trust-stack surface to interpret whether the site's technical, identity, social, academic, and consistency layers look strong enough for GEO reliability goals.
3. Use the negative-signal surface to identify the issues that most reduce source confidence or make the site look less suitable for citation and reuse.
4. Keep the interpretation focused on practical source reliability: explain whether the site looks trustworthy enough to surface and attribute, and which trust weaknesses matter most.
5. If the main need is implementation planning rather than trust interpretation, route to the foundation-repair workflow instead of expanding this skill into a repair plan.

## Output Contract

- `trust_signal_review_summary`: concise judgment of the current trust-signal posture as it relates to GEO goals.
- `prioritized_trust_gaps`: ordered list of the most meaningful trust-related weaknesses, each tied to the evidence surface it comes from.
- `trust_signal_strengths`: clear summary of the trust signals that already support source confidence well.
- `trust_improvement_priorities`: short list of the highest-leverage trust improvements to address first.
- `next_step_recommendation`: one explicit next workflow recommendation, typically foundation repair or a broader GEO audit follow-up.

## Guardrails

- Do not duplicate the full GEO audit output.
- Do not reduce the answer to raw trust-score or negative-signal output.
- Do not drift into a broad repair plan, reputation audit, or generic EEAT advice.
- Keep every claim tied to existing engine surfaces, MCP tools, or repository docs.
