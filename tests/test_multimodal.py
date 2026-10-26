"""Tests for the multimodal readiness bonus check.

Zero network calls — everything works on local HTML strings.
"""

from __future__ import annotations

from bs4 import BeautifulSoup

from geo_optimizer.core.audit_multimodal import audit_multimodal_readiness
from geo_optimizer.models.results import MultimodalResult, SchemaResult


def _soup(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")


class TestAuditMultimodal:
    def test_none_soup_returns_unchecked(self):
        result = audit_multimodal_readiness(None, SchemaResult())
        assert result.checked is False

    def test_no_media_is_level_none(self):
        result = audit_multimodal_readiness(_soup("<html><body><p>text only</p></body></html>"), SchemaResult())
        assert result.checked is True
        assert result.readiness_level == "none"

    def test_images_with_good_alt_and_captions(self):
        html = """<body>
        <figure><img src="a.jpg" alt="A detailed chart of GEO scores"><figcaption>GEO scores</figcaption></figure>
        <img src="b.jpg" alt="Team photo at the 2026 summit">
        </body>"""
        result = audit_multimodal_readiness(_soup(html), SchemaResult())
        assert result.total_images == 2
        assert result.images_with_alt == 2
        assert result.alt_coverage == 1.0
        assert result.caption_count == 1
        assert result.readiness_level == "excellent"

    def test_short_or_missing_alt_not_informative(self):
        html = '<body><img src="a.jpg" alt="img"><img src="b.jpg"></body>'
        result = audit_multimodal_readiness(_soup(html), SchemaResult())
        assert result.images_with_alt == 0
        assert result.readiness_level == "missing"

    def test_video_tag_with_captions_track(self):
        html = """<body>
        <video src="v.mp4"><track kind="captions" src="v.vtt"></video>
        </body>"""
        result = audit_multimodal_readiness(_soup(html), SchemaResult(found_types=["VideoObject"]))
        assert result.has_video and result.video_count == 1
        assert result.has_video_schema is True
        assert result.has_video_captions is True
        assert result.readiness_level == "excellent"

    def test_youtube_iframe_counts_as_video(self):
        html = '<body><iframe src="https://www.youtube.com/embed/xyz"></iframe></body>'
        result = audit_multimodal_readiness(_soup(html), SchemaResult())
        assert result.has_video and result.video_count == 1
        assert result.has_video_schema is False
        assert result.readiness_level == "missing"

    def test_transcript_keyword_detected_for_audio(self):
        html = '<body><audio src="ep1.mp3"></audio><a href="/ep1-text">Read the transcript</a></body>'
        result = audit_multimodal_readiness(_soup(html), SchemaResult())
        assert result.has_audio is True
        assert result.has_transcript is True
        assert result.readiness_level == "excellent"

    def test_audio_schema_detected(self):
        html = '<body><audio src="ep1.mp3"></audio></body>'
        result = audit_multimodal_readiness(_soup(html), SchemaResult(found_types=["PodcastEpisode"]))
        assert result.has_audio_schema is True
        assert result.readiness_level == "excellent"


class TestMultimodalRecommendations:
    def _recs(self, multimodal: MultimodalResult):
        from geo_optimizer.core.audit import build_recommendations
        from geo_optimizer.models.results import (
            ContentResult,
            LlmsTxtResult,
            MetaResult,
            RobotsResult,
        )

        return build_recommendations(
            "https://example.com",
            RobotsResult(found=True, citation_bots_ok=True),
            LlmsTxtResult(found=True, has_sections=True, sections_count=3, has_links=True, links_count=5),
            SchemaResult(has_website=True, has_faq=True, has_organization=True),
            MetaResult(
                has_title=True, has_description=True, has_canonical=True, has_og_title=True, has_og_description=True
            ),
            ContentResult(
                has_numbers=True,
                has_links=True,
                has_h1=True,
                word_count=500,
                has_heading_hierarchy=True,
                has_front_loading=True,
            ),
            multimodal=multimodal,
        )

    def test_low_alt_coverage_recommendation(self):
        mm = MultimodalResult(checked=True, total_images=10, images_with_alt=3, alt_coverage=0.3)
        recs = self._recs(mm)
        assert any("alt text" in r for r in recs)

    def test_video_without_schema_and_transcript(self):
        mm = MultimodalResult(checked=True, has_video=True, video_count=1)
        recs = self._recs(mm)
        assert any("VideoObject" in r for r in recs)
        assert any("transcript" in r for r in recs)

    def test_clean_multimodal_adds_nothing(self):
        mm = MultimodalResult(
            checked=True,
            total_images=4,
            images_with_alt=4,
            alt_coverage=1.0,
            caption_count=2,
            readiness_level="excellent",
        )
        assert self._recs(mm) == []


class TestMultimodalInAuditPipeline:
    def test_full_audit_includes_multimodal(self):
        """_build_audit_result computes multimodal from soup automatically."""
        from geo_optimizer.core.audit import _build_audit_result
        from geo_optimizer.models.results import (
            ContentResult,
            LlmsTxtResult,
            MetaResult,
            RobotsResult,
        )

        html = '<html><body><h1>T</h1><img src="a.jpg" alt="Descriptive alt text here"></body></html>'
        soup = _soup(html)
        result = _build_audit_result(
            "https://example.com",
            RobotsResult(found=True),
            LlmsTxtResult(),
            SchemaResult(),
            MetaResult(has_title=True),
            ContentResult(has_h1=True, word_count=400),
            200,
            1000,
            soup=soup,
        )
        assert result.multimodal.checked is True
        assert result.multimodal.total_images == 1
        assert result.multimodal.alt_coverage == 1.0

    def test_json_formatter_includes_multimodal(self):
        import json

        from geo_optimizer.cli.formatters import format_audit_json
        from geo_optimizer.models.results import AuditResult

        result = AuditResult(
            url="https://example.com",
            multimodal=MultimodalResult(checked=True, total_images=2, readiness_level="good"),
        )
        data = json.loads(format_audit_json(result))
        assert data["multimodal"]["readiness_level"] == "good"
