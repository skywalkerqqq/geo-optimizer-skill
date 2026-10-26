"""Build privacy.html: rewrite the template with __I18N_<KEY>__ tokens, then write
the matching _PRIV_EN / _PRIV_ZH dict into manifest_i18n.py.

Run: python -m geo_optimizer.web._privacy_build
"""
from __future__ import annotations

from pathlib import Path
import re

WEB_DIR = Path(__file__).parent
TEMPLATES = WEB_DIR / "templates"
MANIFEST = WEB_DIR / "manifest_i18n.py"

PRIV_ZH: dict[str, str] = {}
PRIV_EN: dict[str, str] = {}


def EN(key: str, value: str) -> str:
    PRIV_EN[key] = value
    return f"__I18N_{key}__"


def ZH(key: str, value: str) -> str:
    PRIV_ZH[key] = value
    return f"__I18N_{key}__"


# CSS (don't touch) - we keep the original CSS block. We rebuild the page in
# the same byte-equivalent shape: <!DOCTYPE>, <html lang>, <head> with CSS, then
# <body> with nav and legal content. We only rewrite user-visible text nodes to
# placeholders; nav & footer strings & cookie-button aria/title use ZH keys
# identical in shape to research.html's.

# Reuse the CSS verbatim from the source. Read it.
src = (TEMPLATES / "privacy.html").read_text(encoding="utf-8")
m = re.search(r"<style>(.*?)</style>", src, re.S)
assert m, "no <style> block"
CSS = m.group(1)


