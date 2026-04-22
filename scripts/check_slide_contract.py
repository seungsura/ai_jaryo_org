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
            elif shell == "evidence-table-shell" and "evidence-cards-body" in html:
                required_classes = ["top-band", "table-wrap", "evidence-cards-body", "evidence-card-grid", "evidence-card", "footer"]
            elif shell == "evidence-table-shell" and "agentic-pattern-quadrant-body" in html:
                required_classes = ["top-band", "agentic-pattern-quadrant-body", "agentic-pattern-center", "agentic-pattern-card", "footer"]
            elif shell == "evidence-table-shell" and "asset-card-body" in html:
                required_classes = ["top-band", "asset-card-body", "reference-asset-figure", "evidence-card-grid", "evidence-card", "footer"]
            elif shell == "evidence-table-shell" and "era-native-body" in html:
                required_classes = ["top-band", "era-native-body", "era-native-track", "era-native-card", "data-table", "footer"]
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

            for class_name in required_classes:
                if not has_class(html, class_name):
                    errors.append(f"{slide_id}: shell {shell} requires class '{class_name}'")

        if shell == "process-flow-shell":
            if "evolution-body" in html:
                step_count = len(re.findall(r'class="[^"]*\bevolution-step\b[^"]*"', html))
            elif "prompt-era-body" in html or "cursor-tools-body" in html:
                step_count = 3
            elif "pattern-pair-body" in html or "feedback-loop-body" in html:
                step_count = 3
            else:
                step_count = len(re.findall(r'class="[^"]*\bprocess-step\b[^"]*"', html))
            if step_count < 3:
                errors.append(f"{slide_id}: process-flow-shell requires at least three steps")

        if shell == "evidence-table-shell":
            has_table = "<table class=\"data-table\">" in html
            has_cards = "evidence-card-grid" in html
            has_asset_cards = "asset-card-body" in html and has_cards
            if not has_table and not has_cards and not has_asset_cards:
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
                    errors.append(f"{slide_id}: prompt-only card must show top-left 자연어 label")
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
            if '<h1 class="title-placeholder">Chain-of-Thought</h1>' not in html:
                errors.append(f"{slide_id}: title must be Chain-of-Thought")
            for class_name in ["cot-native-body", "cot-example-diagram", "cot-reasoning-step"]:
                if not has_class(html, class_name):
                    errors.append(f"{slide_id}: CoT slide requires native class '{class_name}'")
            for snippet in ["중간 추론 단계", "2캔 × 3개", "11개"]:
                if snippet not in html:
                    errors.append(f"{slide_id}: CoT example missing snippet {snippet}")
            if "02-chain-of-thought.png" in html or "ReAct" in html:
                errors.append(f"{slide_id}: CoT slide must not embed assets or include adjacent patterns")
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
            if "era-native-nesting" in html:
                errors.append(f"{slide_id}: era nesting diagram must be removed")
            if "01-three-era-timeline.png" in html:
                errors.append(f"{slide_id}: raw timeline reference asset is forbidden")
        if slide_id >= "S015" and slide_id <= "S027":
            if "CHAPTER 02" not in html:
                errors.append(f"{slide_id}: chapter label must be CHAPTER 02")
            if "chapter-02" not in attrs:
                errors.append(f"{slide_id}: main root must carry chapter-02 class for body scale control")
            for stale_label in ["ACT 1", "ACT 2", "ACT 3", "LIMIT"]:
                if stale_label in html:
                    errors.append(f"{slide_id}: stale chapter helper label remains: {stale_label}")

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
