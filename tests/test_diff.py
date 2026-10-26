"""Test per il core A/B diff dei GEO audit."""

from __future__ import annotations

import asyncio
from unittest.mock import patch

from geo_optimizer.core.diffing import build_audit_diff, run_diff_audit_async
from geo_optimizer.models.results import AuditResult


def _make_result(url: str, score: int, band: str, breakdown: dict[str, int], recommendations: list[str]) -> AuditResult:
    """Costruisce un AuditResult minimo per i test del diff."""
    return AuditResult(
        url=url,
        score=score,
        band=band,
        http_status=200,
        page_size=1000,
        score_breakdown=breakdown,
        recommendations=recommendations,
    )


class TestAuditDiff:
    """Test per la costruzione del delta A/B."""

    def test_build_audit_diff_computes_score_and_category_deltas(self):
        """Il diff A/B espone score delta, miglioramenti e regressioni di categoria."""
        before_result = _make_result(
            "https://example.com/before",
            60,
            "foundation",
            {"robots": 18, "llms": 8, "schema": 6, "meta": 10},
            ["A", "B", "C"],
        )
        after_result = _make_result(
            "https://example.com/after",
            78,
            "good",
            {"robots": 18, "llms": 15, "schema": 10, "meta": 9},
            ["A"],
        )

        result = build_audit_diff(before_result, after_result)

        assert result.score_delta == 18
        assert result.before_band == "foundation"
        assert result.after_band == "good"
        assert result.before_recommendations_count == 3
        assert result.after_recommendations_count == 1
        assert result.recommendations_delta == -2
        assert result.improved_categories[0].category == "llms"
        assert result.improved_categories[0].delta == 7
        assert result.regressed_categories[0].category == "meta"
        assert result.regressed_categories[0].delta == -1

    @patch("geo_optimizer.core.diffing.asyncio.to_thread")
    @patch("geo_optimizer.core.diffing.run_full_audit")
    def test_run_diff_audit_async_uses_sync_path_with_cache(self, mock_run_full_audit, mock_to_thread):
        """Con cache attiva il diff usa il path sincrono via to_thread."""
        mock_to_thread.side_effect = lambda func, *args, **kwargs: func(*args, **kwargs)
        mock_run_full_audit.side_effect = [
            _make_result("https://example.com/before", 50, "foundation", {"llms": 5}, ["A"]),
            _make_result("https://example.com/after", 70, "good", {"llms": 12}, []),
        ]

        result = asyncio.run(
            run_diff_audit_async("https://example.com/before", "https://example.com/after", use_cache=True)
        )

        assert result.score_delta == 20
        assert mock_run_full_audit.call_count == 2
