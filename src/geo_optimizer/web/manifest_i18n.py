"""Translation tables for the static public pages.

Each page-level table is a flat dict whose keys are also valid as
``__I18N_KEY__`` placeholders. ``render_static(filename, lang)`` reads
``templates/<filename>`` and substitutes any ``__I18N_<KEY>__`` token it
finds. Unknown tokens survive unchanged — this lets us extend per-page
without breaking older deployed HTML.

Naming convention:
  * ``M_*`` — Manifesto (auditable/principles/signals/commitments)
  * ``R_*`` — Research (peer-reviewed papers behind the scoring)
  * ``RM_*`` — Roadmap (Now / Next / Later)
  * ``PR_*`` — Privacy (GDPR-style policy)
  * ``CMP_*`` — Compare (side-by-side website comparison)
  * ``ANZ_*`` — Analyze competitors (narrative analysis)
"""

from __future__ import annotations


# ─────────────────────────────────────────────────────────────────────────
# MANIFESTO (130 keys, generated 2026-09-07 from canonical English source)
# ─────────────────────────────────────────────────────────────────────────

_M_EN = {
    # Metadata / SEO
    "TITLE": "The GEO Optimizer Manifesto — Why AI Search Visibility Should Be Open",
    "META_DESC": "Why AI search visibility should be auditable, open, and accessible to every website on the internet. The GEO Optimizer Manifesto.",
    "OG_TITLE": "The GEO Optimizer Manifesto",
    "OG_DESC": "Why AI search visibility should be auditable, open, and accessible to every website on the internet.",
    "OG_SITE_NAME": "GEO Optimizer",
    "OG_LOCALE": "en_US",
    "JSONLD_WEBSITE_DESC": "Open-source toolkit to audit and optimize websites for AI search engine visibility.",
    "JSONLD_WEBPAGE_NAME": "The GEO Optimizer Manifesto",
    "JSONLD_WEBPAGE_DESC": "Why AI search visibility should be auditable, open, and accessible to every website on the internet.",
    "FAQ1_NAME": "What is GEO Optimizer?",
    "FAQ1_TEXT": "GEO Optimizer is an open-source toolkit that audits websites for AI search engine visibility. It scores sites 0-100 based on 8 categories and 47 research-backed methods, covering robots.txt, llms.txt, Schema JSON-LD, meta tags, content quality, technical signals, AI discovery, and brand entity signals.",
    "FAQ2_NAME": "Why does AI search visibility matter?",
    "FAQ2_TEXT": "AI search engines like ChatGPT, Perplexity, and Claude synthesize answers from cited sources. Sites not optimized for AI visibility are invisible in these answers. Princeton KDD 2024 research shows source citations increase AI visibility by 27-115%, statistics by 33%, and authoritative tone by 29%.",
    "FAQ3_NAME": "Is GEO Optimizer free and open source?",
    "FAQ3_TEXT": "Yes. GEO Optimizer is MIT-licensed open source software. Install with: pip install geo-optimizer-skill. The scoring rubric, algorithms, and all weights are publicly documented.",
    "FAQ4_NAME": "What websites does GEO Optimizer work with?",
    "FAQ4_TEXT": "GEO Optimizer works with any publicly accessible URL regardless of the underlying technology. It audits the HTTP response that AI engines see, so it works with static sites, WordPress, Next.js, custom backends, headless architectures, and anything else that responds to HTTP requests.",

    # Nav
    "NAV_AUDIT": "Audit",
    "NAV_COMPARE": "Compare",
    "NAV_DOCS": "Docs",
    "NAV_MORE": "More",
    "NAV_RESEARCH": "Research",
    "NAV_ROADMAP": "Roadmap",
    "NAV_MANIFESTO": "Manifesto",
    "NAV_GITHUB_CTA": "GitHub",

    # Hero
    "HERO_EYEBROW": "Open Source · Research-Backed · Developer-First",
    "HERO_H1": "The GEO Optimizer<br>Manifesto",
    "HERO_SUB": "Why AI search visibility should be auditable, open, and accessible to every website on the internet.",

    # TOC
    "TOC_TITLE": "Contents",
    "TOC_S1": "The web changed. Most websites don't know it yet.",
    "TOC_S2": "The visibility gap is a tooling problem.",
    "TOC_S3": "What GEO Optimizer stands for.",
    "TOC_S4": "The eight signals that determine AI visibility.",
    "TOC_S4B": "Beyond the score: what no competitor tells you.",
    "TOC_S5": "Who this is for.",
    "TOC_S6": "What we commit to.",
    "TOC_S7": "The bottom line.",

    # Section 1
    "SECT_NUM_01": "01 —",
    "S1_HEADING": "The web changed. Most websites don't know it yet.",
    "S1_PARA_1": "For two decades, search worked the same way. You published content. A crawler indexed it. Users clicked links. The cycle was legible, auditable, understood. An entire ecosystem of tools, agencies, and expertise grew around it — because it was a system you could study and improve.",
    "S1_BLOCKQUOTE": "That cycle is breaking.",
    "S1_PARA_2": "When someone asks ChatGPT which project management tool to use, they don't see ten blue links. They get a synthesized answer. One or two sources get cited. The rest don't exist. When Perplexity answers a question about the best Python libraries for data science, it doesn't return a SERP — it returns a verdict. When Claude summarizes \"the leading GEO optimization tools,\" it draws from a training corpus and live retrieval that most websites have never been optimized for.",
    "S1_PARA_3": "This is Generative Engine Optimization. And right now, most of the web is invisible to it.",
    "S1_PARA_4": "The shift isn't hypothetical. ChatGPT reached 500 million weekly active users in early 2025. Perplexity processes hundreds of millions of queries per month. AI Overviews appear in a significant fraction of Google searches. The number of users receiving their first contact with information through a synthesized AI answer is growing every quarter. Gartner projects that by 2026, traditional search engine volume will drop 25% as AI chatbots capture informational queries.",
    "S1_PARA_5": "Most websites have never accounted for this.",

    # Section 2
    "SECT_NUM_02": "02 —",
    "S2_HEADING": "The visibility gap is a tooling problem.",
    "S2_PARA_1": "The problem isn't that the signals are unknown. Research from Princeton's NLP group (KDD 2024) was the first to quantify what actually increases AI citation rates: source citations boost visibility by 27–115%. Quotation inclusion adds 41%. Statistical claims add 33%. Fluent, authoritative prose adds 29%. These are measurable effects from a peer-reviewed study on 10,000 queries validated on real Perplexity.ai responses.",
    "S2_PARA_2": "AutoGEO (ICLR 2026, Carnegie Mellon) went further — using LLM-based rule extraction and reinforcement learning to improve on Princeton's baseline by 50.99%. The research is there. The signals are documented. The llms.txt specification from Answer.AI is published. The geo-checklist.dev standard exists. The path from \"invisible\" to \"cited\" is not a mystery.",
    "S2_PARA_3": "The problem is that most website owners have no idea any of this exists.",
    "S2_PARA_4": "Enterprise SEO platforms are adding \"AI visibility\" dashboards. They cost hundreds or thousands of dollars per month. They're built for large marketing teams, not independent developers or small agencies. They're walled gardens: black boxes that produce scores without explaining exactly what signal is missing or what fixing it is worth.",
    "S2_PARA_5": "Meanwhile, every piece of data these platforms analyze is public. The robots.txt file is accessible to anyone. The JSON-LD schema is in the HTML source. Whether a site allows GPTBot, ClaudeBot, or PerplexityBot can be checked in seconds. Whether a site has a properly structured llms.txt, an /ai/summary.json, a FAQPage schema — all of this is inspectable without a subscription.",
    "S2_BLOCKQUOTE": "The visibility gap isn't a data problem. It's an access problem. It's a tooling problem.",

    # Section 3 — principles
    "SECT_NUM_03": "03 —",
    "S3_HEADING": "What GEO Optimizer stands for.",
    "PRINCIPLE_AUDITABILITY_TITLE": "Auditability over opacity",
    "PRINCIPLE_AUDITABILITY_BODY": "A score means nothing if you can't verify how it was calculated. Every check in our scoring engine is documented, tied to published research, and open for inspection. When we say Schema JSON-LD is worth 16 points, you can read exactly which signals we measure and why. When we say a site scores 47/100, we tell you exactly which 53 points are missing and precisely what it would take to earn them back.",
    "PRINCIPLE_SCIENTIFIC_TITLE": "Scientific foundation over marketing claims",
    "PRINCIPLE_SCIENTIFIC_BODY": "We don't invent signals. Every check in our engine traces back to empirical research or documented specifications: Princeton KDD 2024, AutoGEO ICLR 2026, the llms.txt spec by Answer.AI, the geo-checklist.dev emerging standard, the established schema.org vocabulary. When we say a signal statistically increases AI citation rates, we cite the paper. When research updates, we update the weights.",
    "PRINCIPLE_UNIVERSALITY_TITLE": "Universality over platform bias",
    "PRINCIPLE_UNIVERSALITY_BODY": "GEO Optimizer works on any publicly accessible URL, regardless of what technology powers it. It doesn't care if your site runs on a custom Rust backend, a static site generator, a PHP monolith, a headless architecture, or anything in between. The HTTP response is what AI engines see. That's what we audit. The tool has no concept of \"supported platforms\" — if it responds to an HTTP request, we can audit it.",
    "PRINCIPLE_OPEN_TITLE": "Open source over gatekeeping",
    "PRINCIPLE_OPEN_BODY": "The algorithms are public. The weights are in the source code. The scoring rubric is in the documentation. Every architectural decision, every weight change, every new check is visible in the git history with a commit message explaining the rationale. You can fork this, extend it, integrate it into your CI pipeline, run it against your own infrastructure, and contribute improvements back — without asking permission or paying a license fee. Visibility shouldn't require a subscription.",
    "PRINCIPLE_PRECISION_TITLE": "Precision over noise",
    "PRINCIPLE_PRECISION_BODY": "An audit that returns 50 vague recommendations helps no one. Every recommendation we surface is concrete, actionable, and tied to a specific score impact. \"Add a FAQPage schema: +3 points.\" \"Allow OAI-SearchBot in robots.txt: +13 points.\" \"Create /llms.txt with at least 1,000 words: +4 points.\" You know exactly what you're getting for the work you do, and you can prioritize by return on effort.",
    "PRINCIPLE_DEVELOPER_TITLE": "Developer experience as a first-class concern",
    "PRINCIPLE_DEVELOPER_BODY": "The web interface is for discovery. The CLI is where real work happens. JSON output that pipes into other tools. CI integration via geo-action. An MCP server for AI agent workflows. A Python API for custom integrations and monitoring scripts. GEO Optimizer is built by developers, for developers, with the assumption that a tool only gets used if it fits naturally into an existing workflow.",

    # Section 4 — eight signals
    "SECT_NUM_04": "04 —",
    "S4_HEADING": "The eight signals that determine AI visibility.",
    "SIG_ROBOTS_NAME": "robots.txt",
    "SIG_ROBOTS_PTS": "max 18 pts",
    "SIG_ROBOTS_DESC": "Are you letting the right crawlers in? OAI-SearchBot, ClaudeBot, Claude-SearchBot, and PerplexityBot are the crawlers that power real-time citations in ChatGPT, Claude, and Perplexity. If they're blocked — explicitly or via an overly restrictive wildcard — you're invisible by default, regardless of how good your content is. This is the most commonly misconfigured signal and the one with the most immediate fix.",
    "SIG_LLMS_NAME": "llms.txt",
    "SIG_LLMS_PTS": "max 18 pts",
    "SIG_LLMS_DESC": "The emerging standard for machine-readable site context. Proposed by Answer.AI, llms.txt gives AI agents a structured index of your content, capabilities, and documentation — without requiring them to crawl and parse hundreds of pages. Think of it as sitemap.xml written for language models. Depth matters: a minimal file scores 5 points; a comprehensive, well-structured companion with llms-full.txt earns all 18.",
    "SIG_SCHEMA_NAME": "Schema JSON-LD",
    "SIG_SCHEMA_PTS": "max 16 pts",
    "SIG_SCHEMA_DESC": "Structured data has always helped search engines. For AI engines, it's how entities, relationships, and facts become machine-readable. FAQPage schema answers questions directly. Article schema signals freshness and authorship. Organization schema establishes legal identity. WebSite schema provides canonical context. The richness of the schema — number of relevant attributes, presence of sameAs knowledge graph links — matters as much as which types are present.",
    "SIG_META_NAME": "Meta Tags",
    "SIG_META_PTS": "max 14 pts",
    "SIG_META_DESC": "The fundamentals: a descriptive title, a meta description that accurately summarizes the page, a canonical URL to prevent duplicate content confusion, and Open Graph tags so AI agents and social platforms have structured context. These signals have mattered for traditional search for decades. They matter for AI search for the same reason: they're the clearest, most explicit signals of what a page is about.",
    "SIG_CONTENT_NAME": "Content Quality",
    "SIG_CONTENT_PTS": "max 12 pts",
    "SIG_CONTENT_DESC": "Concrete numbers. External citations. Proper heading hierarchy with H2 and H3. Key information front-loaded in the first 30% of the content. Lists and tables that break up dense prose. Minimum word count that signals substance. The Princeton research is unambiguous: specific, well-structured, citation-ready content gets cited more. Vague, jargon-heavy, poorly organized content gets ignored.",
    "SIG_TECH_NAME": "Technical Signals",
    "SIG_TECH_PTS": "max 6 pts",
    "SIG_TECH_DESC": "Language declaration on the <html> element. A discoverable RSS or Atom feed. Freshness indicators via dateModified in schema or Last-Modified HTTP headers. Small signals, individually. But they establish context, recency, and trustworthiness — the baseline credibility that AI engines use to decide whether your content is worth referencing.",
    "SIG_DISCOVERY_NAME": "AI Discovery",
    "SIG_DISCOVERY_PTS": "max 6 pts",
    "SIG_DISCOVERY_DESC": "The new standard for machine-readable service context: /.well-known/ai.txt for crawler permissions, /ai/summary.json for structured capability descriptions, /ai/faq.json for pre-answered common queries, /ai/service.json for endpoint and feature discovery. These files are to AI agents what robots.txt was to traditional crawlers — a structured handshake between your site and the systems that will reference it.",
    "SIG_BRAND_NAME": "Brand & Entity Signals",
    "SIG_BRAND_PTS": "max 10 pts",
    "SIG_BRAND_DESC": "AI engines don't just index pages. They build models of entities. Brand name coherence across H1, title, og:title, and schema Organization name is the foundation. Knowledge graph connections via sameAs to Wikipedia, Wikidata, LinkedIn, and Crunchbase establish that your brand is a known, recognized entity, not an unknown string of text. About and contact pages signal that a real organization stands behind the content. Geographic identity and topic authority round out the entity model that AI engines use to decide how much to trust and cite your content.",

    # Section 4b — beyond the score
    "SECT_NUM_04B": "04b —",
    "S4B_HEADING": "Beyond the score: what no competitor tells you.",
    "S4B_INTRO": "The 0-100 score is one dimension. But real-world AI visibility depends on factors that aren't easily reducible to points. GEO Optimizer runs six additional informational checks that surface risks and signals no competitor currently detects:",
    "BEYOND_PROMPT_NAME": "Prompt Injection Detection",
    "BEYOND_PROMPT_PTS": "security",
    "BEYOND_PROMPT_DESC": "Eight patterns of AI manipulation: hidden text via CSS, invisible Unicode characters, direct LLM instructions embedded in content, prompt injection in HTML comments, monochrome cloaking text, micro-font injection, data attribute abuse, and aria-hidden exploitation. Based on UC Berkeley EMNLP 2024 research. Severity: clean, suspicious, or critical.",
    "BEYOND_TRUST_NAME": "Trust Stack Score",
    "BEYOND_TRUST_PTS": "5 layers",
    "BEYOND_TRUST_DESC": "A composite trust assessment across five dimensions: technical trust (HTTPS, security headers), identity trust (authorship, organization, about page), social trust (sameAs links, testimonials, social profiles), academic trust (citations, statistics, authoritative sources), and consistency trust (no contradictions between title, H1, schema, and meta). Grade A through F.",
    "BEYOND_NEG_NAME": "Negative Signals",
    "BEYOND_NEG_PTS": "anti-citation",
    "BEYOND_NEG_DESC": "Eight signals that actively reduce your chances of being cited: excessive CTAs, popup/modal interference, thin content, broken links, keyword stuffing, missing author attribution, high boilerplate ratio, and mixed signals between promise and delivery. Based on UC Berkeley research on what AI engines actively avoid citing.",
    "BEYOND_CDN_NAME": "CDN Crawler Access",
    "BEYOND_CDN_PTS": "access",
    "BEYOND_CDN_DESC": "Tests whether Cloudflare, Akamai, Vercel, or other CDN/WAF configurations are silently blocking AI crawlers. Many sites think they allow GPTBot because their robots.txt says so — but their CDN serves a 403 or CAPTCHA to the actual crawler. This check sends requests with real bot User-Agents and compares the responses.",
    "BEYOND_JS_NAME": "JS Rendering",
    "BEYOND_JS_PTS": "access",
    "BEYOND_JS_DESC": "Detects whether critical content is only available after JavaScript execution. SPA frameworks (React, Vue, Angular) often render content client-side — invisible to crawlers that don't execute JS. This check compares the raw HTML response against expected content signals and flags framework-specific patterns that indicate JS-dependent rendering.",
    "BEYOND_WEBMCP_NAME": "WebMCP Readiness",
    "BEYOND_WEBMCP_PTS": "future",
    "BEYOND_WEBMCP_DESC": "Measures how well a site exposes machine-readable context for MCP-compatible AI agents. Checks for registerTool() patterns, toolname attributes, and potentialAction schema. Four readiness levels: none, basic, ready, advanced. This signal anticipates the next generation of AI agents that consume structured context — not just crawled content — before generating responses.",
    "S4B_OUTRO": "These six checks don't add to the score. They surface problems that the score alone can't capture — and that your competitors' tools don't look for at all.",

    # Section 5 — audience
    "SECT_NUM_05": "05 —",
    "S5_HEADING": "Who this is for.",
    "AUDIENCE_ITEM_1": "Every developer who has ever deployed a project and wondered why it doesn't appear in AI-generated answers about the problem it solves.",
    "AUDIENCE_ITEM_2": "Every agency managing client sites that need to maintain visibility as search behavior fundamentally shifts.",
    "AUDIENCE_ITEM_3": "Every indie founder who can't afford enterprise SEO tools but understands that organic visibility is existential — and that the rules are changing faster than most people realize.",
    "AUDIENCE_ITEM_4": "Every technical writer, documentation team, and open source maintainer who wants their work to be cited when AI assistants answer questions their content directly addresses.",
    "AUDIENCE_ITEM_5": "Every DevOps engineer who wants GEO checks in their CI pipeline — the same way they have linting, security scans, and performance budgets.",
    "AUDIENCE_ITEM_6": "Every researcher who wants to understand, empirically, what the current state of AI citation mechanics actually is.",

    # Section 6 — commitments
    "SECT_NUM_06": "06 —",
    "S6_HEADING": "What we commit to.",
    "COMMIT_1_TITLE": "The core tool will stay open source.",
    "COMMIT_1_BODY": "Every scoring decision will be documented. Every change to the rubric will appear in the changelog with a rationale. If we're wrong about a signal, we'll say so and update the weights.",
    "COMMIT_2_TITLE": "We'll build for developers first.",
    "COMMIT_2_BODY": "That means a CLI that behaves the way CLIs should, JSON output that pipes cleanly, and an API that doesn't require authentication for a basic audit. Complexity lives in the options, not in the defaults.",
    "COMMIT_3_TITLE": "We'll be honest about uncertainty.",
    "COMMIT_3_BODY": "GEO is a young field. Some signals that matter today may matter less as AI architectures evolve. Some signals we're not measuring yet may turn out to be critical. We'll update the rubric when the evidence changes, and we'll document why — not quietly recalibrate and hope no one notices.",
    "COMMIT_4_TITLE": "We won't sell audit credits or put core functionality behind a paywall.",
    "COMMIT_4_BODY": "The score you see is the real score. The recommendations you see are the real recommendations. Every feature in the paid tier of a competitor should be a feature in the open source tool.",

    # Section 7 — bottom line
    "SECT_NUM_07": "07 —",
    "S7_HEADING": "The bottom line.",
    "BOTTOMLINE_PARA_1": "AI search is the next major shift in how people find, evaluate, and trust information online. The signals that determine visibility in that shift are measurable, documented, and optimizable today.",
    "BOTTOMLINE_PARA_2": "Most of the web doesn't know this yet. That gap won't stay open forever.",
    "BOTTOMLINE_PARA_3": "The sites that act now — that structure their content for citability, make themselves discoverable to AI agents, establish entity coherence and knowledge graph presence — will have a durable advantage when AI search becomes the dominant channel and everyone else starts scrambling.",
    "BOTTOMLINE_PARA_4": "GEO Optimizer exists to make that preparation practical, transparent, and accessible. Not just to teams with enterprise budgets. To every developer, every agency, every indie founder, every open source maintainer who wants to be visible in the systems that are increasingly mediating how the world finds information.",
    "BOTTOMLINE_PARA_5": "You shouldn't need a subscription to know if your site is being seen.",
    "BOTTOMLINE_CONCLUSION": "That's why this tool exists. That's what it will keep doing.",

    # Footer
    "FOOTER_GITHUB": "GitHub",
    "FOOTER_PYPI": "PyPI",
    "FOOTER_DOCS": "Docs",
    "FOOTER_ABOUT": "About skywalkerqqq",
    "FOOTER_ISSUES": "Issues",
    "FOOTER_RUNAUDIT": "Run an Audit",
    "FOOTER_CREDIT": "GEO Optimizer is open source software, MIT License · Built by skywalkerqqq · Powered by Princeton KDD 2024 + AutoGEO ICLR 2026 research",

    # Cookie floating button
    "COOKIE_TITLE": "Cookie settings",
}


