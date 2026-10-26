"""Locale-aware translation for `/api/audit` output strings.

Covers:
  - `band` enum (excellent / good / foundation / critical) — already translated
    on the frontend via `window.__('band_xxx')`, exposed here for parity with
    other server-side i18n (JSON-API consumers, CLI wrappers).
  - `recommendations` string list — natural-language audit findings emitted by
    `geo_optimizer.core.audit.run_full_audit`. Translation is best-effort:
    white-list prefix lookup against the curated `_RECS` tables. Strings that
    don't match any entry are returned unmodified so a multilingual frontend
    always sees a valid (possibly English) string.
  - Audit-error / rate-limit / SSRF messages — short UI strings used by the
    frontend when the audit response is rejected.

Only `en` and `zh` are supported. Anything else falls back to English.
"""

from __future__ import annotations

import re
from typing import Iterable

from .i18n import normalize_lang as _normalize_lang

# ─── band enum (server-side mirror of frontend `band_*`) ─────────────────────
_BANDS_EN = ("excellent", "good", "foundation", "critical")
_BANDS_ZH = ("优秀", "良好", "基础", "急需改进")


def band_label(band: str, lang: str = "en") -> str:
    band = (band or "").strip().lower()
    lang = _normalize_lang(lang)
    table = _BANDS_ZH if lang == "zh" else _BANDS_EN
    if band in _BANDS_EN:
        return table[_BANDS_EN.index(band)]
    return band


# ─── recommendations ─────────────────────────────────────────────────────────
# Match strategy:
#   1) Each curated entry has `prefixes` — a tuple of stable English prefixes
#      that the audit core emits verbatim at the start of the recommendation.
#   2) The longest matching prefix wins (so "Create /llms.txt for AI indexing"
#      is preferred over a generic prefix like "Create ").
#   3) The translated template may contain `%s` placeholders that will be
#      re-substituted with regex captures from the original string.
#   4) Recommendations that match no entry fall through unchanged.

# Each entry: (prefixes, template_zh). Capture group index in `prefix_re`
# matches `%s` placeholder index in `template_zh` (1-based order).