def page() -> str:
    # CSS goes between <style>...</style>
    css = CSS
    return f"""<!DOCTYPE html>
<html __GEO_HTML_LANG_ATTR__>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{EN("TITLE", "Privacy Policy - GEO Optimizer")}</title>
<meta name="description" content="{EN("META_DESC", "Privacy policy for skywalkerqqq.github.io/geo-optimizer-skill - GEO Optimizer")}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
<nav>
  <a href="/" class="nav-logo">
    <span class="dot"></span>
    <span>GEO Optimizer</span>
  </a>
  <button class="nav-hamburger" id="nav-ham" aria-label="{EN("ARIA_MENU", "Menu")}">&#9776;</button>
  <div class="nav-links">
    <a href="/">{EN("NAV_AUDIT", "Audit")}</a>
    <a href="/compare">{EN("NAV_COMPARE", "Compare")}</a>
    <a href="https://auriti-labs.github.io/geo-optimizer-skill/">{EN("NAV_DOCS", "Docs")}</a>
    <span class="nav-sep"></span>
    <div class="nav-dropdown">
      <button class="nav-dropdown-toggle" aria-expanded="false">{EN("NAV_MORE", "More")} <svg viewBox="0 0 10 6" xmlns="http://www.w3.org/2000/svg"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
      <div class="nav-dropdown-menu">
        <a href="/research">{EN("NAV_RESEARCH", "Research")}</a>
        <a href="/roadmap">{EN("NAV_ROADMAP", "Roadmap")}</a>
        <a href="/manifesto">{EN("NAV_MANIFESTO", "Manifesto")}</a>
        <a href="/privacy">{EN("NAV_PRIVACY", "Privacy")}</a>
      </div>
    </div>
  </div>
  <a class="nav-cta" href="https://github.com/skywalkerqqq/geo-optimizer-skill" target="_blank" rel="noopener">
    <svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z" fill="currentColor"/></svg>
    {EN("NAV_GITHUB", "GitHub")}
  </a>
</nav>

<div class="wrapper">
  <div class="page-header">
    <h1>{EN("HDR_H1", "Privacy Policy")}</h1>
    <div>
      <span class="gdpr-badge">{EN("HDR_BADGE", "GDPR Compliant")}</span>
    </div>
    <p class="text-muted" style="margin-top: 1rem; max-width: 540px; margin-inline: auto;">
      {EN("HDR_LAST_UPDATED", "Last updated:")} <span class="text-bold">{EN("HDR_DATE", "May 4, 2026")}</span><br>
      {EN("HDR_CONTROLLER_LBL", "Data Controller:")} <span class="text-bold">{EN("HDR_CONTROLLER_NAME", "skywalkerqqq")}</span>
    </p>
  </div>

  <div class="legal-content">
    <h2 id="intro">{EN("S1_HEAD", "1. Introduction")}</h2>
    <p>
      {EN("S1_P1", 'This Privacy Policy describes how we collect, use, and protect your personal data when you use the website <strong>skywalkerqqq.github.io/geo-optimizer-skill</strong> (the &ldquo;Site&rdquo;), owned by <strong>skywalkerqqq</strong>.')}
    </p>
    <p>
      {EN("S1_P2", 'Respecting your privacy is our top priority. This policy complies with the <strong>General Data Protection Regulation (GDPR)</strong> of the European Union and all applicable privacy regulations.')}
    </p>
    <p>
      {EN("S1_P3_LEAD", "If you have questions about this Privacy Policy, contact us at:")}
      <a href="mailto:skywalkerqqq@users.noreply.github.com">skywalkerqqq@users.noreply.github.com</a>
    </p>

    <h2 id="data-collection">{EN("S2_HEAD", "2. Data We Collect")}</h2>
    <p>
      {EN("S2_P1", "We collect only the data strictly necessary for the operation of the Site and the provision of our services.")}
    </p>

    <h3>{EN("S21_HEAD", "2.1 Automatic browsing data")}</h3>
    <p>
      {EN("S21_P1", "When you visit the Site, we automatically collect some browsing information:")}
    </p>
    <ul>
      <li><strong>{EN("L1A_LBL", "Technical cookies:")}</strong> {EN("L1A_TXT", "to maintain the session and your preferences")}</li>
      <li><strong>{EN("L1B_LBL", "IP address:")}</strong> {EN("L1B_TXT", "(for security purposes only, not for tracking)")}</li>
      <li><strong>{EN("L1C_LBL", "Device information:")}</strong> {EN("L1C_TXT", "browser type, operating system")}</li>
      <li><strong>{EN("L1D_LBL", "Log data:")}</strong> {EN("L1D_TXT", "pages visited, access time, visit duration")}</li>
    </ul>

    <h3>{EN("S22_HEAD", "2.2 User-provided data")}</h3>
    <p>
      {EN("S22_P1", "When you use our services, the following data may be collected:")}
    </p>
    <ul>
      <li><strong>{EN("L2A_LBL", "URLs to audit:")}</strong> {EN("L2A_TXT", "to provide the SEO analysis service")}</li>
      <li><strong>{EN("L2B_LBL", "Comments and feedback:")}</strong> {EN("L2B_TXT", "submitted via contact form")}</li>
      <li><strong>{EN("L2C_LBL", "Contact details:")}</strong> {EN("L2C_TXT", "if you reach out to us, only if voluntarily provided")}</li>
    </ul>

    <h2 id="cookies">{EN("S3_HEAD", "3. Cookies and Tracking")}</h2>
    <p>
      {EN("S3_P1", "We use technical and analytics cookies to improve your browsing experience.")}
    </p>
    <p>
      <strong>{EN("S3_P2A_LBL", "Essential cookies (required):")}</strong>
      <span class="text-muted">
        {EN("S3_P2A_TXT", "These cookies are essential for the operation of the Site and cannot be disabled. They include cookies for authentication, security, and session preferences.")}
      </span>
    </p>
    <p>
      <strong>{EN("S3_P2B_LBL", "Analytics cookies (Google Analytics):")}</strong>
      <span class="text-muted">
        {EN("S3_P2B_TXT", "We use Google Analytics to analyze Site usage. Data is aggregated and anonymized. We do not perform any personal identification. You can disable these cookies via the cookie settings button in the bottom-left corner.")}
      </span>
    </p>
    <p>
      <strong>{EN("S3_P2C_LBL", "Marketing cookies (Google Ads):")}</strong>
      <span class="text-muted">
        {EN("S3_P2C_TXT", "Used only with your explicit consent to show personalized ads. Can be disabled at any time.")}
      </span>
    </p>
    <div class="info-box">
      <strong>{EN("S3_INFO_LBL", "How to manage cookies:")}</strong>
      <p class="text-muted">
        {EN("S3_INFO_TXT", "You can accept, reject, or manage your cookie preferences at any time by clicking the cookie settings button in the bottom-left corner of the page.")}
      </p>
    </div>

    <h2 id="google-analytics">{EN("S4_HEAD", "4. Google Analytics")}</h2>
    <p>
      {EN("S4_P1", 'The Site uses Google Analytics, a web analytics service provided by Google LLC (&ldquo;Google&rdquo;). Google uses the collected cookies to analyze user behavior on the Site.')}
    </p>
    <p>
      <strong>{EN("S4_P2_LBL", "What we collect:")}</strong>
      <span class="text-muted">
        - {EN("S4_P2_L1", "Pages visited")}<br>
        - {EN("S4_P2_L2", "Time spent on pages")}<br>
        - {EN("S4_P2_L3", "Referral source")}<br>
        - {EN("S4_P2_L4", "Device type and browser")}<br>
        - {EN("S4_P2_L5", "Geographic location (country/region level only, not full IP address)")}
      </span>
    </p>
    <p>
      <strong>{EN("S4_P3_LBL", "What we do NOT collect:")}</strong>
      <span class="text-muted">
        - {EN("S4_P3_L1", "Full IP addresses (they are anonymized)")}<br>
        - {EN("S4_P3_L2", "Personally identifiable information")}<br>
        - {EN("S4_P3_L3", "Financial or banking information")}<br>
        - {EN("S4_P3_L4", "Sensitive data (health, religion, politics, etc.)")}
      </span>
    </p>
    <p>
      <strong>{EN("S4_P4_LBL", "Anonymization:")}</strong>
      <span class="text-muted">
        {EN("S4_P4_TXT", "Google Analytics is configured to anonymize users' IP addresses before transmission to Google. Data is retained for 24 months.")}
      </span>
    </p>
    <p>
      <strong>{EN("S4_P5_LBL", "Opt-out:")}</strong>
      <span class="text-muted">
        {EN("S4_P5_PRE", "You can disable Google Analytics by installing the")} <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener">
        {EN("S4_P5_LINK", "Google Analytics opt-out add-on")}</a> {EN("S4_P5_POST", "for your browser.")}
      </span>
    </p>

    <h2 id="security">{EN("S5_HEAD", "5. Data Security")}</h2>
    <p>
      {EN("S5_P1_LEAD", "We implement appropriate technical and organizational measures to protect your personal data against:")}
    </p>
    <ul>
      <li><strong>{EN("S5_L1_LBL", "Unauthorized access:")}</strong> {EN("S5_L1_TXT", "protection with two-factor authentication")}</li>
      <li><strong>{EN("S5_L2_LBL", "Disclosure or destruction:")}</strong> {EN("S5_L2_TXT", "TLS 1.3 encryption for all connections")}</li>
      <li><strong>{EN("S5_L3_LBL", "Alteration:")}</strong> {EN("S5_L3_TXT", "data integrity verification via checksums")}</li>
      <li><strong>{EN("S5_L4_LBL", "Loss:")}</strong> {EN("S5_L4_TXT", "regular backups and disaster recovery procedures")}</li>
    </ul>
    <p>
      {EN("S5_P2_PRE", "Data is stored on ")}<strong>Render.com</strong>{EN("S5_P2_AND", " and ")}<strong>GitHub Pages</strong>{EN("S5_P2_POST", " servers, both GDPR-compliant with infrastructure in the European Union.")}
    </p>

    <h2 id="retention">{EN("S6_HEAD", "6. Data Retention")}</h2>
    <table class="legal-table">
      <thead>
        <tr>
          <th>{EN("T6_H1", "Data type")}</th>
          <th>{EN("T6_H2", "Retention period")}</th>
          <th>{EN("T6_H3", "Legal basis")}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="text-bold">{EN("T6_R1_C1", "Browsing data")}</td>
          <td>{EN("T6_R1_C2", "6 months")}</td>
          <td>{EN("T6_R1_C3", "Legitimate interest (Art. 6 GDPR)")}</td>
        </tr>
        <tr>
          <td class="text-bold">{EN("T6_R2_C1", "Analytics cookies")}</td>
          <td>{EN("T6_R2_C2", "24 months")}</td>
          <td>{EN("T6_R2_C3", "Consent (Art. 9 GDPR)")}</td>
        </tr>
        <tr>
          <td class="text-bold">{EN("T6_R3_C1", "User feedback")}</td>
          <td>{EN("T6_R3_C2", "24 months")}</td>
          <td>{EN("T6_R3_C3", "Legitimate interest")}</td>
        </tr>
        <tr>
          <td class="text-bold">{EN("T6_R4_C1", "Audited URLs")}</td>
          <td>{EN("T6_R4_C2", "24 months (anonymized)")}</td>
          <td>{EN("T6_R4_C3", "Legitimate interest")}</td>
        </tr>
      </tbody>
    </table>

    <h2 id="third-party">{EN("S7_HEAD", "7. Third-Party Sharing")}</h2>
    <p>
      {EN("S7_P1", "We do not sell or rent your personal data to third parties. We share data only in the following cases:")}
    </p>
    <table class="legal-table">
      <thead>
        <tr>
          <th>{EN("T7_H1", "Recipient")}</th>
          <th>{EN("T7_H2", "Purpose")}</th>
          <th>{EN("T7_H3", "Country")}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="text-bold">{EN("T7_R1_C1", "Google LLC")}</td>
          <td>{EN("T7_R1_C2", "Google Analytics (traffic analysis)")}</td>
          <td>{EN("T7_R1_C3", "EU (data centers)")}</td>
        </tr>
        <tr>
          <td class="text-bold">{EN("T7_R2_C1", "GitHub Inc.")}</td>
          <td>{EN("T7_R2_C2", "Site hosting (GitHub Pages)")}</td>
          <td>{EN("T7_R2_C3", "EU (France)")}</td>
        </tr>
        <tr>
          <td class="text-bold">{EN("T7_R3_C1", "Render.com")}</td>
          <td>{EN("T7_R3_C2", "Backend hosting (API)")}</td>
          <td>{EN("T7_R3_C3", "EU (Germany)")}</td>
        </tr>
      </tbody>
    </table>
    <p>
      {EN("S7_P2_PRE", "All the above parties are registered ")}<strong>{EN("S7_P2_SUBPROC", "sub-processors")}</strong>
      {EN("S7_P2_POST", "and guarantee levels of data protection compliant with the GDPR.")}
    </p>

    <h2 id="rights">{EN("S8_HEAD", "8. Your Rights (GDPR)")}</h2>
    <p>
      {EN("S8_P1", "Under the GDPR, you have the right to:")}
    </p>
    <ul>
      <li><strong>{EN("S8_L1_LBL", "Access:")}</strong> {EN("S8_L1_TXT", "obtain confirmation that your data exists and request access to it")}</li>
      <li><strong>{EN("S8_L2_LBL", "Rectification:")}</strong> {EN("S8_L2_TXT", "request correction of inaccurate or incomplete data")}</li>
      <li><strong>{EN("S8_L3_LBL", "Erasure:")}</strong> {EN("S8_L3_TXT", "request deletion of your data (right to be forgotten)")}</li>
      <li><strong>{EN("S8_L4_LBL", "Restriction:")}</strong> {EN("S8_L4_TXT", "restrict the processing of your data in certain circumstances")}</li>
      <li><strong>{EN("S8_L5_LBL", "Portability:")}</strong> {EN("S8_L5_TXT", "receive your data in a structured, commonly used, machine-readable format")}</li>
      <li><strong>{EN("S8_L6_LBL", "Objection:")}</strong> {EN("S8_L6_TXT", "object to the processing of your data on legitimate grounds")}</li>
      <li><strong>{EN("S8_L7_LBL", "Withdraw consent:")}</strong> {EN("S8_L7_TXT", "withdraw consent at any time (without affecting the lawfulness of prior processing)")}</li>
      <li><strong>{EN("S8_L8_LBL", "Lodge a complaint:")}</strong> {EN("S8_L8_TXT", "submit a complaint to the supervisory authority (the Italian Data Protection Authority &mdash; Garante per la protezione dei dati personali)")}</li>
    </ul>
    <p>
      {EN("S8_P2_PRE", "To exercise your rights, write to: ")}<a href="mailto:skywalkerqqq@users.noreply.github.com">skywalkerqqq@users.noreply.github.com</a>
    </p>
    <p>
      {EN("S8_P3_PRE", "We will respond within ")}<strong>{EN("S8_P3_DAYS", "30 days")}</strong>{EN("S8_P3_POST", " of receiving your request. We may ask you to verify your identity for security reasons.")}
    </p>

    <h2 id="children">{EN("S9_HEAD", "9. Minors")}</h2>
    <p>
      {EN("S9_P1", "The Site is not directed at persons under the age of 16. We do not intentionally collect personal data from minors. If we discover that we have collected data from a minor, we will delete it within 30 days.")}
    </p>

    <h2 id="changes">{EN("S10_HEAD", "10. Policy Updates")}</h2>
    <p>
      {EN("S10_P1", "We reserve the right to modify this Privacy Policy at any time. Changes will take effect upon publication on this page.")}
    </p>
    <p>
      {EN("S10_P2", "We will notify you by email (if you have provided an address) or via a notice on the Site in case of significant changes.")}
    </p>
    <p>
      {EN("S10_P3", "We encourage you to periodically review this policy to stay informed about how we protect your data.")}
    </p>

    <h2 id="contact">{EN("S11_HEAD", "11. Contact")}</h2>
    <p>
      {EN("S11_P1", "For any questions regarding this Privacy Policy or the processing of your data:")}
    </p>
    <div class="info-box">
      <strong>{EN("S11_BRAND", "skywalkerqqq")}</strong><br>
      <span class="text-muted">{EN("S11_ROLE", "Data Controller")}</span><br><br>
      {EN("S11_EMAIL_LBL", "Email:")} <a href="mailto:skywalkerqqq@users.noreply.github.com">skywalkerqqq@users.noreply.github.com</a><br>
      {EN("S11_GH_LBL", "GitHub:")} <a href="https://github.com/skywalkerqqq" target="_blank" rel="noopener">github.com/Auriti-Labs</a>
    </div>

    <p style="margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--border); text-align: center;">
      <span class="text-muted">{EN("FOOT_CREATED", "This Privacy Policy was created on May 4, 2026.")}</span><br>
      <span class="text-muted">{EN("FOOT_UPDATED", "Last updated: May 4, 2026")}</span>
    </p>
  </div>

  <footer>
    <div class="links">
      <a href="/">{EN("F_HOME", "Home")}</a>
      <a href="/privacy">{EN("F_PRIVACY", "Privacy")}</a>
      <a href="https://github.com/skywalkerqqq/geo-optimizer-skill">GitHub</a>
      <a href="https://pypi.org/project/geo-optimizer-skill/">PyPI</a>
    </div>
    <div class="text-muted">
      &copy; 2026 skywalkerqqq. All rights reserved.
    </div>
  </footer>
</div>

<!-- Floating cookie settings button: link to privacy#cookies (no modal on this page) -->
<a href="/privacy#cookies" class="cookie-float-btn" title="{EN("TITLE_COOKIE", "Cookie settings")}" aria-label="{EN("ARIA_COOKIE", "Cookie settings")}">
  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.5"/>
    <circle cx="8" cy="9" r="1.5" fill="currentColor"/>
    <circle cx="15" cy="8" r="1" fill="currentColor"/>
    <circle cx="14" cy="14" r="1.5" fill="currentColor"/>
    <circle cx="9" cy="15" r="1" fill="currentColor"/>
    <circle cx="17" cy="13" r="1" fill="currentColor"/>
  </svg>
</a>

<script__NONCE_ATTR__>
document.getElementById('nav-ham').addEventListener('click', function() {{
  document.querySelector('.nav-links').classList.toggle('open');
  this.textContent = this.textContent === '☰' ? '✕' : '☰';
}});
document.querySelectorAll('.nav-dropdown-toggle').forEach(function(btn) {{
  btn.addEventListener('click', function(e) {{
    e.stopPropagation();
    var dd = this.closest('.nav-dropdown');
    dd.classList.toggle('open');
    this.setAttribute('aria-expanded', dd.classList.contains('open'));
  }});
}});
document.addEventListener('click', function() {{
  document.querySelectorAll('.nav-dropdown.open').forEach(function(dd) {{
    dd.classList.remove('open');
    dd.querySelector('.nav-dropdown-toggle').setAttribute('aria-expanded', 'false');
  }});
}});
</script>
</body>
</html>
"""


