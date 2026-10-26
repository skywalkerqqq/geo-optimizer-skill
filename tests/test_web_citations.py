"""Tests for POST /api/citations (free AI citation check, cost-guarded).

run_citation_check is mocked at the import site inside the endpoint: zero
network calls and zero Perplexity spend.
"""

import os
from unittest.mock import patch

import pytest

pytest.importorskip("fastapi", reason="FastAPI non installato (pip install geo-optimizer-skill[web])")
pytest.importorskip("httpx", reason="httpx non installato (pip install httpx)")

# Same offline-import isolation as test_web_llms_generate.py
os.environ.setdefault("GEO_STATS_API_URL", "")

from starlette.testclient import TestClient

import geo_optimizer.web.app as web_app
from geo_optimizer.models.results import CitationCheckEntry, CitationCheckResult
from geo_optimizer.web.app import app

client = TestClient(app, raise_server_exceptions=False)

_ENDPOINT = "/api/citations"


def _result(verdict: str = "strong") -> CitationCheckResult:
    return CitationCheckResult(
        checked=True,
        brand="Acme",
        domain="acme.com",
        queries_run=2,
        brand_mention_rate=1.0,
        domain_citation_rate=1.0,
        top_cited_domains=[("other.com", 2)],
        verdict=verdict,
        entries=[
            CitationCheckEntry(
                query="What is the best tool for Acme?",
                platform="perplexity",
                brand_mentioned=True,
                domain_cited=True,
                cited_sources=["https://acme.com/docs", "https://other.com/x"],
                snippet="Acme is widely recommended.",
            ),
            CitationCheckEntry(query="failed one", platform="perplexity", error="boom"),
        ],
    )


@pytest.fixture(autouse=True)
def _reset_caps(monkeypatch):
    """Fresh rate-limit store, daily counter, and Perplexity key per test."""
    monkeypatch.setattr(web_app, "_rate_limit_store", {})
    monkeypatch.setattr(web_app, "_citations_day", "")
    monkeypatch.setattr(web_app, "_citations_count", 0)
    monkeypatch.setenv("PERPLEXITY_API_KEY", "pk-test")


class TestCitationsEndpoint:
    def test_citations_ok_returns_trimmed_payload(self):
        with patch("geo_optimizer.core.citations.run_citation_check", return_value=_result()) as mock_run:
            resp = client.post(_ENDPOINT, json={"brand": "Acme", "domain": "https://www.acme.com"})

        assert resp.status_code == 200
        data = resp.json()
        assert data["verdict"] == "strong"
        assert data["domain"] == "acme.com"
        assert data["top_cited_domains"] == [["other.com", 2]]
        # errored entries are dropped from the public payload
        assert len(data["entries"]) == 1
        assert data["entries"][0]["cited_sources"] == ["https://acme.com/docs", "https://other.com/x"]
        # exactly 2 customer-style queries, never more (cost guard)
        assert len(mock_run.call_args.kwargs["queries"]) == 2
        assert mock_run.call_args.kwargs["provider"] == "perplexity"

    def test_citations_disabled_without_key(self, monkeypatch):
        monkeypatch.delenv("PERPLEXITY_API_KEY", raising=False)
        resp = client.post(_ENDPOINT, json={"brand": "Acme", "domain": "acme.com"})
        assert resp.status_code == 503

    def test_citations_invalid_brand(self):
        resp = client.post(_ENDPOINT, json={"brand": "A", "domain": "acme.com"})
        assert resp.status_code == 400

    def test_citations_invalid_domain(self):
        resp = client.post(_ENDPOINT, json={"brand": "Acme", "domain": "not-a-domain"})
        assert resp.status_code == 400

    def test_citations_daily_cap_exhausted(self, monkeypatch):
        from datetime import datetime, timezone

        monkeypatch.setattr(web_app, "_citations_day", datetime.now(timezone.utc).strftime("%Y-%m-%d"))
        monkeypatch.setattr(web_app, "_citations_count", web_app._CITATIONS_DAILY_CAP)
        resp = client.post(_ENDPOINT, json={"brand": "Acme", "domain": "acme.com"})
        assert resp.status_code == 429
        assert "budget" in resp.json()["detail"].lower()

    def test_citations_provider_failure_maps_to_502(self):
        failed = CitationCheckResult(checked=True, skipped_reason="provider down")
        with patch("geo_optimizer.core.citations.run_citation_check", return_value=failed):
            resp = client.post(_ENDPOINT, json={"brand": "Acme", "domain": "acme.com"})
        assert resp.status_code == 502

    def test_citations_validation_non_string_is_422(self):
        resp = client.post(_ENDPOINT, json={"brand": 42, "domain": "acme.com"})
        assert resp.status_code == 422
