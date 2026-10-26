# Skill Roadmap

Maintainer roadmap for the internal GEO skill catalog.

This document exists to keep the catalog strategic, narrow, and grounded in real GEO Optimizer surfaces. It is not a product roadmap and it is not a prompt backlog. For the product release calendar, see [ROADMAP.md](ROADMAP.md).

## Purpose

The skill catalog should help maintainers add reusable GEO workflows without turning the repository into a loose collection of prompts.

The catalog should grow only when a new skill:

- interprets existing GEO evidence in a meaningfully new way
- produces a distinct remediation workflow
- compares multiple targets in a way the current catalog does not
- stays tightly tied to existing engine, MCP, and documentation surfaces

## Current Skills

### Interpretation skills

- `geo_audit_orchestrator`
  Normalizes a first-pass GEO assessment for a single site.
- `geo_citation_readiness`
  Interprets whether a site or page is realistically ready to be cited, reused, or surfaced by AI systems.
- `geo_schema_readiness`
  Interprets whether the current schema / structured-data layer is strong enough to support extractability, attribution clarity, and machine-readable understanding.
- `geo_ai_discovery_readiness`
  Interprets whether AI bots and AI discovery endpoints make the site realistically discoverable by AI systems.
- `geo_trust_signal_review`
  Interprets whether the current trust, entity, and negative-signal layer is strong enough to support source confidence.

### Remediation skills

- `geo_foundation_repair`
  Converts audit evidence into a technical remediation path for foundations such as robots.txt, llms.txt, schema, and AI discovery.

### Multi-target comparison skills

- `geo_competitor_comparison`
  Compares the GEO posture of multiple sites, explains meaningful deltas, and identifies what the weaker site should prioritize first.

### Deferred skill class

No current skill belongs to the execution-heavy class. This is intentional.

## Current Coverage Map

What the catalog covers well now:

- single-site GEO posture normalization
- foundation-level repair planning
- citation-specific interpretation
- schema / structured-data readiness interpretation
- AI discovery and bot-access interpretation
- trust and negative-signal interpretation
- cross-site comparative gap analysis

What the catalog does not cover yet:

- no major interpretation gap remains in the current roadmap scope

These are the strongest remaining gaps because the engine already exposes the relevant evidence surfaces.

## Design Rules For Future Skills

Every new skill should satisfy all of the following:

- one narrow job
- one clear reason to exist beyond the current catalog
- explicit reliance on real engine or MCP surfaces
- output artifacts that are operationally useful, not just descriptive
- obvious routing relationship to adjacent skills

Good signs:

- the skill answers a question maintainers or users will ask repeatedly
- the skill can be described in one sentence without listing many exceptions
- the skill improves interpretation, remediation, or comparison quality

Bad signs:

- the skill sounds like a generic “AI visibility” or “content strategy” prompt
- the skill overlaps heavily with `geo_audit_orchestrator`
- the skill just restates raw audit output without a new normalization layer
- the skill invents unsupported scoring or heuristics

## Anti-Patterns

Do not build:

- a generic “GEO expert” skill that tries to do everything
- multiple skills that differ only by wording, not by workflow
- broad content-writing skills with no strong coupling to GEO evidence
- market-analysis or brand-strategy skills not grounded in current repository surfaces
- execution-oriented skills that assume orchestration infrastructure the repo does not have yet

The main failure mode to avoid is prompt sprawl: many names, little contract value.

## Candidate Backlog

These are the strongest candidate areas based on the current engine and catalog.

### Interpretation skills worth building

### Remediation skills worth building later

- `geo_schema_repair_planner`
  Only if maintainers see repeated demand for a schema-specific remediation workflow that is meaningfully narrower than `geo_foundation_repair`.
- `geo_ai_discovery_repair`
  Only if AI discovery endpoints and bot-access workflows become large enough to justify their own repair skill.

### Comparison skills worth building later

- `geo_citation_gap_comparison`
  Only after `geo_competitor_comparison` proves too broad for citation-specific competitive analysis.

## Priority Order

Recommended order for the next additions:

1. `geo_schema_repair_planner` only if repeated workflow demand emerges
2. `geo_citation_gap_comparison` only if competitor comparison becomes overloaded
3. `geo_ai_discovery_repair` only if AI discovery workflows become substantially larger

## Recommended Next 3 Skills

### 1. `geo_schema_repair_planner`

Why first:

- schema is now covered on the interpretation side, so the next schema-specific addition should only happen if maintainers need repeated schema-only remediation paths
- this should stay deferred unless `geo_foundation_repair` proves too broad for recurring schema implementation work
- it is the next most plausible focused extension after the main interpretation layer is in place

Likely surfaces:

- `mcp:geo_fix`
- `mcp:geo_schema_validate`
- `doc:docs/schema-injector.md`
- `doc:docs/scoring-rubric.md`
- `doc:docs/geo-fix.md`

### 2. `geo_citation_gap_comparison`

Why second:

- the comparison layer already exists, but a citation-specific comparison skill should remain deferred until maintainers see repeated need for that narrower competitive lens
- this should come only after the interpretation catalog is broader and stable
- it is a plausible future extension, but not yet justified as an immediate addition

Likely surfaces:

- `mcp:geo_compare`
- `mcp:geo_citability`
- `mcp:geo_trust_score`
- `doc:docs/scoring-rubric.md`
- `doc:docs/geo-audit.md`

### 3. `geo_ai_discovery_repair`

Why third:

- AI discovery interpretation now exists, but a dedicated repair skill should stay deferred unless maintainers repeatedly need narrower implementation workflows than `geo_foundation_repair`
- this would only be justified if endpoint templates and bot-access fixes become a recurring specialized path
- it is valid as a later remediation split, not as a current core catalog need

Likely surfaces:

- `mcp:geo_fix`
- `mcp:geo_ai_discovery`
- `mcp:geo_check_bots`
- `doc:docs/ai-bots-reference.md`
- `doc:docs/scoring-rubric.md`
- `doc:docs/geo-fix.md`

## When Runtime Infrastructure Becomes Justified

Do not add broader execution or orchestration infrastructure yet.

That only becomes justified when:

- the catalog has at least several stable interpretation and remediation skills
- maintainers repeatedly need the same multi-skill handoff patterns
- those handoffs cannot be handled clearly through prompt contracts alone

Strong justification signals would be:

- repeated need for deterministic skill chaining
- repeated duplication of routing logic across many skills
- pressure to render skill specs into runtime artifacts automatically

Until then, the current catalog-plus-validation model is the right level of abstraction.

---

*For the product release calendar and project direction, see [ROADMAP.md](ROADMAP.md).*