_M_ZH = {
    # Metadata / SEO
    "TITLE": "GEO Optimizer 宣言 —— 为什么 AI 搜索可见性应该开放",
    "META_DESC": "为什么 AI 搜索可见性应当可审计、开放，并服务于每一个网站。这是 GEO Optimizer 宣言。",
    "OG_TITLE": "GEO Optimizer 宣言",
    "OG_DESC": "为什么 AI 搜索可见性应当可审计、开放，并服务于每一个网站。",
    "OG_SITE_NAME": "GEO Optimizer",
    "OG_LOCALE": "zh_CN",
    "JSONLD_WEBSITE_DESC": "用于审计并优化网站 AI 搜索可见性的开源工具包。",
    "JSONLD_WEBPAGE_NAME": "GEO Optimizer 宣言",
    "JSONLD_WEBPAGE_DESC": "为什么 AI 搜索可见性应当可审计、开放，并服务于每一个网站。",
    "FAQ1_NAME": "什么是 GEO Optimizer？",
    "FAQ1_TEXT": "GEO Optimizer 是一个开源工具包，用于审计网站的 AI 搜索可见性。它基于 8 个类别、47 种研究验证的方法对网站打分（0–100），覆盖 robots.txt、llms.txt、Schema JSON-LD、meta 标签、内容质量、技术信号、AI 可发现性以及品牌实体信号。",
    "FAQ2_NAME": "为什么 AI 搜索可见性很重要？",
    "FAQ2_TEXT": "ChatGPT、Perplexity、Claude 等 AI 搜索引擎会综合引用源后给出答案。未针对 AI 可见性优化的网站，将在这些答案中彻底消失。普林斯顿 KDD 2024 研究表明，引用来源可使 AI 可见性提升 27%–115%，统计数据可提升 33%，权威性语气可提升 29%。",
    "FAQ3_NAME": "GEO Optimizer 是免费且开源的吗？",
    "FAQ3_TEXT": "是的。GEO Optimizer 是 MIT 协议开源软件。安装命令：pip install geo-optimizer-skill。评分细则、算法逻辑及所有权重均已公开记录。",
    "FAQ4_NAME": "GEO Optimizer 适用于哪些网站？",
    "FAQ4_TEXT": "GEO Optimizer 适用于任何可公开访问的 URL，与底层技术无关。它审计的是 AI 引擎实际看到的 HTTP 响应，因此无论是静态站点、WordPress、Next.js、自研后端、无头架构，还是任何能响应 HTTP 请求的系统，都能被审计。",

    # Nav
    "NAV_AUDIT": "审计",
    "NAV_COMPARE": "对比",
    "NAV_DOCS": "文档",
    "NAV_MORE": "更多",
    "NAV_RESEARCH": "研究",
    "NAV_ROADMAP": "路线图",
    "NAV_MANIFESTO": "宣言",
    "NAV_GITHUB_CTA": "GitHub",

    # Hero
    "HERO_EYEBROW": "开源 · 研究驱动 · 开发者优先",
    "HERO_H1": "GEO Optimizer<br>宣言",
    "HERO_SUB": "为什么 AI 搜索可见性应当可审计、开放，并服务于每一个网站。",

    # TOC
    "TOC_TITLE": "目录",
    "TOC_S1": "网络已变。大多数网站还没意识到。",
    "TOC_S2": "可见性鸿沟，本质是工具的缺失。",
    "TOC_S3": "GEO Optimizer 主张什么。",
    "TOC_S4": "决定 AI 可见性的八项信号。",
    "TOC_S4B": "分数之外：竞品从未告诉你的事。",
    "TOC_S5": "这是写给谁的。",
    "TOC_S6": "我们做出的承诺。",
    "TOC_S7": "一句话总结。",

    # Section 1
    "SECT_NUM_01": "01 ——",
    "S1_HEADING": "网络已变。大多数网站还没意识到。",
    "S1_PARA_1": "二十年来，搜索引擎的运作方式从未改变：你发布内容，爬虫索引它，用户点击链接。这条链路是清晰的、可审计的、被广泛理解的。一整套围绕它的工具、代理机构和行业知识因此而生——因为这是一个可以被研究、被优化的系统。",
    "S1_BLOCKQUOTE": "这条链路正在断裂。",
    "S1_PARA_2": "当有人向 ChatGPT 提问「哪款项目管理工具最好用」时，他们看到的不是十条蓝色链接，而是一段综合生成的答案。一两个信源被引用，其余的仿佛不存在。当 Perplexity 回答「最好的 Python 数据科学库」时，它不会返回一份 SERP——它会直接给出一个结论。当 Claude 总结「主流 GEO 优化工具」时，它依赖的是一份训练语料与实时检索，绝大多数网站从未针对它们做过优化。",
    "S1_PARA_3": "这就是生成式引擎优化（Generative Engine Optimization）。而此刻，整个网络中的大多数网站，对它仍然是隐形的。",
    "S1_PARA_4": "这场变革并非假设。ChatGPT 在 2025 年初已达到每周 5 亿活跃用户。Perplexity 每月处理数亿次查询。AI 概览（AI Overviews）已出现在相当比例的 Google 搜索结果中。每季度都有更多用户通过 AI 合成的答案首次接触信息。Gartner 预测，到 2026 年传统搜索引擎的流量将下降 25%，被 AI 聊天机器人接管信息类查询。",
    "S1_PARA_5": "而大多数网站，对此毫无准备。",

    # Section 2
    "SECT_NUM_02": "02 ——",
    "S2_HEADING": "可见性鸿沟，本质是工具的缺失。",
    "S2_PARA_1": "问题不在于信号未被揭示。普林斯顿 NLP 团队（KDD 2024）的研究首次量化了真正能提升 AI 引用率的因素：来源引用提升可见性 27%–115%，加入引文提升 41%，加入统计数据提升 33%，权威流畅的文风提升 29%。这些都来自一项基于真实 Perplexity.ai 响应、在 10,000 条查询上验证的同行评审研究。",
    "S2_PARA_2": "AutoGEO（ICLR 2026，卡内基梅隆大学）走得更远——借助基于 LLM 的规则提取与强化学习，在普林斯顿基线之上再提升 50.99%。研究已有，信号已被记录。Answer.AI 发布的 llms.txt 规范已公开，geo-checklist.dev 标准也已存在。从「隐形」到「被引用」的路径，毫无神秘可言。",
    "S2_PARA_3": "问题是，绝大多数网站主根本不知道这一切的存在。",
    "S2_PARA_4": "企业级 SEO 平台正在加入「AI 可见性」仪表板，售价每月数百到数千美元。它们为大型市场团队打造，而不是独立开发者或小型代理商。它们是一座座黑箱花园：只输出分数，却从不解释到底是哪项信号缺失，修复它又值多少。",
    "S2_PARA_5": "与此同时，这些平台分析的所有数据都是公开的。robots.txt 文件人人可查，JSON-LD 结构就在 HTML 源码里，网站是否允许 GPTBot、ClaudeBot、PerplexityBot 几秒钟就能确认。是否正确配置了 llms.txt、/ai/summary.json、FAQPage schema——所有这些，无需订阅即可检查。",
    "S2_BLOCKQUOTE": "可见性鸿沟不是数据问题，而是访问问题，是工具问题。",

    # Section 3 — principles
    "SECT_NUM_03": "03 ——",
    "S3_HEADING": "GEO Optimizer 主张什么。",
    "PRINCIPLE_AUDITABILITY_TITLE": "可审计，而非黑箱",
    "PRINCIPLE_AUDITABILITY_BODY": "如果无法验证分数是如何算出的，那分数毫无意义。我们评分系统里的每一项检查都有据可查，关联到公开发表的研究，并接受任何人的审视。当我们说 Schema JSON-LD 价值 16 分时，你可以逐条读到我们测量的信号及其依据。当我们说一个站点得分 47/100 时，我们会明确指出缺失的 53 分在哪里，以及拿回它们需要做哪些具体动作。",
    "PRINCIPLE_SCIENTIFIC_TITLE": "科学根基，而非营销话术",
    "PRINCIPLE_SCIENTIFIC_BODY": "我们不发明信号。引擎里的每一项检查都源于实证研究或公开规范：普林斯顿 KDD 2024、AutoGEO ICLR 2026、Answer.AI 的 llms.txt 规范、geo-checklist.dev 新兴标准，以及成熟的 schema.org 词汇表。当我们说某项信号在统计上能提升 AI 引用率时，我们附上论文。研究成果更新，权重同步更新。",
    "PRINCIPLE_UNIVERSALITY_TITLE": "通用性，而非平台偏见",
    "PRINCIPLE_UNIVERSALITY_BODY": "无论你的站点跑在什么技术栈上——自研 Rust 后端、静态站点生成器、PHP 单体、无头架构，或介于其间的一切——只要 URL 可公开访问，GEO Optimizer 就能工作。AI 引擎看到的就是 HTTP 响应，我们审计的也是 HTTP 响应。本工具没有「支持的平台」这一概念：只要能响应 HTTP 请求，我们就能审计。",
    "PRINCIPLE_OPEN_TITLE": "开源，而非设卡",
    "PRINCIPLE_OPEN_BODY": "算法公开，权重写在源码里，评分细则写在文档里。每一项架构决策、每一次权重调整、每一项新增检查，都出现在 git 历史中，并配有解释其理由的 commit message。你可以自由 fork、扩展、接入自己的 CI 流水线、对自己的基础设施运行它，并把改进回馈给社区——无需申请许可，无需支付授权费。可见性不该建立在订阅之上。",
    "PRINCIPLE_PRECISION_TITLE": "精确，而非噪音",
    "PRINCIPLE_PRECISION_BODY": "一份给出 50 条模糊建议的审计，对谁都没有帮助。我们给出的每条建议都具体、可执行，并对应明确的分数影响。「添加 FAQPage schema：+3 分」「在 robots.txt 中放行 OAI-SearchBot：+13 分」「创建至少 1000 词的 /llms.txt：+4 分」。你对自己付出的每分努力得到什么回报一清二楚，并可以按投入产出比排序。",
    "PRINCIPLE_DEVELOPER_TITLE": "把开发者体验当作一等公民",
    "PRINCIPLE_DEVELOPER_BODY": "网页界面用于探索，真正的活儿在 CLI 里完成。JSON 输出能干净地管道到其他工具；通过 geo-action 接入 CI；为 AI Agent 工作流提供 MCP 服务器；为自定义集成与监控脚本提供 Python API。GEO Optimizer 由开发者打造、为开发者打造，前提是：一个工具只有自然融入现有工作流，才会被真正用起来。",

    # Section 4 — eight signals
    "SECT_NUM_04": "04 ——",
    "S4_HEADING": "决定 AI 可见性的八项信号。",
    "SIG_ROBOTS_NAME": "robots.txt",
    "SIG_ROBOTS_PTS": "满分 18 分",
    "SIG_ROBOTS_DESC": "你是否放行了正确的爬虫？OAI-SearchBot、ClaudeBot、Claude-SearchBot 与 PerplexityBot 是驱动 ChatGPT、Claude、Perplexity 实时引用的爬虫。如果它们被屏蔽——无论是显式屏蔽还是过于严格的通配规则——无论内容多好，默认你就是隐形的。这是最常被错配的信号，也是最快可以修复的信号。",
    "SIG_LLMS_NAME": "llms.txt",
    "SIG_LLMS_PTS": "满分 18 分",
    "SIG_LLMS_DESC": "面向机器可读的站点上下文新标准。由 Answer.AI 提出，llms.txt 为 AI Agent 提供一份关于你内容、能力、文档的结构化索引——无需爬取并解析成百上千页面。可以把它理解为「为语言模型重写的 sitemap.xml」。深度很关键：极简版本只得 5 分；结构完善、内容详尽，并附带 llms-full.txt 的版本，可拿满 18 分。",
    "SIG_SCHEMA_NAME": "Schema JSON-LD",
    "SIG_SCHEMA_PTS": "满分 16 分",
    "SIG_SCHEMA_DESC": "结构化数据一直都在帮搜索引擎。对 AI 引擎而言，它是把实体、关系、事实变成机器可读形式的桥梁。FAQPage schema 直接回答问题；Article schema 表达新鲜度与作者归属；Organization schema 确立法人身份；WebSite schema 提供规范化上下文。Schema 的丰富度——相关属性的数量、是否存在 sameAs 知识图谱链接——与 schema 类型本身同等重要。",
    "SIG_META_NAME": "Meta 标签",
    "SIG_META_PTS": "满分 14 分",
    "SIG_META_DESC": "基本功：描述性的标题、准确概括页面的 meta description、避免重复内容混淆的 canonical URL，以及让 AI Agent 与社交平台拥有结构化上下文的 Open Graph 标签。这些信号在传统搜索时代重要了几十年，对 AI 搜索同样重要——原因相同：它们是关于「页面在讲什么」最清晰、最明确的信号。",
    "SIG_CONTENT_NAME": "内容质量",
    "SIG_CONTENT_PTS": "满分 12 分",
    "SIG_CONTENT_DESC": "具体数字、外部引用、清晰的 H2/H3 标题层级、关键信息前置在前 30% 内容、用列表与表格打破密集长段、达到一定字数门槛以体现内容分量。普林斯顿的研究结论毫不含糊：具体、结构清晰、可被引用的内容被引用得更多；含糊、堆砌术语、组织混乱的内容被忽略。",
    "SIG_TECH_NAME": "技术信号",
    "SIG_TECH_PTS": "满分 6 分",
    "SIG_TECH_DESC": "<html> 元素上的语言声明、可发现的 RSS 或 Atom 订阅、通过 schema 中 dateModified 或 HTTP Last-Modified 头表达的新鲜度指标。单看每项都很小，但它们共同建立了语境、新近度与可信度——这是 AI 引擎判断「你的内容是否值得引用」时的基线信誉。",
    "SIG_DISCOVERY_NAME": "AI 可发现性",
    "SIG_DISCOVERY_PTS": "满分 6 分",
    "SIG_DISCOVERY_DESC": "面向机器可读服务上下文的新标准：/.well-known/ai.txt 用于爬虫权限，/ai/summary.json 用于结构化的能力描述，/ai/faq.json 用于预先回答的常见问题，/ai/service.json 用于端点与功能发现。这些文件之于 AI Agent，正如 robots.txt 当年之于传统爬虫——它是你站点与将引用它的系统之间的一次结构化握手。",
    "SIG_BRAND_NAME": "品牌与实体信号",
    "SIG_BRAND_PTS": "满分 10 分",
    "SIG_BRAND_DESC": "AI 引擎不只是索引页面，它还在为实体建模。品牌名在 H1、title、og:title 与 schema Organization name 之间保持一致，是一切的基础。通过 sameAs 指向 Wikipedia、Wikidata、LinkedIn、Crunchbase 的知识图谱关联，证明你的品牌是一个已被知晓、被认可的实体，而不仅仅是一串陌生文本。关于我们与联系方式页面，则在传递「内容背后站着真实组织」的信号。地理身份与领域权威共同补全了 AI 引擎用来决定「该多大程度上信任并引用你的内容」的实体模型。",

    # Section 4b — beyond the score
    "SECT_NUM_04B": "04b ——",
    "S4B_HEADING": "分数之外：竞品从未告诉你的事。",
    "S4B_INTRO": "0–100 的分数只是一个维度。真实世界里的 AI 可见性，还取决于一些无法轻易折算成数字的因素。GEO Optimizer 额外运行六项信息性检查，揭示竞品当前检测不到的风险与信号：",
    "BEYOND_PROMPT_NAME": "提示词注入检测",
    "BEYOND_PROMPT_PTS": "安全",
    "BEYOND_PROMPT_DESC": "八类 AI 操控模式：通过 CSS 隐藏的文本、不可见的 Unicode 字符、内嵌于内容的直接 LLM 指令、HTML 注释中的提示词注入、单色伪装文本、微小字号注入、data 属性滥用、aria-hidden 漏洞利用。基于 UC Berkeley EMNLP 2024 研究。严重等级：干净、可疑、严重。",
    "BEYOND_TRUST_NAME": "信任栈评分",
    "BEYOND_TRUST_PTS": "5 个层次",
    "BEYOND_TRUST_DESC": "从五个维度给出的综合信任评估：技术信任（HTTPS、安全响应头）、身份信任（作者归属、组织、关于页面）、社交信任（sameAs 链接、客户证言、社交档案）、学术信任（引用、统计、权威信源）、一致性信任（title、H1、schema、meta 之间不存在矛盾）。等级 A 到 F。",
    "BEYOND_NEG_NAME": "负面信号",
    "BEYOND_NEG_PTS": "反引用",
    "BEYOND_NEG_DESC": "八项会主动降低你被引用概率的信号：过多的 CTA、弹窗/模态干扰、内容稀薄、死链、关键词堆砌、缺失作者归属、过高的模板化比例、承诺与交付之间的错位信号。基于 UC Berkeley 关于「AI 引擎主动避免引用什么」的研究。",
    "BEYOND_CDN_NAME": "CDN 爬虫访问",
    "BEYOND_CDN_PTS": "访问",
    "BEYOND_CDN_DESC": "检测 Cloudflare、Akamai、Vercel 等 CDN/WAF 配置是否在悄悄屏蔽 AI 爬虫。许多站点以为自己已经放行 GPTBot，因为 robots.txt 里写了——但 CDN 对真实爬虫返回的是 403 或验证码。本检查以真实 Bot User-Agent 发起请求并对比响应。",
    "BEYOND_JS_NAME": "JS 渲染",
    "BEYOND_JS_PTS": "访问",
    "BEYOND_JS_DESC": "检测关键内容是否仅在 JavaScript 执行后才出现。SPA 框架（React、Vue、Angular）常常把内容渲染放到客户端——这对于不执行 JS 的爬虫而言是隐形的。本检查比对原始 HTML 响应与应有的内容信号，并标记那些表明「依赖 JS 渲染」的框架特征模式。",
    "BEYOND_WEBMCP_NAME": "WebMCP 就绪度",
    "BEYOND_WEBMCP_PTS": "未来",
    "BEYOND_WEBMCP_DESC": "衡量站点为兼容 MCP 的 AI Agent 暴露机器可读上下文的水平。检测 registerTool() 模式、toolname 属性，以及 potentialAction schema。四个就绪等级：无、基础、就绪、先进。这项信号为下一代 AI Agent 提前布局——它们消费的不只是爬到的内容，更是结构化上下文，并在生成回答前先行利用。",
    "S4B_OUTRO": "这六项检查不计入分数。它们揭示的是分数本身看不见的问题——而你的竞品工具，根本没有在检查这些。",

    # Section 5 — audience
    "SECT_NUM_05": "05 ——",
    "S5_HEADING": "这是写给谁的。",
    "AUDIENCE_ITEM_1": "每一位发布过项目、并疑惑过「它为什么没出现在 AI 关于这个问题的回答里」的开发者。",
    "AUDIENCE_ITEM_2": "每一位管理客户站点、需要随搜索行为根本性迁移而保持可见性的代理商。",
    "AUDIENCE_ITEM_3": "每一位负担不起企业级 SEO 工具、却明白自然可见性攸关存亡的独立创始人——他们也清楚，规则变化的速度比大多数人意识到的更快。",
    "AUDIENCE_ITEM_4": "每一位技术写作者、文档团队与开源维护者，希望当 AI 助手回答其内容直接覆盖的问题时，他们的工作能被引用。",
    "AUDIENCE_ITEM_5": "每一位希望把 GEO 检查接入 CI 流水线的 DevOps 工程师——就像接入 lint、安全扫描、性能预算一样自然。",
    "AUDIENCE_ITEM_6": "每一位希望以实证方式理解「AI 引用机制当下真实状态」的研究者。",

    # Section 6 — commitments
    "SECT_NUM_06": "06 ——",
    "S6_HEADING": "我们做出的承诺。",
    "COMMIT_1_TITLE": "核心工具将始终保持开源。",
    "COMMIT_1_BODY": "每一项评分决策都将记录在案。每一处评分细则的变更，都将附带理由出现在更新日志里。如果我们对信号的判断有误，我们会承认，并更新权重。",
    "COMMIT_2_TITLE": "我们首先为开发者打造。",
    "COMMIT_2_BODY": "这意味着：行为符合直觉的 CLI、能干净管道传输的 JSON 输出、以及对基础审计无需鉴权的 API。复杂度藏在选项里，而不是默认里。",
    "COMMIT_3_TITLE": "我们会坦诚面对不确定性。",
    "COMMIT_3_BODY": "GEO 是一个年轻的领域。今天重要的某些信号，随着 AI 架构演进可能变得不那么重要；而我们尚未测量的某些信号，未来可能被证明至关重要。一旦证据变化，我们就更新评分细则，并把原因写下来——而不是悄悄重新校准、假装没人察觉。",
    "COMMIT_4_TITLE": "我们不出售审计额度，也不会把核心功能放进付费墙后。",
    "COMMIT_4_BODY": "你看到的分数就是真实分数。你看到的建议就是真实建议。竞品付费版里的每一项功能，都应当出现在开源工具里。",

    # Section 7 — bottom line
    "SECT_NUM_07": "07 ——",
    "S7_HEADING": "一句话总结。",
    "BOTTOMLINE_PARA_1": "AI 搜索是人们在线发现、评估并信任信息方式的下一场重大变革。决定这场变革中可见性的信号，如今是可测量、有据可查、可优化的。",
    "BOTTOMLINE_PARA_2": "而大多数网站对此一无所知。这个窗口期不会永远敞开。",
    "BOTTOMLINE_PARA_3": "那些现在就开始行动的站点——为可被引用而结构化内容、让自己对 AI Agent 可发现、建立实体一致性与知识图谱存在——将在 AI 搜索成为主流渠道、所有人开始仓促应对之时，获得持久优势。",
    "BOTTOMLINE_PARA_4": "GEO Optimizer 的存在，是为了把这份准备工作变得务实、透明、人人可及——不只是面向拥有企业预算的团队，更是面向每一位开发者、每一位代理商、每一位独立创始人、每一位开源维护者：所有希望在被日益介入「世界如何发现信息」的系统里被看见的人。",
    "BOTTOMLINE_PARA_5": "你不应该需要订阅，才能知道自己的网站有没有被看见。",
    "BOTTOMLINE_CONCLUSION": "这就是这个工具存在的理由，也将是它持续要做的事。",

    # Footer
    "FOOTER_GITHUB": "GitHub",
    "FOOTER_PYPI": "PyPI",
    "FOOTER_DOCS": "文档",
    "FOOTER_ABOUT": "关于 skywalkerqqq",
    "FOOTER_ISSUES": "问题反馈",
    "FOOTER_RUNAUDIT": "立即审计",
    "FOOTER_CREDIT": "GEO Optimizer 是开源软件，基于 MIT 协议 · 由 skywalkerqqq 打造 · 受益于普林斯顿 KDD 2024 + AutoGEO ICLR 2026 研究",

    # Cookie floating button
    "COOKIE_TITLE": "Cookie 设置",
}


