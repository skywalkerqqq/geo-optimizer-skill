"""Tests for Semantic Coherence Analysis (#253)."""

from __future__ import annotations

import asyncio
import sys
from unittest.mock import Mock, patch

from bs4 import BeautifulSoup

from geo_optimizer.core.coherence_analyzer import analyze_coherence
from geo_optimizer.core.term_extractor import extract_page_terms
from geo_optimizer.models.results import PageTermExtract, SitemapUrl


def _soup(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")


# ─── Term Extractor ──────────────────────────────────────────────────────────


class TestTermExtractor:
    def test_extracts_title_and_h1(self):
        html = "<html><head><title>My Page</title></head><body><h1>Welcome</h1></body></html>"
        result = extract_page_terms(_soup(html), url="https://example.com")
        assert result.title == "My Page"
        assert result.h1 == "Welcome"
        assert result.url == "https://example.com"

    def test_extracts_language(self):
        html = '<html lang="en"><head><title>T</title></head><body></body></html>'
        result = extract_page_terms(_soup(html))
        assert result.language == "en"

    def test_extracts_definitions(self):
        html = "<html><body><p>Machine Learning is a subset of artificial intelligence.</p></body></html>"
        result = extract_page_terms(_soup(html))
        assert len(result.definitions) >= 1
        assert "Machine Learning" in result.definitions[0]

    def test_extracts_key_terms(self):
        html = "<html><body><p>Google Cloud and Google Cloud are used. Amazon Web Services too.</p></body></html>"
        result = extract_page_terms(_soup(html))
        assert "Google Cloud" in result.key_terms

    def test_empty_body(self):
        result = extract_page_terms(_soup("<html><body></body></html>"))
        assert result.title == ""
        assert result.definitions == []


# ─── Coherence Analyzer ─────────────────────────────────────────────────────


class TestCoherenceAnalyzer:
    def test_single_page_no_issues(self):
        result = analyze_coherence([PageTermExtract(url="https://a.com")])
        assert result.checked is True
        assert result.pages_analyzed == 1
        assert result.issues == []

    def test_no_issues_when_consistent(self):
        extracts = [
            PageTermExtract(url="https://a.com", title="About Us", language="en"),
            PageTermExtract(url="https://b.com", title="Services", language="en"),
        ]
        result = analyze_coherence(extracts)
        assert result.coherence_score == 100
        assert result.language_consistency == 1.0

    def test_detects_duplicate_titles(self):
        extracts = [
            PageTermExtract(url="https://a.com/page1", title="Our Amazing Services"),
            PageTermExtract(url="https://a.com/page2", title="Our Amazing Services"),
        ]
        result = analyze_coherence(extracts)
        dup_issues = [i for i in result.issues if i.issue_type == "duplicate_title"]
        assert len(dup_issues) >= 1
        assert result.coherence_score < 100

    def test_detects_mixed_language(self):
        extracts = [
            PageTermExtract(url="https://a.com/en", language="en"),
            PageTermExtract(url="https://a.com/it", language="it"),
            PageTermExtract(url="https://a.com/en2", language="en"),
        ]
        result = analyze_coherence(extracts)
        lang_issues = [i for i in result.issues if i.issue_type == "mixed_language"]
        assert len(lang_issues) >= 1
        assert result.language_consistency < 1.0

    def test_detects_conflicting_definitions(self):
        extracts = [
            PageTermExtract(
                url="https://a.com/page1",
                definitions=["Machine Learning is a subset of artificial intelligence."],
            ),
            PageTermExtract(
                url="https://a.com/page2",
                definitions=["Machine Learning is a statistical method for data analysis."],
            ),
        ]
        result = analyze_coherence(extracts)
        conflict_issues = [i for i in result.issues if i.issue_type == "conflicting_definition"]
        assert len(conflict_issues) >= 1
        assert result.coherence_score < 100

    def test_score_floor_at_zero(self):
        extracts = [PageTermExtract(url=f"https://a.com/{i}", title="Same Title", language="en") for i in range(25)]
        result = analyze_coherence(extracts)
        assert result.coherence_score >= 0

    def test_empty_list(self):
        result = analyze_coherence([])
        assert result.checked is True
        assert result.pages_analyzed == 0


# ─── Site Coherence Orchestrator ───────────────────────────────────────────────


class TestSiteCoherenceOrchestrator:
    def test_run_site_coherence_with_empty_sitemap(self):
        # Arrange
        with patch("geo_optimizer.core.site_coherence.fetch_sitemap") as mock_sitemap:
            mock_sitemap.return_value = []

            from geo_optimizer.core.site_coherence import run_site_coherence

            result = run_site_coherence("https://example.com/sitemap.xml")

        # Assert
        assert result.checked is True
        assert result.pages_analyzed == 0
        assert result.coherence_score == 0

    def test_run_site_coherence_warns_empty_sitemap_in_text_output(self):
        # Arrange
        with patch("geo_optimizer.core.site_coherence.fetch_sitemap") as mock_sitemap:
            mock_sitemap.return_value = []

            import click

            from geo_optimizer.cli.coherence_cmd import _print_text
            from geo_optimizer.core.site_coherence import run_site_coherence

            result = run_site_coherence("https://example.com/sitemap.xml")
            capturing = []
            original_echo = click.echo

            def mock_echo(msg, *args, **kwargs):
                capturing.append(str(msg))

            click.echo = mock_echo

            # Act
            _print_text(result)

            # Restore
            click.echo = original_echo

        # Assert
        assert result.pages_analyzed == 0
        assert "⚠️  No pages analyzed" in capturing or "No pages analyzed" in " ".join(capturing)

    def test_run_site_coherence_with_realistic_sitemap(self):
        # Arrange
        entries = [
            SitemapUrl(url="https://a.com"),
            SitemapUrl(url="https://b.com"),
        ]

        with (
            patch("geo_optimizer.core.site_coherence.fetch_sitemap") as mock_sitemap,
            patch("geo_optimizer.core.site_coherence._fetch_and_extract") as mock_fetch,
        ):
            mock_sitemap.return_value = entries
            mock_fetch.return_value = [
                PageTermExtract(url="https://a.com", title="Home", language="it"),
                PageTermExtract(url="https://b.com", title="About", language="it"),
            ]

            from geo_optimizer.core.site_coherence import run_site_coherence

            result = run_site_coherence("https://example.com/sitemap.xml")

        # Assert
        assert result.checked is True
        assert result.pages_analyzed == 2
        assert result.coherence_score == 100

    def test_dedupe_urls_removes_duplicates(self):
        # Arrange
        entries = [
            SitemapUrl(url="https://a.com"),
            SitemapUrl(url="https://a.com"),
            SitemapUrl(url="https://b.com"),
        ]

        from geo_optimizer.core.site_coherence import _dedupe_urls

        # Act
        result = _dedupe_urls(entries, max_pages=10)

        # Assert
        assert len(result) == 2
        assert result == ["https://a.com", "https://b.com"]

    def test_dedupe_urls_limits_by_max_pages(self):
        # Arrange
        entries = [
            SitemapUrl(url="https://a.com"),
            SitemapUrl(url="https://b.com"),
            SitemapUrl(url="https://c.com"),
        ]

        from geo_optimizer.core.site_coherence import _dedupe_urls

        # Act
        result = _dedupe_urls(entries, max_pages=2)

        # Assert
        assert len(result) == 2
        assert result == ["https://a.com", "https://b.com"]

    def test_fetch_and_extract_skips_failed_responses(self):
        # Arrange
        urls = ["https://a.com", "https://b.com"]

        with (
            patch("geo_optimizer.core.site_coherence.fetch_url") as mock_fetch,
            patch("geo_optimizer.core.site_coherence.extract_page_terms") as mock_extract,
        ):
            mock_fetch.side_effect = [
                (Mock(text="<html><body><p>Test</p></body></html>", status_code=200), None),
                (None, "SSRF blocked"),
            ]
            mock_extract.return_value = PageTermExtract(url="https://a.com")

            from geo_optimizer.core.site_coherence import _fetch_and_extract

            result = _fetch_and_extract(urls)

        # Assert
        assert len(result) == 1
        assert result[0].url == "https://a.com"

    def test_run_site_coherence_async_fallback_sync(self):
        # Arrange
        entries = [SitemapUrl(url="https://example.com/page1")]

        with (
            patch.dict(sys.modules, {"geo_optimizer.utils.http_async": None}),
            patch("geo_optimizer.core.site_coherence.fetch_sitemap") as mock_sitemap,
            patch("geo_optimizer.core.site_coherence._fetch_and_extract") as mock_fetch,
        ):
            mock_sitemap.return_value = entries
            mock_fetch.return_value = [PageTermExtract(url="https://example.com/page1")]

            from geo_optimizer.core.site_coherence import run_site_coherence_async

            # Must use asyncio.run because the function is async
            result = asyncio.run(run_site_coherence_async("https://example.com/sitemap.xml"))

        # Assert
        assert result.checked is True
        assert result.pages_analyzed == 1

    def test_run_site_coherence_async_success(self):
        # Arrange
        entries = [
            SitemapUrl(url="https://a.com"),
            SitemapUrl(url="https://b.com"),
        ]

        # Mock per fetch_urls_async con una risposta valida e una fallita
        async def mock_fetch_urls_async(urls):
            responses = {}
            for url in urls:
                if url == "https://a.com":
                    mock_resp = Mock()
                    mock_resp.text = "<html><body><p>Content of a</p></body></html>"
                    responses[url] = (mock_resp, None)
                else:
                    responses[url] = (None, "SSRF blocked")
            return responses

        with (
            patch("geo_optimizer.core.site_coherence.fetch_sitemap") as mock_sitemap,
            patch("geo_optimizer.utils.http_async.fetch_urls_async", new=mock_fetch_urls_async),
            patch("geo_optimizer.core.site_coherence.extract_page_terms") as mock_extract,
        ):
            mock_sitemap.return_value = entries
            mock_extract.return_value = PageTermExtract(url="https://a.com")

            from geo_optimizer.core.site_coherence import run_site_coherence_async

            result = asyncio.run(run_site_coherence_async("https://example.com/sitemap.xml"))

        # Assert
        assert result.checked is True
        assert result.pages_analyzed == 1
        assert mock_extract.call_count == 1  # only one valid response