_REC_CATALOG = (
    # 0
    {
        "prefixes": (
            "Create /llms.txt for AI indexing:",
        ),
        # capture: everything from the end of the matched prefix
        "zh": "创建 /llms.txt 以便 AI 索引：%s（注意：llms.txt 是一种组织化信号，并非已证实的排名因子，可帮助 AI 系统结构化内容）",
    },
    {
        "prefixes": ("Add a <title> tag",),
        "zh": "添加 <title> 标签 —— 这是 AI 搜索最重要的页面信号（5 分）",
    },
    {
        "prefixes": ("Update robots.txt to include all AI bots",),
        "zh": "更新 robots.txt，允许所有 AI 爬虫访问（GPTBot、ClaudeBot、PerplexityBot 等）",
    },
    {
        "prefixes": ("Add WebSite JSON-LD schema to homepage",),
        "zh": "为首页添加 WebSite JSON-LD 结构化数据",
    },
    {
        "prefixes": ("Add Organization JSON-LD schema",),
        "zh": "添加 Organization JSON-LD 结构化数据，包含 name、url 与 logo",
    },
    {
        "prefixes": ("Add FAQPage schema",),
        "zh": "添加 FAQPage 结构化数据，覆盖站点常见问答",
    },
    {
        "prefixes": ('Add <link rel="canonical">',),
        "zh": '添加 <link rel="canonical"> 链接，避免 AI 索引时出现重复内容问题',
    },
    {
        "prefixes": ("Add Open Graph tags",),
        "zh": "添加 Open Graph 标签（og:title、og:description、og:image）以完善 AI 与社交平台预览",
    },
    {
        "prefixes": ("Add optimized meta description",),
        "zh": "添加优化后的 meta description（150-160 字符）",
    },
    {
        "prefixes": ("Add a single H1 heading",),
        "zh": "添加一个清晰的 H1 标题，明确本页主题",
    },
    {
        "prefixes": ("Expand content to 300+ words",),
        "zh": "扩充内容至 300 字以上 —— AI 引擎需要实质内容才会引用",
    },
    {
        "prefixes": ("Add H2/H3 subheadings",),
        "zh": "添加 H2/H3 子标题，为 AI 内容抽取提供结构",
    },
    {
        "prefixes": ("Front-load key information",),
        "zh": "将关键信息放在内容前 30%，便于 AI 摘要片段选中",
    },
    {
        "prefixes": ("Add sameAs links",),
        "zh": "在 Organization 结构化数据中添加 sameAs 链接（Wikipedia、Wikidata、LinkedIn、Crunchbase）以帮助知识图谱消歧",
    },
    {
        "prefixes": ("Add a visible /about",),
        "zh": "添加可见的 /about 或 /about-us 链接，为 AI 建立信任信号",
    },
    {
        "prefixes": ("Add address, telephone",),
        "zh": "在 Organization 结构化数据中添加地址、电话或 contactPoint，用于实体校验",
    },
    {
        "prefixes": ("Add numerical data",),
        "zh": "补充具体数值与统计（AI 可见度最高可提升 +40%）",
    },
    {
        "prefixes": ("Cite authoritative sources",),
        "zh": "引用权威来源并配以外链（提升 AI 信誉）",
    },
    {
        "prefixes": ('Add lang attribute to <html>',),
        "zh": '为 <html> 标签添加 lang 属性（如 lang="en"），帮助 AI 识别语言',
    },
    {
        "prefixes": ("Add RSS/Atom feed",),
        "zh": '提供 RSS/Atom 订阅并在 <head> 通过 <link rel="alternate" type="application/rss+xml"> 链接，便于 AI 发现',
    },
    {
        "prefixes": ("Create /.well-known/ai.txt",),
        "zh": "创建 /.well-known/ai.txt 以声明 AI 爬虫权限",
    },
    {
        "prefixes": ("Create /ai/summary.json",),
        "zh": "创建 /ai/summary.json，提供站点名称与描述供 AI 引擎使用",
    },
    {
        "prefixes": ("Create /ai/faq.json",),
        "zh": "创建 /ai/faq.json，提供结构化 FAQ 以提升 AI 搜索可见度",
    },
    {
        "prefixes": ("Create /ai/service.json",),
        "zh": "创建 /ai/service.json，描述服务能力便于 AI 引擎索引",
    },
    {
        "prefixes": ("Add potentialAction",),
        "zh": "为 WebSite 结构化数据添加 potentialAction（SearchAction），便于 AI 智能体发现",
    },
    {
        "prefixes": ("Add descriptive labels to forms",),
        "zh": "为表单添加语义标签（label、aria-label），便于 AI 智能体使用",
    },
    {
        "prefixes": ("Consider adding WebMCP",),
        "zh": "考虑为交互元素添加 WebMCP toolname/tooldescription 属性，以兼容 Chrome AI 智能体",
    },
    {
        # unstable wording: this recommendation contains a unicode warning sign
        # and a generic statement, sometimes prefixed with "Note:" / "Warning:".
        "prefixes": (
            "⚠️ Content requires JavaScript to render",
            "⚠ Content requires JavaScript to render",
            "Content requires JavaScript to render",
        ),
        "zh": "⚠️ 页面依赖 JavaScript 渲染（原始 HTML 中提取到 0 个词）。AI 爬虫不会执行 JS，请实现 SSR、SSG 或预渲染",
    },
)


# Precompute longest-prefix-first matchers so the recommendations list is
# translated in a single O(N) walk.
_PATTERNS = []  # list of (compiled_regex, zh_template)
for _rec in _REC_CATALOG:
    prefixes = sorted(_rec["prefixes"], key=len, reverse=True)
    for _p in prefixes:
        _PATTERNS.append(
            (
                re.compile(r"\s*" + re.escape(_p)),
                _rec["zh"],
            )
        )


def _translate_one(rec: str) -> str:
    """Try every curated prefix; on hit, render the zh template with captures.

    The original English recommendation is returned verbatim if no prefix
    matches so uncurated recommendations are still displayed (in English) to
    the user.
    """
    if not isinstance(rec, str):
        return rec
    # Strip a trailing full stop / period for matching, but preserve in output.
    trailing = ""
    body = rec.rstrip()
    if body and body[-1] in ".!?。！？":
        trailing = body[-1]
        body = body[:-1]
    for pat, zh_tpl in _PATTERNS:
        m = pat.match(body)
        if not m:
            continue
        rest = body[m.end():].lstrip()
        if "%s" in zh_tpl:
            return zh_tpl % rest + trailing
        return zh_tpl + trailing
    return rec


def translate_recommendations(recs: Iterable[str], lang: str = "en") -> list[str]:
    """Translate a list of recommendation strings to the target language.

    For English output (or unknown langs), the input list is returned as-is
    (no copy, no decode pass) — this is hot-path cheap.
    """
    lang = _normalize_lang(lang)
    if lang == "en":
        return list(recs) if not isinstance(recs, list) else recs
    return [_translate_one(r) for r in recs]