PAGES = {
    "manifesto.html": {"en": _M_EN, "zh": _M_ZH},
}


# ─────────────────────────────────────────────────────────────────────────
# RESEARCH (peer-reviewed papers powering the scoring engine)
# ─────────────────────────────────────────────────────────────────────────

_R_EN = {
    # Metadata / SEO
    "TITLE": "Research Foundation — GEO Optimizer",
    "META_DESC": "GEO Optimizer is built on peer-reviewed academic research. Princeton KDD 2024, AutoGEO ICLR 2026, and more.",
    "OG_TITLE": "Research Foundation — GEO Optimizer",
    "OG_DESC": "GEO Optimizer is built on peer-reviewed academic research. Princeton KDD 2024, AutoGEO ICLR 2026, and more.",
    "OG_LOCALE": "en_US",

    # Nav (intentionally re-declared per page; do not share across pages)
    "NAV_AUDIT": "Audit",
    "NAV_COMPARE": "Compare",
    "NAV_DOCS": "Docs",
    "NAV_MORE": "More",
    "NAV_RESEARCH": "Research",
    "NAV_ROADMAP": "Roadmap",
    "NAV_MANIFESTO": "Manifesto",
    "NAV_GITHUB": "GitHub",
    "TITLE_COOKIE": "Cookie settings",
    "ARIA_COOKIE": "Cookie settings",
    "ARIA_MENU": "Menu",

    # Hero
    "HERO_H1": "Research Foundation",
    "HERO_P": "Built on peer-reviewed science, not marketing claims.",

    # Paper 1 — GEO (Princeton KDD 2024)
    "P1_H2": "GEO: Generative Engine Optimization",
    "P1_VENUE": "KDD 2024 \u2014 Princeton, Georgia Tech, AI2, IIT Delhi",
    "P1_FINDING": "Tested 9 optimization strategies across 10,000 queries on GEO-bench. Validated on real Perplexity.ai with 22-37% improvements.",
    "P1_IMPACT_LABEL": "Key:",
    "P1_IMPACT": "Citations increase AI visibility up to +115%. Statistics add +40%. Keyword stuffing has ~0% effect.",
    "P1_M1": "Cite Sources",
    "P1_M2": "Quotations",
    "P1_M3": "Statistics",
    "P1_M4": "Fluency",
    "P1_M5": "Technical Terms",
    "P1_M6": "Authority",
    "P1_M7": "Readability",
    "P1_M8": "Unique Words",
    "P1_M9": "Keyword Stuffing",
    "P1_LINK": "Read paper \u2192",

    # Paper 2 — AutoGEO (CMU ICLR 2026)
    "P2_H2": "AutoGEO: Automatic Generative Engine Optimization",
    "P2_VENUE": "ICLR 2026 \u2014 Carnegie Mellon University",
    "P2_FINDING": "Automatic rule extraction from generative engines via LLMs + reinforcement learning. +50.99% over Princeton baseline. Introduces GEU (utility) metric.",
    "P2_IMPACT_LABEL": "How we use it:",
    "P2_IMPACT": "Informs scoring weight updates. Answer-first structure and passage density checks are based on AutoGEO findings.",
    "P2_LINK": "Read paper \u2192",

    # Paper 3 — C-SEO Bench (Puerto et al., 2025)
    "P3_H2": "C-SEO Bench: Conversational SEO Methods",
    "P3_VENUE": "2025 \u2014 Puerto et al.",
    "P3_FINDING": "Most conversational SEO methods are ineffective and often negative. Gains decrease as adoption increases \u2014 zero-sum competitive dynamic.",
    "P3_IMPACT_LABEL": "How we use it:",
    "P3_IMPACT": "Validates our focus on infrastructure over content manipulation. We build white-hat GEO tools.",
    "P3_LINK": "Read paper \u2192",

    # Paper 4 — Schema Markup & AI Citations (Growth Marshal, Feb 2026)
    "P4_H2": "Schema Markup & AI Citations",
    "P4_VENUE": "Growth Marshal, Feb 2026 \u2014 730 pages",
    "P4_FINDING": "Rich schema (5+ attributes): 61.7% citation rate. Generic schema: 41.6%. Generic actually underperforms no schema.",
    "P4_IMPACT_LABEL": "How we use it:",
    "P4_IMPACT": "Schema richness check differentiates rich vs generic. Generic gets zero bonus.",

    # Paper 5 — AI Citations Report 2026 (OtterlyAI)
    "P5_H2": "AI Citations Report 2026",
    "P5_VENUE": "OtterlyAI \u2014 1M+ citations analyzed",
    "P5_FINDING": "73% of sites have technical barriers blocking AI crawlers. Reference-grade content gets 3-5x more citations.",
    "P5_IMPACT_LABEL": "How we use it:",
    "P5_IMPACT": "robots.txt, CDN, and JS rendering checks address the 73% barrier problem.",

    # Paper 6 — AI Mode Citation Factors (SE Ranking, 2025)
    "P6_H2": "AI Mode Citation Factors",
    "P6_VENUE": "SE Ranking, 2025 \u2014 2.3M pages",
    "P6_FINDING": "Flesch-Kincaid Grade 6-8 is the sweet spot. Sections of 100-150 words are optimal. FAQ schema has zero impact \u2014 only real FAQ content matters.",
    "P6_IMPACT_LABEL": "How we use it:",
    "P6_IMPACT": "Readability, passage density, FAQ-in-content, and section length checks.",

    # Disclaimer
    "DISCLAIMER": "GEO Optimizer focuses on <strong>infrastructure optimization</strong> (robots.txt, llms.txt, schema, meta, content structure) \u2014 not content manipulation. The adversarial research confirms that manipulative techniques degrade the ecosystem.",
}


