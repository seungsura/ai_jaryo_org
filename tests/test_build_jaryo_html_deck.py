from __future__ import annotations

import os
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = ROOT / "scripts/build_jaryo_html_deck.py"
BUILDER_PACKAGE = ROOT / "scripts/jaryo_html_deck"
SLIDE_MODULES_DIR = BUILDER_PACKAGE / "slides"
MANIFEST_PATH = ROOT / "docs/03-html/manifest.md"
OUTLINE_PATH = ROOT / "docs/03-html/outline/slide-outline.md"
DECK_PATH = ROOT / "docs/03-html/deck/index.html"
SCRIPT_PATH = ROOT / "docs/03-html/deck/script.md"
SLIDES_DIR = ROOT / "docs/03-html/slides"
SLIDE_001_PATH = SLIDES_DIR / "slide-001.html"
SLIDE_009_PATH = SLIDES_DIR / "slide-009.html"
SLIDE_012_PATH = SLIDES_DIR / "slide-012.html"
SLIDE_013_PATH = SLIDES_DIR / "slide-013.html"
SLIDE_014_PATH = SLIDES_DIR / "slide-014.html"
SLIDE_016_PATH = SLIDES_DIR / "slide-016.html"
SLIDE_017_PATH = SLIDES_DIR / "slide-017.html"
SLIDE_018_PATH = SLIDES_DIR / "slide-018.html"
SLIDE_019_PATH = SLIDES_DIR / "slide-019.html"
SLIDE_020_PATH = SLIDES_DIR / "slide-020.html"
SLIDE_021_PATH = SLIDES_DIR / "slide-021.html"
SLIDE_022_PATH = SLIDES_DIR / "slide-022.html"
SLIDE_023_PATH = SLIDES_DIR / "slide-023.html"
SLIDE_024_PATH = SLIDES_DIR / "slide-024.html"
SLIDE_025_PATH = SLIDES_DIR / "slide-025.html"
SLIDE_026_PATH = SLIDES_DIR / "slide-026.html"
SLIDE_027_PATH = SLIDES_DIR / "slide-027.html"