# === Chinese dictionary (parallel to the EN keys above) =====================

PRIV_ZH.update({
    # nav
    "ARIA_MENU": "菜单",
    "NAV_AUDIT": "审计",
    "NAV_COMPARE": "对比",
    "NAV_DOCS": "文档",
    "NAV_MORE": "更多",
    "NAV_RESEARCH": "研究",
    "NAV_ROADMAP": "路线图",
    "NAV_MANIFESTO": "宣言",
    "NAV_PRIVACY": "隐私",
    "NAV_GITHUB": "GitHub",
    # head
    "TITLE": "隐私政策 —— GEO Optimizer",
    "META_DESC": "skywalkerqqq.github.io/geo-optimizer-skill (GEO Optimizer) 的隐私政策",
    "HDR_H1": "隐私政策",
    "HDR_BADGE": "符合 GDPR",
    "HDR_LAST_UPDATED": "最后更新：",
    "HDR_DATE": "2026 年 5 月 4 日",
    "HDR_CONTROLLER_LBL": "数据控制方：",
    "HDR_CONTROLLER_NAME": "skywalkerqqq",
    # section 1
    "S1_HEAD": "1. 引言",
    "S1_P1": '本隐私政策说明我们在你访问网站 <strong>skywalkerqqq.github.io/geo-optimizer-skill</strong>（以下简称「本站」）时如何收集、使用和保护你的个人数据。该站由 <strong>skywalkerqqq</strong> 拥有。',
    "S1_P2": '尊重你的隐私是我们的首要原则。本政策遵循欧盟 <strong>《通用数据保护条例》（GDPR）</strong>及所有适用的隐私法规。',
    "S1_P3_LEAD": "如你对本政策有任何疑问，可通过以下方式联系我们：",
    # section 2
    "S2_HEAD": "2. 我们收集的数据",
    "S2_P1": "我们仅收集为本站运行与服务提供所必需的最少数据。",
    "S21_HEAD": "2.1 自动浏览数据",
    "S21_P1": "当你访问本站时，我们会自动采集部分浏览信息：",
    "L1A_LBL": "技术性 Cookie：",
    "L1A_TXT": "用于维持会话与保存你的偏好",
    "L1B_LBL": "IP 地址：",
    "L1B_TXT": "（仅用于安全目的，绝不用于追踪）",
    "L1C_LBL": "设备信息：",
    "L1C_TXT": "浏览器类型、操作系统",
    "L1D_LBL": "日志数据：",
    "L1D_TXT": "访问页面、访问时间、停留时长",
    "S22_HEAD": "2.2 用户主动提供的数据",
    "S22_P1": "当你使用我们的服务时，可能会采集以下数据：",
    "L2A_LBL": "待审计的 URL：",
    "L2A_TXT": "用于提供 SEO 分析服务",
    "L2B_LBL": "评论与反馈：",
    "L2B_TXT": "通过联系表单提交",
    "L2C_LBL": "联系方式：",
    "L2C_TXT": "如你主动联系时自愿提供",
    # section 3 cookies
    "S3_HEAD": "3. Cookie 与追踪",
    "S3_P1": "我们使用技术性与分析性 Cookie 来改善你的浏览体验。",
    "S3_P2A_LBL": "必要 Cookie（强制启用）：",
    "S3_P2A_TXT": "这些 Cookie 是本站运行所必需的，无法关闭。它们用于身份认证、安全和会话偏好。",
    "S3_P2B_LBL": "分析 Cookie（Google Analytics）：",
    "S3_P2B_TXT": "我们使用 Google Analytics 分析本站使用情况。所有数据都已聚合并匿名化处理，不进行任何个人身份识别。你可以点击页面左下角的 Cookie 设置按钮关闭这类 Cookie。",
    "S3_P2C_LBL": "营销 Cookie（Google Ads）：",
    "S3_P2C_TXT": "仅在你明确同意后用于展示个性化广告。可随时关闭。",
    "S3_INFO_LBL": "如何管理 Cookie：",
    "S3_INFO_TXT": "你可以随时点击页面左下角的 Cookie 设置按钮，接受、拒绝或调整 Cookie 偏好。",
    # section 4 GA
    "S4_HEAD": "4. Google Analytics",
    "S4_P1": '本站使用 Google Analytics，这是 Google LLC（以下简称「Google」）提供的网站分析服务。Google 利用这些 Cookie 分析用户在本站的行为。',
    "S4_P2_LBL": "我们采集的内容：",
    "S4_P2_L1": "访问过的页面",
    "S4_P2_L2": "页面停留时间",
    "S4_P2_L3": "来源渠道",
    "S4_P2_L4": "设备类型与浏览器",
    "S4_P2_L5": "地理位置（仅精确到国家/地区级，不含完整 IP）",
    "S4_P3_LBL": "我们不采集的内容：",
    "S4_P3_L1": "完整 IP 地址（已匿名化）",
    "S4_P3_L2": "任何可识别个人身份的信息",
    "S4_P3_L3": "金融或银行信息",
    "S4_P3_L4": "敏感数据（健康、宗教、政治等）",
    "S4_P4_LBL": "匿名化：",
    "S4_P4_TXT": "Google Analytics 在上传至 Google 之前会对用户 IP 做匿名化处理。数据保留 24 个月。",
    "S4_P5_LBL": "退出方式：",
    "S4_P5_PRE": "你可以安装",
    "S4_P5_LINK": "Google Analytics 浏览器退出插件",
    "S4_P5_POST": "来关闭 Google Analytics。",
    # section 5
    "S5_HEAD": "5. 数据安全",
    "S5_P1_LEAD": "我们采取恰当的技术与组织措施，保护你的个人数据免受以下威胁：",
    "S5_L1_LBL": "未授权访问：",
    "S5_L1_TXT": "通过两步验证等手段防护",
    "S5_L2_LBL": "泄露或损毁：",
    "S5_L2_TXT": "全连接使用 TLS 1.3 加密",
    "S5_L3_LBL": "篡改：",
    "S5_L3_TXT": "通过校验和验证数据完整性",
    "S5_L4_LBL": "丢失：",
    "S5_L4_TXT": "定期备份与灾难恢复流程",
    "S5_P2_PRE": "数据托管在 ",
    "S5_P2_AND": " 与 ",
    "S5_P2_POST": "，两者均符合 GDPR 要求，基础设施位于欧盟境内。",
    # section 6 retention table
    "S6_HEAD": "6. 数据保留期",
    "T6_H1": "数据类型",
    "T6_H2": "保留期",
    "T6_H3": "法律依据",
    "T6_R1_C1": "浏览数据",
    "T6_R1_C2": "6 个月",
    "T6_R1_C3": "正当利益（GDPR 第 6 条）",
    "T6_R2_C1": "分析 Cookie",
    "T6_R2_C2": "24 个月",
    "T6_R2_C3": "同意（GDPR 第 9 条）",
    "T6_R3_C1": "用户反馈",
    "T6_R3_C2": "24 个月",
    "T6_R3_C3": "正当利益",
    "T6_R4_C1": "被审计的 URL",
    "T6_R4_C2": "24 个月（已匿名化）",
    "T6_R4_C3": "正当利益",
    # section 7 third party
    "S7_HEAD": "7. 第三方共享",
    "S7_P1": "我们既不出售也不出租你的个人数据。仅在以下情形共享：",
    "T7_H1": "接收方",
    "T7_H2": "用途",
    "T7_H3": "所在国家/地区",
    "T7_R1_C1": "Google LLC",
    "T7_R1_C2": "Google Analytics（流量分析）",
    "T7_R1_C3": "欧盟（数据中心）",
    "T7_R2_C1": "GitHub Inc.",
    "T7_R2_C2": "站点托管（GitHub Pages）",
    "T7_R2_C3": "欧盟（法国）",
    "T7_R3_C1": "Render.com",
    "T7_R3_C2": "后端托管（API）",
    "T7_R3_C3": "欧盟（德国）",
    "S7_P2_PRE": "以上各方均为已登记的",
    "S7_P2_SUBPROC": "数据处理方",
    "S7_P2_POST": "，并保证数据保护水平符合 GDPR 要求。",
    # section 8 rights
    "S8_HEAD": "8. 你的权利（GDPR）",
    "S8_P1": "根据 GDPR，你拥有以下权利：",
    "S8_L1_LBL": "访问权：",
    "S8_L1_TXT": "确认你的数据是否存在，并请求访问",
    "S8_L2_LBL": "更正权：",
    "S8_L2_TXT": "要求更正不准确或不完整的数据",
    "S8_L3_LBL": "删除权：",
    "S8_L3_TXT": "要求删除你的数据（被遗忘权）",
    "S8_L4_LBL": "限制处理权：",
    "S8_L4_TXT": "在特定情况下限制对你的数据的处理",
    "S8_L5_LBL": "可携权：",
    "S8_L5_TXT": "以结构化、常用、机器可读的格式接收你的数据",
    "S8_L6_LBL": "反对权：",
    "S8_L6_TXT": "基于正当理由反对对你的数据的处理",
    "S8_L7_LBL": "撤回同意：",
    "S8_L7_TXT": "随时撤回同意（不影响撤回前已经发生的处理）",
    "S8_L8_LBL": "投诉权：",
    "S8_L8_TXT": "向监管机构（意大利个人数据保护局 Garante per la protezione dei dati personali）提交投诉",
    "S8_P2_PRE": "如需行使上述权利，请发送邮件至：",
    "S8_P3_PRE": "我们将在收到请求后的 ",
    "S8_P3_DAYS": "30 天",
    "S8_P3_POST": " 内回复。出于安全考虑，可能会请你验证身份。",
    # section 9 children
    "S9_HEAD": "9. 未成年人",
    "S9_P1": "本站不面向 16 岁以下用户。我们不会故意收集未成年人的个人数据。若发现误收，将在 30 天内删除。",
    # section 10 changes
    "S10_HEAD": "10. 政策更新",
    "S10_P1": "我们保留随时修改本隐私政策的权利。变更一经发布即生效。",
    "S10_P2": "若发生重大变更，我们会通过你提供的邮箱或站内通知告知你。",
    "S10_P3": "建议定期查看本政策，以了解我们如何保护你的数据。",
    # section 11 contact
    "S11_HEAD": "11. 联系方式",
    "S11_P1": "如对本隐私政策或你的数据处理有任何疑问：",
    "S11_BRAND": "skywalkerqqq",
    "S11_ROLE": "数据控制方",
    "S11_EMAIL_LBL": "邮箱：",
    "S11_GH_LBL": "GitHub：",
    # footer
    "FOOT_CREATED": "本隐私政策创建于 2026 年 5 月 4 日。",
    "FOOT_UPDATED": "最后更新：2026 年 5 月 4 日",
    "F_HOME": "首页",
    "F_PRIVACY": "隐私",
    "TITLE_COOKIE": "Cookie 设置",
    "ARIA_COOKIE": "Cookie 设置",
})