_R_ZH = {
    # Metadata / SEO
    "TITLE": "研究基石 —— GEO Optimizer",
    "META_DESC": "GEO Optimizer 基于同行评审的学术研究打造。包括 Princeton KDD 2024、AutoGEO ICLR 2026 等。",
    "OG_TITLE": "研究基石 —— GEO Optimizer",
    "OG_DESC": "GEO Optimizer 基于同行评审的学术研究打造。包括 Princeton KDD 2024、AutoGEO ICLR 2026 等。",
    "OG_LOCALE": "zh_CN",

    # Nav (intentionally re-declared per page; do not share across pages)
    "NAV_AUDIT": "审计",
    "NAV_COMPARE": "对比",
    "NAV_DOCS": "文档",
    "NAV_MORE": "更多",
    "NAV_RESEARCH": "研究",
    "NAV_ROADMAP": "路线图",
    "NAV_MANIFESTO": "宣言",
    "NAV_GITHUB": "GitHub",
    "TITLE_COOKIE": "Cookie 设置",
    "ARIA_COOKIE": "Cookie 设置",
    "ARIA_MENU": "菜单",

    # Hero
    "HERO_H1": "研究基石",
    "HERO_P": "依托同行评审的科学，而非营销话术。",

    # Paper 1 — GEO (Princeton KDD 2024)
    "P1_H2": "GEO：生成式引擎优化",
    "P1_VENUE": "KDD 2024 —— Princeton、Georgia Tech、AI2、IIT Delhi",
    "P1_FINDING": "在 GEO-bench 上对 9 种优化策略、10,000 条查询进行测试，并在真实 Perplexity.ai 上验证了 22-37% 的可见性提升。",
    "P1_IMPACT_LABEL": "要点：",
    "P1_IMPACT": "来源引用可将 AI 可见性最多提升 +115%；加入统计数据 +40%；而堆砌关键词几乎没有效果 (~0%)。",
    "P1_M1": "引用来源",
    "P1_M2": "原文引用",
    "P1_M3": "统计数据",
    "P1_M4": "行文流畅",
    "P1_M5": "技术术语",
    "P1_M6": "权威信号",
    "P1_M7": "可读性",
    "P1_M8": "独特用词",
    "P1_M9": "关键词堆砌",
    "P1_LINK": "阅读论文 →",

    # Paper 2 — AutoGEO (CMU ICLR 2026)
    "P2_H2": "AutoGEO：自动生成式引擎优化",
    "P2_VENUE": "ICLR 2026 —— Carnegie Mellon University",
    "P2_FINDING": "通过大模型 + 强化学习自动提取生成式引擎的优化规则。较 Princeton 基线提升 +50.99%，并提出 GEU（效用）指标。",
    "P2_IMPACT_LABEL": "我们怎么用：",
    "P2_IMPACT": "指导评分权重的迭代，「先答后述」结构和段落密度检查均基于 AutoGEO 结论。",
    "P2_LINK": "阅读论文 →",

    # Paper 3 — C-SEO Bench (Puerto et al., 2025)
    "P3_H2": "C-SEO Bench：对话式 SEO 方法评测",
    "P3_VENUE": "2025 —— Puerto 等",
    "P3_FINDING": "大多数对话式 SEO 方法实际无效甚至带来负收益；当采用者增多，效果反而递减——典型的零和博弈。",
    "P3_IMPACT_LABEL": "我们怎么用：",
    "P3_IMPACT": "佐证了「基础设施优先、内容操控让位」的方向。GEO Optimizer 只做白帽工具。",
    "P3_LINK": "阅读论文 →",

    # Paper 4 — Schema Markup & AI Citations (Growth Marshal, Feb 2026)
    "P4_H2": "结构化标记与 AI 引用",
    "P4_VENUE": "Growth Marshal，2026 年 2 月 —— 730 个页面",
    "P4_FINDING": "丰富结构化标记（5+ 属性）引用率达 61.7%；通用结构化标记为 41.6%，甚至不如完全没有结构化标记。",
    "P4_IMPACT_LABEL": "我们怎么用：",
    "P4_IMPACT": "结构化标记丰富度检查区分「丰富」与「通用」，通用项不获得加分。",

    # Paper 5 — AI Citations Report 2026 (OtterlyAI)
    "P5_H2": "AI 引用报告 2026",
    "P5_VENUE": "OtterlyAI —— 分析了 1M+ 次引用",
    "P5_FINDING": "73% 的网站存在阻挡 AI 抓取的技术性壁垒；参考级内容获得 3-5 倍更多引用。",
    "P5_IMPACT_LABEL": "我们怎么用：",
    "P5_IMPACT": "通过 robots.txt、CDN、JS 渲染等检查直击那 73% 的壁垒问题。",

    # Paper 6 — AI Mode Citation Factors (SE Ranking, 2025)
    "P6_H2": "AI 模式引用影响因素",
    "P6_VENUE": "SE Ranking，2025 —— 230 万个页面",
    "P6_FINDING": "Flesch-Kincaid 6-8 年级难度最理想；100-150 字的段落长度最优；FAQ 结构化标记则毫无作用——只有真正落到正文的 FAQ 内容才有用。",
    "P6_IMPACT_LABEL": "我们怎么用：",
    "P6_IMPACT": "分别落实为可读性、段落密度、正文内 FAQ、章节长度四项检查。",

    # Disclaimer
    "DISCLAIMER": "GEO Optimizer 聚焦于<strong>基础设施优化</strong>（robots.txt、llms.txt、结构化标记、meta、正文结构）——而非内容操控。对抗性研究证明，操控型手法只会拖累整个生态。",
}


