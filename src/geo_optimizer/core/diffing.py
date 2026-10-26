"""Confronto A/B tra due audit GEO."""

from __future__ import annotations

import asyncio

from geo_optimizer.core.audit import run_full_audit, run_full_audit_async
from geo_optimizer.models.config import SCORING
from geo_optimizer.models.results import AuditDiffResult, AuditResult, CategoryDelta

_CATEGORY_LABELS = {
    "robots": "Robots.txt",
    "llms": "llms.txt",
    "schema": "Schema JSON-LD",
    "meta": "Meta Tags",
    "content": "Content",
    "signals": "Signals",
    "ai_discovery": "AI Discovery",
    "brand_entity": "Brand & Entity",
}

_CATEGORY_MAX_SCORES = {
    "robots": sum(value for key, value in SCORING.items() if key.startswith("robots_")),
    "llms": sum(value for key, value in SCORING.items() if key.startswith("llms_")),
    "schema": sum(value for key, value in SCORING.items() if key.startswith("schema_")),
    "meta": sum(value for key, value in SCORING.items() if key.startswith("meta_")),
    "content": sum(value for key, value in SCORING.items() if key.startswith("content_")),
    "signals": sum(value for key, value in SCORING.items() if key.startswith("signals_")),
    "ai_discovery": sum(value for key, value in SCORING.items() if key.startswith("ai_discovery_")),
    "brand_entity": sum(value for key, value in SCORING.items() if key.startswith("brand_")),
}


def run_diff_audit(
    before_url: str,
    after_url: str,
    *,
    use_cache: bool = False,
    project_config=None,
) -> AuditDiffResult:
    """Esegue due audit e restituisce un confronto A/B strutturato."""
    return asyncio.run(
        run_diff_audit_async(
            before_url,
            after_url,
            use_cache=use_cache,
            project_config=project_config,
        )
    )


async def run_diff_audit_async(
    before_url: str,
    after_url: str,
    *,
    use_cache: bool = False,
    project_config=None,
) -> AuditDiffResult:
    """Variante async del confronto A/B."""
    if use_cache or not _async_runtime_available():
        before_result, after_result = await asyncio.gather(
            asyncio.to_thread(run_full_audit, before_url, use_cache=use_cache, project_config=project_config),
            asyncio.to_thread(run_full_audit, after_url, use_cache=use_cache, project_config=project_config),
        )
    else:
        before_result, after_result = await asyncio.gather(
            run_full_audit_async(before_url, project_config=project_config),
            run_full_audit_async(after_url, project_config=project_config),
        )

    return build_audit_diff(before_result, after_result)


def build_audit_diff(before_result: AuditResult, after_result: AuditResult) -> AuditDiffResult:
    """Costruisce il delta A/B a partire da due `AuditResult`."""
    category_deltas = _compute_category_deltas(before_result, after_result)
    improved = [delta for delta in category_deltas if delta.delta > 0]
    regressed = [delta for delta in category_deltas if delta.delta < 0]
    unchanged = [delta for delta in category_deltas if delta.delta == 0]

    improved.sort(key=lambda item: item.delta, reverse=True)
    regressed.sort(key=lambda item: item.delta)
    unchanged.sort(key=lambda item: item.category)

    return AuditDiffResult(
        before_url=before_result.url,
        after_url=after_result.url,
        before_score=before_result.score,
        after_score=after_result.score,
        score_delta=after_result.score - before_result.score,
        before_band=before_result.band,
        after_band=after_result.band,
        before_http_status=before_result.http_status,
        after_http_status=after_result.http_status,
        before_error=before_result.error,
        after_error=after_result.error,
        before_recommendations_count=len(before_result.recommendations),
        after_recommendations_count=len(after_result.recommendations),
        recommendations_delta=len(after_result.recommendations) - len(before_result.recommendations),
        category_deltas=sorted(category_deltas, key=lambda item: abs(item.delta), reverse=True),
        improved_categories=improved,
        regressed_categories=regressed,
        unchanged_categories=unchanged,
    )


def _compute_category_deltas(before_result: AuditResult, after_result: AuditResult) -> list[CategoryDelta]:
    """Calcola il delta per ogni categoria GEO presente nel breakdown."""
    categories = sorted(set(before_result.score_breakdown) | set(after_result.score_breakdown) | set(_CATEGORY_LABELS))
    deltas: list[CategoryDelta] = []
    for category in categories:
        before_score = before_result.score_breakdown.get(category, 0)
        after_score = after_result.score_breakdown.get(category, 0)
        deltas.append(
            CategoryDelta(
                category=category,
                label=_CATEGORY_LABELS.get(category, category.replace("_", " ").title()),
                before_score=before_score,
                after_score=after_score,
                delta=after_score - before_score,
                max_score=_CATEGORY_MAX_SCORES.get(category, 0),
            )
        )
    return deltas


def _async_runtime_available() -> bool:
    """Verifica se il path async è disponibile per il diff."""
    try:
        import httpx  # noqa: F401

        return True
    except ImportError:
        return False
