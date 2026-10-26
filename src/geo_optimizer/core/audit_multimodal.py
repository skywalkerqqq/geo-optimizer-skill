"""Audit Multimodal Readiness — image/video/audio signals for multimodal AI engines.

The AI platforms driving search in 2026 (Gemini, GPT-4o, Llama 4) synthesize
text, images, video, and audio together — but they reach non-text content
through its text scaffolding: alt text, captions, VideoObject/AudioObject
schema, subtitle tracks, and transcripts. This check measures that scaffolding.

Informational bonus check — does not affect the 100-point score.
Zero HTTP fetches — works only on already-available data.
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from geo_optimizer.models.results import MultimodalResult, SchemaResult

if TYPE_CHECKING:
    from bs4 import BeautifulSoup

# Embedded players that count as video content
_VIDEO_IFRAME_RE = re.compile(r"youtube\.com|youtu\.be|vimeo\.com|wistia\.|loom\.com", re.IGNORECASE)

# Alt text shorter than this is decorative/filename noise, not a description
_MIN_ALT_LEN = 5

_TRANSCRIPT_RE = re.compile(r"\btranscript\b|\btrascrizione\b", re.IGNORECASE)

# Schema types that make audio/video content citable
_VIDEO_SCHEMA_TYPES = {"VideoObject", "Clip", "BroadcastEvent"}
_AUDIO_SCHEMA_TYPES = {"AudioObject", "PodcastEpisode", "PodcastSeries"}


def _informative_alt(img) -> bool:
    alt = (img.get("alt") or "").strip()
    return len(alt) >= _MIN_ALT_LEN


def audit_multimodal_readiness(soup: BeautifulSoup | None, schema_result: SchemaResult) -> MultimodalResult:
    """Check multimodal readiness signals (images, video, audio).

    Args:
        soup: BeautifulSoup of the page (None → unchecked result).
        schema_result: Parsed JSON-LD schema result for the page.

    Returns:
        MultimodalResult with per-medium signals and a readiness level.
    """
    if soup is None:
        return MultimodalResult()

    found_types = set(schema_result.found_types or [])

    images = soup.find_all("img")
    total_images = len(images)
    images_with_alt = sum(1 for img in images if _informative_alt(img))
    alt_coverage = round(images_with_alt / total_images, 2) if total_images else 0.0
    caption_count = len(soup.find_all("figcaption"))

    video_tags = soup.find_all("video")
    video_iframes = [iframe for iframe in soup.find_all("iframe", src=True) if _VIDEO_IFRAME_RE.search(iframe["src"])]
    video_count = len(video_tags) + len(video_iframes)
    has_video = video_count > 0
    has_video_schema = bool(found_types & _VIDEO_SCHEMA_TYPES)
    has_video_captions = any(
        track.get("kind", "").lower() in ("captions", "subtitles")
        for video in video_tags
        for track in video.find_all("track")
    )

    audio_tags = soup.find_all("audio")
    has_audio = len(audio_tags) > 0
    has_audio_schema = bool(found_types & _AUDIO_SCHEMA_TYPES)

    # A transcript makes video/audio citable: look for the keyword in link
    # text or page text, or a transcript property in any schema.
    has_transcript = False
    if has_video or has_audio:
        page_text = soup.get_text(separator=" ", strip=True)
        has_transcript = bool(_TRANSCRIPT_RE.search(page_text)) or any(
            "transcript" in schema for schema in map(str, schema_result.raw_schemas or [])
        )

    # Readiness: score only the media actually present on the page.
    points = 0
    max_points = 0
    if total_images:
        max_points += 2
        points += 1 if alt_coverage >= 0.8 else 0
        points += 1 if caption_count > 0 else 0
    if has_video:
        max_points += 2
        points += 1 if has_video_schema else 0
        points += 1 if (has_video_captions or has_transcript) else 0
    if has_audio:
        max_points += 1
        points += 1 if (has_audio_schema or has_transcript) else 0

    if max_points == 0:
        readiness_level = "none"  # no media on the page — nothing to optimize
    else:
        ratio = points / max_points
        if ratio >= 1.0:
            readiness_level = "excellent"
        elif ratio >= 0.5:
            readiness_level = "good"
        elif ratio > 0:
            readiness_level = "basic"
        else:
            readiness_level = "missing"

    return MultimodalResult(
        checked=True,
        total_images=total_images,
        images_with_alt=images_with_alt,
        alt_coverage=alt_coverage,
        caption_count=caption_count,
        has_video=has_video,
        video_count=video_count,
        has_video_schema=has_video_schema,
        has_video_captions=has_video_captions,
        has_audio=has_audio,
        has_audio_schema=has_audio_schema,
        has_transcript=has_transcript,
        readiness_level=readiness_level,
    )
