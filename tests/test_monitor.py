"""Test per il monitoraggio passivo della visibilita' AI."""

from __future__ import annotations

from geo_optimizer.core.history import HistoryResult
from geo_optimizer.core.monitor import build_passive_monitor_result, normalize_monitor_domain
from geo_optimizer.models.results import (
    AiDiscoveryResult,
    AuditResult,
    BrandEntityResult,
    LlmsTxtResult,
    MonitorSignal,
    RobotsResult,
    TrustStackResult,
)


def _sample_audit_result() -> AuditResult:
    """Crea un AuditResult rappresentativo per i test di monitor."""
    trust = TrustStackResult(checked=True, composite_score=20, grade="B", trust_level="high")
    return AuditResult(
        url="https://example.com",
        timestamp="2026-04-14T10:00:00+00:00",
        score=78,
        band="good",
        robots=RobotsResult(
            found=True,
            bots_allowed=["OAI-SearchBot", "ClaudeBot", "Claude-SearchBot", "ChatGPT-User"],
            bots_missing=["PerplexityBot", "Perplexity-User"],
            citation_bots_ok=False,
        ),
        llms=LlmsTxtResult(found=True, has_h1=True, has_sections=True, has_links=True, word_count=220),
        ai_discovery=AiDiscoveryResult(
            has_well_known_ai=True,
            has_summary=True,
            has_faq=False,
            has_service=False,
            endpoints_found=2,
        ),
        brand_entity=BrandEntityResult(
            brand_name_consistent=True,
            kg_pillar_count=2,
            has_about_link=True,
            has_contact_info=False,
        ),
        trust_stack=trust,
        score_breakdown={"brand_entity": 6},
        recommendations=["Create /ai/faq.json", "Add more sameAs links"],
    )


def test_normalize_monitor_domain_usa_homepage_canonica():
    """Input dominio/url viene normalizzato alla homepage del dominio."""
    assert normalize_monitor_domain("example.com/path?q=1") == "https://example.com"
    assert normalize_monitor_domain("HTTP://Example.com/blog") == "http://example.com"


def test_build_passive_monitor_result_calcola_score_e_recommendations():
    """Il monitor passivo deve aggregare segnali e trend locale."""
    audit_result = _sample_audit_result()
    history_result = HistoryResult(
        url="https://example.com/",
        retention_days=90,
        total_snapshots=3,
        latest_score=78,
        latest_band="good",
        previous_score=72,
        score_delta=6,
        regression_detected=False,
    )

    result = build_passive_monitor_result(audit_result, history_result)

    assert result.domain == "example.com"
    assert result.mode == "passive"
    assert result.direct_mentions_checked is False
    assert result.visibility_score > 0
    assert result.band in {"visible", "strong", "emerging"}
    assert result.total_snapshots == 3
    assert result.score_delta == 6
    assert any(signal.key == "citation_bot_access" for signal in result.signals)
    assert any(signal.status == "strong" for signal in result.signals if signal.key == "momentum")
    assert result.recommendations


def test_monitor_signal_dataclass_restano_serializzabile():
    """MonitorSignal mantiene una struttura minima e stabile."""
    signal = MonitorSignal(key="trust_strength", label="Trust", score=12, max_score=15, status="strong")

    assert signal.key == "trust_strength"
    assert signal.score == 12
