"""
Web UI i18n for GEO Optimizer.

Lightweight per-request translation for the FastAPI demo homepage
(`templates/index.html`). Supported: en, zh. Anything else -> en.

Strategy: a fixed set of `__I18N_*__` placeholders is listed up front and
substituted via str.replace() (no regex). This avoids regex over-matching
on tokens that look like placeholders (e.g. `window.__I18N__`).
"""

from __future__ import annotations

import json
from pathlib import Path

SUPPORTED = ("en", "zh")
DEFAULT = "en"

TEMPLATES_DIR = Path(__file__).parent / "templates"


_EN = {
    "nav_audit": "Audit",
    "nav_compare": "Compare",
    "nav_docs": "Docs",
    "nav_more": "More",
    "nav_research": "Research",
    "nav_roadmap": "Roadmap",
    "nav_manifesto": "Manifesto",
    "nav_github": "GitHub",
    "hero_title": "GEO Optimizer",
    "hero_subtitle": "Audit your website's visibility to ChatGPT, Perplexity, Claude &amp; Gemini",
    "stat_stars": "stars",
    "stat_downloads": "/mo",
    "stat_audits": "audits",
    "audit_url_label": "Website URL to audit",
    "audit_url_placeholder": "https://example.com",
    "audit_url_title": "Insert a valid URL (e.g. https://example.com)",
    "btn_run_audit": "Run Audit",
    "url_invalid_hint": "Please enter a valid URL (e.g. https://example.com)",
    "spin_connecting": "Connecting...",
    "spin_msgs": [
        "Checking robots.txt...",
        "Analyzing llms.txt...",
        "Parsing schema...",
        "Evaluating content...",
        "Scoring citability...",
        "Compiling results...",
    ],
    "citability_label": "Citability Score",
    "trend_label": "Trend",
    "trend_baseline": "Baseline snapshot saved for this URL.",
    "trend_stable": "Stable at {score}/100 since the previous snapshot.",
    "trend_up": "Improved from {prev} to {curr} since the previous snapshot.",
    "trend_down": "Dropped from {prev} to {curr} since the previous snapshot.",
    "trend_current": "Current baseline: {score}/100 ({band}).",
    "trend_delta_base": "BASE",
    "recs_toggle": "Recommendations",
    "action_html_report": "HTML Report",
    "action_download_pdf": "Download PDF",
    "btn_copy_title": "Copy",
    "btn_copy_done": "Done!",
    "manifesto_title": "Why this tool exists",
    "manifesto_body": "AI search is already deciding which websites get cited and which don't. The signals are documented, the research is published — but most of the web has no idea. GEO Optimizer exists to make AI visibility auditable, transparent, and accessible to every developer, not just teams with enterprise budgets.",
    "manifesto_pill_auditability": "Auditability",
    "manifesto_pill_science": "Scientific Foundation",
    "manifesto_pill_open": "Open Source",
    "manifesto_pill_precision": "Precision",
    "manifesto_link": "Read the full manifesto →",
    "footer_credit": "Built by skywalkerqqq · Powered by Princeton KDD 2024 + AutoGEO ICLR 2026 research",
    "footer_privacy": "Privacy",
    "footer_issues": "Issues",
    "cookie_banner_title": "We respect your privacy",
    "cookie_banner_body": "This site uses essential and analytics cookies to deliver a better browsing experience.",
    "cookie_banner_link": "Learn more",
    "cookie_btn_manage": "Manage",
    "cookie_btn_accept_all": "Accept all",
    "cookie_modal_title": "Cookie Settings",
    "cookie_cat_essential": "Essential Cookies",
    "cookie_cat_essential_desc": "Strictly necessary for the site to function. They cannot be disabled and include session, security, and preference cookies.",
    "cookie_cat_analytics": "Analytics Cookies",
    "cookie_cat_analytics_desc": "Help us understand how visitors interact with the site. Data is aggregated and anonymous. Disabling them prevents Google Analytics from loading.",
    "cookie_cat_marketing": "Marketing Cookies",
    "cookie_cat_marketing_desc": "Used to serve relevant ads. Disabling them results in less personalised advertising.",
    "cookie_btn_save": "Save preferences",
    "cookie_btn_reject_all": "Reject all",
    "cookie_float_title": "Cookie settings",
    "cookie_float_aria": "Cookie settings",
    "err_audit_failed": "Audit failed",
    "band_excellent": "Excellent",
    "band_good": "Good",
    "band_foundation": "Foundation",
    "band_critical": "Critical",
    "cat_robots": "Robots.txt",
    "cat_llms": "llms.txt",
    "cat_schema": "Schema JSON-LD",
    "cat_meta": "Meta Tags",
    "cat_content": "Content",
    "cat_signals": "Signals",
    "cat_ai_discovery": "AI Discovery",
    "cat_brand_entity": "Brand & Entity",
    "page_title": "GEO Optimizer — AI Search Visibility Audit",
    "page_description": "Audit your website's visibility to AI search engines. Score 0-100 with actionable fixes for ChatGPT, Perplexity, Claude, Gemini.",
    "faq_q1": "What is GEO Optimizer?",
    "faq_a1": "GEO Optimizer is an open-source toolkit that audits websites for AI search engine visibility. It scores sites 0-100 based on 47 research-backed methods and generates fixes for robots.txt, llms.txt, JSON-LD schema, and meta tags.",
    "faq_q2": "How does the GEO score work?",
    "faq_a2": "The score is calculated across 8 categories: robots.txt (18pt), llms.txt (18pt), JSON-LD schema (16pt), meta tags (14pt), content quality (12pt), signals (6pt), AI discovery (6pt), brand & entity (10pt). Bands: 86-100 excellent, 68-85 good, 36-67 foundation, 0-35 critical.",
    "faq_q3": "Is GEO Optimizer free?",
    "faq_a3": "Yes, GEO Optimizer is free and open-source under MIT License. Install with: pip install geo-optimizer-skill",
}


