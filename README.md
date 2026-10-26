<div align="center">

<img src="assets/geoready-logo.svg" alt="GEO Optimizer — Answer Engine Optimization toolkit" width="520"/>

# GEO Optimizer

**开源的生成式引擎优化（GEO）与答案引擎优化（AEO）工具包**

[![PyPI](https://img.shields.io/pypi/v/geo-optimizer-skill?style=flat-square&color=3b82f6)](https://pypi.org/project/geo-optimizer-skill/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-3776ab?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-22c55e?style=flat-square)](LICENSE)
[![MCP](https://img.shields.io/badge/MCP-compatible-8b5cf6?style=flat-square)](https://modelcontextprotocol.io)

### 🌐 [English](#english) · [简体中文](#简体中文)

一条命令，为你的网站打出 **0–100 的 AI 可见度分数**，并告诉你该怎么修。

</div>

---

<a id="english"></a>

## 🌐 English

Move to [简体中文](#简体中文)

### What is GEO Optimizer?

**GEO Optimizer** is a free, open-source CLI (also a Python library, MCP server, and Astro integration) that measures how visible your website is to **AI answer engines** — ChatGPT, Perplexity, Google AI Overviews, Gemini, and Claude — and tells you how to get cited by them.

This discipline goes by several names: **AEO** (Answer Engine Optimization), **GEO** (Generative Engine Optimization), **AI SEO**, **LLM SEO**, and **AI visibility monitoring**. This tool covers all of them.

```bash
# Zero install — score any site against 8 AI-readiness categories
uvx --from geo-optimizer-skill geo audit --url https://yoursite.com
```

It scores your site against **47 research-backed methods** ([Princeton KDD 2024](https://arxiv.org/abs/2311.09735), [AutoGEO ICLR 2026](https://arxiv.org/abs/2510.11438)) and generates the exact fixes — robots.txt bot rules, `llms.txt`, JSON-LD schema, and the content patterns models quote.

### Why AI visibility matters

AI search engines give one synthesized answer and **cite a handful of sources**. If your site isn't one of them, you're invisible — even if you rank #1 on Google.

- **28.3% of ChatGPT's most-cited pages have *zero* organic visibility on Google** (Ahrefs) — AI engines reward different signals than classic SEO.
- Proper JSON-LD schema lifts LLM extraction accuracy **from 16% to 54%** (Semrush test on GPT-4).

### Install

```bash
pip install geo-optimizer-skill
```

### Quick Start

```bash
# Audit any site — score 0-100 with actionable recommendations
geo audit --url https://yoursite.com

# Audit a full sitemap, surface weakest pages first
geo audit --sitemap https://yoursite.com/sitemap.xml --max-urls 25

# Compare before/after versions of a page
geo diff --before https://yoursite.com/page-old --after https://yoursite.com/page-new

# Save history and detect regressions over time
geo audit --url https://yoursite.com --save-history --regression

# What changed since the last snapshot? (CI: --fail-on warning)
geo drift --url https://yoursite.com

# Ask real AI engines: is my brand mentioned? Is my domain cited?
geo citations --brand "YourBrand" --domain yoursite.com --topic "your category"

# Auto-generate all missing files (robots.txt, llms.txt, schema, meta)
geo fix --url https://yoursite.com --apply

# Generate llms.txt from sitemap
geo llms --base-url https://yoursite.com --output ./public/llms.txt

# Generate JSON-LD schema
geo schema --type faq --url https://yoursite.com
```

### What it checks

| Area | Points | What GEO Optimizer looks for |
|------|--------|------------------------------|
| **Robots.txt** | /18 | 27 AI bots across 3 tiers. Citation bots explicitly allowed? |
| **llms.txt** | /18 | Present, H1 + blockquote, sections, links, depth. Companion llms-full.txt? |
| **Schema JSON-LD** | /16 | WebSite, Organization, FAQPage, Article. Schema richness (5+ attributes)? |
| **Meta Tags** | /14 | Title, description, canonical, Open Graph complete? |
| **Content** | /12 | H1, statistics, external citations, heading hierarchy, front-loading? |
| **Brand & Entity** | /10 | Brand coherence, Knowledge Graph links, about page, topic authority |
| **Signals** | /6 | `<html lang>`, RSS/Atom feed, dateModified freshness? |
| **AI Discovery** | /6 | `.well-known/ai.txt`, `/ai/summary.json`, `/ai/faq.json`? |

**Score bands:** 86-100 Excellent · 68-85 Good · 36-67 Foundation · 0-35 Critical

Plus a separate **Citability Score** (0-100) measuring content quality across 47 methods:
Quotation +41% · Statistics +33% · Fluency +29% · Cite Sources +27% · and 43 more.

### Output formats

```bash
geo audit --url https://example.com --format text   # Human-readable (default)
geo audit --url https://example.com --format json   # Machine-readable
geo audit --url https://example.com --format rich   # Colored terminal
geo audit --url https://example.com --format html   # Self-contained report
geo audit --url https://example.com --format sarif  # GitHub Code Scanning
geo audit --url https://example.com --format junit  # Jenkins, GitLab CI
```

### CI/CD — fail the build when AI-readiness drops

```yaml
# .github/workflows/geo.yml
- uses: skywalkerqqq/geo-optimizer-skill@v4.17.1
  with:
    url: https://yoursite.com
    min-score: 70        # Fail the build if the GEO score drops below 70
    format: sarif        # Upload findings to the GitHub Security tab
```

### MCP Server

```bash
pip install geo-optimizer-skill[mcp]
claude mcp add geo-optimizer -- geo-mcp
```

Then ask: *"audit my site and fix what's missing"*

### Python API

```python
from geo_optimizer import audit

result = audit("https://example.com")
print(result.score)          # 85
print(result.band)           # "good"
print(result.recommendations)
```

### Research foundation

| Paper | Venue | Key finding |
|-------|-------|-------------|
| [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) | **KDD 2024** | 9 methods on 10k queries. Cite Sources +115%, Statistics +40% |
| [AutoGEO](https://arxiv.org/abs/2510.11438) | **ICLR 2026** | Automatic rule extraction. +50.99% over Princeton baseline |
| [C-SEO Bench](https://arxiv.org/abs/2506.11097) | **2025** | Most content manipulation is ineffective. Infrastructure matters most |

### Scope and limits

GEO Optimizer scores **input-side readiness** — the technical and content signals that make a site reachable, parseable, and citable. It does **not** observe what AI engines actually say about a brand outside its own `geo citations` LLM check.

A high score means the signals are in place. It does **not** guarantee citation: that also depends on the question, the competition, and the engine.

### License

MIT © skywalkerqqq — see [LICENSE](LICENSE).

---

<a id="简体中文"></a>

## 🌐 简体中文

返回 [English](#english)

### 什么是 GEO Optimizer？

**GEO Optimizer** 是一个免费的开源命令行工具（同时可作为 Python 库、MCP Server 和 Astro 集成使用），用于衡量你的网站在 **AI 答案引擎**（ChatGPT、Perplexity、Google AI Overviews、Gemini、Claude）中的可见度，并告诉你如何让它引用你。

这个领域有多种叫法：**AEO**（答案引擎优化）、**GEO**（生成式引擎优化）、**AI SEO**、**LLM SEO**、**AI 可见度监测**。本工具覆盖全部含义。

```bash
# 无需安装 —— 一条命令给任意网站打出 8 大维度的 AI 就绪度分数
uvx --from geo-optimizer-skill geo audit --url https://yoursite.com
```

它依据 **47 项研究方法**（[Princeton KDD 2024](https://arxiv.org/abs/2311.09735)、[AutoGEO ICLR 2026](https://arxiv.org/abs/2510.11438)）为站点评分，并直接生成修复内容——robots.txt 机器人规则、`llms.txt`、JSON-LD 结构化数据，以及模型最爱引用的内容写法。

### 为什么 AI 可见度重要

AI 搜索引擎只给**一个综合答案**，并只引用**少数几个来源**。如果你的站点不在其中，即使你在 Google 排名第一，也等于隐形。

- **ChatGPT 最常引用的页面中，28.3% 在 Google 上零自然流量**（Ahrefs）——AI 引擎的信号偏好与传统 SEO 不同。
- 完善的 JSON-LD 结构化数据可将 LLM 抽取准确率 **从 16% 提升到 54%**（Semrush 在 GPT-4 上的测试）。

### 安装

```bash
pip install geo-optimizer-skill
```

### 快速开始

```bash
# 审计任意站点 —— 0-100 分 + 可执行建议
geo audit --url https://yoursite.com

# 审计整个 sitemap，优先暴露最弱的页面
geo audit --sitemap https://yoursite.com/sitemap.xml --max-urls 25

# 对比页面改版前后
geo diff --before https://yoursite.com/page-old --after https://yoursite.com/page-new

# 保存历史并检测分数回退
geo audit --url https://yoursite.com --save-history --regression

# 距上次快照发生了什么变化？（CI 可用 --fail-on warning）
geo drift --url https://yoursite.com

# 直接问 AI 引擎：我的品牌被提及了吗？我的域名被引用了吗？
geo citations --brand "你的品牌" --domain yoursite.com --topic "你的品类"

# 一次性生成所有缺失文件（robots.txt、llms.txt、schema、meta）
geo fix --url https://yoursite.com --apply

# 从 sitemap 生成 llms.txt
geo llms --base-url https://yoursite.com --output ./public/llms.txt

# 生成 JSON-LD 结构化数据
geo schema --type faq --url https://yoursite.com
```

### 评分维度

| 维度 | 分值 | 检查内容 |
|------|------|----------|
| **Robots.txt** | /18 | 27 个 AI 爬虫分 3 层。引用型机器人是否显式放行？ |
| **llms.txt** | /18 | 是否存在、H1 + 引用块、分节、链接、深度。有 llms-full.txt 吗？ |
| **Schema JSON-LD** | /16 | WebSite、Organization、FAQPage、Article。丰富度（5+ 属性）？ |
| **Meta 标签** | /14 | title、description、canonical、Open Graph 是否完整？ |
| **内容** | /12 | H1、数据、外部引用、标题层级、结论前置？ |
| **品牌与实体** | /10 | 品牌一致性、知识图谱链接、关于页、主题权威度 |
| **信号** | /6 | `<html lang>`、RSS/Atom、dateModified 新鲜度？ |
| **AI 发现** | /6 | `.well-known/ai.txt`、`/ai/summary.json`、`/ai/faq.json`？ |

**分数区间：** 86-100 优秀 · 68-85 良好 · 36-67 基础 · 0-35 危急

另有独立的**可被引述性得分**（0-100），覆盖 47 项方法：
引用 +41% · 数据 +33% · 流畅度 +29% · 引用来源 +27% 等。

### 输出格式

```bash
geo audit --url https://example.com --format text   # 终端可读（默认）
geo audit --url https://example.com --format json   # 机器可读
geo audit --url https://example.com --format rich   # 彩色终端
geo audit --url https://example.com --format html   # 自包含 HTML 报告
geo audit --url https://example.com --format sarif  # GitHub Code Scanning
geo audit --url https://example.com --format junit  # Jenkins、GitLab CI
```

### CI/CD —— AI 就绪度下降就构建失败

```yaml
# .github/workflows/geo.yml
- uses: skywalkerqqq/geo-optimizer-skill@v4.17.1
  with:
    url: https://yoursite.com
    min-score: 70        # 分数低于 70 则构建失败
    format: sarif        # 结果上传到 GitHub Security 标签页
```

### MCP Server

```bash
pip install geo-optimizer-skill[mcp]
claude mcp add geo-optimizer -- geo-mcp
```

然后直接问：*"审计我的站点并修复缺失项"*

### Python API

```python
from geo_optimizer import audit

result = audit("https://example.com")
print(result.score)          # 85
print(result.band)           # "good"
print(result.recommendations)
```

### 研究基础

| 论文 | 会议 | 核心发现 |
|------|------|----------|
| [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) | **KDD 2024** | 1 万条查询测试 9 种方法。引用来源 +115%、数据 +40% |
| [AutoGEO](https://arxiv.org/abs/2510.11438) | **ICLR 2026** | 自动规则抽取，较 Princeton 基线 +50.99% |
| [C-SEO Bench](https://arxiv.org/abs/2506.11097) | **2025** | 多数内容操纵无效，基础设施才是关键 |

### 能力边界

GEO Optimizer 评估的是**输入侧就绪度**——让站点可被抓取、可被解析、可被引用的技术与内容信号。它**不**监测 AI 引擎实际如何提及你的品牌（除 `geo citations` 自带的 LLM 检查外）。

高分代表信号已到位，**不等于保证被引**——最终还取决于提问方式、竞争对手和引擎本身。

### 许可

MIT © skywalkerqqq — 详见 [LICENSE](LICENSE)。

---

<div align="center">

MIT License · Built and maintained by [skywalkerqqq](https://github.com/skywalkerqqq)

If this saved you time, a star helps others find it.

[![Star on GitHub](https://img.shields.io/github/stars/skywalkerqqq/geo-optimizer-skill?style=for-the-badge&color=facc15&logo=github&label=Star)](https://github.com/skywalkerqqq/geo-optimizer-skill/stargazers)

</div>