PAGES["research.html"] = {"en": _R_EN, "zh": _R_ZH}


# ─────────────────────────────────────────────────────────────────────────
# ROADMAP (Now / Next / Later — public roadmap page)
# ─────────────────────────────────────────────────────────────────────────

_RM_EN = {
    # Metadata / SEO
    "TITLE": "Roadmap \u2014 GEO Optimizer",
    "META_DESC": "GEO Optimizer roadmap: what we're building now, what's next, and what we're exploring.",
    "OG_TITLE": "Roadmap \u2014 GEO Optimizer",
    "OG_DESC": "GEO Optimizer roadmap: what we're building now, what's next, and what we're exploring.",
    "OG_LOCALE": "en_US",

    # Nav (intentionally re-declared per page; do not share across pages)
    "NAV_AUDIT": "Audit",
    "NAV_COMPARE": "Compare",
    "NAV_DOCS": "Docs",
    "NAV_MORE": "More",
    "NAV_RESEARCH": "Research",
    "NAV_ROADMAP": "Roadmap",
    "NAV_MANIFESTO": "Manifesto",
    "NAV_GITHUB": "GitHub",
    "ARIA_MENU": "Menu",
    "TITLE_COOKIE": "Cookie settings",
    "ARIA_COOKIE": "Cookie settings",

    # Hero
    "HERO_H1": "Roadmap",
    "HERO_P": "Where GEO Optimizer is heading. No dates, just direction.",

    # Phase: Now
    "PHASE_NOW_TAG": "Now",
    "PHASE_NOW_HEAD": "In Development",
    "PHASE_NOW_L1": "AI Visibility Checker \u2014 are you being cited by ChatGPT, Perplexity, Claude?",
    "PHASE_NOW_L2": "Visual audit dashboard with radar charts",
    "PHASE_NOW_L3": "Scheduled monitoring with trend tracking",
    "PHASE_NOW_L4": "REST API for third-party integrations",
    "PHASE_NOW_L5": "Prompt injection detection (GEO security) \u2713 Implemented",

    # Phase: Next
    "PHASE_NEXT_TAG": "Next",
    "PHASE_NEXT_HEAD": "Planned",
    "PHASE_NEXT_L1": "WordPress plugin with admin dashboard",
    "PHASE_NEXT_L2": "Server log analysis for AI crawler activity",
    "PHASE_NEXT_L3": "Multi-site batch audit with CSV export",
    "PHASE_NEXT_L4": "Competitor comparison reports",
    "PHASE_NEXT_L5": "Slack/Discord notifications on score changes",

    # Phase: Later
    "PHASE_LATER_TAG": "Later",
    "PHASE_LATER_HEAD": "Exploring",
    "PHASE_LATER_L1": "WebMCP agent-readiness audit",
    "PHASE_LATER_L2": "Topical cluster architecture analysis",
    "PHASE_LATER_L3": "Trust Stack \u2014 5-layer trust signal aggregation",
    "PHASE_LATER_L4": "Multi-language GEO optimization",

    # Note paragraph (lead + connectors + tail)
    "NOTE_LEAD": "Want to influence the roadmap?",
    "NOTE_OR": "or",
    "NOTE_TAIL": ".",
    "NOTE_ISSUE": "Open an issue",
    "NOTE_DISCUSSION": "start a discussion",
}


