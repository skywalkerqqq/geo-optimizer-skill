"""
GEO Audit — Instruction Following Readiness sub-audit (#371).

Analyzes how easily an AI agent can interact with a page:
- Action clarity: buttons/links with descriptive text vs icon-only
- Form machine-readability: inputs with label, type, placeholder
- Workflow linearity: stateful URLs, navigation complexity
- Error recovery: aria-live regions, role="alert", aria-invalid

Informational check — does not affect GEO score.
"""

from __future__ import annotations

import re

from geo_optimizer.models.results import InstructionReadinessResult

# Elements that represent interactive actions
_BUTTON_TAGS = {"button", "a"}
_INPUT_TYPES_EXPLICIT = {
    "text",
    "email",
    "password",
    "tel",
    "url",
    "number",
    "date",
    "datetime-local",
    "month",
    "week",
    "time",
    "search",
    "color",
    "range",
    "file",
    "checkbox",
    "radio",
}


def audit_instruction_readiness(soup, raw_html: str = "") -> InstructionReadinessResult:
    """Analyze page for AI agent instruction following readiness.

    Args:
        soup: BeautifulSoup of the full HTML document.
        raw_html: Raw HTML string for pattern matching.

    Returns:
        InstructionReadinessResult with readiness metrics.
    """
    if not soup:
        return InstructionReadinessResult(checked=True)

    body = soup.find("body")
    if not body:
        return InstructionReadinessResult(checked=True)

    # 1. Action clarity: buttons and links with descriptive text
    labeled, unlabeled = _analyze_actions(body)

    # 2. Form machine-readability
    total_inputs, labeled_inputs, typed_inputs = _analyze_forms(body)

    # 3. Workflow linearity
    nav_links = len(body.find_all("a", href=True))
    stateful_urls = bool(body.find("a", href=re.compile(r"[?#]")))

    # 4. Error recovery
    has_aria_live = bool(body.find(attrs={"aria-live": True}))
    has_error_roles = bool(body.find(attrs={"role": "alert"}) or body.find(attrs={"aria-invalid": True}))

    # Compute sub-scores
    action_score = _action_clarity_score(labeled, unlabeled)
    form_score = _form_readability_score(total_inputs, labeled_inputs, typed_inputs)
    readiness_score = _compute_readiness_score(
        action_score,
        form_score,
        stateful_urls,
        has_aria_live,
        has_error_roles,
    )
    readiness_level = _compute_level(readiness_score)

    return InstructionReadinessResult(
        checked=True,
        labeled_buttons=labeled,
        unlabeled_buttons=unlabeled,
        action_clarity_score=action_score,
        total_inputs=total_inputs,
        labeled_inputs=labeled_inputs,
        typed_inputs=typed_inputs,
        form_readability_score=form_score,
        nav_links=nav_links,
        stateful_urls=stateful_urls,
        has_aria_live=has_aria_live,
        has_error_roles=has_error_roles,
        readiness_score=readiness_score,
        readiness_level=readiness_level,
    )


def _analyze_actions(body) -> tuple[int, int]:
    """Count labeled vs unlabeled interactive elements."""
    labeled = 0
    unlabeled = 0

    for btn in body.find_all("button"):
        if _has_label(btn):
            labeled += 1
        else:
            unlabeled += 1

    # Links that look like CTAs (role=button or class containing btn/button/cta)
    for a in body.find_all("a", href=True):
        role = (a.get("role") or "").lower()
        classes = " ".join(a.get("class", []))
        if role == "button" or re.search(r"\b(?:btn|button|cta)\b", classes, re.IGNORECASE):
            if _has_label(a):
                labeled += 1
            else:
                unlabeled += 1

    return labeled, unlabeled


def _has_label(el) -> bool:
    """Check if an element has descriptive text for an AI agent."""
    # Direct text content (stripped, min 2 chars to exclude icon-only)
    text = el.get_text(strip=True)
    if len(text) >= 2:
        return True
    # aria-label
    if el.get("aria-label"):
        return True
    # title attribute
    return bool(el.get("title"))


def _analyze_forms(body) -> tuple[int, int, int]:
    """Analyze form inputs for machine-readability."""
    inputs = body.find_all(["input", "select", "textarea"])
    total = 0
    labeled = 0
    typed = 0

    for inp in inputs:
        inp_type = (inp.get("type") or "").lower()
        # Skip hidden and submit inputs
        if inp_type in ("hidden", "submit", "image", "reset"):
            continue
        total += 1

        # Check if labeled
        if _input_has_label(inp, body):
            labeled += 1

        # Check if explicitly typed
        if inp.name == "select" or inp.name == "textarea" or inp_type in _INPUT_TYPES_EXPLICIT:
            typed += 1

    return total, labeled, typed


def _input_has_label(inp, body) -> bool:
    """Check if an input has an associated label."""
    # aria-label or aria-labelledby
    if inp.get("aria-label") or inp.get("aria-labelledby"):
        return True
    # placeholder (weak but present)
    if inp.get("placeholder"):
        return True
    # Explicit <label for="id">
    inp_id = inp.get("id")
    if inp_id and body.find("label", attrs={"for": inp_id}):
        return True
    # Wrapping <label>
    return bool(inp.find_parent("label"))


def _action_clarity_score(labeled: int, unlabeled: int) -> int:
    """Score action clarity 0-100."""
    total = labeled + unlabeled
    if total == 0:
        return 100  # No actions = no problem
    ratio = labeled / total
    return min(int(ratio * 100), 100)


def _form_readability_score(total: int, labeled: int, typed: int) -> int:
    """Score form machine-readability 0-100."""
    if total == 0:
        return 100  # No forms = no problem
    label_ratio = labeled / total
    type_ratio = typed / total
    return min(int(label_ratio * 60 + type_ratio * 40), 100)


def _compute_readiness_score(
    action_score: int,
    form_score: int,
    stateful_urls: bool,
    has_aria_live: bool,
    has_error_roles: bool,
) -> int:
    """Compute overall readiness score (0-100)."""
    score = 0

    # Action clarity (max 30)
    score += int(action_score * 0.3)

    # Form readability (max 30)
    score += int(form_score * 0.3)

    # Workflow linearity (max 15)
    if stateful_urls:
        score += 15

    # Error recovery (max 25)
    if has_aria_live:
        score += 15
    if has_error_roles:
        score += 10

    return min(score, 100)


def _compute_level(score: int) -> str:
    """Map score to readiness level."""
    if score >= 80:
        return "advanced"
    if score >= 50:
        return "ready"
    if score >= 20:
        return "basic"
    return "none"