def run_builder() -> None:
    subprocess.run(
        ["python3", str(BUILD_SCRIPT)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )


def manifest_rows() -> list[str]:
    rows: list[str] = []
    in_registry = False
    for raw_line in MANIFEST_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("| order | slide id |"):
            in_registry = True
            continue
        if not in_registry:
            continue
        if not line.startswith("|"):
            break
        normalized = line.replace("|", "").replace(" ", "")
        if normalized and set(normalized) == {"-"}:
            continue
        rows.append(line)
    return rows


class BuildJaryoHtmlDeckTest(unittest.TestCase):
    def test_builder_is_split_into_per_slide_modules(self) -> None:
        entrypoint = BUILD_SCRIPT.read_text(encoding="utf-8")
        slide_modules = sorted(SLIDE_MODULES_DIR.glob("slide_*.py"))

        self.assertLessEqual(len(entrypoint.splitlines()), 12)
        self.assertNotIn("def build_all_specs", entrypoint)
        self.assertNotIn("make_slide(", entrypoint)
        self.assertEqual(len(slide_modules), 27)
        self.assertEqual(slide_modules[0].name, "slide_001.py")
        self.assertEqual(slide_modules[-1].name, "slide_027.py")

        for path in slide_modules:
            source = path.read_text(encoding="utf-8")
            self.assertIn("def build() -> SlideSpec:", source)
            self.assertIn("make_slide(", source)
            self.assertNotIn("render_shell", source)
            self.assertNotIn("render_slide_markup", source)

    def test_builder_common_logic_is_split_by_responsibility(self) -> None:
        expected_modules = [
            "assets.py",
            "builder.py",
            "config.py",
            "content.py",
            "documents.py",
            "model.py",
            "registry.py",
            "renderers.py",
            "writer.py",
        ]

        for module_name in expected_modules:
            self.assertTrue((BUILDER_PACKAGE / module_name).exists(), module_name)

        core = BUILDER_PACKAGE / "core.py"
        self.assertTrue(core.exists())
        self.assertLessEqual(len(core.read_text(encoding="utf-8").splitlines()), 80)

    def test_builder_generates_27_slide_registry(self) -> None:
        run_builder()

        rows = manifest_rows()
        self.assertEqual(len(rows), 27)
        self.assertIn("`S001`", rows[0])
        self.assertIn("`S027`", rows[-1])

    def test_builder_uses_three_digit_slide_files(self) -> None:
        run_builder()

        slide_files = sorted(SLIDES_DIR.glob("slide-*.html"))
        self.assertEqual(len(slide_files), 27)
        self.assertEqual(slide_files[0].name, "slide-001.html")
        self.assertEqual(slide_files[-1].name, "slide-027.html")

    def test_builder_writes_outline_deck_and_script(self) -> None:
        run_builder()

        outline = OUTLINE_PATH.read_text(encoding="utf-8")
        deck = DECK_PATH.read_text(encoding="utf-8")

        self.assertIn("### S001.", outline)
        self.assertIn("### S014.", outline)
        self.assertIn("### S027.", outline)
        self.assertTrue(SCRIPT_PATH.exists())
        self.assertIn('data-slide-id="S001"', deck)
        self.assertIn('data-slide-id="S014"', deck)
        self.assertIn('data-slide-id="S027"', deck)
        self.assertIn("function goTo(index)", deck)

    def test_builder_applies_latest_slide_feedback(self) -> None:
        run_builder()

        deck = DECK_PATH.read_text(encoding="utf-8")
        slide_001 = SLIDE_001_PATH.read_text(encoding="utf-8")
        slide_009 = SLIDE_009_PATH.read_text(encoding="utf-8")
        slide_012 = SLIDE_012_PATH.read_text(encoding="utf-8")
        slide_013 = SLIDE_013_PATH.read_text(encoding="utf-8")
        slide_014 = SLIDE_014_PATH.read_text(encoding="utf-8")
        slide_016 = SLIDE_016_PATH.read_text(encoding="utf-8")
        slide_017 = SLIDE_017_PATH.read_text(encoding="utf-8")
        slide_018 = SLIDE_018_PATH.read_text(encoding="utf-8")
        slide_019 = SLIDE_019_PATH.read_text(encoding="utf-8")
        slide_020 = SLIDE_020_PATH.read_text(encoding="utf-8")
        slide_021 = SLIDE_021_PATH.read_text(encoding="utf-8")
        slide_022 = SLIDE_022_PATH.read_text(encoding="utf-8")
        slide_023 = SLIDE_023_PATH.read_text(encoding="utf-8")
        slide_024 = SLIDE_024_PATH.read_text(encoding="utf-8")
        slide_025 = SLIDE_025_PATH.read_text(encoding="utf-8")
        slide_026 = SLIDE_026_PATH.read_text(encoding="utf-8")
        slide_027 = SLIDE_027_PATH.read_text(encoding="utf-8")

        self.assertIn("<title>Harness 잘 사용하기</title>", deck)
        self.assertIn("<h1 class=\"title-placeholder\">Harness 잘 사용하기</h1>", slide_001)
        self.assertNotIn("Harness를 설계하는 법", deck)
        self.assertNotIn("Harness를 설계하는 법", slide_001)

        self.assertIn("<p class=\"prompt-text\">이 함수를 리펙토링하고 테스트 코드를 작성해줘.</p>", slide_009)
        self.assertIn("<p class=\"prompt-language-label\">자연어</p>", slide_009)
        self.assertNotIn("자연어 지시", slide_009)
        self.assertIn("자연어로 시키는 건 진짜 개발이 아니다!", slide_009)
        self.assertNotIn("<pre class=\"code-block\">", slide_009)
        self.assertNotIn("compare-grid", slide_009)
        self.assertNotIn("compare-col", slide_009)
        self.assertNotIn("더 큰 구조 설계", slide_009)
        self.assertIn("negative-opinion", slide_009)

        self.assertIn("<img", slide_012)
        self.assertNotIn("doc-icon-claude", slide_012)
        self.assertNotIn("doc-icon-cursor", slide_012)
        self.assertNotIn("doc-icon-copilot", slide_012)
        self.assertNotIn("doc-icon-codex", slide_012)
        self.assertTrue((ROOT / "assets/icons/toolcards/cursor-icon.svg").exists())

        self.assertIn("evolution-flow", slide_013)
        self.assertIn("analogy-block", slide_013)
        self.assertIn("CHAPTER 01", slide_013)
        self.assertNotIn("SECTION 1", slide_013)
        self.assertIn("var(--color-dark-surface)", (ROOT / "docs/03-html/shared/slide-base.css").read_text(encoding="utf-8"))

        self.assertIn("그래도 기초가 중요하다", slide_014)
        self.assertIn("summary-cards-body", slide_014)
        self.assertIn("CHAPTER 01", slide_014)
        self.assertNotIn("SECTION 1", slide_014)
        self.assertIn("AI가 더 많이 해줄수록 기초 지식을 가진 사람의 경쟁력 상승", slide_014)
        self.assertNotIn("코딩은 에이전트가 일할 환경을 설계하고 검증하는 영역으로 이동하고 있습니다.", slide_014)
        self.assertNotIn("데모까지는 쉽지만", slide_014)
        self.assertNotIn("BASICS", slide_014)
        self.assertNotIn("statement-chip", slide_014)

        self.assertIn("에이전틱 코딩의 실제 성과", slide_016)
        self.assertIn("2주", slide_016)
        self.assertIn("1~2일", slide_016)
        self.assertIn("불가능하던 작업 실현", slide_016)
        self.assertIn("카카오 AI 팀 내부 공유 사례", slide_016)
        self.assertNotIn("Augment Code + Vertex AI", slide_016)
        self.assertNotIn("Augment Code + Vertex AI", deck)
        self.assertNotIn("SECTION 2", slide_016)
        self.assertIn("metric-impact-body is-tall-reference", slide_016)

        self.assertIn("<h1 class=\"title-placeholder\">1막: Copilot과 ChatGPT, 프롬프트의 시대</h1>", slide_017)
        self.assertNotIn("Agent = Model + Harness", slide_017)
        self.assertNotIn("<h1 class=\"title-placeholder\">1막: Copilot과 ChatGPT, 프롬프트의 시대 (2022~2024)</h1>", slide_017)
        self.assertIn("2022~2024", slide_017)
        self.assertIn("era-range", slide_017)
        self.assertIn("prompt-era-body", slide_017)

        self.assertIn("<h1 class=\"title-placeholder\">Chain-of-Thought</h1>", slide_018)
        self.assertIn("cot-native-body", slide_018)
        self.assertIn("cot-example-diagram", slide_018)
        self.assertIn("중간 추론 단계", slide_018)
        self.assertIn("2캔 × 3개", slide_018)
        self.assertIn("11개", slide_018)
        self.assertNotIn("02-chain-of-thought.png", slide_018)
        self.assertNotIn("ReAct", slide_018)

        self.assertIn("<h1 class=\"title-placeholder\">ReAct / Tree-of-Thought</h1>", slide_019)
        self.assertIn("pattern-pair-body", slide_019)
        self.assertIn("ReAct", slide_019)
        self.assertIn("Tree-of-Thought", slide_019)
        self.assertIn("react-diagram", slide_019)
        self.assertIn("tot-diagram", slide_019)
        self.assertNotIn("Chain-of-Thought", slide_019)
        self.assertNotIn("Self-Refine", slide_019)
        self.assertNotIn("Reflexion", slide_019)
        self.assertNotIn("03-react-pattern.png", slide_019)
        self.assertNotIn("04-tree-of-thought.png", slide_019)

        self.assertIn("<h1 class=\"title-placeholder\">Self-Refine / Reflexion</h1>", slide_020)
        self.assertIn("feedback-loop-body", slide_020)
        self.assertIn("Self-Refine", slide_020)
        self.assertIn("Reflexion", slide_020)
        self.assertIn("self-refine-diagram", slide_020)
        self.assertIn("reflexion-diagram", slide_020)
        self.assertNotIn("ReAct", slide_020)
        self.assertNotIn("Tree-of-Thought", slide_020)

        self.assertIn("<h1 class=\"title-placeholder\">네 가지 에이전틱 패턴</h1>", slide_021)
        self.assertIn("agentic-pattern-quadrant-body", slide_021)
        self.assertIn("agentic-pattern-center", slide_021)
        self.assertIn("agentic-mini-diagram", slide_021)
        self.assertIn("Generate", slide_021)
        self.assertIn("Critique", slide_021)
        self.assertIn("Search/API", slide_021)
        self.assertIn("Reviewer", slide_021)
        self.assertNotIn("05-andrew-ng-agentic-design-patterns.png", slide_021)

        self.assertIn("<h1 class=\"title-placeholder\">프롬프트 시대의 벽</h1>", slide_022)
        self.assertIn("모델은 보지 못한 것을 알 수 없음", slide_022)
        self.assertIn("blind-prompting-matrix-body", slide_022)
        self.assertIn("2막: Cursor와 컨텍스트의 시대", slide_023)
        self.assertIn("cursor-tools-body", slide_023)
        self.assertNotIn("linear-gradient", (ROOT / "docs/03-html/shared/slide-base.css").read_text(encoding="utf-8"))
        self.assertIn("Cursor 아키텍처", slide_024)
        self.assertIn("cursor-architecture-redraw-body", slide_024)
        self.assertIn("cursor-architecture-example-canvas", slide_024)
        for flow_item in ["사용자 요청", "indexing", "retrieval", "context assembly", "edit/run", "verify"]:
            self.assertIn(flow_item, slide_024)
        self.assertIn("codebase index", slide_024)
        self.assertIn("context bundle", slide_024)
        self.assertIn("architecture-side-tools", slide_024)
        self.assertNotIn("06-cursor-ai-code-editor-architecture.png", slide_024)
        for loop_step in ["gather context", "take action", "verify", "repeat"]:
            self.assertIn(loop_step, slide_025)
        self.assertIn("<h1 class=\"title-placeholder\">컨텍스트 시대의 벽</h1>", slide_025)
        self.assertIn("loop-cycle-body", slide_025)
        self.assertIn("loop-cycle-arrow", slide_025)
        self.assertNotIn("loop-repeat-arc", slide_025)
        self.assertNotIn("↺ repeat", slide_025)
        self.assertIn("<h1 class=\"title-placeholder\">3막: 하네스의 시대</h1>", slide_026)
        self.assertIn("harness-era-signs-body", slide_026)
        for component in ["CLAUDE.md", "Skills", "Hooks", "MCP", "Plugins", "Subagents", "승인 체계"]:
            self.assertIn(component, slide_026)
        self.assertNotIn("component-tier-body", slide_026)
        self.assertNotIn("무엇을 보는지", slide_026)
        self.assertNotIn("기초", slide_026)
        self.assertNotIn("자동화", slide_026)
        self.assertNotIn("연결", slide_026)
        self.assertNotIn("확장", slide_026)
        self.assertIn("era-native-body", slide_027)
        self.assertIn("Agent = Model + Harness", slide_027)
        self.assertIn("Prompt ⊂ Context ⊂ Harness", slide_027)
        self.assertNotIn("era-native-nesting", slide_027)
        self.assertNotIn("01-three-era-timeline.png", slide_027)
        for era in ["Prompt Engineering", "Context Engineering", "Harness Engineering"]:
            self.assertIn(era, slide_027)
        for index in range(15, 28):
            slide = (ROOT / f"docs/03-html/slides/slide-{index:03d}.html").read_text(encoding="utf-8")
            self.assertIn("CHAPTER 02", slide)
            self.assertIn("chapter-02", slide)
            self.assertNotIn("ACT 1", slide)
            self.assertNotIn("ACT 2", slide)
            self.assertNotIn("ACT 3", slide)
            self.assertNotIn("LIMIT", slide)

        slide_011 = (ROOT / "docs/03-html/slides/slide-011.html").read_text(encoding="utf-8")
        self.assertIn("evidence-card-grid", slide_011)
        self.assertNotIn("<table class=\"data-table\">", slide_011)
        self.assertNotIn("원문 사실", slide_011)
        slide_005 = (ROOT / "docs/03-html/slides/slide-005.html").read_text(encoding="utf-8")
        self.assertIn("컴파일러가 만든 코드가 사람보다 효율적일 리 없다!", slide_005)
        self.assertNotIn("기계어를 직접 다루지 않으면 진정한 개발이 아니다!", slide_005)
        self.assertIn("<p class=\"table-question\">직접하는 일을 줄고, 설계하는 일은 늘어난다</p>", (ROOT / "docs/03-html/slides/slide-010.html").read_text(encoding="utf-8"))
        self.assertIn("Point p = new Point(10, 20);", (ROOT / "docs/03-html/slides/slide-007.html").read_text(encoding="utf-8"))
        self.assertNotIn("        Point p = new Point(10, 20);", (ROOT / "docs/03-html/slides/slide-007.html").read_text(encoding="utf-8"))
        self.assertNotIn("<code>\n", (ROOT / "docs/03-html/slides/slide-007.html").read_text(encoding="utf-8"))
        self.assertNotIn("\n</code>", (ROOT / "docs/03-html/slides/slide-007.html").read_text(encoding="utf-8"))

        css = (ROOT / "docs/03-html/shared/slide-base.css").read_text(encoding="utf-8")
        tokens = (ROOT / "docs/03-html/shared/tokens.css").read_text(encoding="utf-8")
        self.assertRegex(css, r"\.density-heavy\.family-agenda \.agenda-layout \{[^}]*grid-template-columns: minmax\(210px, 0\.82fr\) minmax\(0, 1\.18fr\);")
        self.assertRegex(css, r"\.density-heavy\.family-agenda \.agenda-list \{[^}]*grid-template-columns: 1fr;")
        self.assertRegex(css, r"\.density-heavy\.family-agenda \.agenda-item \{[^}]*grid-template-columns: 44px minmax\(0, 1\.12fr\) minmax\(0, 0\.98fr\);")
        self.assertNotIn("<p class=\"prompt-label\">", slide_009)
        self.assertRegex(css, r"\.prompt-only-body \{[^}]*align-content: start;")
        self.assertRegex(css, r"\.prompt-card \{[^}]*justify-items: stretch;")
        self.assertRegex(css, r"\.prompt-language-label \{[^}]*color: var\(--color-signal\);")
        self.assertRegex(css, r"\.cot-example-diagram \{[^}]*grid-template-columns: 1fr;")
        self.assertRegex(css, r"\.chapter-02 \.process-step \.step-title \{[^}]*font-size: 18px;")
        self.assertRegex(css, r"\.chapter-02 \.step-copy \{[^}]*font-size: 13px;")
        self.assertRegex(css, r"\.chapter-02 \.centered-claim \{[^}]*font-size: 20px;")
        self.assertRegex(css, r"\.pattern-example-card \{[^}]*padding: 12px;")
        self.assertRegex(css, r"\.cursor-architecture-example-canvas \{[^}]*grid-template-columns:")
        self.assertRegex(css, r"\.component-tier-body \{[^}]*grid-template-columns: 84px minmax\(0, 1fr\);")
        self.assertRegex(css, r"\.era-native-equation \{[^}]*font-size: 24px;")
        self.assertRegex(css, r"\.evidence-card \{[^}]*min-height: 148px;")
        self.assertRegex(css, r"\.evidence-card \{[^}]*padding: 20px 22px 22px;")
        self.assertRegex(css, r"\.summary-card \{[^}]*background: var\(--color-surface\);")
        self.assertRegex(css, r"\.summary-card \{[^}]*border: 1px solid var\(--color-line-soft\);")
        self.assertRegex(css, r"\.evolution-step \{[^}]*background: var\(--color-surface\);")
        self.assertRegex(css, r"\.evolution-step \{[^}]*border: 1px solid var\(--color-line-soft\);")
        self.assertRegex(css, r"\.evolution-step\.is-final \{[^}]*background: var\(--color-dark-surface\);")
        self.assertRegex(css, r"\.metric-impact-body\.is-tall-reference \{[^}]*top: 126px;")
        self.assertRegex(css, r"\.metric-impact-body\.is-tall-reference \{[^}]*bottom: 72px;")
        self.assertRegex(css, r"\.metric-impact-body\.is-tall-reference \.impact-card \{[^}]*min-height: 222px;")
        self.assertRegex(css, r"\.cot-native-body \{[^}]*grid-template-columns:")
        self.assertRegex(css, r"\.pattern-pair-body,\n\.feedback-loop-body \{[^}]*grid-template-columns: repeat\(2, minmax\(0, 1fr\)\);")
        self.assertRegex(css, r"\.harness-era-signs-body \{[^}]*grid-template-rows: auto 1fr auto;")
        self.assertNotIn("background: var(--color-dark-card);", css)
        self.assertNotIn("border: 1px solid var(--color-dark-card-border);", css)
        self.assertNotIn("background: var(--color-dark-surface-muted);", css)
        self.assertNotIn("--color-dark-card", css + tokens)
        self.assertNotIn("--color-dark-card-border", css + tokens)
        self.assertNotIn("--color-dark-surface-muted", css + tokens)
        self.assertNotIn("#f3efe7", css + tokens)
        self.assertNotIn("#eee9e1", css + tokens)
        self.assertNotIn("#e8e1d5", css + tokens)
        self.assertNotIn("--color-dark-accent", css + tokens)
        self.assertNotIn("#c76640", css + tokens)


if __name__ == "__main__":
    unittest.main()
