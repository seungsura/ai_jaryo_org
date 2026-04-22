from __future__ import annotations

import html
import textwrap
from pathlib import Path

from .assets import render_asset_figure, render_document_icon, render_tool_icons
from .config import BASE_CSS, THEME, TOKENS_CSS
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
        keywords = "".join(f'<li class="section-keyword">{html.escape(keyword)}</li>' for keyword in spec.body.get("keywords", []))
        return (
            '<section class="section-main">'
            f'<p class="chapter-marker">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f"{render_short_line(spec.lead)}"
            f'<ul class="section-keywords">{keywords}</ul>'
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

        if spec.body.get("variant") == "cot-native":
            step_items = list(spec.body.get("steps", []))
            problem = step_items[0] if len(step_items) > 0 else {"title": "", "text": ""}
            reasoning = step_items[1] if len(step_items) > 1 else {"title": "", "text": ""}
            answer = step_items[2] if len(step_items) > 2 else {"title": "", "text": ""}
            return (
                '<section class="top-band">'
                f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
                f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
                "</section>"
                '<section class="cot-native-body">'
                '<article class="process-step cot-claim-card">'
                f'<h2>{html.escape(spec.body.get("claim", spec.key_claim))}</h2>'
                f'<p>{html.escape(spec.body.get("meaning", ""))}</p>'
                "</article>"
                '<article class="process-step cot-example-card">'
                '<div class="cot-example-diagram">'
                '<div class="cot-example-panel cot-reasoning-step cot-example-input">'
                f'<strong>{html.escape(str(problem["title"]))}</strong>'
                f'<p>{html.escape(str(problem["text"]))}</p>'
                "</div>"
                '<div class="cot-example-panel cot-reasoning-step cot-example-output">'
                f'<strong>{html.escape(str(reasoning["title"]))}</strong>'
                f'<p class="cot-highlight">{html.escape(str(reasoning["text"]))}</p>'
                f'<p class="cot-answer">{html.escape(str(answer["text"]))}</p>'
                "</div>"
                "</div>"
                "</article>"
                '<article class="process-step cot-summary-card">'
                '<h2>reasoning path</h2>'
                f'<p>{html.escape(spec.body.get("meaning", ""))}</p>'
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
                f'<p class="flow-thesis loop-center centered-claim">{html.escape(spec.body.get("thesis", spec.key_claim))}</p>'
                '<div class="loop-cycle-arrow arrow-south" aria-hidden="true">↓</div>'
                f"{step_parts[3]}"
                '<div class="loop-cycle-arrow arrow-west" aria-hidden="true">←</div>'
                f"{step_parts[2]}"
                "</div>"
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
        return (
            '<section class="top-band">'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f"{render_lead(spec.lead)}"
            "</section>"
            '<section class="body-area flow-body">'
            f'<ol class="process-track {html.escape(spec.body.get("variant", ""))}">{steps}</ol>'
            f"{thesis}"
            "</section>"
        )

    if spec.shell == "split-compare-shell":
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
