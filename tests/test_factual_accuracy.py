"""Test per l'audit di accuratezza fattuale."""

from __future__ import annotations

from unittest.mock import Mock

from bs4 import BeautifulSoup

from geo_optimizer.core.factual_accuracy import audit_factual_accuracy, run_factual_accuracy_audit


def _soup(html: str):
    """Costruisce una soup di test."""
    return BeautifulSoup(html, "html.parser")


def test_audit_factual_accuracy_rileva_claims_fonti_incoerenze_e_link_rotti():
    """L'audit deve distinguere claim source-backed, unsourced e contraddizioni."""
    html = """
    <html><body>
      <p>Studies show 42% of users prefer GEO workflows.</p>
      <p>Our conversion rate is 42% according to <a href="https://data.example.com/report">Data Report</a>.</p>
      <p>We guarantee the best results in 7 days.</p>
      <p>Our conversion rate is 45% according to <a href="https://broken.example.com/report">Other Report</a>.</p>
      <footer>Copyright 2024</footer>
      <p>Last updated 2026</p>
    </body></html>
    """

    def _fake_fetch(url: str):
        if "broken.example.com" in url:
            response = Mock(status_code=404)
            return response, None
        response = Mock(status_code=200)
        return response, None

    result = audit_factual_accuracy(
        soup=_soup(html),
        html=html,
        base_url="https://example.com",
        link_fetcher=_fake_fetch,
    )

    assert result.checked is True
    assert result.claims_found == 4
    assert result.claims_sourced == 2
    assert result.claims_unsourced == 1
    assert result.severity == "high"
    assert result.source_links_checked == 2
    assert result.broken_source_links == ["https://broken.example.com/report"]
    assert any("42% of users prefer GEO workflows" in claim for claim in result.unsourced_claims)
    assert any("best results" in claim for claim in result.unverifiable_claims)
    assert any("conversion rate" in item for item in result.inconsistencies)
    assert any("Updated year 2026" in item for item in result.inconsistencies)


def test_audit_factual_accuracy_restituisce_clean_su_contenuto_neutro():
    """Contenuto senza claim fattuali non deve generare warning."""
    html = """
    <html><body>
      <p>This page explains our product features and onboarding steps.</p>
      <p>Use the dashboard to manage your workspace and settings.</p>
    </body></html>
    """

    result = audit_factual_accuracy(
        soup=_soup(html),
        html=html,
        base_url="https://example.com",
        link_fetcher=lambda url: (Mock(status_code=200), None),
    )

    assert result.checked is True
    assert result.claims_found == 0
    assert result.claims_sourced == 0
    assert result.claims_unsourced == 0
    assert result.inconsistencies == []
    assert result.broken_source_links == []
    assert result.severity == "clean"


def test_run_factual_accuracy_audit_gestisce_errori_http():
    """Il runner completo deve degradare in modo leggibile se la pagina non e' raggiungibile."""
    original_fetch = run_factual_accuracy_audit.__globals__["fetch_url"]

    def _fake_fetch(url: str):
        return None, "timeout"

    run_factual_accuracy_audit.__globals__["fetch_url"] = _fake_fetch
    try:
        result = run_factual_accuracy_audit("https://example.com")
    finally:
        run_factual_accuracy_audit.__globals__["fetch_url"] = original_fetch

    assert result.checked is False
    assert result.severity == "high"
    assert any("Unable to reach https://example.com" in item for item in result.inconsistencies)