_ZH = {
    "nav_audit": "审计",
    "nav_compare": "对比",
    "nav_docs": "文档",
    "nav_more": "更多",
    "nav_research": "研究",
    "nav_roadmap": "路线图",
    "nav_manifesto": "宣言",
    "nav_github": "GitHub",
    "hero_title": "GEO Optimizer",
    "hero_subtitle": "审计你的网站在 ChatGPT、Perplexity、Claude &amp; Gemini 中的可见度",
    "stat_stars": "星标",
    "stat_downloads": "/月",
    "stat_audits": "次审计",
    "audit_url_label": "待审计的网址",
    "audit_url_placeholder": "https://example.com",
    "audit_url_title": "请输入合法 URL（如 https://example.com）",
    "btn_run_audit": "开始审计",
    "url_invalid_hint": "请输入合法 URL（如 https://example.com）",
    "spin_connecting": "连接中...",
    "spin_msgs": [
        "检查 robots.txt...",
        "分析 llms.txt...",
        "解析结构化数据...",
        "评估内容质量...",
        "评估可被引述性...",
        "汇总结果...",
    ],
    "citability_label": "可被引述性得分",
    "trend_label": "趋势",
    "trend_baseline": "已为该 URL 保存基线快照。",
    "trend_stable": "自上次快照以来稳定在 {score}/100。",
    "trend_up": "自上次快照以来从 {prev} 提升至 {curr}。",
    "trend_down": "自上次快照以来从 {prev} 降至 {curr}。",
    "trend_current": "当前基线：{score}/100（{band}）。",
    "trend_delta_base": "基线",
    "recs_toggle": "优化建议",
    "action_html_report": "HTML 报告",
    "action_download_pdf": "下载 PDF",
    "btn_copy_title": "复制",
    "btn_copy_done": "已复制！",
    "manifesto_title": "为什么做这个工具",
    "manifesto_body": "AI 搜索已经在决定哪些网站被引用、哪些被遗忘。信号已被记录，研究已经发表——但绝大多数网站浑然不知。GEO Optimizer 的使命是让 AI 可见度变得可审计、可透明、人人可及——而不只是企业级预算团队的专利。",
    "manifesto_pill_auditability": "可审计",
    "manifesto_pill_science": "科学根基",
    "manifesto_pill_open": "开源",
    "manifesto_pill_precision": "精确",
    "manifesto_link": "阅读完整宣言 →",
    "footer_credit": "由 skywalkerqqq 制作 · 基于 Princeton KDD 2024 + AutoGEO ICLR 2026 研究",
    "footer_privacy": "隐私",
    "footer_issues": "问题反馈",
    "cookie_banner_title": "我们尊重你的隐私",
    "cookie_banner_body": "本站使用必要与分析类 Cookie，以提供更佳的浏览体验。",
    "cookie_banner_link": "了解更多",
    "cookie_btn_manage": "管理",
    "cookie_btn_accept_all": "全部接受",
    "cookie_modal_title": "Cookie 设置",
    "cookie_cat_essential": "必要 Cookie",
    "cookie_cat_essential_desc": "网站运行所必需，无法关闭，包含会话、安全与偏好 Cookie。",
    "cookie_cat_analytics": "分析 Cookie",
    "cookie_cat_analytics_desc": "帮助我们了解访客与网站的互动方式，数据为匿名汇总。关闭后将不再加载 Google Analytics。",
    "cookie_cat_marketing": "营销 Cookie",
    "cookie_cat_marketing_desc": "用于投放相关性更高的广告。关闭后个性化广告将减少。",
    "cookie_btn_save": "保存偏好",
    "cookie_btn_reject_all": "全部拒绝",
    "cookie_float_title": "Cookie 设置",
    "cookie_float_aria": "Cookie 设置",
    "err_audit_failed": "审计失败",
    "band_excellent": "优秀",
    "band_good": "良好",
    "band_foundation": "基础",
    "band_critical": "急需改进",
    "cat_robots": "Robots.txt",
    "cat_llms": "llms.txt",
    "cat_schema": "Schema JSON-LD",
    "cat_meta": "Meta 标签",
    "cat_content": "内容",
    "cat_signals": "信号",
    "cat_ai_discovery": "AI 发现",
    "cat_brand_entity": "品牌与实体",
    "page_title": "GEO Optimizer — AI 搜索可见度审计",
    "page_description": "审计你的网站在 AI 搜索引擎中的可见度，基于 47 项研究背书方法给出 0-100 分与可执行修复建议，覆盖 ChatGPT、Perplexity、Claude、Gemini。",
    "faq_q1": "什么是 GEO Optimizer？",
    "faq_a1": "GEO Optimizer 是开源工具集，审计网站在 AI 搜索引擎中的可见度。它基于 47 项研究背书的方法为网站打分（0-100），并生成 robots.txt、llms.txt、JSON-LD 结构化数据与 Meta 标签的修复建议。",
    "faq_q2": "GEO 分数怎么算？",
    "faq_a2": "分数由 8 个维度计算：robots.txt（18 分）、llms.txt（18 分）、JSON-LD 结构化数据（16 分）、Meta 标签（14 分）、内容质量（12 分）、信号（6 分）、AI 发现（6 分）、品牌与实体（10 分）。分档：86-100 优秀，68-85 良好，36-67 基础，0-35 急需改进。",
    "faq_q3": "GEO Optimizer 是免费的吗？",
    "faq_a3": "是的。GEO Optimizer 基于 MIT 协议免费开源。安装命令：pip install geo-optimizer-skill",
}