_RM_ZH = {
    # Metadata / SEO
    "TITLE": "路线图 —— GEO Optimizer",
    "META_DESC": "GEO Optimizer 路线图：我们正在做的、即将做的、以及正在探索的。",
    "OG_TITLE": "路线图 —— GEO Optimizer",
    "OG_DESC": "GEO Optimizer 路线图：我们正在做的、即将做的、以及正在探索的。",
    "OG_LOCALE": "zh_CN",

    # Nav (intentionally re-declared per page; do not share across pages)
    "NAV_AUDIT": "审计",
    "NAV_COMPARE": "对比",
    "NAV_DOCS": "文档",
    "NAV_MORE": "更多",
    "NAV_RESEARCH": "研究",
    "NAV_ROADMAP": "路线图",
    "NAV_MANIFESTO": "宣言",
    "NAV_GITHUB": "GitHub",
    "ARIA_MENU": "菜单",
    "TITLE_COOKIE": "Cookie 设置",
    "ARIA_COOKIE": "Cookie 设置",

    # Hero
    "HERO_H1": "路线图",
    "HERO_P": "GEO Optimizer 的前进方向。只讲趋势，不报日期。",

    # Phase: Now
    "PHASE_NOW_TAG": "现在",
    "PHASE_NOW_HEAD": "开发中",
    "PHASE_NOW_L1": "AI 可见性检查器 —— 你的内容有没有被 ChatGPT、Perplexity、Claude 引用？",
    "PHASE_NOW_L2": "可视化审计仪表盘 + 雷达图",
    "PHASE_NOW_L3": "定时巡检与趋势追踪",
    "PHASE_NOW_L4": "面向第三方集成的 REST API",
    "PHASE_NOW_L5": "提示词注入检测（GEO 安全）✓ 已落地",

    # Phase: Next
    "PHASE_NEXT_TAG": "下一步",
    "PHASE_NEXT_HEAD": "规划中",
    "PHASE_NEXT_L1": "WordPress 插件 + 管理后台",
    "PHASE_NEXT_L2": "服务器日志分析（识别 AI 爬虫活动）",
    "PHASE_NEXT_L3": "多站点批量审计 + CSV 导出",
    "PHASE_NEXT_L4": "竞品对比报告",
    "PHASE_NEXT_L5": "Slack / Discord 分数变动通知",

    # Phase: Later
    "PHASE_LATER_TAG": "远期",
    "PHASE_LATER_HEAD": "探索中",
    "PHASE_LATER_L1": "WebMCP 智能体可读性审计",
    "PHASE_LATER_L2": "主题集群结构分析",
    "PHASE_LATER_L3": "Trust Stack —— 五层信任信号聚合",
    "PHASE_LATER_L4": "多语言 GEO 优化",

    # Note paragraph (lead + connectors + tail)
    "NOTE_LEAD": "想影响路线图方向？去",
    "NOTE_OR": "，或者",
    "NOTE_TAIL": "。",
    "NOTE_ISSUE": "提交 issue",
    "NOTE_DISCUSSION": "开个讨论",
}


PAGES["roadmap.html"] = {"en": _RM_EN, "zh": _RM_ZH}


# ─────────────────────────────────────────────────────────────────────────
# COMPARE (side-by-side website comparison)
# ─────────────────────────────────────────────────────────────────────────

_C_EN = {
    # Metadata / SEO
    "TITLE": "Compare GEO Scores — GEO Optimizer",
    "META_DESC": "Compare GEO scores between two websites side by side.",
    "OG_TITLE": "Compare GEO Scores — GEO Optimizer",
    "OG_DESC": "Compare GEO scores between two websites side by side.",
    "OG_LOCALE": "en_US",

    # Nav (intentionally re-declared per page; do not share across pages)
    # compare.html nav does NOT have an Analyze link.
    "NAV_AUDIT": "Audit",
    "NAV_COMPARE": "Compare",
    "NAV_DOCS": "Docs",
    "NAV_MORE": "More",
    "NAV_RESEARCH": "Research",
    "NAV_ROADMAP": "Roadmap",
    "NAV_MANIFESTO": "Manifesto",
    "NAV_GITHUB": "GitHub",
    "ARIA_MENU": "Menu",
    "TITLE_COOKIE": "Cookie settings",
    "ARIA_COOKIE": "Cookie settings",

    # Hero
    "HERO_H1": "Compare GEO Scores",
    "HERO_P": "Side-by-side — see who's more visible to AI",

    # Form
    "FORM_ARIA_URL1": "First website URL to compare",
    "FORM_ARIA_URL2": "Second website URL to compare",
    "FORM_VS": "VS",
    "BTN_COMPARE": "Compare",

    # Spinner
    "SPIN_MSG": "Analyzing both sites... this may take up to 60 seconds.",
}


_C_ZH = {
    # Metadata / SEO
    "TITLE": "对比 GEO 评分 —— GEO Optimizer",
    "META_DESC": "并排对比两个网站的 GEO 评分。",
    "OG_TITLE": "对比 GEO 评分 —— GEO Optimizer",
    "OG_DESC": "并排对比两个网站的 GEO 评分。",
    "OG_LOCALE": "zh_CN",

    # Nav (intentionally re-declared per page; do not share across pages)
    # compare.html nav does NOT have an Analyze link.
    "NAV_AUDIT": "审计",
    "NAV_COMPARE": "对比",
    "NAV_DOCS": "文档",
    "NAV_MORE": "更多",
    "NAV_RESEARCH": "研究",
    "NAV_ROADMAP": "路线图",
    "NAV_MANIFESTO": "宣言",
    "NAV_GITHUB": "GitHub",
    "ARIA_MENU": "菜单",
    "TITLE_COOKIE": "Cookie 设置",
    "ARIA_COOKIE": "Cookie 设置",

    # Hero
    "HERO_H1": "对比 GEO 评分",
    "HERO_P": "并排呈现 —— 一眼看出谁对 AI 更可见",

    # Form
    "FORM_ARIA_URL1": "要对比的第一个站点 URL",
    "FORM_ARIA_URL2": "要对比的第二个站点 URL",
    "FORM_VS": "对",
    "BTN_COMPARE": "开始对比",

    # Spinner
    "SPIN_MSG": "正在同时分析两个站点……最长约 60 秒。",
}


PAGES["compare.html"] = {"en": _C_EN, "zh": _C_ZH}


# ─────────────────────────────────────────────────────────────────────────
# ANALYZE COMPETITORS (narrative analysis)
# ─────────────────────────────────────────────────────────────────────────

_AC_EN = {
    # Metadata / SEO
    "TITLE": "Analyze Competitors — GEO Optimizer",
    "META_DESC": "See how AI search engines describe your competitors vs your brand.",
    "OG_TITLE": "Analyze Competitors — GEO Optimizer",
    "OG_DESC": "See how AI search engines describe your competitors vs your brand.",
    "OG_LOCALE": "en_US",

    # Nav (intentionally re-declared per page; do not share across pages)
    # analyze_competitors.html nav has Analyze as the active link.
    "NAV_AUDIT": "Audit",
    "NAV_COMPARE": "Compare",
    "NAV_ANALYZE": "Analyze",
    "NAV_DOCS": "Docs",
    "NAV_MORE": "More",
    "NAV_RESEARCH": "Research",
    "NAV_ROADMAP": "Roadmap",
    "NAV_MANIFESTO": "Manifesto",
    "NAV_GITHUB": "GitHub",
    "ARIA_MENU": "Menu",
    "TITLE_COOKIE": "Cookie settings",
    "ARIA_COOKIE": "Cookie settings",

    # Hero
    "HERO_H1": "Analyze Competitive Narratives",
    "HERO_P": "See how AI search engines describe your competitors vs your brand",

    # Form
    "FORM_ARIA_TARGET": "Your website URL",
    "FORM_LABEL_COMPETITORS": "Competitor URLs (comma-separated)",
    "FORM_ARIA_COMPETITORS": "Competitor URLs",
    "FORM_HINT_COMPETITORS": "Enter up to 5 competitors",
    "BTN_ANALYZE": "Analyze",

    # Spinner
    "SPIN_MSG": "Analyzing... this may take up to 90 seconds.",

    # Results section headings
    "RES_SUMMARY_H2": "Executive Summary",
    "RES_NARRATIVES_H2": "Competitor Narratives",
    "RES_GAPS_H2": "Competitive Gaps",

    # Gap table header columns
    "GAP_TH_CATEGORY": "Category",
    "GAP_TH_COMPETITOR": "Competitor",
    "GAP_TH_TYPE": "Gap Type",
    "GAP_TH_MISSING": "Missing From Your Content",
    "GAP_TH_SUGGESTION": "Suggestion",
}


