from __future__ import annotations

import html
import textwrap
from pathlib import Path

from .assets import asset_data_uri, render_asset_figure, render_document_icon, render_tool_icons
from .config import BASE_CSS, THEME, TOKENS_CSS, TOOLCARD_ICON_ROOT
from .model import SlideSpec

def attr_escape(text: str) -> str:
    return html.escape(text, quote=True)

def render_footer(spec: SlideSpec) -> str:
    return (
        '<footer class="footer">'
        f'<span class="footer-left">{html.escape(spec.footer_left)}</span>'
        f'<span class="footer-right">{spec.order}</span>'
        "</footer>"
    )

def render_lead(lead: str) -> str:
    return f'<p class="lead-placeholder">{html.escape(lead)}</p>' if lead else ""

def render_short_line(lead: str) -> str:
    return f'<p class="short-line">{html.escape(lead)}</p>' if lead else ""

def normalize_code_display(code: str) -> str:
    return textwrap.dedent(code).strip("\n")

def render_code_block(code: str) -> str:
    return f'<pre class="code-block"><code>{html.escape(normalize_code_display(code))}</code></pre>\n'

def render_native_nodes(nodes: list[str], class_name: str = "") -> str:
    parts: list[str] = []
    for index, node in enumerate(nodes):
        parts.append(f'<span>{html.escape(node)}</span>')
        if index < len(nodes) - 1:
            parts.append('<i aria-hidden="true">→</i>')
    return f'<div class="ch-native-nodes {html.escape(class_name)}">{"".join(parts)}</div>'

def render_chapter_card(card: dict[str, object], class_name: str = "") -> str:
    index = str(card.get("index", card.get("value", "")))
    title = str(card.get("title", card.get("label", "")))
    text = str(card.get("text", ""))
    evidence = str(card.get("evidence", card.get("detail", "")))
    nodes = [str(node) for node in card.get("nodes", [])]
    diagram = render_native_nodes(nodes, str(card.get("diagram", ""))) if nodes else ""
    evidence_html = f'<small>{html.escape(evidence)}</small>' if evidence else ""
    index_html = f'<span class="ch-card-index">{html.escape(index)}</span>' if index else ""
    return (
        f'<article class="ch-card {html.escape(class_name)}">'
        f"{index_html}"
        f'<h2>{html.escape(title)}</h2>'
        f"{diagram}"
        f'<p>{html.escape(text)}</p>'
        f"{evidence_html}"
        "</article>"
    )

def render_compare_content(spec: SlideSpec, side: str) -> str:
    code = spec.body.get(f"{side}_code")
    if code is not None:
        return render_code_block(str(code))

    points = "".join(
        f'<li class="compare-point">{html.escape(point)}</li>'
        for point in spec.body.get(f"{side}_points", [])
    )
    return f'<ul class="compare-list">{points}</ul>'


def render_progression_card_map(spec: SlideSpec) -> str:
    cards = "".join(
        '<article class="progression-card">'
        f'<span class="progression-step">{html.escape(str(card["step"]))}</span>'
        f'<strong>{html.escape(str(card["percent"]))}</strong>'
        f'<p>{html.escape(str(card["result"]))}</p>'
        "</article>"
        for card in spec.body.get("cards", [])
    )
    gates = "".join(
        f'<li class="progression-gate">{html.escape(str(item))}</li>'
        for item in spec.body.get("gates", [])
    )
    return (
        '<section class="top-band">'
        f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
        f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
        f"{render_lead(spec.lead)}"
        "</section>"
        '<section class="progression-card-map">'
        f'<div class="progression-card-grid">{cards}</div>'
        f'<ul class="progression-gates">{gates}</ul>'
        "</section>"
    )