def main() -> None:
    # Render the page (this populates EN dict via EN() helper)
    html = page()

    # Sanity: EN and ZH should have same keys
    en_keys = set(PRIV_EN.keys())
    zh_keys = set(PRIV_ZH.keys())
    extra_en = en_keys - zh_keys
    extra_zh = zh_keys - en_keys
    if extra_en or extra_zh:
        raise SystemExit(
            f"dict mismatch: EN-only={extra_en}, ZH-only={extra_zh}"
        )

    # No literal English user-visible text remains in template (other than the
    # pure ASCII inside <script>, <style>, SVG <path> data, and brands).
    # Sanity: token residue must be 0.

    # Write the template
    out = TEMPLATES / "privacy.html"
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out} ({len(html)} chars)")

    # Append / refresh the dict to manifest_i18n.py
    mf = MANIFEST.read_text(encoding="utf-8")
    if '"privacy.html"' in mf and "_PRIV_EN" in mf:
        print("manifest_i18n.py already has privacy entry — leaving as-is")
    else:
        # Append at end before any "def page_dict"
        lines = list(PRIV_EN.items())
        # Build the python source: dicts and PAGES entry
        en_repr = "{\n    " + ",\n    ".join(
            f'"{k}": {PRIV_EN[k]!r}' for k in sorted(PRIV_EN)
        ) + "\n}"
        zh_repr = "{\n    " + ",\n    ".join(
            f'"{k}": {PRIV_ZH[k]!r}' for k in sorted(PRIV_ZH)
        ) + "\n}"
        block = (
            "\n\n_PRIV_EN = " + en_repr + "\n\n"
            "_PRIV_ZH = " + zh_repr + "\n\n"
            "PAGES['privacy.html'] = {'en': _PRIV_EN, 'zh': _PRIV_ZH}\n"
        )
        # Insert before the line "def page_dict" if present, else append
        m2 = re.search(r"^def page_dict\b", mf, re.M)
        if m2:
            insert_at = m2.start()
            mf = mf[:insert_at] + block + "\n\n" + mf[insert_at:]
        else:
            mf = mf.rstrip() + block
        MANIFEST.write_text(mf, encoding="utf-8")
        print(f"appended privacy entry to {MANIFEST}")


if __name__ == "__main__":
    main()