_AC_ZH = {
    # Metadata / SEO
    "TITLE": "竞品叙事分析 —— GEO Optimizer",
    "META_DESC": "看 AI 搜索引擎如何描述你的竞品，以及如何描述你的品牌。",
    "OG_TITLE": "竞品叙事分析 —— GEO Optimizer",
    "OG_DESC": "看 AI 搜索引擎如何描述你的竞品，以及如何描述你的品牌。",
    "OG_LOCALE": "zh_CN",

    # Nav (intentionally re-declared per page; do not share across pages)
    # analyze_competitors.html nav has Analyze as the active link.
    "NAV_AUDIT": "审计",
    "NAV_COMPARE": "对比",
    "NAV_ANALYZE": "竞品",
    "NAV_DOCS": "文档",
    "NAV_MORE": "更多",
    "NAV_RESEARCH": "研究",
    "NAV_ROADMAP": "路线图",
    "NAV_MANIFESTO": "宣言",
    "NAV_GITHUB": "GitHub",
    "ARIA_MENU": "菜单",
    "TITLE_COOKIE": "Cookie 设置",
    "ARIA_COOKIE": "Cookie 设置",

    # Hero
    "HERO_H1": "竞品叙事分析",
    "HERO_P": "看 AI 搜索引擎如何描述你的竞品，以及如何描述你的品牌",

    # Form
    "FORM_ARIA_TARGET": "你的站点 URL",
    "FORM_LABEL_COMPETITORS": "竞品 URL（英文逗号分隔）",
    "FORM_ARIA_COMPETITORS": "竞品 URL 列表",
    "FORM_HINT_COMPETITORS": "最多输入 5 个竞品",
    "BTN_ANALYZE": "开始分析",

    # Spinner
    "SPIN_MSG": "正在分析……最长约 90 秒。",

    # Results section headings
    "RES_SUMMARY_H2": "执行摘要",
    "RES_NARRATIVES_H2": "竞品叙事",
    "RES_GAPS_H2": "差距分析",

    # Gap table header columns
    "GAP_TH_CATEGORY": "类别",
    "GAP_TH_COMPETITOR": "竞品",
    "GAP_TH_TYPE": "缺口类型",
    "GAP_TH_MISSING": "你内容里缺失的",
    "GAP_TH_SUGGESTION": "建议补充",
}


PAGES["analyze_competitors.html"] = {"en": _AC_EN, "zh": _AC_ZH}




_PRIV_EN = {
    "ARIA_COOKIE": 'Cookie settings',
    "ARIA_MENU": 'Menu',
    "FOOT_CREATED": 'This Privacy Policy was created on May 4, 2026.',
    "FOOT_UPDATED": 'Last updated: May 4, 2026',
    "F_HOME": 'Home',
    "F_PRIVACY": 'Privacy',
    "HDR_BADGE": 'GDPR Compliant',
    "HDR_CONTROLLER_LBL": 'Data Controller:',
    "HDR_CONTROLLER_NAME": 'skywalkerqqq',
    "HDR_DATE": 'May 4, 2026',
    "HDR_H1": 'Privacy Policy',
    "HDR_LAST_UPDATED": 'Last updated:',
    "L1A_LBL": 'Technical cookies:',
    "L1A_TXT": 'to maintain the session and your preferences',
    "L1B_LBL": 'IP address:',
    "L1B_TXT": '(for security purposes only, not for tracking)',
    "L1C_LBL": 'Device information:',
    "L1C_TXT": 'browser type, operating system',
    "L1D_LBL": 'Log data:',
    "L1D_TXT": 'pages visited, access time, visit duration',
    "L2A_LBL": 'URLs to audit:',
    "L2A_TXT": 'to provide the SEO analysis service',
    "L2B_LBL": 'Comments and feedback:',
    "L2B_TXT": 'submitted via contact form',
    "L2C_LBL": 'Contact details:',
    "L2C_TXT": 'if you reach out to us, only if voluntarily provided',
    "META_DESC": 'Privacy policy for skywalkerqqq.github.io/geo-optimizer-skill - GEO Optimizer',
    "NAV_AUDIT": 'Audit',
    "NAV_COMPARE": 'Compare',
    "NAV_DOCS": 'Docs',
    "NAV_GITHUB": 'GitHub',
    "NAV_MANIFESTO": 'Manifesto',
    "NAV_MORE": 'More',
    "NAV_PRIVACY": 'Privacy',
    "NAV_RESEARCH": 'Research',
    "NAV_ROADMAP": 'Roadmap',
    "S10_HEAD": '10. Policy Updates',
    "S10_P1": 'We reserve the right to modify this Privacy Policy at any time. Changes will take effect upon publication on this page.',
    "S10_P2": 'We will notify you by email (if you have provided an address) or via a notice on the Site in case of significant changes.',
    "S10_P3": 'We encourage you to periodically review this policy to stay informed about how we protect your data.',
    "S11_BRAND": 'skywalkerqqq',
    "S11_EMAIL_LBL": 'Email:',
    "S11_GH_LBL": 'GitHub:',
    "S11_HEAD": '11. Contact',
    "S11_P1": 'For any questions regarding this Privacy Policy or the processing of your data:',
    "S11_ROLE": 'Data Controller',
    "S1_HEAD": '1. Introduction',
    "S1_P1": 'This Privacy Policy describes how we collect, use, and protect your personal data when you use the website <strong>skywalkerqqq.github.io/geo-optimizer-skill</strong> (the &ldquo;Site&rdquo;), owned by <strong>skywalkerqqq</strong>.',
    "S1_P2": 'Respecting your privacy is our top priority. This policy complies with the <strong>General Data Protection Regulation (GDPR)</strong> of the European Union and all applicable privacy regulations.',
    "S1_P3_LEAD": 'If you have questions about this Privacy Policy, contact us at:',
    "S21_HEAD": '2.1 Automatic browsing data',
    "S21_P1": 'When you visit the Site, we automatically collect some browsing information:',
    "S22_HEAD": '2.2 User-provided data',
    "S22_P1": 'When you use our services, the following data may be collected:',
    "S2_HEAD": '2. Data We Collect',
    "S2_P1": 'We collect only the data strictly necessary for the operation of the Site and the provision of our services.',
    "S3_HEAD": '3. Cookies and Tracking',
    "S3_INFO_LBL": 'How to manage cookies:',
    "S3_INFO_TXT": 'You can accept, reject, or manage your cookie preferences at any time by clicking the cookie settings button in the bottom-left corner of the page.',
    "S3_P1": 'We use technical and analytics cookies to improve your browsing experience.',
    "S3_P2A_LBL": 'Essential cookies (required):',
    "S3_P2A_TXT": 'These cookies are essential for the operation of the Site and cannot be disabled. They include cookies for authentication, security, and session preferences.',
    "S3_P2B_LBL": 'Analytics cookies (Google Analytics):',
    "S3_P2B_TXT": 'We use Google Analytics to analyze Site usage. Data is aggregated and anonymized. We do not perform any personal identification. You can disable these cookies via the cookie settings button in the bottom-left corner.',
    "S3_P2C_LBL": 'Marketing cookies (Google Ads):',
    "S3_P2C_TXT": 'Used only with your explicit consent to show personalized ads. Can be disabled at any time.',
    "S4_HEAD": '4. Google Analytics',
    "S4_P1": 'The Site uses Google Analytics, a web analytics service provided by Google LLC (&ldquo;Google&rdquo;). Google uses the collected cookies to analyze user behavior on the Site.',
    "S4_P2_L1": 'Pages visited',
    "S4_P2_L2": 'Time spent on pages',
    "S4_P2_L3": 'Referral source',
    "S4_P2_L4": 'Device type and browser',
    "S4_P2_L5": 'Geographic location (country/region level only, not full IP address)',
    "S4_P2_LBL": 'What we collect:',
    "S4_P3_L1": 'Full IP addresses (they are anonymized)',
    "S4_P3_L2": 'Personally identifiable information',
    "S4_P3_L3": 'Financial or banking information',
    "S4_P3_L4": 'Sensitive data (health, religion, politics, etc.)',
    "S4_P3_LBL": 'What we do NOT collect:',
    "S4_P4_LBL": 'Anonymization:',
    "S4_P4_TXT": "Google Analytics is configured to anonymize users' IP addresses before transmission to Google. Data is retained for 24 months.",
    "S4_P5_LBL": 'Opt-out:',
    "S4_P5_LINK": 'Google Analytics opt-out add-on',
    "S4_P5_POST": 'for your browser.',
    "S4_P5_PRE": 'You can disable Google Analytics by installing the',
    "S5_HEAD": '5. Data Security',
    "S5_L1_LBL": 'Unauthorized access:',
    "S5_L1_TXT": 'protection with two-factor authentication',
    "S5_L2_LBL": 'Disclosure or destruction:',
    "S5_L2_TXT": 'TLS 1.3 encryption for all connections',
    "S5_L3_LBL": 'Alteration:',
    "S5_L3_TXT": 'data integrity verification via checksums',
    "S5_L4_LBL": 'Loss:',
    "S5_L4_TXT": 'regular backups and disaster recovery procedures',
    "S5_P1_LEAD": 'We implement appropriate technical and organizational measures to protect your personal data against:',
    "S5_P2_AND": ' and ',
    "S5_P2_POST": ' servers, both GDPR-compliant with infrastructure in the European Union.',
    "S5_P2_PRE": 'Data is stored on ',
    "S6_HEAD": '6. Data Retention',
    "S7_HEAD": '7. Third-Party Sharing',
    "S7_P1": 'We do not sell or rent your personal data to third parties. We share data only in the following cases:',
    "S7_P2_POST": 'and guarantee levels of data protection compliant with the GDPR.',
    "S7_P2_PRE": 'All the above parties are registered ',
    "S7_P2_SUBPROC": 'sub-processors',
    "S8_HEAD": '8. Your Rights (GDPR)',
    "S8_L1_LBL": 'Access:',
    "S8_L1_TXT": 'obtain confirmation that your data exists and request access to it',
    "S8_L2_LBL": 'Rectification:',
    "S8_L2_TXT": 'request correction of inaccurate or incomplete data',
    "S8_L3_LBL": 'Erasure:',
    "S8_L3_TXT": 'request deletion of your data (right to be forgotten)',
    "S8_L4_LBL": 'Restriction:',
    "S8_L4_TXT": 'restrict the processing of your data in certain circumstances',
    "S8_L5_LBL": 'Portability:',
    "S8_L5_TXT": 'receive your data in a structured, commonly used, machine-readable format',
    "S8_L6_LBL": 'Objection:',
    "S8_L6_TXT": 'object to the processing of your data on legitimate grounds',
    "S8_L7_LBL": 'Withdraw consent:',
    "S8_L7_TXT": 'withdraw consent at any time (without affecting the lawfulness of prior processing)',
    "S8_L8_LBL": 'Lodge a complaint:',
    "S8_L8_TXT": 'submit a complaint to the supervisory authority (the Italian Data Protection Authority &mdash; Garante per la protezione dei dati personali)',
    "S8_P1": 'Under the GDPR, you have the right to:',
    "S8_P2_PRE": 'To exercise your rights, write to: ',
    "S8_P3_DAYS": '30 days',
    "S8_P3_POST": ' of receiving your request. We may ask you to verify your identity for security reasons.',
    "S8_P3_PRE": 'We will respond within ',
    "S9_HEAD": '9. Minors',
    "S9_P1": 'The Site is not directed at persons under the age of 16. We do not intentionally collect personal data from minors. If we discover that we have collected data from a minor, we will delete it within 30 days.',
    "T6_H1": 'Data type',
    "T6_H2": 'Retention period',
    "T6_H3": 'Legal basis',
    "T6_R1_C1": 'Browsing data',
    "T6_R1_C2": '6 months',
    "T6_R1_C3": 'Legitimate interest (Art. 6 GDPR)',
    "T6_R2_C1": 'Analytics cookies',
    "T6_R2_C2": '24 months',
    "T6_R2_C3": 'Consent (Art. 9 GDPR)',
    "T6_R3_C1": 'User feedback',
    "T6_R3_C2": '24 months',
    "T6_R3_C3": 'Legitimate interest',
    "T6_R4_C1": 'Audited URLs',
    "T6_R4_C2": '24 months (anonymized)',
    "T6_R4_C3": 'Legitimate interest',
    "T7_H1": 'Recipient',
    "T7_H2": 'Purpose',
    "T7_H3": 'Country',
    "T7_R1_C1": 'Google LLC',
    "T7_R1_C2": 'Google Analytics (traffic analysis)',
    "T7_R1_C3": 'EU (data centers)',
    "T7_R2_C1": 'GitHub Inc.',
    "T7_R2_C2": 'Site hosting (GitHub Pages)',
    "T7_R2_C3": 'EU (France)',
    "T7_R3_C1": 'Render.com',
    "T7_R3_C2": 'Backend hosting (API)',
    "T7_R3_C3": 'EU (Germany)',
    "TITLE": 'Privacy Policy - GEO Optimizer',
    "TITLE_COOKIE": 'Cookie settings'
}