def render_shell(spec: SlideSpec) -> str:
    if spec.shell == "title-hero-shell":
        points = "".join(f'<li class="hero-point">{html.escape(point)}</li>' for point in spec.body.get("points", []))
        presenter = ""
        if "presenter" in spec.body:
            presenter = f'<p class="cover-presenter">{html.escape(spec.body["presenter"])}</p>'
        return (
            '<section class="cover-main">'
            '<div class="cover-rule"></div>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f"{render_lead(spec.lead)}"
            f'<ul class="hero-points cover-meta">{points}</ul>'
            "</section>"
            f"{presenter}"
        )

    if spec.shell == "agenda-list-shell":
        items = "".join(
            '<li class="agenda-item">'
            f'<span class="agenda-number">{html.escape(item["number"])}</span>'
            f'<span class="agenda-topic">{html.escape(item["topic"])}</span>'
            f'<span class="agenda-text">{html.escape(item["text"])}</span>'
            "</li>"
            for item in spec.body.get("items", [])
        )
        return (
            '<section class="agenda-layout">'
            '<div class="agenda-side">'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f"{render_lead(spec.lead)}"
            "</div>"
            f'<ol class="agenda-list">{items}</ol>'
            "</section>"
        )

    if spec.shell == "section-divider-shell":
        keyword_items = [str(keyword) for keyword in spec.body.get("keywords", [])]
        keywords = "".join(
            f'<span class="section-keyword-plain">{html.escape(keyword)}</span>'
            + ('<span class="section-keyword-separator" aria-hidden="true">/</span>' if index < len(keyword_items) - 1 else "")
            for index, keyword in enumerate(keyword_items)
        )
        return (
            '<section class="section-main">'
            f'<p class="chapter-marker">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f"{render_short_line(spec.lead)}"
            f'<p class="section-keywords section-keyword-rail">{keywords}</p>'
            "</section>"
        )

    if spec.shell == "statement-editorial-shell":
        if spec.body.get("variant") == "progression-card-map":
            return render_progression_card_map(spec)

        if spec.body.get("variant") == "prompt-only":
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="prompt-only-body">'
                '<p class="prompt-language-label">자연어</p>'
                '<article class="prompt-card">'
                f'<p class="prompt-text">{html.escape(str(spec.body.get("prompt", "")))}</p>'
                "</article>"
                '<p class="negative-opinion">자연어로 시키는 건 진짜 개발이 아니다!</p>'
                "</section>"
            )

        if spec.body.get("variant") == "tdd-control-layers":
            flow_steps = "".join(
                '<article class="tdd-flow-step">'
                f'<h2>{html.escape(step["title"])}</h2>'
                f'<p>{html.escape(step["text"])}</p>'
                "</article>"
                for step in spec.body.get("flow", [])
            )
            control_blocks = "".join(
                '<article class="tdd-control-block">'
                f'<h2>{html.escape(block["title"])}</h2>'
                f'<p>{html.escape(block["text"])}</p>'
                "</article>"
                for block in spec.body.get("controls", [])
            )
            chapter_label = ""
            if not spec.body.get("hide_chapter_label"):
                chapter_label = f'<p class="chapter-label statement-tag">{html.escape(spec.chapter_label)}</p>'
            return (
                '<section class="top-band">'
                f"{chapter_label}"
                f'<h1 class="title-placeholder statement-text">{html.escape(spec.title)}</h1>'
                f"{render_lead(spec.lead)}"
                "</section>"
                '<section class="statement-panel tdd-control-layers-body">'
                '<div class="tdd-control-grid">'
                '<div class="tdd-flow-stack">'
                f"{flow_steps}"
                "</div>"
                '<div class="tdd-control-column">'
                f"{control_blocks}"
                "</div>"
                "</div>"
                "</section>"
            )

        if spec.body.get("variant") == "question-summary":
            bullets = "".join(
                f'<li class="summary-item">{html.escape(item)}</li>'
                for item in spec.body.get("bullets", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="statement-panel question-summary-panel">'
                f'<p class="statement-tag question-tag">{html.escape(spec.body.get("tag", spec.chapter_label))}</p>'
                f'<p class="statement-text question-label">{html.escape(spec.body.get("question", ""))}</p>'
                f'<p class="statement-support summary-quote centered-claim">{html.escape(spec.body.get("summary", ""))}</p>'
                f'<ul class="summary-items">{bullets}</ul>'
                "</section>"
            )

        if spec.body.get("variant") == "basics-editorial":
            bullets = "".join(
                f'<li class="basics-item">{html.escape(item)}</li>'
                for item in spec.body.get("bullets", [])
            )
            return (
                '<section class="statement-panel statement-basics">'
                f'<p class="statement-tag">{html.escape(spec.body.get("tag", spec.chapter_label))}</p>'
                f'<h1 class="statement-text">{html.escape(spec.body.get("statement", spec.key_claim))}</h1>'
                f'<ul class="statement-support basics-grid">{bullets}</ul>'
                "</section>"
            )

        if spec.body.get("variant") == "summary-cards":
            cards = "".join(
                '<article class="summary-card">'
                f'<p class="summary-card-eyebrow">{html.escape(card["eyebrow"])}</p>'
                f'<h2 class="summary-card-title">{html.escape(card["title"])}</h2>'
                '<div class="summary-card-lines">'
                + "".join(f'<p>{html.escape(line)}</p>' for line in card.get("lines", []))
                + "</div>"
                "</article>"
                for card in spec.body.get("cards", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="summary-cards-body">'
                f'<div class="summary-quote-panel"><p class="summary-quote summary-quote-dark">{html.escape(spec.body.get("quote", ""))}</p></div>'
                f'<div class="summary-card-grid">{cards}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "context-rot-native":
            def render_rot_panel(panel_class: str, title: str, items: list[str]) -> str:
                item_nodes = "".join(f'<li class="context-rot-item">{html.escape(item)}</li>' for item in items)
                return (
                    f'<article class="{panel_class}">'
                    f'<h2>{html.escape(title)}</h2>'
                    f'<ul>{item_nodes}</ul>'
                    "</article>"
                )

            return (
                '<section class="top-band">'
                f'<p class="chapter-label statement-tag">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="context-rot-native-body">'
                f'<p class="context-rot-native-claim">{html.escape(spec.body.get("claim", spec.key_claim))}</p>'
                '<div class="context-rot-native-map">'
                f'{render_rot_panel("context-rot-window", str(spec.body.get("left_title", "")), [str(item) for item in spec.body.get("left_items", [])])}'
                f'{render_rot_panel("context-rot-break", str(spec.body.get("center_title", "")), [str(item) for item in spec.body.get("center_items", [])])}'
                f'{render_rot_panel("context-rot-artifacts", str(spec.body.get("right_title", "")), [str(item) for item in spec.body.get("right_items", [])])}'
                "</div>"
                "</section>"
            )

        if spec.body.get("variant") == "failure-card-grid":
            card_nodes = []
            for card in spec.body.get("cards", []):
                lines = "".join(f'<p>{html.escape(line)}</p>' for line in card.get("lines", []))
                card_nodes.append(
                    '<article class="failure-card">'
                    f'<h2 class="failure-card-title">{html.escape(card["title"])}</h2>'
                    f'<div class="failure-card-lines">{lines}</div>'
                    "</article>"
                )
            synthesis = ""
            if spec.body.get("synthesis"):
                synthesis = f'<p class="failure-card-synthesis">{html.escape(spec.body["synthesis"])}</p>'
            grid_class = f'failure-card-grid failure-card-grid-{len(card_nodes)}'
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="failure-card-body">'
                f'<div class="{grid_class}">{"".join(card_nodes)}</div>'
                f"{synthesis}"
                "</section>"
            )

        if spec.body.get("variant") == "calibrated-trust-scale":
            zones = []
            for zone in spec.body.get("zones", []):
                items = "".join(f'<li class="trust-scale-item">{html.escape(item)}</li>' for item in zone.get("items", []))
                zones.append(
                    '<article class="trust-scale-zone">'
                    f'<h2>{html.escape(zone["title"])}</h2>'
                    f'<ul>{items}</ul>'
                    "</article>"
                )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="calibrated-trust-scale-body">'
                f'<p class="trust-scale-claim">{html.escape(spec.body.get("claim", spec.key_claim))}</p>'
                f'<div class="trust-scale-track">{"".join(zones)}</div>'
                f'<p class="trust-scale-warning">{html.escape(spec.body.get("warning", ""))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "closing-gate":
            supports = "".join(
                '<article class="closing-gate-support">'
                f'<h2>{html.escape(block["title"])}</h2>'
                f'<p>{html.escape(block["text"])}</p>'
                "</article>"
                for block in spec.body.get("supports", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="closing-gate-body">'
                f'<p class="closing-gate-claim">{html.escape(spec.body.get("claim", spec.key_claim))}</p>'
                f'<div class="closing-gate-grid">{supports}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-proof-memory":
            main_lines = "".join(
                f'<span>{html.escape(line)}</span>' for line in spec.body.get("main", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="chapter-proof-memory-body">'
                f'<p class="memory-hook">{html.escape(spec.body.get("hook", ""))}</p>'
                '<div class="memory-proof-card">'
                f'<div class="memory-main">{main_lines}</div>'
                f'<p class="memory-proof">{html.escape(spec.body.get("proof", ""))}</p>'
                "</div>"
                f'<p class="memory-kicker">{html.escape(spec.body.get("kicker", ""))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "experience-testimony":
            cards = "".join(
                '<article class="testimony-card">'
                f'<p class="testimony-speaker">{html.escape(card["speaker"])}</p>'
                f'<p class="testimony-role">{html.escape(card.get("role", ""))}</p>'
                f'<p class="testimony-quote">{html.escape(card["quote"])}</p>'
                "</article>"
                for card in spec.body.get("cards", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="experience-testimony-body">'
                f'<p class="testimony-lead">{html.escape(spec.body.get("lead", ""))}</p>'
                f'<div class="testimony-grid">{cards}</div>'
                '<div class="testimony-summary">'
                f'<p>{html.escape(spec.body.get("statement", ""))}</p>'
                f'<span>{html.escape(spec.body.get("support", ""))}</span>'
                "</div>"
                "</section>"
            )

        if spec.body.get("variant") == "tomorrow-actions":
            actions = "".join(
                '<article class="tomorrow-action">'
                f'<h2>{html.escape(action["title"])}</h2>'
                f'<p>{html.escape(action["text"])}</p>'
                "</article>"
                for action in spec.body.get("actions", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="tomorrow-actions-body">'
                f'<div class="tomorrow-action-stack">{actions}</div>'
                f'<p class="tomorrow-quote">{html.escape(spec.body.get("quote", ""))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "thesis-harness":
            mappings = "".join(
                '<article class="harness-mapping-card">'
                f'<h2>{html.escape(item["title"])}</h2>'
                f'<p>{html.escape(item["text"])}</p>'
                "</article>"
                for item in spec.body.get("mapping", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="thesis-harness-body thesis-harness-equation-body">'
                '<div class="thesis-harness-main">'
                f'<p class="harness-equation">{html.escape(spec.body.get("statement", spec.key_claim))}</p>'
                f'<p class="harness-quote centered-claim">{html.escape(spec.body.get("quote", ""))}</p>'
                "</div>"
                '<div class="harness-definition-card harness-meaning">'
                '<span>Harness 원의미</span>'
                f'<p>{html.escape(spec.body.get("meaning", ""))}</p>'
                "</div>"
                f'<div class="harness-mapping-grid">{mappings}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "thesis-quote":
            return (
                '<section class="statement-panel thesis-quote-panel">'
                f'<p class="statement-tag">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="statement-text">{html.escape(spec.body.get("statement", spec.key_claim))}</h1>'
                f'<p class="statement-quote centered-claim">{html.escape(spec.body.get("quote", ""))}</p>'
                f'<p class="statement-support centered-claim">{html.escape(spec.body.get("source", ""))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "spec-tdd-bridge":
            cards = []
            for card in spec.body.get("cards", []):
                items = "".join(f'<li>{html.escape(item)}</li>' for item in card.get("items", []))
                cards.append(
                    '<article class="spec-tdd-card">'
                    f'<h2>{html.escape(card["title"])}</h2>'
                    f'<ul>{items}</ul>'
                    "</article>"
                )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label statement-tag">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder statement-text spec-tdd-subheading">{html.escape(spec.body.get("subheading", spec.body.get("statement", "Spec + TDD")))}</h1>'
                "</section>"
                '<section class="statement-panel spec-tdd-bridge-body">'
                '<div class="spec-tdd-card-grid">'
                f"{cards[0] if cards else ''}"
                '<div class="spec-tdd-plus" aria-hidden="true">+</div>'
                f"{cards[1] if len(cards) > 1 else ''}"
                "</div>"
                f'<p class="statement-support spec-tdd-synthesis centered-claim">{html.escape(spec.body.get("synthesis", spec.key_claim))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "blind-prompting":
            cards = "".join(
                '<article class="blind-prompting-card">'
                f'<h2>{html.escape(card["title"])}</h2>'
                f'<p>{html.escape(card["text"])}</p>'
                "</article>"
                for card in spec.body.get("cards", [])
            )
            quote_card = (
                '<article class="blind-prompting-card blind-prompting-quote-card">'
                '<blockquote>'
                f'{html.escape(spec.body.get("quote", ""))}'
                "</blockquote>"
                f'<p>{html.escape(spec.body.get("quote_source", ""))}</p>'
                "</article>"
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="blind-prompting-body blind-prompting-matrix-body">'
                f'<div class="blind-prompting-grid">{cards}{quote_card}</div>'
                "</section>"
            )

        if spec.body.get("variant") in {"harness-hierarchy", "harness-layered"}:
            decisions = "".join(
                '<article class="harness-layer-row">'
                '<div class="harness-decision">'
                f'<h2>{html.escape(item["title"])}</h2>'
                f'<p>{html.escape(item["text"])}</p>'
                "</div>"
                "</article>"
                for item in spec.body.get("decisions", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="harness-layered-body">'
                f'<p class="harness-core centered-claim">{html.escape(spec.body.get("statement", spec.key_claim))}</p>'
                f'<div class="harness-layer-grid">{decisions}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "harness-decision-map":
            decisions = "".join(
                '<article class="decision-card">'
                f'<h2>{html.escape(item["title"])}</h2>'
                f'<p>{html.escape(item["text"])}</p>'
                "</article>"
                for item in spec.body.get("decisions", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="decision-map-body">'
                f'<p class="decision-thesis">{html.escape(spec.body.get("statement", spec.key_claim))}</p>'
                f'<div class="decision-grid">{decisions}</div>'
                "</section>"
            )

        code = ""
        if spec.body.get("code"):
            code = render_code_block(str(spec.body["code"]))
        quote = ""
        if spec.body.get("quote"):
            quote = f'<p class="statement-quote centered-claim">{html.escape(spec.body["quote"])}</p>'
        chips = "".join(f'<li class="statement-chip">{html.escape(chip)}</li>' for chip in spec.body.get("chips", []))
        chips_markup = f'<ul class="statement-chips">{chips}</ul>' if chips else ""
        return (
            '<section class="statement-panel">'
            f'<p class="statement-tag">{html.escape(spec.body.get("tag", spec.chapter_label))}</p>'
            f'<h1 class="statement-text">{html.escape(spec.body.get("statement", spec.key_claim))}</h1>'
            f"{code}"
            f"{quote}"
            f'<p class="statement-support">{html.escape(spec.body.get("support", spec.lead))}</p>'
            f"{chips_markup}"
            "</section>"
        )

    if spec.shell == "process-flow-shell":
        if spec.body.get("variant") == "chapter-pattern-row":
            cards = "".join(render_chapter_card(card, "ch-pattern-card") for card in spec.body.get("cards", []))
            thesis = ""
            if spec.body.get("thesis"):
                thesis = f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body["thesis"]))}</p>'
            source_label = ""
            if spec.body.get("source_label"):
                source_label = f'<p class="flow-source-label">{html.escape(str(spec.body["source_label"]))}</p>'
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                f"{render_lead(spec.lead)}"
                "</section>"
                '<section class="ch-pattern-row-body">'
                f'<div class="ch-pattern-row">{cards}</div>'
                f"{source_label}"
                f"{thesis}"
                "</section>"
            )

        if spec.body.get("variant") == "chapter-map-side":
            side_cards = "".join(render_chapter_card(card, "ch-side-card") for card in spec.body.get("side_cards", []))
            main = dict(spec.body.get("main", {}))
            sub = dict(spec.body.get("sub", {}))
            return_items = "".join(f'<span>{html.escape(str(item))}</span>' for item in spec.body.get("artifacts", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                f"{render_lead(spec.lead)}"
                "</section>"
                '<section class="ch-map-side-body">'
                '<div class="ch-main-sub-map">'
                '<article class="ch-map-node ch-map-main">'
                f'<strong>{html.escape(str(main.get("title", "Main")))}</strong>'
                f'<span>{html.escape(str(main.get("text", "")))}</span>'
                "</article>"
                '<div class="ch-map-arrow ch-map-arrow-out"><span>task</span></div>'
                '<article class="ch-map-node ch-map-sub">'
                f'<strong>{html.escape(str(sub.get("title", "Sub")))}</strong>'
                f'<span>{html.escape(str(sub.get("text", "")))}</span>'
                f'<div class="ch-map-artifacts">{return_items}</div>'
                "</article>"
                '<div class="ch-map-arrow ch-map-arrow-back"><span>summary</span></div>'
                "</div>"
                f'<div class="ch-side-stack">{side_cards}</div>'
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-fanout":
            workers = "".join(
                '<article class="ch-worker-node">'
                f'<strong>{html.escape(str(worker.get("title", "")))}</strong>'
                f'<span>{html.escape(str(worker.get("text", "")))}</span>'
                "</article>"
                for worker in spec.body.get("workers", [])
            )
            path = render_native_nodes([str(item) for item in spec.body.get("path", [])], "ch-path-nodes")
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-fanout-body">'
                '<article class="ch-planner-node">'
                f'<strong>{html.escape(str(spec.body.get("planner", "Planner")))}</strong>'
                f'<span>{html.escape(str(spec.body.get("planner_text", "")))}</span>'
                "</article>"
                f'<div class="ch-worker-grid">{workers}</div>'
                f"{path}"
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-lanes":
            lanes = "".join(render_chapter_card(card, "ch-lane-card") for card in spec.body.get("lanes", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-lanes-body">'
                f'<div class="ch-lane-grid">{lanes}</div>'
                f'<p class="ch-merge-point centered-claim">{html.escape(str(spec.body.get("merge", "")))}</p>'
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-feedback-loop":
            roles = "".join(render_chapter_card(card, "ch-loop-role") for card in spec.body.get("roles", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-feedback-loop-body">'
                f'<div class="ch-loop-grid">{roles}</div>'
                f'<p class="ch-loop-feedback centered-claim">{html.escape(str(spec.body.get("feedback", "")))}</p>'
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-team-graph":
            graph_nodes = "".join(
                f'<article class="ch-team-node ch-team-node-{index + 1}"><strong>{html.escape(str(node.get("title", "")))}</strong><span>{html.escape(str(node.get("text", "")))}</span></article>'
                for index, node in enumerate(spec.body.get("nodes", []))
            )
            side_cards = "".join(render_chapter_card(card, "ch-side-card") for card in spec.body.get("side_cards", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-team-graph-body">'
                '<div class="ch-team-canvas">'
                '<div class="ch-team-lines" aria-hidden="true"></div>'
                f"{graph_nodes}"
                "</div>"
                f'<div class="ch-side-stack">{side_cards}</div>'
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-staged-flow":
            primary = render_native_nodes([str(item) for item in spec.body.get("primary", [])], "ch-stage-primary")
            secondary = render_native_nodes([str(item) for item in spec.body.get("secondary", [])], "ch-stage-secondary")
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-staged-flow-body">'
                f"{primary}"
                f"{secondary}"
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-tool-gate-grid":
            cards = "".join(render_chapter_card(card, "ch-principle-card") for card in spec.body.get("cards", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-principle-grid-body ch-tool-gate-body">'
                f'<div class="ch-principle-grid">{cards}</div>'
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-command-artifacts":
            left = "".join(render_chapter_card(card, "ch-command-card") for card in spec.body.get("commands", []))
            right = "".join(render_chapter_card(card, "ch-command-card") for card in spec.body.get("artifacts", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-command-artifact-body">'
                f'<div class="ch-command-column">{left}</div>'
                f'<div class="ch-command-column is-dark">{right}</div>'
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-workspace-map":
            windows = "".join(render_chapter_card(card, "ch-window-card") for card in spec.body.get("windows", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-workspace-body">'
                f'<div class="ch-window-grid">{windows}</div>'
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-issue-hub":
            spokes = "".join(render_chapter_card(card, "ch-issue-spoke") for card in spec.body.get("spokes", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-issue-hub-body">'
                '<article class="ch-issue-center">'
                f'<strong>{html.escape(str(spec.body.get("center", "이슈")))}</strong>'
                f'<span>{html.escape(str(spec.body.get("center_text", "")))}</span>'
                "</article>"
                f'<div class="ch-issue-spokes">{spokes}</div>'
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "spec-kit-workflow":
            stages = []
            for step in spec.body.get("steps", []):
                items = "".join(f'<li>{html.escape(item)}</li>' for item in step.get("items", []))
                stages.append(
                    '<li class="process-step spec-kit-stage">'
                    f'<span class="step-index spec-kit-stage-label">{html.escape(step["index"])}</span>'
                    f'<span class="step-title">{html.escape(step["title"])}</span>'
                    f'<span class="step-copy">{html.escape(step["text"])}</span>'
                    f'<ul class="spec-kit-stage-notes">{items}</ul>'
                    "</li>"
                )
            source = spec.body.get("source", {})
            icon_markup = ""
            icon_label = str(source.get("icon_label", ""))
            if icon_label:
                icon_path = TOOLCARD_ICON_ROOT / "github-copilot-octicon.svg"
                icon_markup = (
                    '<span class="spec-kit-source-icon">'
                    f'<img src="{asset_data_uri(icon_path)}" alt="{html.escape(icon_label)}">'
                    "</span>"
                )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                f"{render_lead(spec.lead)}"
                "</section>"
                '<section class="body-area flow-body spec-kit-workflow-body">'
                f'<ol class="process-track spec-kit-stage-track">{"".join(stages)}</ol>'
                '<div class="spec-kit-side-stack">'
                f'<article class="spec-kit-principle"><h2>{html.escape(str(spec.body.get("principle_title", "")))}</h2><p>{html.escape(str(spec.body.get("principle", "")))}</p></article>'
                f'<article class="spec-kit-outcome"><h2>{html.escape(str(spec.body.get("outcome_title", "")))}</h2><p>{html.escape(str(spec.body.get("outcome", "")))}</p></article>'
                f'<p class="spec-kit-source">{icon_markup}<span>{html.escape(icon_label)}</span><span>{html.escape(str(source.get("text", "")))}</span></p>'
                "</div>"
                "</section>"
            )

        if spec.body.get("variant") == "prompt-era":
            cards = []
            stages = spec.body.get("stages", [])
            for index, stage in enumerate(stages):
                items = "".join(f'<li>{html.escape(item)}</li>' for item in stage.get("items", []))
                cards.append(
                    '<article class="process-step prompt-era-card">'
                    f'<h2>{html.escape(stage["title"])}</h2>'
                    f'<p>{html.escape(stage["text"])}</p>'
                    f'<ul>{items}</ul>'
                    "</article>"
                )
                if index < len(stages) - 1:
                    cards.append('<div class="prompt-era-arrow" aria-hidden="true">→</div>')
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="prompt-era-body">'
                f'<p class="era-range">{html.escape(spec.body.get("range", ""))}</p>'
                f'<div class="prompt-era-flow">{"".join(cards)}</div>'
                f'<p class="prompt-era-thesis centered-claim">{html.escape(spec.body.get("thesis", spec.key_claim))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "cot-triad":
            marker_ids = {
                "cot": "cot-triad-cot-arrow",
                "react": "cot-triad-react-arrow",
                "tot": "cot-triad-tot-arrow",
            }

            def render_card(card: dict[str, object]) -> str:
                kind = str(card.get("kind", ""))
                title = html.escape(str(card.get("title", "")))
                acronym = html.escape(str(card.get("acronym", "")))
                meaning = html.escape(str(card.get("meaning", "")))
                marker_id = marker_ids.get(kind, "cot-triad-arrow")

                if kind == "react":
                    diagram = (
                        '<div class="cot-triad-diagram">'
                        '<svg class="cot-diagram-svg cot-react-svg" viewBox="0 0 286 170" preserveAspectRatio="xMidYMid meet" role="img" aria-label="ReAct diagram">'
                        f'<defs><marker id="{marker_id}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path class="cot-arrow-head" d="M0,0 L8,4 L0,8 z"></path></marker></defs>'
                        '<text class="cot-svg-caption" x="48" y="73" text-anchor="middle" aria-label="Reasoning Traces" font-size="13">'
                        '<tspan x="48" dy="0">Reasoning</tspan>'
                        '<tspan x="48" dy="15">Traces</tspan>'
                        '</text>'
                        '<rect class="cot-svg-node cot-svg-node-outline cot-react-node" x="118" y="58" width="50" height="42"></rect>'
                        '<text class="cot-svg-text" x="143" y="79" text-anchor="middle" dominant-baseline="middle" font-size="15">LM</text>'
                        '<rect class="cot-svg-node cot-svg-node-outline cot-react-node" x="218" y="58" width="50" height="42"></rect>'
                        '<text class="cot-svg-text" x="243" y="79" text-anchor="middle" dominant-baseline="middle" font-size="15">Env</text>'
                        '<path class="cot-svg-edge" d="M54 52 C78 24, 116 24, 138 55" marker-end="url(#cot-triad-react-arrow)"></path>'
                        '<path class="cot-svg-edge" d="M151 55 C172 24, 219 24, 239 55" marker-end="url(#cot-triad-react-arrow)"></path>'
                        '<text class="cot-svg-caption" x="194" y="20" text-anchor="middle" font-size="13">Actions</text>'
                        '<path class="cot-svg-edge cot-svg-edge-muted" d="M238 103 C218 132, 173 132, 151 104" marker-end="url(#cot-triad-react-arrow)"></path>'
                        '<path class="cot-svg-edge cot-svg-edge-muted" d="M134 103 C112 132, 75 132, 54 103" marker-end="url(#cot-triad-react-arrow)"></path>'
                        '<text class="cot-svg-caption" x="176" y="151" text-anchor="middle" font-size="13">Observations</text>'
                        '<text class="cot-svg-caption cot-svg-muted" x="143" y="166" text-anchor="middle" font-size="13">ReAct (Reason + Act)</text>'
                        "</svg>"
                        "</div>"
                    )
                elif kind == "tot":
                    diagram = (
                        '<div class="cot-triad-diagram">'
                        '<svg class="cot-diagram-svg cot-tot-svg" viewBox="0 0 240 170" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Tree-of-Thought diagram">'
                        f'<defs><marker id="{marker_id}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path class="cot-arrow-head" d="M0,0 L8,4 L0,8 z"></path></marker></defs>'
                        '<line class="cot-svg-edge" x1="115" y1="43" x2="66" y2="72" marker-end="url(#cot-triad-tot-arrow)"></line>'
                        '<line class="cot-svg-edge" x1="124" y1="44" x2="144" y2="73" marker-end="url(#cot-triad-tot-arrow)"></line>'
                        '<line class="cot-svg-edge" x1="58" y1="94" x2="58" y2="122" marker-end="url(#cot-triad-tot-arrow)"></line>'
                        '<line class="cot-svg-edge" x1="143" y1="96" x2="104" y2="123" marker-end="url(#cot-triad-tot-arrow)"></line>'
                        '<line class="cot-svg-edge" x1="157" y1="96" x2="194" y2="123" marker-end="url(#cot-triad-tot-arrow)"></line>'
                        '<circle class="cot-svg-node cot-svg-node-outline" cx="120" cy="28" r="18"></circle>'
                        '<circle class="cot-svg-node cot-svg-node-outline" cx="58" cy="84" r="18"></circle>'
                        '<circle class="cot-svg-node cot-svg-node-outline" cx="150" cy="84" r="18"></circle>'
                        '<circle class="cot-svg-node cot-svg-node-outline" cx="58" cy="140" r="18"></circle>'
                        '<circle class="cot-svg-node cot-svg-node-dark" cx="96" cy="140" r="18"></circle>'
                        '<circle class="cot-svg-node cot-svg-node-outline" cx="202" cy="140" r="18"></circle>'
                        "</svg>"
                        "</div>"
                    )
                else:
                    diagram = (
                        '<div class="cot-triad-diagram">'
                        '<svg class="cot-diagram-svg cot-cot-svg" viewBox="0 0 240 180" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Chain-of-Thought diagram">'
                        '<circle class="cot-svg-node cot-svg-node-outline" cx="120" cy="24" r="16"></circle>'
                        '<circle class="cot-svg-node cot-svg-node-outline" cx="120" cy="70" r="16"></circle>'
                        '<circle class="cot-svg-node cot-svg-node-outline" cx="120" cy="116" r="16"></circle>'
                        '<circle class="cot-svg-node cot-svg-node-dark" cx="120" cy="162" r="16"></circle>'
                        '<line class="cot-svg-edge" x1="120" y1="42.5" x2="120" y2="45"></line>'
                        '<path class="cot-arrow-head" d="M114,45 L120,51 L126,45 z"></path>'
                        '<line class="cot-svg-edge" x1="120" y1="88.5" x2="120" y2="91"></line>'
                        '<path class="cot-arrow-head" d="M114,91 L120,97 L126,91 z"></path>'
                        '<line class="cot-svg-edge" x1="120" y1="134.5" x2="120" y2="137"></line>'
                        '<path class="cot-arrow-head" d="M114,137 L120,143 L126,137 z"></path>'
                        "</svg>"
                        "</div>"
                    )

                return (
                    '<article class="process-step cot-triad-card">'
                    f'<h2>{title}</h2>'
                    f'<p class="cot-triad-acronym">{acronym}</p>'
                    f"{diagram}"
                    f'<small>{meaning}</small>'
                    "</article>"
                )

            cards = "".join(render_card(card) for card in spec.body.get("cards", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="cot-triad-body process-track">'
                f"{cards}"
                "</section>"
            )

        if spec.body.get("variant") == "cot-native":
            nodes = [str(node) for node in spec.body.get("nodes", [])]
            chain = "".join(
                f'<span class="process-step cot-reasoning-step cot-chain-node{" cot-chain-answer" if index == len(nodes) - 1 else ""}">{html.escape(node)}</span>'
                + ('<i class="cot-chain-arrow" aria-hidden="true">↓</i>' if index < len(nodes) - 1 else "")
                for index, node in enumerate(nodes)
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="cot-native-body">'
                '<div class="cot-linear-stage">'
                '<div class="cot-example-diagram">'
                f"{chain}"
                "</div>"
                "</div>"
                '<article class="cot-minimal-card">'
                f'<h2>{html.escape(spec.body.get("claim", spec.key_claim))}</h2>'
                "</article>"
                "</section>"
            )

        if spec.body.get("variant") == "pattern-pair":
            def render_pair_diagram(item: dict[str, object]) -> str:
                nodes = [str(node) for node in item.get("nodes", [])]
                if item.get("kind") == "tot":
                    branches = "".join(
                        f'<span class="{"selected" if index == 1 else ""}">{html.escape(node)}</span>'
                        for index, node in enumerate(nodes)
                    )
                    return (
                        '<div class="pattern-native-diagram tot-diagram">'
                        '<span class="tree-root">문제</span>'
                        f"{branches}"
                        '<span class="tree-leaf">후보</span>'
                        '<span class="tree-leaf selected">후보</span>'
                        '<span class="tree-leaf">후보</span>'
                        "</div>"
                    )
                return (
                    '<div class="pattern-native-diagram react-diagram">'
                    f'<span class="react-node react-reasoning">{html.escape(nodes[0]) if len(nodes) > 0 else ""}</span>'
                    f'<span class="react-node react-action">{html.escape(nodes[1]) if len(nodes) > 1 else ""}</span>'
                    f'<span class="react-node react-observation">{html.escape(nodes[2]) if len(nodes) > 2 else ""}</span>'
                    '<i class="react-arrow react-arrow-action">→</i>'
                    '<i class="react-arrow react-arrow-observation">←</i>'
                    '<i class="react-arrow react-arrow-reasoning">↺</i>'
                    + "</div>"
                )

            cards = "".join(
                '<article class="process-step pattern-pair-card">'
                f'<span class="step-index">{html.escape(item["index"])}</span>'
                f'<h2>{html.escape(item["title"])}</h2>'
                f'<p>{html.escape(item["text"])}</p>'
                f'{render_pair_diagram(item)}'
                f'<small>{html.escape(item["meaning"])}</small>'
                "</article>"
                for item in spec.body.get("patterns", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="pattern-pair-body">'
                f"{cards}"
                "</section>"
            )

        if spec.body.get("variant") == "feedback-pair":
            cards = "".join(
                '<article class="process-step feedback-loop-card">'
                f'<h2>{html.escape(item["title"])}</h2>'
                f'<p>{html.escape(item["text"])}</p>'
                f'<div class="pattern-native-diagram feedback-diagram {html.escape(item["class"])}">'
                + "".join(
                    f'<span>{html.escape(str(node))}</span>' + ("<i>→</i>" if index < len(item.get("nodes", [])) - 1 else "")
                    for index, node in enumerate(item.get("nodes", []))
                )
                + "</div>"
                f'<small>{html.escape(item["meaning"])}</small>'
                "</article>"
                for item in spec.body.get("patterns", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="feedback-loop-body">'
                f"{cards}"
                "</section>"
            )

        if spec.body.get("variant") == "pattern-diagram":
            def render_pattern_diagram(item: dict[str, object]) -> str:
                kind = str(item.get("kind", "cot"))
                example = item.get("example")
                if kind == "react":
                    if isinstance(example, dict):
                        return (
                            '<div class="pattern-native-diagram react-diagram pattern-example-diagram">'
                            f'<span>{html.escape(str(example.get("start", "")))}</span><i>→</i>'
                            f'<span>{html.escape(str(example.get("action", "")))}</span><i>→</i>'
                            f'<span>{html.escape(str(example.get("observation", "")))}</span>'
                            "</div>"
                        )
                    return (
                        '<div class="pattern-native-diagram react-diagram">'
                        '<span>Reason</span><i>↔</i><span>Act</span><i>↔</i><span>Observe</span>'
                        "</div>"
                    )
                if kind == "tot":
                    if isinstance(example, dict):
                        branches = "".join(
                            f'<span class="{html.escape(branch.get("class", ""))}">{html.escape(branch["text"])}</span>'
                            for branch in example.get("branches", [])
                        )
                        return (
                            '<div class="pattern-native-diagram tot-diagram pattern-example-diagram">'
                            f'<span class="tree-root">{html.escape(str(example.get("root", "")))}</span>'
                            f"{branches}"
                            "</div>"
                        )
                    return (
                        '<div class="pattern-native-diagram tot-diagram">'
                        '<span class="tree-root">문제</span>'
                        '<span>경로 A</span><span class="selected">경로 B</span><span>경로 C</span>'
                        "</div>"
                    )
                if kind == "reflexion":
                    if isinstance(example, dict):
                        return (
                            '<div class="pattern-native-diagram feedback-diagram reflexion-diagram pattern-example-diagram">'
                            f'<span>{html.escape(str(example.get("trial", "")))}</span><i>→</i>'
                            f'<span>{html.escape(str(example.get("memory", "")))}</span><i>→</i>'
                            f'<span>{html.escape(str(example.get("retry", "")))}</span>'
                            "</div>"
                        )
                    return (
                        '<div class="pattern-native-diagram feedback-diagram reflexion-diagram">'
                        '<span>실행</span><i>→</i><span>피드백</span><i>→</i><span>기억</span>'
                        "</div>"
                    )
                if kind == "refine":
                    if isinstance(example, dict):
                        return (
                            '<div class="pattern-native-diagram feedback-diagram refine-diagram pattern-example-diagram">'
                            f'<span>{html.escape(str(example.get("draft", "")))}</span><i>→</i>'
                            f'<span>{html.escape(str(example.get("feedback", "")))}</span><i>→</i>'
                            f'<span>{html.escape(str(example.get("refined", "")))}</span>'
                            "</div>"
                        )
                    return (
                        '<div class="pattern-native-diagram feedback-diagram refine-diagram">'
                        '<span>초안</span><i>→</i><span>비판</span><i>→</i><span>수정</span>'
                        "</div>"
                    )
                if kind == "cot" and isinstance(example, dict):
                    return (
                        '<div class="pattern-native-diagram cot-diagram cot-example-diagram pattern-example-diagram">'
                        f'<span class="cot-example-problem">{html.escape(str(example.get("problem", "")))}</span>'
                        '<i>→</i>'
                        f'<span>{html.escape(str(example.get("step", "")))}</span>'
                        '<i>→</i>'
                        f'<strong class="cot-example-answer">{html.escape(str(example.get("answer", "")))}</strong>'
                        "</div>"
                    )
                return (
                    '<div class="pattern-native-diagram cot-diagram">'
                    '<span>문제</span><i>→</i><span>추론 경로</span><i>→</i><span>답</span>'
                    "</div>"
                )

            cards = []
            for item in spec.body.get("patterns", []):
                example_label = ""
                if isinstance(item.get("example"), dict):
                    example_label = f'<span class="pattern-example-title">{html.escape(str(item["example"].get("label", "")))}</span>'
                cards.append(
                    '<li class="process-step pattern-diagram-card pattern-example-card">'
                    f'<span class="step-index">{html.escape(item["index"])}</span>'
                    f'<span class="step-title">{html.escape(item["title"])}</span>'
                    f'<span class="step-copy">{html.escape(item["text"])}</span>'
                    f"{example_label}"
                    f'{render_pattern_diagram(item)}'
                    "</li>"
                )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="prompt-pattern-lab-body">'
                f'<ol class="process-track pattern-diagram-grid">{"".join(cards)}</ol>'
                "</section>"
            )

        if spec.body.get("variant") == "cursor-tools":
            def render_cursor_panel(panel: dict[str, object], class_name: str) -> str:
                items = "".join(f'<li>{html.escape(str(item))}</li>' for item in panel.get("items", []))
                return (
                    f'<article class="process-step cursor-tool-panel {class_name}">'
                    f'<h2>{html.escape(str(panel["title"]))}</h2>'
                    f'<ul>{items}</ul>'
                    "</article>"
                )

            tools = "".join(f'<span>{html.escape(tool)}</span>' for tool in spec.body.get("tools", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="cursor-tools-body">'
                '<div class="cursor-tools-compare">'
                f'{render_cursor_panel(spec.body.get("left", {}), "is-before")}'
                '<div class="cursor-tools-arrow" aria-hidden="true">→</div>'
                f'{render_cursor_panel(spec.body.get("right", {}), "is-after")}'
                "</div>"
                f'<div class="cursor-tools-rail">{tools}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "cursor-architecture-native":
            steps = "".join(
                '<li class="process-step cursor-architecture-step">'
                f'<span class="step-index">{html.escape(step["index"])}</span>'
                f'<span class="step-title">{html.escape(step["title"])}</span>'
                f'<span class="step-copy">{html.escape(step["text"])}</span>'
                "</li>"
                for step in spec.body.get("steps", [])
            )
            tools = "".join(f"<span>{html.escape(tool)}</span>" for tool in spec.body.get("tools", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="cursor-architecture-redraw-body">'
                '<div class="cursor-architecture-canvas">'
                '<div class="cursor-architecture-example-canvas">'
                f'<p class="architecture-request">{html.escape(spec.body.get("request", "사용자 요청"))}</p>'
                '<div class="architecture-arrow" aria-hidden="true">→</div>'
                '<article class="architecture-boundary codebase-index-box">'
                '<h2>codebase index</h2>'
                f'<p>{html.escape(spec.body.get("index", ""))}</p>'
                "</article>"
                '<div class="architecture-arrow" aria-hidden="true">→</div>'
                '<article class="architecture-boundary context-bundle-box">'
                '<h2>context bundle</h2>'
                f'<p>{html.escape(spec.body.get("context", ""))}</p>'
                "</article>"
                '<div class="architecture-arrow" aria-hidden="true">→</div>'
                '<p class="architecture-editrun">edit/run</p>'
                '<div class="architecture-arrow" aria-hidden="true">→</div>'
                f'<p class="architecture-feedback">{html.escape(spec.body.get("feedback", spec.key_claim))}</p>'
                "</div>"
                f'<ol class="process-track cursor-architecture-flow">{steps}</ol>'
                "</div>"
                '<aside class="architecture-side-tools">'
                '<p>Tools</p>'
                f"{tools}"
                "</aside>"
                "</div>"
                "</section>"
            )

        if spec.body.get("variant") == "cursor-architecture-asset":
            flow_steps = "".join(
                '<li class="cursor-architecture-graph-step">'
                '<div class="cursor-architecture-graph-node">'
                f'<span class="cursor-architecture-graph-title">{html.escape(step["title"])}</span>'
                + (
                    f'<span class="cursor-architecture-graph-detail">{html.escape(step["detail"])}</span>'
                    if step.get("detail")
                    else ""
                )
                + "</div>"
                "</li>"
                for step in spec.body.get("flow", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="cursor-architecture-asset-body">'
                f'{render_asset_figure(Path(spec.body["asset"]), "cursor-architecture-reference-figure", spec.title)}'
                '<div class="cursor-architecture-explanation">'
                f'<ol class="cursor-architecture-arrow-graph">{flow_steps}</ol>'
                "</div>"
                "</section>"
            )

        if spec.body.get("variant") == "harness-era-signs":
            cards = "".join(
                '<article class="process-step harness-era-card">'
                f'<h2>{html.escape(card["title"])}</h2>'
                f'<p>{html.escape(card["text"])}</p>'
                "</article>"
                for card in spec.body.get("cards", [])
            )
            components = "".join(
                f'<span class="harness-era-component">{html.escape(component)}</span>'
                for component in spec.body.get("components", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="harness-era-signs-body">'
                f'<p class="harness-era-claim centered-claim">{html.escape(spec.body.get("statement", spec.key_claim))}</p>'
                '<div class="harness-era-system">'
                f'<div class="harness-era-components">{components}</div>'
                '<div class="harness-era-runtime centered-claim">실행 환경</div>'
                "</div>"
                f'<div class="harness-era-grid">{cards}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "harness-environment-map":
            decision_cards = "".join(
                '<article class="responsibility-card harness-decision-card">'
                f'<h2>{html.escape(str(card.get("title", "")))}</h2>'
                f'<p>{html.escape(str(card.get("text", "")))}</p>'
                "</article>"
                for card in spec.body.get("decisions", [])
            )
            flow_parts: list[str] = []
            flow = spec.body.get("flow", [])
            for index, step in enumerate(flow):
                flow_parts.append(
                    '<li class="process-step harness-runtime-step">'
                    f'<span class="step-index">{html.escape(str(step.get("index", "")))}</span>'
                    f'<span class="step-title">{html.escape(str(step.get("title", "")))}</span>'
                    "</li>"
                )
                if index < len(flow) - 1:
                    flow_parts.append('<div class="harness-runtime-arrow" aria-hidden="true">→</div>')
            support_groups = "".join(
                '<div class="harness-support-stack">'
                + "".join(
                    '<article class="tool-cluster-card harness-support-card">'
                    f'<h2>{html.escape(str(item))}</h2>'
                    "</article>"
                    for item in group
                )
                + "</div>"
                for group in spec.body.get("groups", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="harness-environment-map-body">'
                f'<div class="responsibility-column harness-decision-column">{decision_cards}</div>'
                '<div class="harness-runtime-column">'
                f'<ol class="process-track harness-runtime-flow">{"".join(flow_parts)}</ol>'
                f'<div class="harness-support-grid">{support_groups}</div>'
                "</div>"
                "</section>"
            )

        if spec.body.get("variant") == "harness-era-minimal":
            flow_nodes = "".join(
                '<li class="harness-era-minimal-node'
                + (" is-emphasis" if node.get("emphasis") else "")
                + '">'
                f'<span>{html.escape(node["title"])}</span>'
                + (f'<small>{html.escape(node["text"])}</small>' if node.get("text") else "")
                + "</li>"
                for node in spec.body.get("flow", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="harness-era-minimal-body">'
                '<article class="harness-era-minimal-claim">'
                f'<h2>{html.escape(spec.body.get("claim", spec.key_claim))}</h2>'
                "</article>"
                f'<ol class="harness-era-minimal-flow">{flow_nodes}</ol>'
                "</section>"
            )

        if spec.body.get("variant") == "pattern-map":
            nodes = "".join(
                '<li class="process-step pattern-node">'
                f'<span class="step-index">{html.escape(item["index"])}</span>'
                f'<span class="step-title">{html.escape(item["title"])}</span>'
                f'<span class="step-copy">{html.escape(item["text"])}</span>'
                "</li>"
                for item in spec.body.get("patterns", [])
            )
            assets = "".join(
                render_asset_figure(Path(asset), "pattern-asset", Path(asset).name)
                for asset in spec.body.get("assets", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="pattern-map-body">'
                f'<ol class="process-track pattern-node-grid">{nodes}</ol>'
                f'<div class="pattern-assets">{assets}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "asset-process":
            steps = "".join(
                '<li class="process-step asset-process-step">'
                f'<span class="step-index">{html.escape(step["index"])}</span>'
                f'<span class="step-title">{html.escape(step["title"])}</span>'
                f'<span class="step-copy">{html.escape(step["text"])}</span>'
                "</li>"
                for step in spec.body.get("steps", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="asset-process-body">'
                f'{render_asset_figure(Path(spec.body["asset"]), "asset-process-figure", spec.title)}'
                f'<ol class="asset-process-list">{steps}</ol>'
                "</section>"
            )

        if spec.body.get("variant") == "loop-map":
            loop_steps = spec.body.get("steps", [])
            step_parts = []
            for index, step in enumerate(loop_steps[:4], start=1):
                step_parts.append(
                    f'<article class="process-step loop-step loop-step-{index}">'
                    f'<span class="step-index">{html.escape(step["index"])}</span>'
                    f'<span class="step-title">{html.escape(step["title"])}</span>'
                    f'<span class="step-copy">{html.escape(step["text"])}</span>'
                    "</article>"
                )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="loop-cycle-body">'
                '<div class="loop-cycle-track">'
                f"{step_parts[0]}"
                '<div class="loop-cycle-arrow arrow-east" aria-hidden="true">→</div>'
                f"{step_parts[1]}"
                '<div class="loop-cycle-arrow arrow-north" aria-hidden="true">↑</div>'
                '<div class="loop-center-gap" aria-hidden="true"></div>'
                '<div class="loop-cycle-arrow arrow-south" aria-hidden="true">↓</div>'
                f"{step_parts[3]}"
                '<div class="loop-cycle-arrow arrow-west" aria-hidden="true">←</div>'
                f"{step_parts[2]}"
                "</div>"
                f'<p class="flow-thesis loop-synthesis centered-claim">{html.escape(spec.body.get("thesis", spec.key_claim))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "context-failure-focus":
            risks = "".join(
                '<article class="context-failure-risk">'
                f'<p>{html.escape(risk)}</p>'
                "</article>"
                for risk in spec.body.get("risks", [])
            )
            emphasis = "".join(
                '<p class="context-failure-emphasis-line">'
                f"{html.escape(line)}"
                "</p>"
                for line in spec.body.get("emphasis", [])
            )
            minor_controls = "".join(
                '<span class="context-failure-minor-control">'
                f"{html.escape(control)}"
                "</span>"
                for control in spec.body.get("minor_controls", [])
            )
            priority_controls = "".join(
                '<article class="context-failure-priority-card">'
                f'<p>{html.escape(control)}</p>'
                "</article>"
                for control in spec.body.get("priority_controls", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="context-failure-body">'
                '<div class="context-failure-grid">'
                f'<div class="context-failure-risk-grid">{risks}</div>'
                '<div class="context-failure-side">'
                f'<p class="context-failure-support centered-claim">{html.escape(spec.body.get("support", spec.key_claim))}</p>'
                f'<article class="context-failure-emphasis">{emphasis}</article>'
                '<div class="context-failure-controls">'
                f'<div class="context-failure-minor">{minor_controls}</div>'
                f'<div class="context-failure-priority">{priority_controls}</div>'
                "</div>"
                "</div>"
                "</div>"
                "</section>"
            )

        if spec.body.get("variant") == "context-wall":
            risks = "".join(
                f'<span class="context-wall-risk">{html.escape(risk)}</span>'
                for risk in spec.body.get("risks", [])
            )
            controls = "".join(
                f'<li class="context-wall-control">{html.escape(control)}</li>'
                for control in spec.body.get("controls", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="context-wall-body">'
                '<div class="context-wall-grid">'
                '<article class="context-wall-source">'
                f'<span class="context-wall-kicker">컨텍스트 시대의 질문</span>'
                f'<p>{html.escape(spec.body.get("source", ""))}</p>'
                "</article>"
                f'<p class="context-wall-claim centered-claim">{html.escape(spec.body.get("claim", spec.key_claim))}</p>'
                '<article class="context-wall-controls">'
                f'<span class="context-wall-kicker">필요해진 통제</span>'
                f'<ul>{controls}</ul>'
                "</article>"
                "</div>"
                f'<div class="context-wall-risk-strip">{risks}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "context-quote":
            steps = "".join(
                '<li class="process-step context-strategy-card">'
                f'<span class="step-index">{html.escape(step["index"])}</span>'
                f'<span class="step-title">{html.escape(step["title"])}</span>'
                f'<span class="step-copy">{html.escape(step["text"])}</span>'
                "</li>"
                for step in spec.body.get("steps", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="body-area flow-body context-engineering-body">'
                f'<ol class="process-track context-strategy-grid">{steps}</ol>'
                '<figure class="quote-card-block context-quote-block">'
                f'<blockquote>{html.escape(str(spec.body.get("thesis", spec.key_claim)))}</blockquote>'
                f'<figcaption>{html.escape(str(spec.body.get("source_label", "")))}</figcaption>'
                "</figure>"
                "</section>"
            )

        if spec.body.get("variant") == "mcp-context-architecture":
            flow_nodes = "".join(
                (
                    '<div class="mcp-usage-stage">'
                    f'<strong>{html.escape(str(node.get("title", "")))}</strong>'
                    f'<span>{html.escape(str(node.get("text", "")))}</span>'
                    "</div>"
                    + (
                        '<div class="mcp-usage-arrow" aria-hidden="true">→</div>'
                        if index < len(spec.body.get("flow", [])) - 1
                        else ""
                    )
                )
                for index, node in enumerate(spec.body.get("flow", []))
            )
            principles = "".join(
                '<div class="context7-note">'
                f'<dt>{html.escape(str(item.get("label", "")))}</dt>'
                f'<dd>{html.escape(str(item.get("text", "")))}</dd>'
                "</div>"
                for item in spec.body.get("principles", [])
            )
            examples = " · ".join(str(tool) for tool in spec.body.get("tools", []))
            examples_html = (
                f'<p class="mcp-connected-examples">{html.escape(examples)}</p>'
                if examples
                else ""
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="mcp-context-card-body">'
                '<article class="mcp-usage-card">'
                '<p class="panel-kicker">에이전트가 MCP를 쓰는 구조</p>'
                f'<div class="mcp-usage-flow">{flow_nodes}</div>'
                f'<p class="mcp-usage-note">{html.escape(str(spec.body.get("usage_note", "")))}</p>'
                f"{examples_html}"
                "</article>"
                '<article class="context7-mcp-card">'
                f'<p class="panel-kicker">{html.escape(str(spec.body.get("hub_label", "Context 7 MCP")))}</p>'
                f'<h2>{html.escape(str(spec.body.get("hub_title", "최신 문서 연결")))}</h2>'
                f'<dl class="context7-notes">{principles}</dl>'
                "</article>"
                "</section>"
            )

        if spec.body.get("variant") == "component-clusters":
            if spec.body.get("tiers"):
                rows = []
                for tier in spec.body.get("tiers", []):
                    items = []
                    for item in tier.get("items", []):
                        item_class = " component-main-block" if item.get("primary") else ""
                        items.append(
                            f'<article class="process-step component-tier-card{item_class}">'
                            f'<span class="step-title">{html.escape(item["title"])}</span>'
                            f'<span class="step-copy">{html.escape(item["text"])}</span>'
                            "</article>"
                        )
                    rows.append(
                        '<div class="component-tier-row">'
                        f'<span class="component-tier-label">{html.escape(tier["label"])}</span>'
                        f'<div class="component-tier-items">{"".join(items)}</div>'
                        "</div>"
                    )
                return (
                    '<section class="top-band">'
                    f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                    f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                    "</section>"
                    '<section class="component-tier-body">'
                    f'{"".join(rows)}'
                    "</section>"
                )
            steps = "".join(
                '<li class="process-step component-step">'
                f'<span class="step-index">{html.escape(step["index"])}</span>'
                f'<span class="step-title">{html.escape(step["title"])}</span>'
                f'<span class="step-copy">{html.escape(step["text"])}</span>'
                "</li>"
                for step in spec.body.get("steps", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="body-area component-body">'
                f'<p class="component-context centered-claim">{html.escape(spec.body.get("context", ""))}</p>'
                f'<ol class="process-track component-grid">{steps}</ol>'
                "</section>"
            )

        if spec.body.get("variant") == "evolution-analogies":
            flow_steps = "".join(
                (
                    f'<div class="evolution-step{" is-final" if index == len(spec.body.get("flow", [])) - 1 else ""}">'
                    f'<p>{html.escape(step)}</p>'
                    "</div>"
                    + ('<div class="evolution-arrow" aria-hidden="true">↓</div>' if index < len(spec.body.get("flow", [])) - 1 else "")
                )
                for index, step in enumerate(spec.body.get("flow", []))
            )
            analogies = "".join(
                '<article class="analogy-block">'
                f'<p class="analogy-title">{html.escape(item["title"])}</p>'
                + "".join(f'<p>{html.escape(line)}</p>' for line in item.get("lines", []))
                + "</article>"
                for item in spec.body.get("analogies", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="evolution-body">'
                '<div class="evolution-flow">'
                f"{flow_steps}"
                "</div>"
                '<div class="analogy-stack">'
                f"{analogies}"
                "</div>"
                "</section>"
            )

        if spec.body.get("variant") == "document-grid":
            steps = "".join(
                '<li class="process-step document-card">'
                f'{render_document_icon(step.get("icon", "file"), step.get("tool", ""))}'
                f'<span class="doc-product">{html.escape(step.get("tool", ""))}</span>'
                f'<span class="step-title">{html.escape(step["title"])}</span>'
                "</li>"
                for step in spec.body.get("steps", [])
            )
        elif spec.body.get("variant") == "role-split":
            groups = "".join(
                '<article class="role-panel">'
                f'<h2>{html.escape(group["title"])}</h2>'
                "<ul>"
                + "".join(f'<li>{html.escape(item)}</li>' for item in group.get("items", []))
                + "</ul>"
                "</article>"
                for group in spec.body.get("groups", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                f"{render_lead(spec.lead)}"
                "</section>"
                '<section class="role-split-body">'
                f'<p class="role-summary centered-claim">{html.escape(spec.body.get("summary", spec.key_claim))}</p>'
                f'<div class="role-panels">{groups}</div>'
                "</section>"
            )
        else:
            steps = "".join(
                '<li class="process-step">'
                f'<span class="step-index">{html.escape(step["index"])}</span>'
                f'<span class="step-title">{html.escape(step["title"])}</span>'
                f'<span class="step-copy">{html.escape(step["text"])}</span>'
                "</li>"
                for step in spec.body.get("steps", [])
            )
        thesis = ""
        if spec.body.get("thesis"):
            thesis = f'<p class="flow-thesis centered-claim">{html.escape(spec.body["thesis"])}</p>'
        source_label = ""
        if spec.body.get("source_label"):
            source_label = f'<p class="flow-source-label">{html.escape(spec.body["source_label"])}</p>'
        return (
            '<section class="top-band">'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f"{render_lead(spec.lead)}"
            "</section>"
            '<section class="body-area flow-body">'
            f'<ol class="process-track {html.escape(spec.body.get("variant", ""))}">{steps}</ol>'
            f"{thesis}"
            f"{source_label}"
            "</section>"
        )

    if spec.shell == "split-compare-shell":
        if spec.body.get("variant") == "long-work-cost-map":
            examples = "".join(
                f'<li class="long-work-example">{html.escape(item)}</li>'
                for item in spec.body.get("examples", [])
            )
            gates = "".join(
                f'<li class="long-work-gate">{html.escape(item)}</li>'
                for item in spec.body.get("gates", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                f"{render_lead(spec.lead)}"
                "</section>"
                '<section class="long-work-cost-map">'
                '<div class="long-work-flow">'
                f'<article class="long-work-node is-start">{html.escape(spec.body.get("start", ""))}</article>'
                '<i class="long-work-arrow" aria-hidden="true">→</i>'
                '<article class="long-work-conversion">'
                f'<span>{html.escape(spec.body.get("conversion_left", ""))}</span>'
                '<b aria-hidden="true">→</b>'
                f'<span>{html.escape(spec.body.get("conversion_right", ""))}</span>'
                "</article>"
                '<i class="long-work-arrow" aria-hidden="true">→</i>'
                f'<article class="long-work-node is-end">{html.escape(spec.body.get("end", ""))}</article>'
                "</div>"
                f'<ul class="long-work-examples">{examples}</ul>'
                f'<ul class="long-work-gates">{gates}</ul>'
                "</section>"
            )

        if spec.body.get("variant") == "context-signal-stack":
            noise_items = "".join(
                f'<li class="context-noise-chip">{html.escape(item)}</li>'
                for item in spec.body.get("noise", [])
            )
            equation = str(spec.body.get("equation", ""))
            if not equation:
                equation = f'{spec.body.get("left", "")} ≠ {spec.body.get("right", "")}'
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                f"{render_lead(spec.lead)}"
                "</section>"
                '<section class="context-signal-body">'
                f'<p class="context-signal-claim">{html.escape(spec.body.get("claim", spec.key_claim))}</p>'
                '<div class="context-signal-equation">'
                f'<span>{html.escape(equation)}</span>'
                "</div>"
                f'<ul class="context-noise-row">{noise_items}</ul>'
                f'<p class="context-signal-operating">{html.escape(spec.body.get("operating", ""))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "control-gate-board":
            left_items = "".join(f'<li class="control-gate-item">{html.escape(item)}</li>' for item in spec.body.get("left_items", []))
            right_items = "".join(f'<li class="control-gate-item">{html.escape(item)}</li>' for item in spec.body.get("right_items", []))
            claim_parts = "".join(
                f'<span>{html.escape(part)}</span>'
                for part in spec.body.get("claim_parts", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                f"{render_lead(spec.lead)}"
                "</section>"
                '<section class="control-gate-board-body">'
                f'<p class="control-gate-claim">{claim_parts}</p>'
                '<div class="control-gate-board">'
                '<article class="control-gate-lane is-deterministic">'
                f'<h2>{html.escape(spec.body.get("left_title", ""))}</h2>'
                f'<ul class="control-gate-list">{left_items}</ul>'
                "</article>"
                '<article class="control-gate-lane is-probabilistic">'
                f'<h2>{html.escape(spec.body.get("right_title", ""))}</h2>'
                f'<ul class="control-gate-list">{right_items}</ul>'
                "</article>"
                "</div>"
                "</section>"
            )

        if spec.body.get("variant") == "prefix-suffix-cache":
            def render_cache_tokens(points: list[str]) -> str:
                return "".join(f'<li class="cache-token">{html.escape(point)}</li>' for point in points)

            left_badges = "".join(
                f'<span>{html.escape(str(badge))}</span>' for badge in spec.body.get("left_badges", [])
            )
            right_badges = "".join(
                f'<span>{html.escape(str(badge))}</span>' for badge in spec.body.get("right_badges", [])
            )
            quote = ""
            if spec.body.get("quote"):
                quote = (
                    '<figure class="quote-card-block cache-quote-block">'
                    f'<blockquote>{html.escape(str(spec.body.get("quote", "")))}</blockquote>'
                    f'<figcaption>{html.escape(str(spec.body.get("attribution", "")))}</figcaption>'
                    "</figure>"
                )
            elif spec.body.get("opinion"):
                quote = f'<p class="cache-synthesis centered-claim">{html.escape(str(spec.body.get("opinion", spec.key_claim)))}</p>'

            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                f"{render_lead(spec.lead)}"
                "</section>"
                '<section class="compare-grid with-arrow cache-sequence-body">'
                '<article class="compare-col cache-segment stable-prefix-block">'
                f'<p class="compare-label">{html.escape(spec.body.get("left_label", "Stable Prefix"))}</p>'
                f'<div class="cache-badge-row">{left_badges}</div>'
                f'<ul class="cache-token-stack">{render_cache_tokens([str(point) for point in spec.body.get("left_points", [])])}</ul>'
                f'<p class="cache-role-note">{html.escape(str(spec.body.get("left_note", "")))}</p>'
                "</article>"
                '<div class="compare-arrow cache-sequence-arrow" aria-hidden="true">→</div>'
                '<article class="compare-col cache-segment variable-suffix-block is-focus">'
                f'<p class="compare-label">{html.escape(spec.body.get("right_label", "Variable Suffix"))}</p>'
                f'<div class="cache-badge-row">{right_badges}</div>'
                f'<ul class="cache-token-stack">{render_cache_tokens([str(point) for point in spec.body.get("right_points", [])])}</ul>'
                f'<p class="cache-role-note">{html.escape(str(spec.body.get("right_note", "")))}</p>'
                "</article>"
                "</section>"
                f"{quote}"
            )

        if spec.body.get("variant") == "context-loop-injection":
            step_parts = []
            for index, step in enumerate(spec.body.get("steps", [])[:4], start=1):
                step_parts.append(
                    f'<article class="process-step loop-step context-loop-step context-loop-step-{index}">'
                    f'<span class="step-index">{html.escape(str(step["index"]))}</span>'
                    f'<span class="step-title">{html.escape(str(step["title"]))}</span>'
                    "</article>"
                )
            issue_cards = "".join(
                '<article class="context-issue-tile">'
                f'<h2>{html.escape(issue)}</h2>'
                "</article>"
                for issue in spec.body.get("issues", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="compare-grid with-arrow context-loop-injection-body">'
                '<article class="compare-col context-loop-column">'
                '<div class="context-loop-panel">'
                '<p class="context-loop-caption">루프</p>'
                '<div class="loop-cycle-track context-loop-mini-track">'
                f"{step_parts[0]}"
                '<div class="loop-cycle-arrow arrow-east context-loop-mini-arrow" aria-hidden="true">→</div>'
                f"{step_parts[1]}"
                '<div class="loop-cycle-arrow arrow-north context-loop-mini-arrow" aria-hidden="true">↑</div>'
                '<div class="loop-center-gap context-loop-mini-gap" aria-hidden="true"></div>'
                '<div class="loop-cycle-arrow arrow-south context-loop-mini-arrow" aria-hidden="true">↓</div>'
                f"{step_parts[3]}"
                '<div class="loop-cycle-arrow arrow-west context-loop-mini-arrow" aria-hidden="true">←</div>'
                f"{step_parts[2]}"
                "</div>"
                "</div>"
                "</article>"
                '<div class="compare-arrow context-injection-rail">'
                '<div class="context-injection-plus" aria-hidden="true">+</div>'
                "</div>"
                '<article class="compare-col context-issue-column">'
                f'<div class="context-issue-grid">{issue_cards}</div>'
                "</article>"
                "</section>"
                f'<p class="context-loop-synthesis centered-claim">{html.escape(str(spec.body.get("opinion", spec.key_claim)))}</p>'
            )

        if spec.body.get("variant") == "waterfall-comparison":
            header = (
                '<div class="comparison-column-headers">'
                '<div class="comparison-column-spacer" aria-hidden="true"></div>'
                '<div class="compare-col comparison-column-header">'
                f'{html.escape(spec.body.get("left_label", "축 A"))}'
                "</div>"
                '<div class="comparison-column-gap" aria-hidden="true"></div>'
                '<div class="compare-col comparison-column-header is-focus">'
                f'{html.escape(spec.body.get("right_label", "축 B"))}'
                "</div>"
                "</div>"
            )
            rows = "".join(
                '<article class="comparison-row">'
                f'<p class="comparison-row-key">{html.escape(row["key"])}</p>'
                f'<p class="comparison-row-left">{html.escape(row["left"])}</p>'
                '<div class="comparison-row-gap" aria-hidden="true"></div>'
                f'<p class="comparison-row-right">{html.escape(row["right"])}</p>'
                "</article>"
                for row in spec.body.get("rows", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="waterfall-comparison-body">'
                f"{header}"
                '<div class="comparison-row-grid">'
                f"{rows}"
                "</div>"
                "</section>"
            )

        left_content = render_compare_content(spec, "left")
        right_content = render_compare_content(spec, "right")
        arrow = '<div class="compare-arrow" aria-hidden="true">→</div>' if spec.body.get("arrow") else ""
        grid_class = "compare-grid with-arrow" if spec.body.get("arrow") else "compare-grid"
        if spec.body.get("variant"):
            grid_class += f' {html.escape(str(spec.body["variant"]))}'
        opinion = ""
        if spec.body.get("opinion"):
            opinion = f'<p class="negative-opinion">{html.escape(spec.body["opinion"])}</p>'
        return (
            '<section class="top-band">'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f"{render_lead(spec.lead)}"
            "</section>"
            f'<section class="{grid_class}">'
            '<article class="compare-col">'
            f'<p class="compare-label">{html.escape(spec.body.get("left_label", "축 A"))}</p>'
            f"{left_content}"
            "</article>"
            f"{arrow}"
            '<article class="compare-col is-focus">'
            f'<p class="compare-label">{html.escape(spec.body.get("right_label", "축 B"))}</p>'
            f"{right_content}"
            "</article>"
            "</section>"
            f"{opinion}"
        )

    if spec.shell == "evidence-table-shell":
        if spec.body.get("variant") == "chapter-wall-cards":
            cards = "".join(render_chapter_card(card, "ch-wall-card") for card in spec.body.get("cards", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-wall-body">'
                f'<div class="ch-wall-grid">{cards}</div>'
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-principle-grid":
            cards = "".join(render_chapter_card(card, "ch-principle-card") for card in spec.body.get("cards", []))
            count = len(spec.body.get("cards", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                f'<section class="ch-principle-grid-body ch-principle-count-{count}">'
                f'<div class="ch-principle-grid">{cards}</div>'
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-solid-cards":
            cards = "".join(render_chapter_card(card, "ch-solid-card") for card in spec.body.get("cards", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-solid-body">'
                f'<div class="ch-solid-grid">{cards}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-risk-matrix":
            cards = "".join(render_chapter_card(card, "ch-risk-card") for card in spec.body.get("cards", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-risk-body">'
                f'<div class="ch-risk-grid">{cards}</div>'
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-model-rail":
            models = "".join(render_chapter_card(card, "ch-model-card") for card in spec.body.get("models", []))
            rail = render_native_nodes([str(item) for item in spec.body.get("rail", [])], "ch-decision-rail")
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-model-rail-body">'
                f'<div class="ch-model-grid">{models}</div>'
                f"{rail}"
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "chapter-split-panels":
            panels = "".join(render_chapter_card(card, "ch-split-panel") for card in spec.body.get("cards", []))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="ch-split-panels-body">'
                f'<div class="ch-split-panels">{panels}</div>'
                f'<p class="ch-dark-conclusion centered-claim">{html.escape(str(spec.body.get("conclusion", spec.key_claim)))}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "agent-harness-quote":
            components = "".join(
                '<article class="agent-component-card">'
                f'<h2>{html.escape(item["title"])}</h2>'
                f'<p>{html.escape(item["text"])}</p>'
                "</article>"
                for item in spec.body.get("components", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="table-wrap agent-harness-quote-body">'
                '<figure class="quote-card-block agent-quote-block">'
                f'<blockquote>{html.escape(str(spec.body.get("quote", spec.key_claim)))}</blockquote>'
                f'<figcaption>{html.escape(str(spec.body.get("attribution", "")))}</figcaption>'
                "</figure>"
                f'<div class="agent-component-grid">{components}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "rag-context-researched":
            cards = "".join(
                f'<article class="rag-context-card{" is-focus" if card.get("focus") else ""}">'
                f'<p class="compare-label">{html.escape(str(card.get("label", "")))}</p>'
                f'<h2>{html.escape(str(card.get("title", "")))}</h2>'
                "<ul>"
                + "".join(f'<li>{html.escape(str(item))}</li>' for item in card.get("items", []))
                + "</ul>"
                "</article>"
                for card in spec.body.get("cards", [])
            )
            grid_class = "rag-context-grid"
            if len(spec.body.get("cards", [])) > 2:
                grid_class += " rag-context-card-set"
            decision = ""
            if spec.body.get("decision"):
                decision = (
                    '<article class="rag-context-decision">'
                    f'<span>{html.escape(str(spec.body.get("decision_label", "선택 기준")))}</span>'
                    f'<p>{html.escape(str(spec.body.get("decision", spec.key_claim)))}</p>'
                    "</article>"
                )
            source = ""
            if spec.body.get("source_label"):
                source = f'<p class="research-source-line">{html.escape(str(spec.body.get("source_label", "")))}</p>'
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="table-wrap rag-context-research-body">'
                f'<div class="{grid_class}">{cards}</div>'
                f"{decision}"
                f"{source}"
                "</section>"
            )

        if spec.body.get("variant") == "rag-context-table":
            columns = [str(column) for column in spec.body.get("columns", ["구분", "RAG", "Context 7"])]
            header = "".join(f"<th>{html.escape(column)}</th>" for column in columns)
            rows = "".join(
                "<tr>"
                f'<th scope="row">{html.escape(str(row.get("axis", "")))}</th>'
                f'<td>{html.escape(str(row.get("rag", "")))}</td>'
                f'<td class="is-focus">{html.escape(str(row.get("context", "")))}</td>'
                "</tr>"
                for row in spec.body.get("rows", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="table-wrap rag-context-table-body">'
                f'<p class="rag-context-table-caption">{html.escape(spec.key_claim)}</p>'
                '<table class="rag-context-table">'
                f"<thead><tr>{header}</tr></thead>"
                f"<tbody>{rows}</tbody>"
                "</table>"
                "</section>"
            )

        if spec.body.get("variant") == "metric-impact-cards":
            body_class = "table-wrap evidence-cards-body metric-impact-body"
            if spec.body.get("reference") == "tall":
                body_class += " is-tall-reference"
            cards = "".join(
                '<article class="evidence-card impact-card">'
                f'<strong>{html.escape(card["value"])}</strong>'
                f'<span>{html.escape(card["label"])}</span>'
                f'<p>{html.escape(card["text"])}</p>'
                f'<small>{html.escape(card["meta"])}</small>'
                "</article>"
                for card in spec.body.get("cards", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                f'<section class="{body_class}">'
                f'<div class="evidence-card-grid impact-card-grid">{cards}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "agentic-native":
            def render_agentic_diagram(kind: str) -> str:
                def marker(marker_id: str) -> str:
                    return (
                        f'<defs><marker id="{marker_id}" viewBox="0 0 10 10" refX="8" refY="5" '
                        'markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
                        '<path class="agentic-arrow-head" d="M 0 0 L 10 5 L 0 10 z"></path>'
                        "</marker></defs>"
                    )

                if kind == "reflection":
                    return (
                        '<div class="agentic-system-diagram agentic-reflection-diagram">'
                        '<svg class="agentic-map-svg" viewBox="0 0 320 88" aria-hidden="true" focusable="false">'
                        f'{marker("agentic-arrow-reflection")}'
                        '<rect class="agentic-flow-workspace" x="86" y="14" width="128" height="60" rx="10"></rect>'
                        '<circle class="agentic-flow-node is-input" cx="38" cy="44" r="9"></circle>'
                        '<path class="agentic-flow-edge" marker-end="url(#agentic-arrow-reflection)" d="M50 44 H83"></path>'
                        '<circle class="agentic-flow-node" cx="128" cy="30" r="10"></circle>'
                        '<circle class="agentic-flow-node is-accent" cx="176" cy="44" r="10"></circle>'
                        '<circle class="agentic-flow-node" cx="128" cy="58" r="10"></circle>'
                        '<path class="agentic-flow-edge" marker-end="url(#agentic-arrow-reflection)" d="M139 30 C154 25 168 30 173 38"></path>'
                        '<path class="agentic-flow-edge" marker-end="url(#agentic-arrow-reflection)" d="M173 50 C162 62 145 64 137 59"></path>'
                        '<path class="agentic-flow-edge" marker-end="url(#agentic-arrow-reflection)" d="M120 53 C108 45 109 37 120 33"></path>'
                        '<path class="agentic-flow-edge" marker-end="url(#agentic-arrow-reflection)" d="M214 44 H263"></path>'
                        '<circle class="agentic-flow-node is-output" cx="282" cy="44" r="11"></circle>'
                        "</svg>"
                        "</div>"
                    )
                if kind == "tool-use":
                    return (
                        '<div class="agentic-system-diagram agentic-tool-diagram">'
                        '<svg class="agentic-map-svg" viewBox="0 0 320 88" aria-hidden="true" focusable="false">'
                        f'{marker("agentic-arrow-tool")}'
                        '<rect class="agentic-flow-workspace" x="112" y="13" width="102" height="62" rx="10"></rect>'
                        '<circle class="agentic-flow-node is-input" cx="36" cy="23" r="7"></circle>'
                        '<circle class="agentic-flow-node is-input" cx="36" cy="44" r="7"></circle>'
                        '<circle class="agentic-flow-node is-input" cx="36" cy="65" r="7"></circle>'
                        '<circle class="agentic-flow-node" cx="156" cy="23" r="9"></circle>'
                        '<circle class="agentic-flow-node" cx="156" cy="44" r="9"></circle>'
                        '<circle class="agentic-flow-node" cx="156" cy="65" r="9"></circle>'
                        '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-tool)" d="M46 23 H144"></path>'
                        '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-tool)" d="M46 44 H144"></path>'
                        '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-tool)" d="M46 65 H144"></path>'
                        '<path class="agentic-flow-edge" marker-end="url(#agentic-arrow-tool)" d="M166 23 C204 24 224 34 254 42"></path>'
                        '<path class="agentic-flow-edge" marker-end="url(#agentic-arrow-tool)" d="M166 44 H254"></path>'
                        '<path class="agentic-flow-edge" marker-end="url(#agentic-arrow-tool)" d="M166 65 C204 64 224 54 254 46"></path>'
                        '<circle class="agentic-flow-node is-output" cx="280" cy="44" r="10"></circle>'
                        '<circle class="agentic-flow-node is-output is-ghost" cx="292" cy="44" r="10"></circle>'
                        '<circle class="agentic-flow-node is-output is-ghost" cx="286" cy="32" r="10"></circle>'
                        '<circle class="agentic-flow-node is-output is-ghost" cx="286" cy="56" r="10"></circle>'
                        "</svg>"
                        "</div>"
                    )
                if kind == "planning":
                    return (
                        '<div class="agentic-system-diagram agentic-planning-diagram">'
                        '<svg class="agentic-map-svg" viewBox="0 0 320 88" aria-hidden="true" focusable="false">'
                        f'{marker("agentic-arrow-planning")}'
                        '<rect class="agentic-flow-workspace" x="96" y="10" width="122" height="68" rx="10"></rect>'
                        '<circle class="agentic-flow-node is-input" cx="58" cy="44" r="8"></circle>'
                        '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-planning)" d="M68 44 H102"></path>'
                        '<circle class="agentic-flow-node is-accent" cx="116" cy="44" r="11"></circle>'
                        '<circle class="agentic-flow-node" cx="184" cy="23" r="9"></circle>'
                        '<circle class="agentic-flow-node" cx="184" cy="44" r="9"></circle>'
                        '<circle class="agentic-flow-node" cx="184" cy="65" r="9"></circle>'
                        '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-planning)" d="M129 39 C148 29 162 24 172 23"></path>'
                        '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-planning)" d="M129 44 H172"></path>'
                        '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-planning)" d="M129 49 C148 59 162 64 172 65"></path>'
                        '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-planning)" d="M195 23 H252"></path>'
                        '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-planning)" d="M195 44 H252"></path>'
                        '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-planning)" d="M195 65 H252"></path>'
                        '<circle class="agentic-flow-node is-output" cx="272" cy="23" r="8"></circle>'
                        '<circle class="agentic-flow-node is-output" cx="272" cy="44" r="8"></circle>'
                        '<circle class="agentic-flow-node is-output" cx="272" cy="65" r="8"></circle>'
                        "</svg>"
                        "</div>"
                    )
                return (
                    '<div class="agentic-system-diagram agentic-multi-diagram">'
                    '<svg class="agentic-map-svg" viewBox="0 0 320 88" aria-hidden="true" focusable="false">'
                    f'{marker("agentic-arrow-multi")}'
                    '<rect class="agentic-flow-workspace" x="88" y="14" width="144" height="60" rx="10"></rect>'
                    '<circle class="agentic-flow-node is-input" cx="38" cy="44" r="9"></circle>'
                    '<path class="agentic-flow-edge" marker-end="url(#agentic-arrow-multi)" d="M50 44 H88"></path>'
                    '<circle class="agentic-flow-node" cx="128" cy="28" r="10"></circle>'
                    '<circle class="agentic-flow-node is-accent" cx="190" cy="44" r="10"></circle>'
                    '<circle class="agentic-flow-node" cx="128" cy="60" r="10"></circle>'
                    '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-multi)" d="M139 30 C160 28 174 34 183 39"></path>'
                    '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-multi)" d="M139 58 C160 60 174 54 183 49"></path>'
                    '<path class="agentic-flow-edge is-soft" marker-end="url(#agentic-arrow-multi)" d="M128 39 V49"></path>'
                    '<path class="agentic-flow-edge" marker-end="url(#agentic-arrow-multi)" d="M202 44 H258"></path>'
                    '<circle class="agentic-flow-node is-output" cx="280" cy="44" r="11"></circle>'
                    "</svg>"
                    "</div>"
                )

            cards = "".join(
                f'<article class="evidence-card agentic-pattern-card is-{html.escape(str(card.get("kind", "pattern")))}">'
                f'<h2>{html.escape(card["title"])}</h2>'
                f'<p>{html.escape(card["text"])}</p>'
                f'{render_agentic_diagram(str(card.get("kind", "")))}'
                f'<small>{html.escape(card["effect"])}</small>'
                "</article>"
                for card in spec.body.get("cards", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="agentic-pattern-quadrant-body">'
                '<div class="evidence-card-grid agentic-pattern-canvas">'
                f"{cards}"
                "</div>"
                "</section>"
            )

        if spec.body.get("variant") == "asset-plus-cards":
            cards = "".join(
                '<article class="evidence-card agentic-pattern-card">'
                f'<span>{html.escape(card["title"])}</span>'
                f'<p>{html.escape(card["text"])}</p>'
                "</article>"
                for card in spec.body.get("cards", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="asset-card-body">'
                f'{render_asset_figure(Path(spec.body["asset"]), "reference-asset-figure", spec.title)}'
                f'<div class="evidence-card-grid agentic-pattern-grid">{cards}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "era-native":
            cards = "".join(
                '<article class="era-native-card">'
                f'<span>{html.escape(card["range"])}</span>'
                f'<h2>{html.escape(card["title"])}</h2>'
                f'<p>{html.escape(card["question"])}</p>'
                "</article>"
                for card in spec.body.get("cards", [])
            )
            question = ""
            if spec.body.get("question"):
                question = f'<p class="table-question">{html.escape(spec.body["question"])}</p>'
            formula = ""
            if spec.body.get("formula"):
                formula = f'<p class="era-native-formula centered-claim">{html.escape(str(spec.body["formula"]))}</p>'
            relationship = html.escape(str(spec.body.get("relationship", "Prompt ⊂ Context ⊂ Harness")))
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="era-native-body">'
                f'<div class="era-native-track">{cards}</div>'
                f"{formula}"
                f'<p class="era-native-equation centered-claim">{relationship}</p>'
                f"{question}"
                "</section>"
            )

        if spec.body.get("variant") == "tool-relation-map":
            tool_items = [dict(item) for item in spec.body.get("tools", [])]
            tool_titles = [str(item["title"]) for item in tool_items]
            responsibility_items = [dict(item) for item in spec.body.get("responsibilities", [])]
            resp_count = max(len(responsibility_items), 1)
            tool_count = max(len(tool_items), 1)
            resp_y = {
                str(item["title"]): 18 + index * (248 / max(resp_count - 1, 1))
                for index, item in enumerate(responsibility_items)
            }
            tool_y = {
                title: 14 + index * (256 / max(tool_count - 1, 1))
                for index, title in enumerate(tool_titles)
            }
            paths: list[str] = []
            for item in responsibility_items:
                source = str(item["title"])
                source_y = resp_y[source]
                for tool in item.get("tools", []):
                    target = str(tool)
                    target_y = tool_y.get(target, source_y)
                    paths.append(
                        '<path class="tool-network-line" '
                        f'd="M 6 {source_y:.1f} C 96 {source_y:.1f}, 220 {target_y:.1f}, 334 {target_y:.1f}" />'
                    )
            connectors = "".join(paths)
            responsibilities = "".join(
                '<article class="responsibility-card">'
                f'<h2>{html.escape(item["title"])}</h2>'
                "</article>"
                for item in responsibility_items
            )
            tools = "".join(
                '<article class="tool-cluster-card">'
                f'<h2>{html.escape(item["title"])}</h2>'
                "</article>"
                for item in tool_items
            )
            relation_claim = ""
            if spec.body.get("question"):
                relation_claim = f'<p class="relation-claim centered-claim">{html.escape(str(spec.body["question"]))}</p>'
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="table-wrap tool-relation-map">'
                f"{relation_claim}"
                '<div class="tool-relation-grid">'
                f'<div class="responsibility-column">{responsibilities}</div>'
                '<svg class="relation-connector tool-network-lines" viewBox="0 0 340 284" preserveAspectRatio="none" aria-hidden="true">'
                f"{connectors}"
                "</svg>"
                f'<div class="tool-cluster-grid">{tools}</div>'
                "</div>"
                f'<p class="tool-network-synthesis centered-claim">{html.escape(spec.key_claim)}</p>'
                "</section>"
            )

        if spec.body.get("variant") == "memory-artifact-map":
            artifacts = "".join(
                '<article class="memory-artifact-card">'
                f'<h2>{html.escape(item["title"])}</h2>'
                f'<p>{html.escape(item["text"])}</p>'
                "</article>"
                for item in spec.body.get("artifacts", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="table-wrap memory-artifact-map">'
                f'<div class="memory-artifact-grid">{artifacts}</div>'
                f'<p class="memory-core-claim centered-claim">{html.escape(spec.body.get("question", spec.key_claim))}</p>'
                "</section>"
            )

        if spec.body.get("variant") in {"evidence-cards", "source-boundary-cards"}:
            cards = "".join(
                '<article class="evidence-card">'
                f'<strong>{html.escape(card["value"])}</strong>'
                f'<span>{html.escape(card["label"])}</span>'
                f'<p>{html.escape(card["text"])}</p>'
                "</article>"
                for card in spec.body.get("cards", [])
            )
            question = ""
            if spec.body.get("question"):
                question = f'<p class="table-question">{html.escape(str(spec.body["question"]))}</p>'
            body_class = f'table-wrap evidence-cards-body {html.escape(str(spec.body.get("variant", "")))}'
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                f'<section class="{body_class}">'
                f'<div class="evidence-card-grid">{cards}</div>'
                f"{question}"
                "</section>"
            )

        if spec.body.get("variant") == "maturity-ladder":
            tiers = "".join(
                '<article class="maturity-tier">'
                f'<span class="maturity-index">{html.escape(tier["index"])}</span>'
                '<div class="maturity-main">'
                f'<h2>{html.escape(tier["title"])}</h2>'
                f'<p>{html.escape(tier["state"])}</p>'
                f'<small>{html.escape(tier["goal"])}</small>'
                "</div>"
                f'<strong>{html.escape(tier.get("metric", ""))}</strong>'
                "</article>"
                for tier in spec.body.get("tiers", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="table-wrap maturity-ladder-body">'
                f'<p class="table-callout">{html.escape(spec.body.get("callout", ""))}</p>'
                f'<div class="maturity-ladder">{tiers}</div>'
                "</section>"
            )

        if spec.body.get("variant") == "role-split":
            groups = "".join(
                '<article class="role-panel">'
                f'<h2>{html.escape(group["title"])}</h2>'
                "<ul>"
                + "".join(f'<li>{html.escape(item)}</li>' for item in group.get("items", []))
                + "</ul>"
                "</article>"
                for group in spec.body.get("groups", [])
            )
            rows = "".join(
                "<tr>"
                f"<td>{html.escape(group['title'])}</td>"
                f"<td>{html.escape(' / '.join(group.get('items', [])))}</td>"
                "</tr>"
                for group in spec.body.get("groups", [])
            )
            return (
                '<section class="top-band capability-header">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                f"{render_lead(spec.lead)}"
                "</section>"
                '<section class="table-wrap role-split-body">'
                f'<p class="role-summary centered-claim">{html.escape(spec.body.get("summary", spec.key_claim))}</p>'
                f'<div class="role-panels">{groups}</div>'
                '<div class="hidden-data-table">'
                '<table class="data-table">'
                "<thead><tr><th>축</th><th>능력</th></tr></thead>"
                f"<tbody>{rows}</tbody>"
                "</table>"
                "</div>"
                "</section>"
            )

        if spec.body.get("variant") == "capability-map":
            items = "".join(
                '<li class="capability-item">'
                f'<span>{index:02d}</span>'
                f'<strong>{html.escape(item)}</strong>'
                "</li>"
                for index, item in enumerate(spec.body.get("capabilities", []), start=1)
            )
            headers = "".join(f"<th>{html.escape(header)}</th>" for header in spec.body.get("headers", []))
            rows = "".join(
                "<tr>" + "".join(f"<td>{html.escape(cell)}</td>" for cell in row) + "</tr>"
                for row in spec.body.get("rows", [])
            )
            return (
                '<section class="top-band capability-header">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                f"{render_lead(spec.lead)}"
                "</section>"
                '<section class="table-wrap capability-map">'
                f'<ol class="capability-rail">{items}</ol>'
                '<table class="data-table">'
                f"<thead><tr>{headers}</tr></thead>"
                f"<tbody>{rows}</tbody>"
                "</table>"
                "</section>"
            )

        metrics = ""
        if spec.body.get("metrics"):
            metrics = '<div class="metric-grid">' + "".join(
                '<article class="metric-card">'
                f'<strong>{html.escape(metric["value"])}</strong>'
                f'<span>{html.escape(metric["label"])}</span>'
                f'<p>{html.escape(metric["text"])}</p>'
                "</article>"
                for metric in spec.body["metrics"]
            ) + "</div>"
        headers = "".join(f"<th>{html.escape(header)}</th>" for header in spec.body.get("headers", []))
        rows = "".join(
            "<tr>" + "".join(f"<td>{html.escape(cell)}</td>" for cell in row) + "</tr>"
            for row in spec.body.get("rows", [])
        )
        question = ""
        if spec.body.get("question"):
            question = f'<p class="table-question">{html.escape(spec.body["question"])}</p>'
        callout = ""
        if spec.body.get("callout"):
            callout = f'<div class="table-callout">{html.escape(spec.body["callout"])}</div>'
        return (
            '<section class="top-band">'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f"{render_lead(spec.lead)}"
            "</section>"
            f'<section class="table-wrap {html.escape(spec.body.get("variant", ""))}">'
            f"{callout}"
            f"{metrics}"
            '<table class="data-table">'
            f"<thead><tr>{headers}</tr></thead>"
            f"<tbody>{rows}</tbody>"
            "</table>"
            f"{question}"
            "</section>"
        )

    raise ValueError(f"unknown shell: {spec.shell}")

def render_slide_markup(spec: SlideSpec) -> str:
    chapter_class = f" chapter-{spec.source_section}" if spec.source_section else ""
    return (
        f'<main class="slide family-{spec.family} layout-{spec.layout} density-{spec.density}{chapter_class}" '
        f'data-slide-id="{spec.slide_id}" '
        f'data-shell="{spec.shell}" '
        f'data-notes="{attr_escape(spec.notes)}" '
        'data-footer="default">'
        f"{render_tool_icons() if spec.order == 1 else ''}"
        f"{render_shell(spec)}"
        f"{render_footer(spec)}"
        "</main>"
    )

def render_slide_file(spec: SlideSpec) -> str:
    return "\n".join(
        [
            "<!DOCTYPE html>",
            '<html lang="ko">',
            "<head>",
            '<meta charset="UTF-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            f"<title>{html.escape(spec.title)}</title>",
            '<link rel="icon" href="data:,">',
            '<link rel="stylesheet" href="../shared/tokens.css">',
            '<link rel="stylesheet" href="../shared/slide-base.css">',
            "</head>",
            f'<body class="{THEME}">',
            render_slide_markup(spec),
            "</body>",
            "</html>",
            "",
        ]
    )

def render_deck(specs: list[SlideSpec]) -> str:
    tokens = TOKENS_CSS.read_text(encoding="utf-8")
    base = BASE_CSS.read_text(encoding="utf-8")
    wrappers = []
    for spec in specs:
        active = " active" if spec.order == 1 else ""
        wrappers.append(f'<section class="deck-slide{active}" data-slide-id="{spec.slide_id}">{render_slide_markup(spec)}</section>')

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Harness 잘 사용하기</title>
<link rel="icon" href="data:,">
<style>
{tokens}
{base}
:root {{
  --deck-scale: 1;
}}
html, body {{
  width: 100%;
  height: 100%;
  margin: 0;
  overflow: hidden;
  background: var(--color-paper);
}}
body {{
  width: 100vw;
  height: 100vh;
}}
.deck {{
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}}
.deck-slide {{
  position: absolute;
  inset: 0;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 18px;
  overflow: hidden;
}}
.deck-slide.active {{
  display: flex;
}}
.deck-slide .slide {{
  transform: scale(var(--deck-scale));
  transform-origin: center center;
  box-shadow: 0 18px 60px rgba(0, 0, 0, 0.08);
}}
@media print {{
  html, body {{
    overflow: visible;
    height: auto;
    background: #fff;
  }}
  .deck {{
    height: auto;
    overflow: visible;
  }}
  .deck-slide {{
    position: relative;
    display: block !important;
    page-break-after: always;
    page-break-inside: avoid;
    padding: 0;
  }}
  .deck-slide .slide {{
    transform: none !important;
    box-shadow: none;
  }}
  @page {{
    size: 720pt 405pt;
    margin: 0;
  }}
}}
</style>
</head>
<body class="{THEME}">
<div class="deck">
{''.join(wrappers)}
</div>
<script>
const slides = Array.from(document.querySelectorAll('.deck-slide'));
let currentIndex = 0;
let touchStartX = 0;

function updateScale() {{
  const widthScale = window.innerWidth / 960;
  const heightScale = window.innerHeight / 540;
  const scale = Math.min(widthScale, heightScale);
  document.documentElement.style.setProperty('--deck-scale', String(scale));
}}

function goTo(index) {{
  const bounded = Math.max(0, Math.min(index, slides.length - 1));
  slides[currentIndex].classList.remove('active');
  currentIndex = bounded;
  slides[currentIndex].classList.add('active');
}}

window.addEventListener('resize', updateScale);
window.addEventListener('keydown', (event) => {{
  if (event.key === 'ArrowRight' || event.key === ' ') {{
    event.preventDefault();
    goTo(currentIndex + 1);
  }}
  if (event.key === 'ArrowLeft') {{
    event.preventDefault();
    goTo(currentIndex - 1);
  }}
}});

window.addEventListener('touchstart', (event) => {{
  touchStartX = event.changedTouches[0].clientX;
}});

window.addEventListener('touchend', (event) => {{
  const delta = event.changedTouches[0].clientX - touchStartX;
  if (delta < -40) goTo(currentIndex + 1);
  if (delta > 40) goTo(currentIndex - 1);
}});

updateScale();
</script>
</body>
</html>
"""
