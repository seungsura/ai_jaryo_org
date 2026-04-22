#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "docs/03-html/manifest.md"

SHELL_RULES = {
    "title-hero-shell": ["cover-main", "cover-rule", "title-placeholder", "hero-points", "footer"],
    "agenda-list-shell": ["agenda-layout", "agenda-side", "agenda-list", "agenda-item", "footer"],
    "section-divider-shell": ["section-main", "chapter-marker", "title-placeholder", "section-keywords", "footer"],
    "statement-editorial-shell": ["statement-panel", "statement-tag", "statement-text", "statement-support", "footer"],
    "wide-bullets-shell": ["top-band", "body-area", "callout-card", "bullet-list", "footer"],
    "process-flow-shell": ["top-band", "process-track", "process-step", "footer"],
    "split-compare-shell": ["top-band", "compare-grid", "compare-col", "footer"],
    "evidence-table-shell": ["top-band", "table-wrap", "data-table", "footer"],
    "closing-shell": ["closing-main", "cover-rule", "title-placeholder", "closing-points", "footer"],
}


def parse_markdown_table(path: Path) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    in_registry = False
    headers: list[str] = []
    rows: list[dict[str, str]] = []

    for raw_line in lines:
        line = raw_line.strip()
        if line.startswith("| order | slide id |"):
            in_registry = True
            headers = [part.strip() for part in line.strip("|").split("|")]
            continue
        if not in_registry:
            continue
        if not line.startswith("|"):
            break
        normalized = line.replace("|", "").replace(" ", "")
        if normalized and set(normalized) == {"-"}:
            continue
        parts = [part.strip().strip("`") for part in line.strip("|").split("|")]
        if len(parts) != len(headers):
            continue
        rows.append(dict(zip(headers, parts, strict=True)))
    return rows


def extract_main_attrs(html: str) -> str | None:
    match = re.search(r"<main\b([^>]*)>", html, flags=re.IGNORECASE | re.DOTALL)
    return match.group(1) if match else None


def has_class(html: str, class_name: str) -> bool:
    pattern = rf'class="[^"]*\b{re.escape(class_name)}\b[^"]*"'
    return re.search(pattern, html) is not None


def footer_number(html: str) -> str | None:
    match = re.search(r'<span class="footer-right">\s*([^<]+?)\s*</span>', html)
    return match.group(1).strip() if match else None


def footer_left(html: str) -> str | None:
    match = re.search(r'<span class="footer-left">\s*([^<]+?)\s*</span>', html)
    return match.group(1).strip() if match else None


def body_class(html: str) -> str | None:
    match = re.search(r"<body\b[^>]*class=\"([^\"]+)\"", html)
    return match.group(1) if match else None


def check_forbidden_surface_tokens(path: Path, text: str, errors: list[str]) -> None:
    forbidden_snippets = [
        ("token", "--color-dark-surface-muted"),
        ("token", "--color-dark-card"),
        ("token", "--color-dark-card-border"),
        ("literal", "#eee9e1"),
        ("literal", "#f3efe7"),
        ("literal", "#e8e1d5"),
        ("summary-card", "background: var(--color-dark-card);"),
        ("summary-card", "border: 1px solid var(--color-dark-card-border);"),
        ("evolution-step", "background: var(--color-dark-surface-muted);"),
    ]
    for label, snippet in forbidden_snippets:
        if snippet in text:
            errors.append(f"{path.relative_to(ROOT)}: {label} still uses forbidden ivory/paper surface token")


