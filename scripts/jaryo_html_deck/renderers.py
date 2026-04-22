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

def render_compare_content(spec: SlideSpec, side: str) -> str:
    code = spec.body.get(f"{side}_code")
    if code is not None:
        return render_code_block(str(code))

    points = "".join(
        f'<li class="compare-point">{html.escape(point)}</li>'
        for point in spec.body.get(f"{side}_points", [])
    )
    return f'<ul class="compare-list">{points}</ul>'

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
            lead = ""
            if spec.lead:
                lead = f'<p class="tdd-control-lead">{html.escape(spec.lead)}</p>'
            return (
                '<section class="top-band">'
                f'<p class="chapter-label statement-tag">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder statement-text">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="statement-panel tdd-control-layers-body">'
                f"{lead}"
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
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="blind-prompting-body blind-prompting-matrix-body">'
                f'<p class="blind-prompting-claim centered-claim">{html.escape(spec.body.get("statement", spec.key_claim))}</p>'
                f'<div class="blind-prompting-grid">{cards}</div>'
                f'<p class="blind-prompting-thesis centered-claim">{html.escape(spec.body.get("thesis", ""))}</p>'
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
        if spec.body.get("variant") == "spec-kit-workflow":
            stages = []
            for step in spec.body.get("steps", []):
                items = "".join(f'<li>{html.escape(item)}</li>' for item in step.get("items", []))
                stages.append(
                    '<li class="process-step spec-kit-stage">'
                    f'<span class="step-index">{html.escape(step["index"])}</span>'
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
                        '<svg class="cot-diagram-svg cot-react-svg" viewBox="0 0 246 164" preserveAspectRatio="xMidYMid meet" role="img" aria-label="ReAct diagram">'
                        f'<defs><marker id="{marker_id}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path class="cot-arrow-head" d="M0,0 L8,4 L0,8 z"></path></marker></defs>'
                        '<path class="cot-svg-edge" d="M66 54 C28 36, 22 128, 66 112" marker-end="url(#cot-triad-react-arrow)"></path>'
                        '<text class="cot-svg-caption cot-svg-accent" x="14" y="22" text-anchor="start" aria-label="Reasoning Traces">'
                        '<tspan x="14" dy="0">Reasoning</tspan>'
                        '<tspan x="14" dy="13">Traces</tspan>'
                        '</text>'
                        '<rect class="cot-svg-node cot-svg-node-outline" x="70" y="54" rx="18" ry="18" width="70" height="42"></rect>'
                        '<text class="cot-svg-text" x="105" y="75" text-anchor="middle" dominant-baseline="middle" font-size="15">LM</text>'
                        '<rect class="cot-svg-node cot-svg-node-outline" x="164" y="54" rx="18" ry="18" width="70" height="42"></rect>'
                        '<text class="cot-svg-text" x="199" y="75" text-anchor="middle" dominant-baseline="middle" font-size="15">Env</text>'
                        '<path class="cot-svg-edge" d="M104 50 C122 28, 146 28, 164 50" marker-end="url(#cot-triad-react-arrow)"></path>'
                        '<text class="cot-svg-caption cot-svg-accent" x="134" y="26" text-anchor="middle">Actions</text>'
                        '<path class="cot-svg-edge" d="M164 100 C146 124, 122 124, 104 104" marker-end="url(#cot-triad-react-arrow)"></path>'
                        '<text class="cot-svg-caption cot-svg-accent" x="134" y="144" text-anchor="middle">Observations</text>'
                        '<text class="cot-svg-caption cot-svg-muted" x="124" y="156" text-anchor="middle">ReAct (Reason + Act)</text>'
                        "</svg>"
                        "</div>"
                    )
                elif kind == "tot":
                    diagram = (
                        '<div class="cot-triad-diagram">'
                        '<svg class="cot-diagram-svg cot-tot-svg" viewBox="0 0 240 160" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Tree-of-Thought diagram">'
                        f'<defs><marker id="{marker_id}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path class="cot-arrow-head" d="M0,0 L8,4 L0,8 z"></path></marker></defs>'
                        '<line class="cot-svg-edge cot-svg-edge-muted" x1="120" y1="46" x2="62" y2="86"></line>'
                        '<line class="cot-svg-edge" x1="120" y1="46" x2="120" y2="86" marker-end="url(#cot-triad-tot-arrow)"></line>'
                        '<line class="cot-svg-edge cot-svg-edge-muted" x1="120" y1="46" x2="178" y2="86"></line>'
                        '<rect class="cot-svg-node cot-svg-node-outline" x="80" y="16" rx="18" ry="18" width="80" height="30"></rect>'
                        '<text class="cot-svg-text" x="120" y="31" text-anchor="middle" dominant-baseline="middle" font-size="15">문제</text>'
                        '<rect class="cot-svg-node cot-svg-node-outline" x="32" y="86" rx="18" ry="18" width="58" height="30"></rect>'
                        '<text class="cot-svg-text" x="61" y="101" text-anchor="middle" dominant-baseline="middle" font-size="12">경로 A</text>'
                        '<rect class="cot-svg-node cot-svg-node-dark" x="91" y="86" rx="18" ry="18" width="58" height="30"></rect>'
                        '<text class="cot-svg-text cot-svg-text-invert" x="120" y="101" text-anchor="middle" dominant-baseline="middle" font-size="12">경로 B</text>'
                        '<rect class="cot-svg-node cot-svg-node-outline" x="150" y="86" rx="18" ry="18" width="58" height="30"></rect>'
                        '<text class="cot-svg-text" x="179" y="101" text-anchor="middle" dominant-baseline="middle" font-size="12">경로 C</text>'
                        "</svg>"
                        "</div>"
                    )
                else:
                    diagram = (
                        '<div class="cot-triad-diagram">'
                        '<svg class="cot-diagram-svg cot-cot-svg" viewBox="0 0 240 160" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Chain-of-Thought diagram">'
                        f'<defs><marker id="{marker_id}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path class="cot-arrow-head" d="M0,0 L8,4 L0,8 z"></path></marker></defs>'
                        '<line class="cot-svg-edge" x1="120" y1="41" x2="120" y2="56" marker-end="url(#cot-triad-cot-arrow)"></line>'
                        '<line class="cot-svg-edge" x1="120" y1="87" x2="120" y2="102" marker-end="url(#cot-triad-cot-arrow)"></line>'
                        '<rect class="cot-svg-node cot-svg-node-outline" x="56" y="10" rx="18" ry="18" width="128" height="30"></rect>'
                        '<text class="cot-svg-text" x="120" y="25" text-anchor="middle" dominant-baseline="middle" font-size="15">문제</text>'
                        '<rect class="cot-svg-node cot-svg-node-outline" x="46" y="56" rx="18" ry="18" width="148" height="30"></rect>'
                        '<text class="cot-svg-text" x="120" y="71" text-anchor="middle" dominant-baseline="middle" font-size="14">중간 추론</text>'
                        '<rect class="cot-svg-node cot-svg-node-dark" x="78" y="102" rx="18" ry="18" width="84" height="30"></rect>'
                        '<text class="cot-svg-text cot-svg-text-invert" x="120" y="117" text-anchor="middle" dominant-baseline="middle" font-size="15">답</text>'
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
                    '<article class="mcp-usage-node">'
                    f'<span>{html.escape(str(node.get("title", "")))}</span>'
                    f'<p>{html.escape(str(node.get("text", "")))}</p>'
                    "</article>"
                    + (
                        '<div class="mcp-usage-arrow" aria-hidden="true">→</div>'
                        if index < len(spec.body.get("flow", [])) - 1
                        else ""
                    )
                )
                for index, node in enumerate(spec.body.get("flow", []))
            )
            principles = "".join(
                '<article class="context-hub-principle">'
                f'<span>{html.escape(str(item.get("label", "")))}</span>'
                f'<p>{html.escape(str(item.get("text", "")))}</p>'
                "</article>"
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
                '<section class="mcp-context-explainer-body">'
                '<article class="mcp-usage-panel">'
                '<p class="panel-kicker">에이전트가 MCP를 쓰는 구조</p>'
                f'<div class="mcp-usage-flow">{flow_nodes}</div>'
                f'<p class="mcp-usage-note">{html.escape(str(spec.body.get("usage_note", "")))}</p>'
                f"{examples_html}"
                "</article>"
                '<article class="context-hub-explainer-card">'
                '<p class="panel-kicker">Context Hub MCP</p>'
                f'<h2>{html.escape(str(spec.body.get("hub_title", "최신 문서 연결")))}</h2>'
                f'<div class="context-hub-principles">{principles}</div>'
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
        if spec.body.get("variant") == "prefix-suffix-cache":
            def render_cache_tokens(points: list[str]) -> str:
                return "".join(f'<li class="cache-token">{html.escape(point)}</li>' for point in points)

            left_badges = "".join(
                f'<span>{html.escape(str(badge))}</span>' for badge in spec.body.get("left_badges", [])
            )
            right_badges = "".join(
                f'<span>{html.escape(str(badge))}</span>' for badge in spec.body.get("right_badges", [])
            )
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
                f'<p class="cache-synthesis centered-claim">{html.escape(str(spec.body.get("opinion", spec.key_claim)))}</p>'
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
                '<article class="rag-context-card">'
                f'<p class="compare-label">{html.escape(str(card.get("label", "")))}</p>'
                f'<h2>{html.escape(str(card.get("title", "")))}</h2>'
                "<ul>"
                + "".join(f'<li>{html.escape(str(item))}</li>' for item in card.get("items", []))
                + "</ul>"
                "</article>"
                for card in spec.body.get("cards", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="table-wrap rag-context-research-body">'
                f'<div class="rag-context-grid">{cards}</div>'
                '<article class="rag-context-decision">'
                f'<span>{html.escape(str(spec.body.get("decision_label", "선택 기준")))}</span>'
                f'<p>{html.escape(str(spec.body.get("decision", spec.key_claim)))}</p>'
                "</article>"
                f'<p class="research-source-line">{html.escape(str(spec.body.get("source_label", "")))}</p>'
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
            cards = "".join(
                '<article class="evidence-card agentic-pattern-card">'
                f'<h2>{html.escape(card["title"])}</h2>'
                f'<p>{html.escape(card["text"])}</p>'
                '<div class="agentic-mini-diagram">'
                + "".join(f'<span>{html.escape(node)}</span>' + ('<i>→</i>' if index < len(card.get("example", [])) - 1 else "") for index, node in enumerate(card.get("example", [])))
                + "</div>"
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
                f'<p class="agentic-pattern-center centered-claim">{html.escape(spec.body.get("thesis", spec.key_claim))}</p>'
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

        if spec.body.get("variant") == "evidence-cards":
            cards = "".join(
                '<article class="evidence-card">'
                f'<strong>{html.escape(card["value"])}</strong>'
                f'<span>{html.escape(card["label"])}</span>'
                f'<p>{html.escape(card["text"])}</p>'
                "</article>"
                for card in spec.body.get("cards", [])
            )
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="table-wrap evidence-cards-body">'
                f'<div class="evidence-card-grid">{cards}</div>'
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
            '<section class="table-wrap">'
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
