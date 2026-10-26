"""Tests for Content Decay Predictor (#383)."""

from __future__ import annotations

from bs4 import BeautifulSoup

from geo_optimizer.core.audit_decay import audit_content_decay


def _soup(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")


class TestContentDecay:
    def test_empty_body(self):
        result = audit_content_decay(_soup("<html><body></body></html>"))
        assert result.checked is True
        assert result.signals == []
        assert result.evergreen_score == 100

    def test_detects_temporal_year(self):
        result = audit_content_decay(_soup("<html><body><p>In 2024, the market grew rapidly.</p></body></html>"))
        types = [s.decay_type for s in result.signals]
        assert "temporal" in types

    def test_detects_statistical(self):
        result = audit_content_decay(_soup("<html><body><p>About 42% of users prefer this approach.</p></body></html>"))
        types = [s.decay_type for s in result.signals]
        assert "statistical" in types

    def test_detects_version(self):
        result = audit_content_decay(_soup("<html><body><p>Requires Python 3.11 or later.</p></body></html>"))
        types = [s.decay_type for s in result.signals]
        assert "version" in types

    def test_detects_event_recency(self):
        result = audit_content_decay(_soup("<html><body><p>We recently launched a new feature.</p></body></html>"))
        types = [s.decay_type for s in result.signals]
        assert "event" in types

    def test_detects_price(self):
        result = audit_content_decay(_soup("<html><body><p>Starting at $99/month for teams.</p></body></html>"))
        types = [s.decay_type for s in result.signals]
        assert "price" in types

    def test_evergreen_content_scores_100(self):
        html = "<html><body><p>Machine learning is a subset of artificial intelligence that enables systems to learn from data.</p></body></html>"
        result = audit_content_decay(_soup(html))
        assert result.evergreen_score == 100
        assert result.decay_risk == "low"

    def test_high_risk_with_many_signals(self):
        html = "<html><body><p>In 2023, we recently launched version 3.2 at $49/month. About 67% of growth was seen last quarter.</p></body></html>"
        result = audit_content_decay(_soup(html))
        assert result.decay_risk in {"medium", "high"}
        assert result.evergreen_score < 100

    def test_max_20_signals(self):
        years = " ".join(f"In {y}, something happened." for y in range(2020, 2026))
        stats = " ".join(f"About {i}% of users do X." for i in range(10, 40))
        html = f"<html><body><p>{years} {stats}</p></body></html>"
        result = audit_content_decay(_soup(html))
        assert len(result.signals) <= 20

    def test_earliest_decay_days(self):
        result = audit_content_decay(_soup("<html><body><p>We just launched this product.</p></body></html>"))
        assert result.earliest_decay_days is not None
        assert result.earliest_decay_days > 0

    def test_accepts_clean_text(self):
        result = audit_content_decay(_soup("<html></html>"), clean_text="In 2025, the trend shifted.")
        assert len(result.signals) >= 1

    def test_evergreen_floor_at_zero(self):
        signals_text = " ".join(f"In {y}, something changed. We recently updated." for y in range(2020, 2026))
        result = audit_content_decay(_soup(f"<html><body><p>{signals_text}</p></body></html>"))
        assert result.evergreen_score >= 0