def main() -> int:
    rows = parse_markdown_table(MANIFEST_PATH)
    if not rows:
        print(f"ERROR manifest slide registry not found: {MANIFEST_PATH}")
        return 1

    errors: list[str] = []
    warnings: list[str] = []

    css_text = ""
    slide_base_css = ROOT / "docs/03-html/shared/slide-base.css"
    if slide_base_css.exists():
        css_text = slide_base_css.read_text(encoding="utf-8")

    expected_slide_ids = [f"S{index:03d}" for index in range(1, 46)]
    actual_slide_ids = [row["slide id"] for row in rows]
    if actual_slide_ids != expected_slide_ids:
        errors.append("manifest must register exactly S001-S045 in order")

    for css_path in [
        ROOT / "docs/03-html/shared/tokens.css",
        ROOT / "docs/03-html/shared/slide-base.css",
        ROOT / "docs/03-html/deck/index.html",
    ]:
        if css_path.exists():
            css = css_path.read_text(encoding="utf-8")
            if "--color-dark-accent" in css or "#c76640" in css.lower():
                errors.append(f"{css_path.relative_to(ROOT)}: copper accent token/literal is not allowed")
            if css_path.name in {"slide-base.css", "index.html"}:
                check_forbidden_surface_tokens(css_path, css, errors)

    for row in rows:
        slide_id = row["slide id"]
        shell = row["shell"]
        layout = row["layout"]
        slide_type = row["slide type"]
        file_name = row["file"]
        path = ROOT / "docs/03-html/slides" / file_name

        if not path.exists():
            errors.append(f"{slide_id}: missing file {path}")
            continue

        html = path.read_text(encoding="utf-8")
        attrs = extract_main_attrs(html)
        if attrs is None:
            errors.append(f"{slide_id}: missing <main> root")
            continue

        if f'data-slide-id="{slide_id}"' not in attrs:
            errors.append(f"{slide_id}: main root missing data-slide-id")
        if f'data-shell="{shell}"' not in attrs:
            errors.append(f"{slide_id}: main root missing data-shell={shell}")
        if f"layout-{layout}" not in attrs:
            errors.append(f"{slide_id}: main root missing layout-{layout}")

        family_match = re.search(r"family-([a-z]+)", attrs)
        if not family_match:
            errors.append(f"{slide_id}: main root missing family-* class")
        if "density-" not in attrs:
            errors.append(f"{slide_id}: main root missing density-* class")
        if 'data-footer="default"' not in attrs:
            errors.append(f'{slide_id}: data-footer must be "default"')

        current_body_class = body_class(html)
        if current_body_class is None or "theme-minimal-light" not in current_body_class:
            errors.append(f"{slide_id}: <body> must declare theme-minimal-light")

        if 'style="' in html:
            errors.append(f"{slide_id}: inline style attribute is not allowed")

        if footer_left(html) != "Harness 잘 사용하기":
            errors.append(f"{slide_id}: footer-left must be 'Harness 잘 사용하기'")
        if footer_number(html) != row["order"]:
            errors.append(f"{slide_id}: footer-right must match order {row['order']}")

        required_classes = SHELL_RULES.get(shell)
        if required_classes is None:
            warnings.append(f"{slide_id}: unknown shell {shell}")
        else:
            if shell == "statement-editorial-shell":
                if "prompt-only-body" in html:
                    required_classes = ["top-band", "prompt-only-body", "prompt-card", "prompt-text", "negative-opinion", "footer"]
                elif "summary-cards-body" in html:
                    required_classes = ["top-band", "summary-cards-body", "summary-quote-panel", "summary-card-grid", "summary-card", "footer"]
                elif "blind-prompting-body" in html:
                    required_classes = ["top-band", "blind-prompting-body", "blind-prompting-matrix-body", "blind-prompting-card", "blind-prompting-thesis", "footer"]
                elif "harness-layered-body" in html:
                    required_classes = ["top-band", "harness-layered-body", "harness-core", "harness-layer-row", "harness-decision", "footer"]
                elif "decision-map-body" in html:
                    required_classes = ["top-band", "decision-map-body", "decision-thesis", "decision-grid", "decision-card", "footer"]
                elif "tdd-control-layers-body" in html:
                    required_classes = ["top-band", "tdd-control-layers-body", "tdd-control-grid", "tdd-flow-step", "tdd-control-block", "footer"]
                elif "spec-tdd-bridge-body" in html:
                    required_classes = ["statement-panel", "statement-tag", "statement-text", "spec-tdd-card-grid", "spec-tdd-plus", "statement-support", "footer"]
            elif shell == "evidence-table-shell" and "evidence-cards-body" in html:
                required_classes = ["top-band", "table-wrap", "evidence-cards-body", "evidence-card-grid", "evidence-card", "footer"]
            elif shell == "evidence-table-shell" and "agentic-pattern-quadrant-body" in html:
                required_classes = ["top-band", "agentic-pattern-quadrant-body", "agentic-pattern-center", "agentic-pattern-card", "footer"]
            elif shell == "evidence-table-shell" and "asset-card-body" in html:
                required_classes = ["top-band", "asset-card-body", "reference-asset-figure", "evidence-card-grid", "evidence-card", "footer"]
            elif shell == "evidence-table-shell" and "era-native-body" in html:
                required_classes = ["top-band", "era-native-body", "era-native-track", "era-native-card", "era-native-formula", "era-native-equation", "footer"]
            elif shell == "evidence-table-shell" and "tool-relation-map" in html:
                required_classes = ["top-band", "table-wrap", "tool-relation-map", "responsibility-column", "tool-cluster-grid", "relation-connector", "tool-network-line", "tool-network-synthesis", "footer"]
            elif shell == "evidence-table-shell" and "memory-artifact-map" in html:
                required_classes = ["top-band", "table-wrap", "memory-artifact-map", "memory-artifact-card", "memory-core-claim", "footer"]
            elif shell == "evidence-table-shell" and "agent-harness-quote-body" in html:
                required_classes = ["top-band", "table-wrap", "agent-harness-quote-body", "quote-card-block", "agent-quote-block", "agent-component-grid", "agent-component-card", "footer"]
            elif shell == "evidence-table-shell" and "rag-context-research-body" in html:
                required_classes = ["top-band", "table-wrap", "rag-context-research-body", "rag-context-grid", "rag-context-card", "rag-context-decision", "research-source-line", "footer"]
            elif shell == "process-flow-shell" and "prompt-era-body" in html:
                required_classes = ["top-band", "prompt-era-body", "prompt-era-card", "prompt-era-arrow", "footer"]
            elif shell == "process-flow-shell" and "evolution-body" in html:
                required_classes = ["top-band", "evolution-body", "evolution-flow", "evolution-step", "analogy-block", "footer"]
            elif shell == "process-flow-shell" and "prompt-pattern-lab-body" in html:
                required_classes = ["top-band", "prompt-pattern-lab-body", "pattern-diagram-card", "pattern-example-card", "cot-diagram", "react-diagram", "tot-diagram", "feedback-diagram", "footer"]
            elif shell == "process-flow-shell" and "cot-native-body" in html:
                required_classes = ["top-band", "cot-native-body", "cot-example-diagram", "cot-reasoning-step", "footer"]
            elif shell == "process-flow-shell" and "pattern-pair-body" in html:
                required_classes = ["top-band", "pattern-pair-body", "pattern-pair-card", "react-diagram", "tot-diagram", "footer"]
            elif shell == "process-flow-shell" and "feedback-loop-body" in html:
                required_classes = ["top-band", "feedback-loop-body", "feedback-loop-card", "self-refine-diagram", "reflexion-diagram", "footer"]
            elif shell == "process-flow-shell" and "pattern-map-body" in html:
                required_classes = ["top-band", "pattern-map-body", "process-track", "process-step", "pattern-assets", "footer"]
            elif shell == "process-flow-shell" and "cursor-tools-body" in html:
                required_classes = ["top-band", "cursor-tools-body", "cursor-tool-panel", "cursor-tools-rail", "footer"]
            elif shell == "process-flow-shell" and "cursor-architecture-redraw-body" in html:
                required_classes = ["top-band", "cursor-architecture-redraw-body", "cursor-architecture-flow", "cursor-architecture-step", "cursor-architecture-example-canvas", "architecture-side-tools", "footer"]
            elif shell == "process-flow-shell" and "harness-era-signs-body" in html:
                required_classes = ["top-band", "harness-era-signs-body", "harness-era-claim", "harness-era-card", "harness-era-component", "footer"]
            elif shell == "process-flow-shell" and "component-tier-body" in html:
                required_classes = ["top-band", "component-tier-body", "component-tier-label", "component-tier-row", "component-main-block", "process-step", "footer"]
            elif shell == "process-flow-shell" and "asset-process-body" in html:
                required_classes = ["top-band", "asset-process-body", "asset-process-figure", "asset-process-list", "process-step", "footer"]
            elif shell == "process-flow-shell" and "loop-cycle-body" in html:
                required_classes = ["top-band", "loop-cycle-body", "loop-cycle-track", "process-step", "loop-cycle-arrow", "footer"]
            elif shell == "process-flow-shell" and "context-engineering-body" in html:
                required_classes = ["top-band", "context-engineering-body", "context-strategy-grid", "quote-card-block", "context-quote-block", "process-step", "footer"]
            elif shell == "process-flow-shell" and "mcp-context-explainer-body" in html:
                required_classes = ["top-band", "mcp-context-explainer-body", "mcp-usage-panel", "mcp-usage-flow", "mcp-usage-node", "context-hub-explainer-card", "context-hub-principle", "footer"]
            elif shell == "split-compare-shell" and "waterfall-comparison-body" in html:
                required_classes = ["top-band", "waterfall-comparison-body", "comparison-row-grid", "comparison-row", "footer"]
            elif shell == "split-compare-shell" and "cache-sequence-body" in html:
                required_classes = ["top-band", "cache-sequence-body", "stable-prefix-block", "variable-suffix-block", "cache-token-stack", "cache-synthesis", "footer"]

            for class_name in required_classes:
                if not has_class(html, class_name):
                    errors.append(f"{slide_id}: shell {shell} requires class '{class_name}'")

        if shell == "process-flow-shell":
            if "evolution-body" in html:
                step_count = len(re.findall(r'class="[^"]*\bevolution-step\b[^"]*"', html))
            elif "prompt-era-body" in html or "cursor-tools-body" in html:
                step_count = 3
            elif "mcp-architecture-body" in html or "mcp-context-explainer-body" in html:
                step_count = 4
            elif "pattern-pair-body" in html or "feedback-loop-body" in html:
                step_count = 3
            else:
                step_count = len(re.findall(r'class="[^"]*\bprocess-step\b[^"]*"', html))
            if step_count < 3:
                errors.append(f"{slide_id}: process-flow-shell requires at least three steps")

        if slide_id == "S032" and "comparison-synthesis" in html:
            errors.append("S032: bottom one-line synthesis/dark bar must be removed")

        if slide_id == "S033":
            if "spec-tdd-thesis" in html or ">Spec + TDD<" in html:
                errors.append("S033: central visible Spec + TDD thesis text must be removed")

        if shell == "evidence-table-shell":
            has_table = "<table class=\"data-table\">" in html
            has_cards = "evidence-card-grid" in html
            has_asset_cards = "asset-card-body" in html and has_cards
            has_era_native = "era-native-body" in html and "era-native-card" in html
            has_tool_relation_map = "tool-relation-map" in html
            has_memory_artifact_map = "memory-artifact-map" in html
            has_agent_harness_quote = "agent-harness-quote-body" in html
            has_rag_context_research = "rag-context-research-body" in html
            if not has_table and not has_cards and not has_asset_cards and not has_era_native and not has_tool_relation_map and not has_memory_artifact_map and not has_agent_harness_quote and not has_rag_context_research:
                errors.append(f"{slide_id}: evidence-table-shell requires a data table or evidence cards")
            if has_cards and "원문 사실" in html:
                errors.append(f"{slide_id}: evidence cards must not include a 원문 사실 column")
        if shell == "statement-editorial-shell" and "prompt-only-body" in html:
            if "prompt-label" in html:
                errors.append(f"{slide_id}: stale prompt-label class is not allowed")
            if "자연어 지시" in html:
                errors.append(f"{slide_id}: prompt-only cards must not show '자연어 지시'")
            if slide_id == "S009":
                if "prompt-language-label" not in html or "자연어" not in html:
                    errors.append(f"{slide_id}: prompt-only page must show 자연어 language label")
                if re.search(r'<article class="prompt-card">\s*<p class="prompt-language-label">', html):
                    errors.append(f"{slide_id}: 자연어 label must sit outside the prompt card")
                if "이 함수를 리펙토링하고 테스트 코드를 작성해줘." not in html:
                    errors.append(f"{slide_id}: prompt-only card must keep source prompt text")
                if "자연어로 시키는 건 진짜 개발이 아니다!" not in html:
                    errors.append(f"{slide_id}: prompt-only card must keep source negative opinion")
        if slide_id == "S005":
            if "컴파일러가 만든 코드가 사람보다 효율적일 리 없다!" not in html:
                errors.append(f"{slide_id}: source-synced negative opinion is missing")
            if "기계어를 직접 다루지 않으면 진정한 개발이 아니다!" in html:
                errors.append(f"{slide_id}: stale negative opinion remains")
        if slide_id == "S010" and "직접하는 일을 줄고, 설계하는 일은 늘어난다" not in html:
            errors.append(f"{slide_id}: table question must follow current source quote")
        if slide_id == "S014":
            if "AI가 더 많이 해줄수록 기초 지식을 가진 사람의 경쟁력 상승" not in html:
                errors.append(f"{slide_id}: S014 must follow current source quote")
            if "코딩은 에이전트가 일할 환경을 설계하고 검증하는 영역으로 이동하고 있습니다." in html:
                errors.append(f"{slide_id}: stale S014 summary quote remains")
        if slide_id == "S016":
            for snippet in ["2주", "1~2일", "불가능하던 작업 실현"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: missing metric impact snippet {snippet}")
            if "카카오 AI 팀 내부 공유 사례" not in html:
                errors.append(f"{slide_id}: missing source-backed internal sharing case meta")
            if "Augment Code + Vertex AI" in html:
                errors.append(f"{slide_id}: source-outside tool label remains visible")
            if "metric-impact-body is-tall-reference" not in html:
                errors.append(f"{slide_id}: metric impact slide must use tall reference layout")
        if slide_id == "S017":
            if '<h1 class="title-placeholder">1막: Copilot과 ChatGPT, 프롬프트의 시대</h1>' not in html:
                errors.append(f"{slide_id}: title must be prompt-era act heading")
            if "Agent = Model + Harness" in html:
                errors.append(f"{slide_id}: standalone Agent formula page must be removed")
            if "2022~2024" not in html or "era-range" not in html:
                errors.append(f"{slide_id}: date range must remain body metadata")
            if "prompt-era-body" not in html:
                errors.append(f"{slide_id}: prompt era slide must use prompt-era-body")
        if slide_id in {"S013", "S014"}:
            if "CHAPTER 01" not in html:
                errors.append(f"{slide_id}: chapter label must be CHAPTER 01")
            if "SECTION 1" in html:
                errors.append(f"{slide_id}: stale SECTION 1 label remains")
        if slide_id == "S018":
            if '<h1 class="title-placeholder">CoT / ReAct / ToT</h1>' not in html:
                errors.append(f"{slide_id}: title must be CoT / ReAct / ToT")
            for class_name in ["cot-triad-body", "cot-triad-card", "cot-triad-diagram", "cot-diagram-svg", "cot-cot-svg", "cot-react-svg", "cot-tot-svg"]:
                if not has_class(html, class_name):
                    errors.append(f"{slide_id}: triad slide requires native class '{class_name}'")
            for snippet in [
                "Chain-of-Thought",
                "CoT",
                "중간 추론 단계",
                "ReAct",
                "Reason + Act",
                "추론과 행동 반복",
                "Tree-of-Thought",
                "ToT",
                "여러 추론 경로",
                "LM",
                "Env",
                "Reasoning Traces",
                "Actions",
                "Observations",
                "ReAct (Reason + Act)",
            ]:
                if snippet not in html:
                    errors.append(f"{slide_id}: triad slide missing snippet {snippet}")
            for forbidden in [
                "2캔 × 3개",
                "11개",
                "Graph-of-Thought",
                "GoT",
                "02-chain-of-thought.png",
                "http://",
                "https://",
            ]:
                if forbidden in html:
                    errors.append(f"{slide_id}: triad slide has forbidden visible/reference token {forbidden}")
        if slide_id == "S019":
            if '<h1 class="title-placeholder">ReAct / Tree-of-Thought</h1>' not in html:
                errors.append(f"{slide_id}: title must be ReAct / Tree-of-Thought")
            for class_name in ["pattern-pair-body", "pattern-pair-card", "react-diagram", "tot-diagram"]:
                if not has_class(html, class_name):
                    errors.append(f"{slide_id}: ReAct/ToT slide requires native class '{class_name}'")
            for snippet in ["ReAct", "Tree-of-Thought", "추론과 행동", "여러 추론 경로"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: ReAct/ToT slide missing snippet {snippet}")
            for forbidden in ["Chain-of-Thought", "Self-Refine", "Reflexion", "03-react-pattern.png", "04-tree-of-thought.png"]:
                if forbidden in html:
                    errors.append(f"{slide_id}: ReAct/ToT slide has stale combined content {forbidden}")
        if slide_id == "S020":
            if '<h1 class="title-placeholder">Self-Refine / Reflexion</h1>' not in html:
                errors.append(f"{slide_id}: title must be Self-Refine / Reflexion")
            for class_name in ["feedback-loop-body", "feedback-loop-card", "self-refine-diagram", "reflexion-diagram"]:
                if not has_class(html, class_name):
                    errors.append(f"{slide_id}: feedback slide requires native class '{class_name}'")
            for snippet in ["Self-Refine", "Reflexion", "자기 출력", "피드백 루프"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: feedback slide missing snippet {snippet}")
            for forbidden in ["ReAct", "Tree-of-Thought"]:
                if forbidden in html:
                    errors.append(f"{slide_id}: feedback slide has stale adjacent pattern {forbidden}")
        if slide_id == "S021":
            if "agentic-pattern-quadrant-body" not in html or "agentic-pattern-center" not in html:
                errors.append(f"{slide_id}: agentic pattern slide must use native quadrant layout")
            for snippet in ["agentic-mini-diagram", "Generate", "Critique", "Search/API", "Reviewer"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: agentic pattern examples missing snippet {snippet}")
            if "05-andrew-ng-agentic-design-patterns.png" in html:
                errors.append(f"{slide_id}: agentic pattern slide must not embed cropped reference asset")
        if slide_id == "S022":
            if '<h1 class="title-placeholder">프롬프트 시대의 벽</h1>' not in html:
                errors.append(f"{slide_id}: title must be shortened to avoid two-line title")
            if "모델은 보지 못한 것을 알 수 없음" not in html:
                errors.append(f"{slide_id}: blind prompting claim is missing")
            if "blind-prompting-matrix-body" not in html:
                errors.append(f"{slide_id}: blind prompting slide must use matrix body")
        if slide_id == "S023":
            if "2막: Cursor와 컨텍스트의 시대" not in html:
                errors.append(f"{slide_id}: title must follow source heading")
            if "cursor-tools-body" not in html:
                errors.append(f"{slide_id}: cursor tools slide must use cursor-tools-body")
        if slide_id == "S024":
            if "cursor-architecture-redraw-body" not in html or "architecture-side-tools" not in html:
                errors.append(f"{slide_id}: Cursor architecture must use native redraw pipeline layout")
            for snippet in ["cursor-architecture-example-canvas", "codebase index", "context bundle", "사용자 요청", "indexing", "retrieval", "context assembly", "edit/run", "verify"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: Cursor architecture example missing snippet {snippet}")
            if "06-cursor-ai-code-editor-architecture.png" in html:
                errors.append(f"{slide_id}: Cursor architecture must not embed cropped reference asset")
        if slide_id == "S025":
            for snippet in ["gather context", "take action", "verify", "repeat"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: missing loop step {snippet}")
            for class_name in ["loop-cycle-body", "loop-cycle-arrow"]:
                if not has_class(html, class_name):
                    errors.append(f"{slide_id}: loop slide requires class '{class_name}'")
            if "loop-repeat-arc" in html or "↺ repeat" in html:
                errors.append(f"{slide_id}: dashed repeat label is forbidden")
            if '<h1 class="title-placeholder">컨텍스트 시대의 벽</h1>' not in html:
                errors.append(f"{slide_id}: long loop title must be shortened")
        if slide_id == "S026":
            if "harness-era-signs-body" not in html:
                errors.append(f"{slide_id}: harness era slide must use era signs layout")
            for snippet in ["CLAUDE.md", "Skills", "Hooks", "MCP", "Plugins", "Subagents", "승인 체계"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: harness era component sign missing {snippet}")
            for forbidden in ["component-tier-body", "무엇을 보는지", "기초", "자동화", "연결", "확장"]:
                if forbidden in html:
                    errors.append(f"{slide_id}: harness era slide over-expands mechanics with {forbidden}")
        if slide_id == "S027":
            if "era-native-body" not in html:
                errors.append(f"{slide_id}: era flow must use native timeline/table layout")
            if "Agent = Model + Harness" not in html:
                errors.append(f"{slide_id}: final conclusion must include Agent formula")
            if "Prompt ⊂ Context ⊂ Harness" not in html:
                errors.append(f"{slide_id}: era relationship must use text equation")
            if "<table class=\"data-table\">" in html:
                errors.append(f"{slide_id}: final conclusion must not include a bottom data table")
            if "era-native-nesting" in html:
                errors.append(f"{slide_id}: era nesting diagram must be removed")
            if "01-three-era-timeline.png" in html:
                errors.append(f"{slide_id}: raw timeline reference asset is forbidden")
        if slide_id == "S028":
            if '<h1 class="title-placeholder">AI 시대의 개발 방법론</h1>' not in html:
                errors.append(f"{slide_id}: chapter divider title must be fixed")
            if "<li class=\"section-keyword\">" in html:
                errors.append(f"{slide_id}: chapter divider must stay section-only without keyword chips")
        if slide_id == "S029":
            for snippet in ["2025.02", "Vibe Coding", "2025 중반", "구조화된 검토", "2025 하반기", "Spec-first", "2026 초", "Context Engineering"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: method timeline missing snippet {snippet}")
            if "AI에게 무엇을 시킬지, 어떻게 검증할 것인지" not in html:
                errors.append(f"{slide_id}: method timeline question is missing")
            content_without_footer = html.split('<footer class="footer">', maxsplit=1)[0]
            for forbidden in ["Harness", "Agent", "Prompt", "Model", "Waterfall"]:
                if forbidden in content_without_footer:
                    errors.append(f"{slide_id}: topic creep label is forbidden: {forbidden}")
        if slide_id == "S030":
            for snippet in ["SDD", "Spec-Driven Development", "WHAT", "WHY", "HOW", "/speckit.specify", "/speckit.plan", "/speckit.tasks", "[NEEDS CLARIFICATION]", "Constitution Check"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: SDD flow missing snippet {snippet}")
            if "하네스" in html:
                errors.append(f"{slide_id}: SDD page must not become a Harness summary")
        if slide_id == "S031":
            for snippet in [
                "TDD (Test-Driven Development)",
                "테스트를 먼저 쓰고, 통과하는 코드를 나중에 쓴다",
                "AI 시대에는 인간이 테스트, AI가 구현",
                "Red",
                "Green",
                "Refactor",
                "인간이 실패 테스트 작성",
                "AI가 통과 코드 구현",
                "인간 리뷰 → AI가 리팩토링",
                "왜 AI에게 특히 중요한가",
                'AI는 &quot;동작하는 것 같은&quot; 코드를 자신 있게 만듦',
                "테스트 없으면 맞는지 틀린지 확인 불가.",
                "AI의 치팅에 주의",
                "테스트 수정 금지 규칙 필수",
                "테스트 코드 임의 수정 금지",
                "assert 조건 약화",
                "실패 확인 전 구현 금지",
            ]:
                if snippet not in html:
                    errors.append(f"{slide_id}: TDD control map missing snippet {snippet}")
            for class_name in ["tdd-control-layers-body", "tdd-flow-stack", "tdd-control-column", "tdd-control-lead"]:
                if not has_class(html, class_name):
                    errors.append(f"{slide_id}: TDD revision requires class '{class_name}'")
            if len(re.findall(r'class="[^"]*\btdd-flow-step\b[^"]*"', html)) != 3:
                errors.append(f"{slide_id}: TDD revision must render exactly three left flow steps")
            if len(re.findall(r'class="[^"]*\btdd-control-block\b[^"]*"', html)) != 2:
                errors.append(f"{slide_id}: TDD revision must render exactly two right control blocks")
            if "AI 시대의 TDD는 권한 통제 기법" in html:
                errors.append(f"{slide_id}: large TDD authority statement card must be removed")
            for forbidden in ["REFACTOR", "권한 통제", "assert 약화 금지 · 구현 먼저 금지"]:
                if forbidden in html:
                    errors.append(f"{slide_id}: stale TDD control copy remains: {forbidden}")
            if "decision-map-body" in html:
                errors.append(f"{slide_id}: stale four-card decision map remains")
        if slide_id == "S032":
            for snippet in [
                "Waterfall",
                "SDD",
                "Waterfall vs SDD",
                "개발 흐름",
                "검증 시점",
                "실행 산출물",
                "요구사항 → 설계 → 코딩 → 테스트",
                "테스트가 개발 후반에 실제 제약을 드러냄",
                "스펙이 primary artifact",
                "/speckit.specify",
                "/speckit.plan",
                "/speckit.tasks",
                "요구사항 또는 설계를 다시 고침",
                "spec · plan · tasks를 실행 산출물로 갱신",
            ]:
                if snippet not in html:
                    errors.append(f"{slide_id}: Waterfall comparison missing snippet {snippet}")
            for class_name in ["waterfall-comparison-body", "comparison-column-spacer", "comparison-row-grid"]:
                if not has_class(html, class_name):
                    errors.append(f"{slide_id}: Waterfall comparison requires class '{class_name}'")
            if len(re.findall(r'<article class="[^"]*\bcomparison-row\b[^"]*"', html)) != 3:
                errors.append(f"{slide_id}: Waterfall comparison must render exactly three horizontal rows")
            if "compare-grid" in html:
                errors.append(f"{slide_id}: stale skewed split comparison layout remains")
            for forbidden in ["AI 시대 SDD + TDD", "앞단의 문서", "검증은", "실제 작동 원리", "문서의 성격", "검증 타이밍", "작동 방식", "검증 루프", "timing · storage · I/O"]:
                if forbidden in html:
                    errors.append(f"{slide_id}: stale Waterfall comparison copy remains: {forbidden}")
            if "Waterfall은 끝에서 제약이 드러나고, SDD는 스펙이 계획과 태스크를 만든다." in html:
                errors.append(f"{slide_id}: stale bottom synthesis remains")
            if "하네스" in html:
                errors.append(f"{slide_id}: Waterfall comparison must not bridge to Harness")
        if slide_id == "S033":
            for snippet in ["SDD + TDD가 Harness로 이어지는 이유", "스펙 템플릿", "계획 문서", "TDD 루프", "Skills", "Hooks", "하네스", "이 시스템이 곧 하네스 엔지니어링"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: Harness bridge missing snippet {snippet}")
            for class_name in ["spec-tdd-bridge-body", "spec-tdd-subheading", "spec-tdd-card-grid", "spec-tdd-plus", "spec-tdd-synthesis"]:
                if not has_class(html, class_name):
                    errors.append(f"{slide_id}: Spec + TDD bridge requires class '{class_name}'")
            if "spec-tdd-thesis" in html or "Spec + TDD" in html:
                errors.append(f"{slide_id}: stale explicit Spec + TDD thesis remains")
            if len(re.findall(r'<article class="[^"]*\bspec-tdd-card\b[^"]*"', html)) != 2:
                errors.append(f"{slide_id}: Spec + TDD bridge must render exactly two large cards")
            if "decision-map-body" in html:
                errors.append(f"{slide_id}: stale four-card decision map remains")
            tdd_card_match = re.search(
                r'<article class="[^"]*\bspec-tdd-card\b[^"]*">\s*<h2>TDD</h2>(.*?)</article>',
                html,
                flags=re.DOTALL,
            )
            if tdd_card_match is None:
                errors.append(f"{slide_id}: Spec + TDD bridge must render a TDD card")
            elif "하네스" in tdd_card_match.group(1):
                errors.append(f"{slide_id}: TDD card must not list 하네스 as an item")
        if slide_id == "S034":
            for snippet in ["프롬프트를 넘어서", "Prompt", "Context", "Harness"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: chapter divider missing snippet {snippet}")
            if '<li class="section-keyword">' in html or re.search(r"\.section-keyword\s*\{", css_text):
                errors.append(f"{slide_id}: section divider keywords must not render as pill/chip elements")
            if "section-keyword-plain" not in html:
                errors.append(f"{slide_id}: section divider keywords must use plain text rail")
        if slide_id == "S035":
            for snippet in ["Prompt", "Context", "Harness", "무엇을/어떻게 말할 것인가", "무엇을/어떻게 보여줄 것인가", "무엇을/어떻게 통제할 것인가", "Prompt ⊂ Context ⊂ Harness"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: hierarchy slide missing snippet {snippet}")
        if slide_id == "S036":
            for snippet in ["Agent = Model + Harness", "모델이 아닌 것은 전부 하네스입니다.", "LangChain, Vivek Trivedy", "Context Engineering", "Tool Orchestration", "State &amp; Memory", "Verification Loop", "Error Recovery", "Human-in-the-Loop Control"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: agent formula slide missing snippet {snippet}")
            if "quote-card-block" not in html or "agent-quote-block" not in html or "agent-component-grid" not in html:
                errors.append(f"{slide_id}: quote must be emphasized in a dedicated quote card and components must render as cards")
            if "table-callout" in html:
                errors.append(f"{slide_id}: quote must not remain an unattributed table callout")
        if slide_id == "S037":
            for snippet in ["gather context", "take action", "verify work", "repeat", "이 네 지점을 신뢰성 있게 만드는 일"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: loop slide missing snippet {snippet}")
            if "하네스 엔지니어링 = 이 네 단계의 신뢰성" in html:
                errors.append(f"{slide_id}: rejected non-source one-line statement remains")
            if 'class="flow-thesis loop-center centered-claim"' in html:
                errors.append(f"{slide_id}: center claim card must not remain in the loop")
            if "loop-synthesis" not in html:
                errors.append(f"{slide_id}: loop claim must move to synthesis strip")
        if slide_id == "S038":
            for snippet in ["Guardrails", "Specification", "Verification", "State Management", "Observability"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: responsibilities slide missing snippet {snippet}")
            if "먼저 책임을 정하고" in html:
                errors.append(f"{slide_id}: awkward one-line thesis card must be removed")
        if slide_id == "S039":
            if '<h1 class="title-placeholder">하네스의 도구</h1>' not in html:
                errors.append(f"{slide_id}: title must be 하네스의 도구")
            if "<table class=\"data-table\">" in html:
                errors.append(f"{slide_id}: tool relation map must not collapse into a data table")
            if "<h1 class=\"title-placeholder\">책임과 도구는 1:1이 아니다</h1>" in html:
                errors.append(f"{slide_id}: 1:1 statement must not be the title")
            if "N:N" in html or "relation-tags" in html:
                errors.append(f"{slide_id}: crude N:N badge/tag mapping must not remain")
            if "tool-network-line" not in html or "tool-network-synthesis" not in html:
                errors.append(f"{slide_id}: tool relation map must use native connector network")
            if '<p class="tool-network-synthesis centered-claim">책임과 도구는 1:1이 아니다</p>' not in html:
                errors.append(f"{slide_id}: bottom synthesis must be 책임과 도구는 1:1이 아니다")
            if "도구 이름보다 그 도구가 맡는 책임" in html:
                errors.append(f"{slide_id}: stale bottom synthesis remains")
            if "하네스의 책임 ↔ 하네스의 도구" in html:
                errors.append(f"{slide_id}: redundant responsibility/tool label must be removed")
        if slide_id == "S040":
            for snippet in ["Context Engineering", "smallest set of high-signal tokens", "Anthropic Research", "Write", "Select", "Compress", "Isolate"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: context engineering slide missing snippet {snippet}")
            if "context-quote-block" not in html or "quote-card-block" not in html:
                errors.append(f"{slide_id}: Anthropic phrase must render as dedicated quote card treatment")
            if 'class="flow-thesis centered-claim">smallest set of high-signal tokens' in html:
                errors.append(f"{slide_id}: Anthropic phrase must not remain as oversized flow thesis")
            if "Antrophic" in html:
                errors.append(f"{slide_id}: misspelled Anthropic source label remains")
        if slide_id == "S041":
            for snippet in ["MCP", "Context Hub", "Context Hub MCP", "GitHub", "Slack", "DB", "Filesystem", "Internal API", "외부 도구·데이터 소스", "최신 API 문서", "모델 기억 대신"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: MCP slide missing snippet {snippet}")
            if "mcp-context-explainer-body" not in html:
                errors.append(f"{slide_id}: MCP slide must use left/right explainer layout")
            if "mcp-tool-grid" in html or "mcp-tool-chip" in html:
                errors.append(f"{slide_id}: MCP slide must not remain a tool-chip pile")
            if "process-track" in html:
                errors.append(f"{slide_id}: MCP slide must not remain a generic process list")
            if "connected tools" in html:
                errors.append(f"{slide_id}: source-outside English helper label remains")
        if slide_id == "S042":
            for snippet in ["RAG", "Context Hub MCP", "passage", "벡터 인덱스", "retriever", "공식·버전별 API 문서", "SDK/API 변경", "Lewis et al. 2020", "MCP Docs"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: RAG vs Context Hub slide missing snippet {snippet}")
            if "<table class=\"data-table\">" in html:
                errors.append(f"{slide_id}: researched RAG vs Context Hub slide must not remain the old rough table")
            if "rag-context-research-body" not in html:
                errors.append(f"{slide_id}: researched RAG vs Context Hub slide must use native research comparison cards")
        if slide_id == "S043":
            if "<table class=\"data-table\">" in html:
                errors.append(f"{slide_id}: memory slide must not render as a two-column table")
            if "memory-artifact-map" not in html:
                errors.append(f"{slide_id}: memory slide must use native memory-artifact-map composition")
            if html.find("memory-core-claim") < html.find("memory-artifact-grid"):
                errors.append(f"{slide_id}: memory claim must sit below artifact grid")
            for snippet in ["Memory: 세션을 넘어서는 기억", "CLAUDE.md / AGENTS.md", "프로젝트 노트와 결정 기록", "이슈와 PR 히스토리", "대화창을 기억 저장소로 착각하지 않는다"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: memory slide missing snippet {snippet}")
        if slide_id == "S044":
            for class_name in ["cache-sequence-body", "stable-prefix-block", "variable-suffix-block", "cache-token-stack", "cache-synthesis"]:
                if not has_class(html, class_name):
                    errors.append(f"{slide_id}: Stable Prefix slide requires class '{class_name}'")
            for snippet in ["Stable Prefix", "Variable Suffix", "KV-cache", "시스템 프롬프트", "도구 정의", "장기 규칙", "최신 사용자 입력", "도구 결과", "잘 쓰는 것 못지않게 안 바꾸는 것도 능력"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: Stable Prefix slide missing snippet {snippet}")
            if "<table class=\"data-table\">" in html:
                errors.append(f"{slide_id}: Stable Prefix comparison must not be a table")
        if slide_id == "S045":
            for snippet in ["하네스는 환경 그 자체다", "필요한 파일", "필요한 도구", "필요한 규칙", "Harness Builder"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: chapter conclusion missing snippet {snippet}")
        if slide_id >= "S015" and slide_id <= "S027":
            if "CHAPTER 02" not in html:
                errors.append(f"{slide_id}: chapter label must be CHAPTER 02")
            if "chapter-02" not in attrs:
                errors.append(f"{slide_id}: main root must carry chapter-02 class for body scale control")
            for stale_label in ["ACT 1", "ACT 2", "ACT 3", "LIMIT"]:
                if stale_label in html:
                    errors.append(f"{slide_id}: stale chapter helper label remains: {stale_label}")
        if slide_id >= "S028" and slide_id <= "S033":
            if "CHAPTER 03" not in html:
                errors.append(f"{slide_id}: chapter label must be CHAPTER 03")
            if "chapter-03" not in attrs:
                errors.append(f"{slide_id}: main root must carry chapter-03 class")
            if "SECTION 3" in html:
                errors.append(f"{slide_id}: stale SECTION 3 label remains")
        if slide_id >= "S034" and slide_id <= "S045":
            if "CHAPTER 04" not in html:
                errors.append(f"{slide_id}: chapter label must be CHAPTER 04")
            if "chapter-04" not in attrs:
                errors.append(f"{slide_id}: main root must carry chapter-04 class")
            if "SECTION 4" in html:
                errors.append(f"{slide_id}: stale SECTION 4 label remains")
        if slide_type == "comparison":
            compare_count = len(re.findall(r'class="[^"]*\bcompare-col\b[^"]*"', html))
            if compare_count != 2:
                errors.append(f"{slide_id}: comparison slide must render two compare columns")
            if re.search(r'class="[^"]*\bcard\b[^"]*"', html):
                errors.append(f"{slide_id}: comparison slide must not introduce nested card classes")

    for warning in warnings:
        print(f"WARN {warning}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(f"OK slide contract passed for {len(rows)} slides")
    return 0


if __name__ == "__main__":
    sys.exit(main())