_TABLES = {"en": _EN, "zh": _ZH}


def normalize_lang(lang):
    if not lang:
        return DEFAULT
    lang = lang.lower().strip()
    if "-" in lang:
        lang = lang.split("-", 1)[0]
    if lang in _TABLES:
        return lang
    return DEFAULT


def get_dict(lang):
    return _TABLES[normalize_lang(lang)]


# Special placeholders (non-key tokens)
# We deliberately do NOT use the `__I18N_LANG__` form because that token collides
# with the JS-side `window.__I18N_LANG__` literal that the page itself references
# to read the active locale at runtime. Use the `__GEO_*__` namespace for our
# own server-side substitution placeholders instead.
_TOKEN_LANG = "__GEO_LANG__"
_TOKEN_HTML_LANG = "__GEO_HTML_LANG_ATTR__"  # inserts the full lang="..." attribute
_TOKEN_DICT = "__GEO_I18N_DICT__"
_TOKEN_FAQ = "__GEO_FAQ__"
_TOKEN_SCHEMA_APP = "__GEO_SCHEMA_APP__"


def _faq_json(lang):
    d = get_dict(lang)
    return json.dumps([
        {"q": d["faq_q1"], "a": d["faq_a1"]},
        {"q": d["faq_q2"], "a": d["faq_a2"]},
        {"q": d["faq_q3"], "a": d["faq_a3"]},
    ], ensure_ascii=False)