_PRIV_ZH = {
    "ARIA_COOKIE": 'Cookie 设置',
    "ARIA_MENU": '菜单',
    "FOOT_CREATED": '本隐私政策创建于 2026 年 5 月 4 日。',
    "FOOT_UPDATED": '最后更新：2026 年 5 月 4 日',
    "F_HOME": '首页',
    "F_PRIVACY": '隐私',
    "HDR_BADGE": '符合 GDPR',
    "HDR_CONTROLLER_LBL": '数据控制方：',
    "HDR_CONTROLLER_NAME": 'skywalkerqqq',
    "HDR_DATE": '2026 年 5 月 4 日',
    "HDR_H1": '隐私政策',
    "HDR_LAST_UPDATED": '最后更新：',
    "L1A_LBL": '技术性 Cookie：',
    "L1A_TXT": '用于维持会话与保存你的偏好',
    "L1B_LBL": 'IP 地址：',
    "L1B_TXT": '（仅用于安全目的，绝不用于追踪）',
    "L1C_LBL": '设备信息：',
    "L1C_TXT": '浏览器类型、操作系统',
    "L1D_LBL": '日志数据：',
    "L1D_TXT": '访问页面、访问时间、停留时长',
    "L2A_LBL": '待审计的 URL：',
    "L2A_TXT": '用于提供 SEO 分析服务',
    "L2B_LBL": '评论与反馈：',
    "L2B_TXT": '通过联系表单提交',
    "L2C_LBL": '联系方式：',
    "L2C_TXT": '如你主动联系时自愿提供',
    "META_DESC": 'skywalkerqqq.github.io/geo-optimizer-skill (GEO Optimizer) 的隐私政策',
    "NAV_AUDIT": '审计',
    "NAV_COMPARE": '对比',
    "NAV_DOCS": '文档',
    "NAV_GITHUB": 'GitHub',
    "NAV_MANIFESTO": '宣言',
    "NAV_MORE": '更多',
    "NAV_PRIVACY": '隐私',
    "NAV_RESEARCH": '研究',
    "NAV_ROADMAP": '路线图',
    "S10_HEAD": '10. 政策更新',
    "S10_P1": '我们保留随时修改本隐私政策的权利。变更一经发布即生效。',
    "S10_P2": '若发生重大变更，我们会通过你提供的邮箱或站内通知告知你。',
    "S10_P3": '建议定期查看本政策，以了解我们如何保护你的数据。',
    "S11_BRAND": 'skywalkerqqq',
    "S11_EMAIL_LBL": '邮箱：',
    "S11_GH_LBL": 'GitHub：',
    "S11_HEAD": '11. 联系方式',
    "S11_P1": '如对本隐私政策或你的数据处理有任何疑问：',
    "S11_ROLE": '数据控制方',
    "S1_HEAD": '1. 引言',
    "S1_P1": '本隐私政策说明我们在你访问网站 <strong>skywalkerqqq.github.io/geo-optimizer-skill</strong>（以下简称「本站」）时如何收集、使用和保护你的个人数据。该站由 <strong>skywalkerqqq</strong> 拥有。',
    "S1_P2": '尊重你的隐私是我们的首要原则。本政策遵循欧盟 <strong>《通用数据保护条例》（GDPR）</strong>及所有适用的隐私法规。',
    "S1_P3_LEAD": '如你对本政策有任何疑问，可通过以下方式联系我们：',
    "S21_HEAD": '2.1 自动浏览数据',
    "S21_P1": '当你访问本站时，我们会自动采集部分浏览信息：',
    "S22_HEAD": '2.2 用户主动提供的数据',
    "S22_P1": '当你使用我们的服务时，可能会采集以下数据：',
    "S2_HEAD": '2. 我们收集的数据',
    "S2_P1": '我们仅收集为本站运行与服务提供所必需的最少数据。',
    "S3_HEAD": '3. Cookie 与追踪',
    "S3_INFO_LBL": '如何管理 Cookie：',
    "S3_INFO_TXT": '你可以随时点击页面左下角的 Cookie 设置按钮，接受、拒绝或调整 Cookie 偏好。',
    "S3_P1": '我们使用技术性与分析性 Cookie 来改善你的浏览体验。',
    "S3_P2A_LBL": '必要 Cookie（强制启用）：',
    "S3_P2A_TXT": '这些 Cookie 是本站运行所必需的，无法关闭。它们用于身份认证、安全和会话偏好。',
    "S3_P2B_LBL": '分析 Cookie（Google Analytics）：',
    "S3_P2B_TXT": '我们使用 Google Analytics 分析本站使用情况。所有数据都已聚合并匿名化处理，不进行任何个人身份识别。你可以点击页面左下角的 Cookie 设置按钮关闭这类 Cookie。',
    "S3_P2C_LBL": '营销 Cookie（Google Ads）：',
    "S3_P2C_TXT": '仅在你明确同意后用于展示个性化广告。可随时关闭。',
    "S4_HEAD": '4. Google Analytics',
    "S4_P1": '本站使用 Google Analytics，这是 Google LLC（以下简称「Google」）提供的网站分析服务。Google 利用这些 Cookie 分析用户在本站的行为。',
    "S4_P2_L1": '访问过的页面',
    "S4_P2_L2": '页面停留时间',
    "S4_P2_L3": '来源渠道',
    "S4_P2_L4": '设备类型与浏览器',
    "S4_P2_L5": '地理位置（仅精确到国家/地区级，不含完整 IP）',
    "S4_P2_LBL": '我们采集的内容：',
    "S4_P3_L1": '完整 IP 地址（已匿名化）',
    "S4_P3_L2": '任何可识别个人身份的信息',
    "S4_P3_L3": '金融或银行信息',
    "S4_P3_L4": '敏感数据（健康、宗教、政治等）',
    "S4_P3_LBL": '我们不采集的内容：',
    "S4_P4_LBL": '匿名化：',
    "S4_P4_TXT": 'Google Analytics 在上传至 Google 之前会对用户 IP 做匿名化处理。数据保留 24 个月。',
    "S4_P5_LBL": '退出方式：',
    "S4_P5_LINK": 'Google Analytics 浏览器退出插件',
    "S4_P5_POST": '来关闭 Google Analytics。',
    "S4_P5_PRE": '你可以安装',
    "S5_HEAD": '5. 数据安全',
    "S5_L1_LBL": '未授权访问：',
    "S5_L1_TXT": '通过两步验证等手段防护',
    "S5_L2_LBL": '泄露或损毁：',
    "S5_L2_TXT": '全连接使用 TLS 1.3 加密',
    "S5_L3_LBL": '篡改：',
    "S5_L3_TXT": '通过校验和验证数据完整性',
    "S5_L4_LBL": '丢失：',
    "S5_L4_TXT": '定期备份与灾难恢复流程',
    "S5_P1_LEAD": '我们采取恰当的技术与组织措施，保护你的个人数据免受以下威胁：',
    "S5_P2_AND": ' 与 ',
    "S5_P2_POST": '，两者均符合 GDPR 要求，基础设施位于欧盟境内。',
    "S5_P2_PRE": '数据托管在 ',
    "S6_HEAD": '6. 数据保留期',
    "S7_HEAD": '7. 第三方共享',
    "S7_P1": '我们既不出售也不出租你的个人数据。仅在以下情形共享：',
    "S7_P2_POST": '，并保证数据保护水平符合 GDPR 要求。',
    "S7_P2_PRE": '以上各方均为已登记的',
    "S7_P2_SUBPROC": '数据处理方',
    "S8_HEAD": '8. 你的权利（GDPR）',
    "S8_L1_LBL": '访问权：',
    "S8_L1_TXT": '确认你的数据是否存在，并请求访问',
    "S8_L2_LBL": '更正权：',
    "S8_L2_TXT": '要求更正不准确或不完整的数据',
    "S8_L3_LBL": '删除权：',
    "S8_L3_TXT": '要求删除你的数据（被遗忘权）',
    "S8_L4_LBL": '限制处理权：',
    "S8_L4_TXT": '在特定情况下限制对你的数据的处理',
    "S8_L5_LBL": '可携权：',
    "S8_L5_TXT": '以结构化、常用、机器可读的格式接收你的数据',
    "S8_L6_LBL": '反对权：',
    "S8_L6_TXT": '基于正当理由反对对你的数据的处理',
    "S8_L7_LBL": '撤回同意：',
    "S8_L7_TXT": '随时撤回同意（不影响撤回前已经发生的处理）',
    "S8_L8_LBL": '投诉权：',
    "S8_L8_TXT": '向监管机构（意大利个人数据保护局 Garante per la protezione dei dati personali）提交投诉',
    "S8_P1": '根据 GDPR，你拥有以下权利：',
    "S8_P2_PRE": '如需行使上述权利，请发送邮件至：',
    "S8_P3_DAYS": '30 天',
    "S8_P3_POST": ' 内回复。出于安全考虑，可能会请你验证身份。',
    "S8_P3_PRE": '我们将在收到请求后的 ',
    "S9_HEAD": '9. 未成年人',
    "S9_P1": '本站不面向 16 岁以下用户。我们不会故意收集未成年人的个人数据。若发现误收，将在 30 天内删除。',
    "T6_H1": '数据类型',
    "T6_H2": '保留期',
    "T6_H3": '法律依据',
    "T6_R1_C1": '浏览数据',
    "T6_R1_C2": '6 个月',
    "T6_R1_C3": '正当利益（GDPR 第 6 条）',
    "T6_R2_C1": '分析 Cookie',
    "T6_R2_C2": '24 个月',
    "T6_R2_C3": '同意（GDPR 第 9 条）',
    "T6_R3_C1": '用户反馈',
    "T6_R3_C2": '24 个月',
    "T6_R3_C3": '正当利益',
    "T6_R4_C1": '被审计的 URL',
    "T6_R4_C2": '24 个月（已匿名化）',
    "T6_R4_C3": '正当利益',
    "T7_H1": '接收方',
    "T7_H2": '用途',
    "T7_H3": '所在国家/地区',
    "T7_R1_C1": 'Google LLC',
    "T7_R1_C2": 'Google Analytics（流量分析）',
    "T7_R1_C3": '欧盟（数据中心）',
    "T7_R2_C1": 'GitHub Inc.',
    "T7_R2_C2": '站点托管（GitHub Pages）',
    "T7_R2_C3": '欧盟（法国）',
    "T7_R3_C1": 'Render.com',
    "T7_R3_C2": '后端托管（API）',
    "T7_R3_C3": '欧盟（德国）',
    "TITLE": '隐私政策 —— GEO Optimizer',
    "TITLE_COOKIE": 'Cookie 设置'
}

PAGES['privacy.html'] = {'en': _PRIV_EN, 'zh': _PRIV_ZH}


def page_dict(filename: str, lang: str) -> dict:
    """Return the translation dict for a static page in the requested language.

    Falls back to English for unknown languages. Returns an empty dict for
    pages that haven't been catalogued yet so render_static() remains a
    no-op (English original is returned unchanged).
    """
    pg = PAGES.get(filename, {})
    if lang in pg:
        return pg[lang]
    if "en" in pg:
        return pg["en"]
    return {}