def _schema_app_json(lang):
    d = get_dict(lang)
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "GEO Optimizer",
        "url": "https://skywalkerqqq.github.io/geo-optimizer-skill",
        "description": d["page_description"],
        "applicationCategory": "DeveloperApplication",
        "operatingSystem": "Web",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "author": {
            "@type": "Organization",
            "name": "skywalkerqqq",
            "url": "https://github.com/skywalkerqqq",
        },
    }, ensure_ascii=False)


def _schema_faq_json(lang):
    d = get_dict(lang)
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": d["faq_q1"], "acceptedAnswer": {"@type": "Answer", "text": d["faq_a1"]}},
            {"@type": "Question", "name": d["faq_q2"], "acceptedAnswer": {"@type": "Answer", "text": d["faq_a2"]}},
            {"@type": "Question", "name": d["faq_q3"], "acceptedAnswer": {"@type": "Answer", "text": d["faq_a3"]}},
        ],
    }, ensure_ascii=False)


def render_index(lang):
    """Render templates/index.html with placeholders replaced for the given language.

    Per-string placeholders use the form `__I18N_KEY__` (one per translatable
    string). For special tokens we use the `__GEO_*__` namespace to avoid
    colliding with the JS-side `window.__I18N_LANG__` / `window.__I18N__`
    identifiers. `__NONCE_ATTR__` is left intact for the caller to substitute.
    """
    lang = normalize_lang(lang)
    d = _TABLES[lang]

    template_path = TEMPLATES_DIR / "index.html"
    html = template_path.read_text(encoding="utf-8")

    # Per-key string placeholders: `__I18N_KEY__` -> translated value.
    # Skip non-string values (lists/dicts) — they're injected as the JSON
    # `__GEO_I18N_DICT__` token below and accessed at runtime via
    # `window.__I18N__.key_name`.
    for key, value in d.items():
        if not isinstance(value, str):
            continue
        token = "__I18N_" + key.upper() + "__"
        if token not in html:
            continue
        html = html.replace(token, value)

    # Special placeholders (different prefix so they don't clash with JS literals)
    html = html.replace(_TOKEN_LANG, lang)
    html = html.replace(_TOKEN_HTML_LANG, f'lang="{lang}"')
    html = html.replace(_TOKEN_DICT, json.dumps(d, ensure_ascii=False))
    html = html.replace(_TOKEN_FAQ, _schema_faq_json(lang))
    html = html.replace(_TOKEN_SCHEMA_APP, _schema_app_json(lang))

    return html


def render_static(filename: str, lang: str) -> str:
    """Render a static page (manifesto.html, roadmap.html, …) with locale.

    Strategy mirrors ``render_index``: placeholders are ``__I18N_<KEY>__``
    tokens that match keys in the per-page table from ``manifest_i18n``.
    Unknown tokens survive unchanged so unlocalized pages still serve a
    valid (English) response. Special placeholders (``__NONCE_ATTR__``,
    ``__GEO_LANG__``) are still substituted here so templates can use them.
    """
    from .manifest_i18n import page_dict as _page_dict

    lang = normalize_lang(lang)
    d = _page_dict(filename, lang)
    template_path = TEMPLATES_DIR / filename
    html = template_path.read_text(encoding="utf-8")

    for key, value in d.items():
        if not isinstance(value, str):
            continue
        token = "__I18N_" + key.upper() + "__"
        if token not in html:
            continue
        html = html.replace(token, value)

    # Static pages mostly still carry __NONCE_ATTR__ on their <script> tag.
    html = html.replace("__GEO_LANG__", lang)
    if "__GEO_HTML_LANG_ATTR__" in html:
        html = html.replace("__GEO_HTML_LANG_ATTR__", f'lang="{lang}"')
    return html
