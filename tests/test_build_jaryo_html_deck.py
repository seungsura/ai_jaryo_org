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
SLIDE_021_PATH = SLIDES_DIR / "slide-019.html"
SLIDE_022_PATH = SLIDES_DIR / "slide-020.html"
SLIDE_023_PATH = SLIDES_DIR / "slide-021.html"
SLIDE_024_PATH = SLIDES_DIR / "slide-022.html"
SLIDE_025_PATH = SLIDES_DIR / "slide-023.html"
SLIDE_026_PATH = SLIDES_DIR / "slide-024.html"
SLIDE_027_PATH = SLIDES_DIR / "slide-025.html"
SLIDE_028_PATH = SLIDES_DIR / "slide-026.html"
SLIDE_029_PATH = SLIDES_DIR / "slide-027.html"
SLIDE_030_PATH = SLIDES_DIR / "slide-028.html"
SLIDE_031_PATH = SLIDES_DIR / "slide-029.html"
SLIDE_032_PATH = SLIDES_DIR / "slide-030.html"
SLIDE_033_PATH = SLIDES_DIR / "slide-031.html"
SLIDE_034_PATH = SLIDES_DIR / "slide-032.html"
SLIDE_035_PATH = SLIDES_DIR / "slide-033.html"
SLIDE_036_PATH = SLIDES_DIR / "slide-034.html"
SLIDE_037_PATH = SLIDES_DIR / "slide-035.html"
SLIDE_038_PATH = SLIDES_DIR / "slide-036.html"
SLIDE_039_PATH = SLIDES_DIR / "slide-037.html"
SLIDE_040_PATH = SLIDES_DIR / "slide-038.html"
SLIDE_041_PATH = SLIDES_DIR / "slide-039.html"
SLIDE_042_PATH = SLIDES_DIR / "slide-040.html"
SLIDE_043_PATH = SLIDES_DIR / "slide-041.html"
SLIDE_044_PATH = SLIDES_DIR / "slide-042.html"
SLIDE_045_PATH = SLIDES_DIR / "slide-043.html"
SLIDE_046_PATH = SLIDES_DIR / "slide-044.html"
SLIDE_048_PATH = SLIDES_DIR / "slide-046.html"
SLIDE_049_PATH = SLIDES_DIR / "slide-047.html"
SLIDE_051_PATH = SLIDES_DIR / "slide-049.html"
SLIDE_055_PATH = SLIDES_DIR / "slide-053.html"
SLIDE_056_PATH = SLIDES_DIR / "slide-054.html"
SLIDE_081_PATH = SLIDES_DIR / "slide-079.html"
SLIDE_082_PATH = SLIDES_DIR / "slide-080.html"
SLIDE_094_PATH = SLIDES_DIR / "slide-092.html"


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
        chapter_dirs = sorted(SLIDE_MODULES_DIR.glob("chapter_[0-9][0-9]"))
        slide_modules = sorted(SLIDE_MODULES_DIR.glob("chapter_[0-9][0-9]/slide_*.py"))

        self.assertLessEqual(len(entrypoint.splitlines()), 12)
        self.assertNotIn("def build_all_specs", entrypoint)
        self.assertNotIn("make_slide(", entrypoint)
        self.assertEqual(len(chapter_dirs), 10)
        self.assertEqual(len(slide_modules), 92)
        self.assertEqual(slide_modules[0].relative_to(SLIDE_MODULES_DIR).as_posix(), "chapter_00/slide_001.py")
        self.assertEqual(slide_modules[-1].relative_to(SLIDE_MODULES_DIR).as_posix(), "chapter_09/slide_092.py")

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

    def test_builder_generates_92_slide_registry(self) -> None:
        run_builder()

        rows = manifest_rows()
        self.assertEqual(len(rows), 92)
        self.assertIn("`S001`", rows[0])
        self.assertIn("`S092`", rows[-1])

    def test_builder_uses_three_digit_slide_files(self) -> None:
        run_builder()

        slide_files = sorted(SLIDES_DIR.glob("slide-*.html"))
        self.assertEqual(len(slide_files), 92)
        self.assertEqual(slide_files[0].name, "slide-001.html")
        self.assertEqual(slide_files[-1].name, "slide-092.html")

    def test_builder_writes_outline_deck_and_script(self) -> None:
        run_builder()

        outline = OUTLINE_PATH.read_text(encoding="utf-8")
        deck = DECK_PATH.read_text(encoding="utf-8")

        self.assertIn("### S001.", outline)
        self.assertIn("### S014.", outline)
        self.assertIn("### S027.", outline)
        self.assertIn("### S033.", outline)
        self.assertIn("### S045.", outline)
        self.assertIn("### S092.", outline)
        self.assertIn("00/01/02/03/04/05/06/07/08/09 92-slide", outline)
        self.assertTrue(SCRIPT_PATH.exists())
        self.assertIn('data-slide-id="S001"', deck)
        self.assertIn('data-slide-id="S014"', deck)
        self.assertIn('data-slide-id="S027"', deck)
        self.assertIn('data-slide-id="S033"', deck)
        self.assertIn('data-slide-id="S045"', deck)
        self.assertIn('data-slide-id="S092"', deck)
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
        slide_028 = SLIDE_028_PATH.read_text(encoding="utf-8")
        slide_029 = SLIDE_029_PATH.read_text(encoding="utf-8")
        slide_030 = SLIDE_030_PATH.read_text(encoding="utf-8")
        slide_031 = SLIDE_031_PATH.read_text(encoding="utf-8")
        slide_032 = SLIDE_032_PATH.read_text(encoding="utf-8")
        slide_033 = SLIDE_033_PATH.read_text(encoding="utf-8")
        slide_034 = SLIDE_034_PATH.read_text(encoding="utf-8")
        slide_035 = SLIDE_035_PATH.read_text(encoding="utf-8")
        slide_036 = SLIDE_036_PATH.read_text(encoding="utf-8")
        slide_037 = SLIDE_037_PATH.read_text(encoding="utf-8")
        slide_038 = SLIDE_038_PATH.read_text(encoding="utf-8")
        slide_039 = SLIDE_039_PATH.read_text(encoding="utf-8")
        slide_040 = SLIDE_040_PATH.read_text(encoding="utf-8")
        slide_041 = SLIDE_041_PATH.read_text(encoding="utf-8")
        slide_042 = SLIDE_042_PATH.read_text(encoding="utf-8")
        slide_043 = SLIDE_043_PATH.read_text(encoding="utf-8")
        slide_044 = SLIDE_044_PATH.read_text(encoding="utf-8")
        slide_045 = SLIDE_045_PATH.read_text(encoding="utf-8")
        slide_046 = SLIDE_046_PATH.read_text(encoding="utf-8")
        slide_048 = SLIDE_048_PATH.read_text(encoding="utf-8")
        slide_049 = SLIDE_049_PATH.read_text(encoding="utf-8")
        slide_051 = SLIDE_051_PATH.read_text(encoding="utf-8")
        slide_055 = SLIDE_055_PATH.read_text(encoding="utf-8")
        slide_056 = SLIDE_056_PATH.read_text(encoding="utf-8")
        slide_081 = SLIDE_081_PATH.read_text(encoding="utf-8")
        slide_082 = SLIDE_082_PATH.read_text(encoding="utf-8")
        slide_094 = SLIDE_094_PATH.read_text(encoding="utf-8")
        css = (ROOT / "docs/03-html/shared/slide-base.css").read_text(encoding="utf-8")

        self.assertIn("<title>Harness 잘 사용하기</title>", deck)
        self.assertIn("<h1 class=\"title-placeholder\">Harness 잘 사용하기</h1>", slide_001)
        self.assertNotIn("Harness를 설계하는 법", deck)
        self.assertNotIn("Harness를 설계하는 법", slide_001)

        self.assertIn("<p class=\"prompt-text\">이 함수를 리펙토링하고 테스트 코드를 작성해줘.</p>", slide_009)
        self.assertIn("<p class=\"prompt-language-label\">자연어</p>", slide_009)
        self.assertNotIn("<article class=\"prompt-card\"><p class=\"prompt-language-label\">", slide_009)
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

        self.assertIn("<h1 class=\"title-placeholder\">CoT / ReAct / ToT</h1>", slide_018)
        self.assertIn("cot-triad-body", slide_018)
        self.assertIn("cot-triad-card", slide_018)
        self.assertIn("cot-triad-diagram", slide_018)
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
            self.assertIn(snippet, slide_018)
        self.assertNotIn("02-chain-of-thought.png", slide_018)
        for forbidden in [
            "Graph-of-Thought",
            "GoT",
            "Self-Refine",
            "Reflexion",
            "Thought 1",
            "2캔 × 3개",
            "11개",
            "http://",
            "https://",
        ]:
            self.assertNotIn(forbidden, slide_018)

        self.assertIn("<h1 class=\"title-placeholder\">네 가지 에이전틱 패턴</h1>", slide_019)
        self.assertIn("agentic-pattern-quadrant-body", slide_019)
        self.assertIn("agentic-map-svg", slide_019)

        self.assertIn("<h1 class=\"title-placeholder\">프롬프트 시대의 벽</h1>", slide_020)
        self.assertIn("blind-prompting-matrix-body", slide_020)
        self.assertIn("blind-prompting-quote-card", slide_020)

        self.assertIn("<h1 class=\"title-placeholder\">네 가지 에이전틱 패턴</h1>", slide_021)
        self.assertIn("agentic-pattern-quadrant-body", slide_021)
        self.assertIn("agentic-map-svg", slide_021)
        for snippet in [
            "Reflection",
            "Tool Use",
            "Planning",
            "Multi-Agent Collaboration",
            "자기 결과를 비판하고 반복 개선",
            "외부 도구로 정보 수집과 실행",
            "목표를 실행 순서로 나눠 추진",
            "전문 역할로 나눠 복잡한 작업 수행",
            "자기 수정 루프",
            "모델 바깥 세계 연결",
            "긴 작업 추진",
            "생성과 검증 분리",
            'cx="58" cy="44"',
            'cx="116" cy="44"',
            "M129 44 H172",
            'cx="272" cy="65"',
        ]:
            self.assertIn(snippet, slide_021)
        self.assertNotIn("agentic-pattern-center", slide_021)
        self.assertNotIn("agentic-mini-diagram", slide_021)
        self.assertNotIn("05-andrew-ng-agentic-design-patterns.png", slide_021)

        self.assertIn("<h1 class=\"title-placeholder\">프롬프트 시대의 벽</h1>", slide_022)
        self.assertIn("blind-prompting-matrix-body", slide_022)
        self.assertIn("blind-prompting-quote-card", slide_022)
        self.assertIn("모델은 컨텍스트 창 안에 들어온 지식만 다룰 수 있다.", slide_022)
        self.assertIn("Vivek Trivedy, LangChain", slide_022)
        self.assertNotIn("모델은 보지 못한 것을 알 수 없음", slide_022)
        self.assertNotIn("문제는 지시문이 아니라 모델이 소비하는 정보", slide_022)
        self.assertIn("2막: Cursor와 컨텍스트의 시대", slide_023)
        self.assertIn("cursor-tools-body", slide_023)
        self.assertNotIn("linear-gradient", (ROOT / "docs/03-html/shared/slide-base.css").read_text(encoding="utf-8"))
        self.assertIn("Cursor 아키텍처", slide_024)
        self.assertIn("cursor-architecture-asset-body", slide_024)
        self.assertIn("cursor-architecture-reference-figure", slide_024)
        for flow_item in ["사용자 요청", "코드베이스 인덱싱", "(파일, 심볼, AST, 문서)", "관련 파일 / 규칙 / 히스토리 검색", "컨텍스트 조립", "Composer / Agent Mode", "멀티파일 수정 + 명령 실행", "테스트 / 린트 / 로그 확인"]:
            self.assertIn(flow_item, slide_024)
        self.assertIn("06-cursor-ai-code-editor-architecture.png", slide_024)
        self.assertNotIn("cursor-architecture-redraw-body", slide_024)
        self.assertNotIn("architecture-side-tools", slide_024)
        for snippet in [
            "폭주를 만드는 것",
            "잘못된 결과나 응답 유입",
            "느슨한 실행 권한",
            "잘못된 검증",
            "먼저 고정할 것",
            "허용/차단 범위",
            "멈춤 기준",
            "검증 경로",
            "멈춤 기준과 검증 경로를 먼저 설계해야 한다",
        ]:
            self.assertIn(snippet, slide_025)
        self.assertIn("<h1 class=\"title-placeholder\">컨텍스트만으로는 부족하다</h1>", slide_025)
        self.assertIn("cache-sequence-body", slide_025)
        self.assertIn("compare-grid with-arrow", slide_025)
        self.assertNotIn("context-failure-body", slide_025)
        self.assertNotIn("context-wall-body", slide_025)
        for forbidden in ["gather context", "take action", "verify", "repeat", "loop-cycle-body", "loop-cycle-arrow", "loop-repeat-arc", "↺ repeat"]:
            self.assertNotIn(forbidden, slide_025)
        self.assertIn("<h1 class=\"title-placeholder\">3막: 하네스의 시대</h1>", slide_026)
        self.assertIn("harness-era-minimal-body", slide_026)
        for snippet in ["코딩 도구는 이제 실행 환경을 품는다", "자동완성·채팅", "작업 환경 전체", "파일 · 셸 · 테스트", "Harness"]:
            self.assertIn(snippet, slide_026)
        for component in ["Plan Mode", "승인 체계", "CLAUDE.md", "Skills", "Hooks", "MCP", "Plugins", "Subagents", "허용", "차단", "기록"]:
            self.assertNotIn(component, slide_026)
        self.assertNotIn("harness-era-signs-body", slide_026)
        self.assertNotIn("component-tier-body", slide_026)
        self.assertNotIn("무엇을 보는지", slide_026)
        self.assertNotIn("기초", slide_026)
        self.assertNotIn("자동화", slide_026)
        self.assertNotIn("연결", slide_026)
        self.assertNotIn("확장", slide_026)
        self.assertIn("era-native-body", slide_027)
        self.assertIn("Agent = Model + Harness", slide_027)
        self.assertIn("Prompt ⊂ Context ⊂ Harness", slide_027)
        self.assertNotIn("<table class=\"data-table\">", slide_027)
        self.assertNotIn("era-native-nesting", slide_027)
        self.assertNotIn("01-three-era-timeline.png", slide_027)
        for era in ["Prompt Engineering", "Context Engineering", "Harness Engineering"]:
            self.assertIn(era, slide_027)
        self.assertIn("<h1 class=\"title-placeholder\">AI 시대의 개발 방법론</h1>", slide_028)
        self.assertIn("CHAPTER 03", slide_028)
        self.assertIn("chapter-03", slide_028)
        self.assertIn("<h1 class=\"title-placeholder\">왜 지금 방법론</h1>", slide_029)
        for snippet in ["2025.02", "Vibe Coding", "2025 중반", "구조화된 검토", "2025 하반기", "Spec-first", "2026 초", "Context Engineering"]:
            self.assertIn(snippet, slide_029)
        self.assertIn("AI에게 무엇을 시킬지, 어떻게 검증할 것인지", slide_029)
        slide_029_content = slide_029.split('<footer class="footer">', maxsplit=1)[0]
        for forbidden in ["Harness", "Agent", "Prompt", "Model", "Waterfall"]:
            self.assertNotIn(forbidden, slide_029_content)
        self.assertIn("<h1 class=\"title-placeholder\">SDD</h1>", slide_030)
        for snippet in [
            "Spec-Driven Development",
            "GitHub Copilot icon",
            "GitHub spec-kit",
            "WHAT",
            "WHY",
            "HOW",
            "/speckit.specify",
            "/speckit.plan",
            "/speckit.tasks",
            "[NEEDS CLARIFICATION]",
            "Constitution Check",
        ]:
            self.assertIn(snippet, slide_030)
        self.assertNotIn("하네스", slide_030)
        self.assertIn("<h1 class=\"title-placeholder statement-text\">TDD (Test-Driven Development)</h1>", slide_031)
        self.assertIn("tdd-control-lead", slide_031)
        for snippet in [
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
            self.assertIn(snippet, slide_031)
        self.assertIn("tdd-control-layers-body", slide_031)
        self.assertIn("tdd-flow-stack", slide_031)
        self.assertEqual(slide_031.count("tdd-flow-step"), 3)
        self.assertIn("tdd-control-column", slide_031)
        self.assertEqual(slide_031.count("tdd-control-block"), 2)
        self.assertNotIn("AI 시대의 TDD는 권한 통제 기법", slide_031)
        self.assertNotIn("권한 통제", slide_031)
        self.assertNotIn("REFACTOR", slide_031)
        self.assertNotIn("assert 약화 금지 · 구현 먼저 금지", slide_031)
        self.assertNotIn("decision-map-body", slide_031)
        self.assertIn("<h1 class=\"title-placeholder\">Waterfall vs SDD</h1>", slide_032)
        for snippet in [
            "Waterfall",
            "SDD",
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
            self.assertIn(snippet, slide_032)
        self.assertNotIn("Waterfall은 끝에서 제약이 드러나고, SDD는 스펙이 계획과 태스크를 만든다.", slide_032)
        for forbidden in ["AI 시대 SDD + TDD", "앞단의 문서", "검증은", "실제 작동 원리", "문서의 성격", "검증 타이밍", "작동 방식", "검증 루프"]:
            self.assertNotIn(forbidden, slide_032)
        self.assertIn("waterfall-comparison-body", slide_032)
        self.assertIn("comparison-row-grid", slide_032)
        self.assertNotIn("comparison-synthesis", slide_032)
        self.assertEqual(slide_032.count('<article class="comparison-row"'), 3)
        self.assertNotIn("compare-grid", slide_032)
        self.assertNotIn("하네스", slide_032)
        self.assertIn("spec-tdd-subheading", slide_033)
        for snippet in ["SDD + TDD가 Harness로 이어지는 이유", "스펙 템플릿", "계획 문서", "TDD 루프", "Skills", "Hooks", "하네스", "이 시스템이 곧 하네스 엔지니어링"]:
            self.assertIn(snippet, slide_033)
        self.assertIn("spec-tdd-bridge-body", slide_033)
        self.assertNotIn("spec-tdd-thesis", slide_033)
        self.assertNotIn("Spec + TDD", slide_033)
        self.assertIn("spec-tdd-card-grid", slide_033)
        self.assertIn("spec-tdd-plus", slide_033)
        self.assertEqual(slide_033.count('<article class="spec-tdd-card"'), 2)
        self.assertIn("spec-tdd-synthesis", slide_033)
        self.assertNotIn("decision-map-body", slide_033)
        tdd_card = slide_033.split("<h2>TDD</h2>", maxsplit=1)[1].split("</article>", maxsplit=1)[0]
        self.assertNotIn("하네스", tdd_card)
        self.assertIn("<h1 class=\"title-placeholder\">프롬프트를 넘어서</h1>", slide_034)
        self.assertIn("section-keyword-plain", slide_034)
        self.assertNotIn("<li class=\"section-keyword\">", slide_034)
        for snippet in ["Prompt", "Context", "Harness"]:
            self.assertIn(snippet, slide_034)
        self.assertIn("<h1 class=\"title-placeholder\">Prompt, Context, Harness</h1>", slide_035)
        for snippet in ["무엇을/어떻게 말할 것인가", "무엇을/어떻게 보여줄 것인가", "무엇을/어떻게 통제할 것인가", "Prompt ⊂ Context ⊂ Harness"]:
            self.assertIn(snippet, slide_035)
        self.assertIn("<h1 class=\"title-placeholder\">Agent = Model + Harness</h1>", slide_036)
        for snippet in ["모델이 아닌 것은 전부 하네스입니다.", "LangChain, Vivek Trivedy", "Context Engineering", "Tool Orchestration", "State &amp; Memory", "Verification Loop", "Error Recovery", "Human-in-the-Loop Control"]:
            self.assertIn(snippet, slide_036)
        self.assertIn("quote-card-block", slide_036)
        self.assertIn("agent-quote-block", slide_036)
        self.assertIn("agent-component-grid", slide_036)
        self.assertNotIn("table-callout", slide_036)
        self.assertIn("<h1 class=\"title-placeholder\">에이전트 루프: 하네스의 심장</h1>", slide_037)
        self.assertIn("loop-synthesis", slide_037)
        self.assertNotIn("loop-center centered-claim", slide_037)
        self.assertIn("거의 모든 에이전트가 반복하는 4단계.", slide_037)
        self.assertNotIn("맥락을 모으고, 행동하고, 검증한 뒤, 다음 행동만 남긴다", slide_037)
        self.assertNotIn("이 네 지점을 신뢰성 있게 만드는 일", slide_037)
        self.assertNotIn("하네스 엔지니어링 = 이 네 단계의 신뢰성", slide_037)
        for snippet in ["gather context", "take action", "verify work", "repeat"]:
            self.assertIn(snippet, slide_037)
        self.assertIn("<h1 class=\"title-placeholder\">하네스의 책임</h1>", slide_038)
        self.assertNotIn("먼저 책임을 정하고, 그다음 도구와 게이트를 배치", slide_038)
        self.assertIn("<h1 class=\"title-placeholder\">하네스의 도구</h1>", slide_039)
        self.assertNotIn("<h1 class=\"title-placeholder\">책임과 도구는 1:1이 아니다</h1>", slide_039)
        self.assertNotIn("<table class=\"data-table\">", slide_039)
        self.assertNotIn("N:N", slide_039)
        self.assertNotIn("하네스의 책임 ↔ 하네스의 도구", slide_039)
        self.assertIn("tool-network-line", slide_039)
        self.assertIn("tool-network-synthesis", slide_039)
        self.assertIn("<p class=\"tool-network-synthesis centered-claim\">책임과 도구는 1:1이 아니다</p>", slide_039)
        self.assertNotIn("도구 이름보다 그 도구가 맡는 책임", slide_039)
        self.assertIn("<h1 class=\"title-placeholder\">Context Engineering</h1>", slide_040)
        for snippet in ["Anthropic의 4가지 전략: 필요한 정보만 남기고 잡음은 덜어낸다.", "Anthropic Research", "Write", "Select", "Compress", "Isolate"]:
            self.assertIn(snippet, slide_040)
        self.assertIn("quote-card-block", slide_040)
        self.assertIn("context-quote-block", slide_040)
        self.assertNotIn("<p class=\"flow-thesis centered-claim\">smallest set of high-signal tokens</p>", slide_040)
        self.assertNotIn("smallest set of high-signal tokens", slide_040)
        self.assertNotIn("신호가 큰 토큰", slide_040)
        self.assertNotIn("Antrophic", slide_040)
        self.assertIn("<h1 class=\"title-placeholder\">MCP와 Context 7</h1>", slide_041)
        for snippet in ["MCP", "Context 7", "Context 7 MCP", "GitHub", "Slack", "DB", "Filesystem", "Internal API", "최신 API 문서", "모델 기억 대신"]:
            self.assertIn(snippet, slide_041)
        self.assertIn("mcp-context-card-body", slide_041)
        self.assertIn("mcp-usage-flow", slide_041)
        self.assertIn("mcp-usage-stage", slide_041)
        self.assertIn("mcp-usage-card", slide_041)
        self.assertIn("context7-mcp-card", slide_041)
        self.assertIn("context7-note", slide_041)
        self.assertIn("context7-notes", slide_041)
        self.assertIn("외부 도구·데이터 소스", slide_041)
        self.assertNotIn("Context Hub", slide_041)
        self.assertNotIn("context-hub", slide_041)
        self.assertNotIn("context7-principle", slide_041)
        self.assertNotIn("mcp-usage-lane", slide_041)
        self.assertNotIn("context-hub-explainer-lane", slide_041)
        self.assertNotIn("mcp-usage-panel", slide_041)
        self.assertNotIn("context-hub-explainer-card", slide_041)
        self.assertEqual(slide_041.count("<article"), 2)
        self.assertNotIn("mcp-usage-node", slide_041)
        self.assertNotIn("<article class=\"context7-note\">", slide_041)
        self.assertNotIn("mcp-tool-chip", slide_041)
        self.assertNotIn("connected tools", slide_041)
        self.assertNotIn("process-track", slide_041)
        self.assertIn("<h1 class=\"title-placeholder\">RAG vs Context 7</h1>", slide_042)
        for snippet in ["RAG", "Context 7", "대상", "강점", "기대", "문제점", "검색 범위와 기준 시점의 차이"]:
            self.assertIn(snippet, slide_042)
        self.assertIn("rag-context-table-body", slide_042)
        self.assertIn("rag-context-table", slide_042)
        self.assertNotIn("rag-context-research-body", slide_042)
        self.assertNotIn("rag-context-card", slide_042)
        self.assertNotIn("Context Hub", slide_042)
        self.assertNotIn("선택 기준", slide_042)
        self.assertNotIn("Sources:", slide_042)
        self.assertNotIn("Lewis et al. 2020", slide_042)
        self.assertNotIn("MCP Docs", slide_042)
        self.assertNotIn("rag-context-decision", slide_042)
        self.assertNotIn("research-source-line", slide_042)
        self.assertNotIn("passage 검색", slide_042)
        self.assertNotIn("retriever 품질", slide_042)
        self.assertIn("<h1 class=\"title-placeholder\">Memory: 세션을 넘어서는 기억</h1>", slide_043)
        self.assertNotIn("<table class=\"data-table\">", slide_043)
        self.assertIn("memory-artifact-map", slide_043)
        self.assertLess(slide_043.find("memory-artifact-grid"), slide_043.find("memory-core-claim"))
        self.assertIn("대화창을 기억 저장소로 착각하지 않는다", slide_043)
        self.assertIn("<h1 class=\"title-placeholder\">Stable Prefix와 Variable Suffix</h1>", slide_044)
        for snippet in ["cache-sequence-body", "stable-prefix-block", "variable-suffix-block", "KV-cache", "시스템 프롬프트", "도구 정의", "장기 규칙", "최신 사용자 입력", "도구 결과", "최신 입력과 도구 결과만 뒤에서 갈아 끼워야 KV-cache hit rate가 살아납니다.", "Manus Research", "cache-quote-block"]:
            self.assertIn(snippet, slide_044)
        self.assertNotIn("앞쪽 규칙은 고정하고, 최신 입력과 도구 결과만 뒤에서 바꾼다", slide_044)
        self.assertNotIn("Manus 사례", slide_044)
        self.assertNotIn("하네스 시대에는 잘 쓰는 것 못지않게 안 바꾸는 것도 능력", slide_044)
        self.assertIn("<h1 class=\"title-placeholder\">하네스는 환경 그 자체다</h1>", slide_045)
        for snippet in ["필요한 파일", "필요한 도구", "필요한 규칙", "Harness Builder"]:
            self.assertIn(snippet, slide_045)
        for index in range(26, 32):
            slide = (ROOT / f"docs/03-html/slides/slide-{index:03d}.html").read_text(encoding="utf-8")
            self.assertIn("CHAPTER 03", slide)
            self.assertIn("chapter-03", slide)
            self.assertNotIn("SECTION 3", slide)
        for index in range(15, 26):
            slide = (ROOT / f"docs/03-html/slides/slide-{index:03d}.html").read_text(encoding="utf-8")
            self.assertIn("CHAPTER 02", slide)
            self.assertIn("chapter-02", slide)
            self.assertNotIn("ACT 1", slide)
            self.assertNotIn("ACT 2", slide)
            self.assertNotIn("ACT 3", slide)
            self.assertNotIn("LIMIT", slide)
        for index in range(32, 44):
            slide = (ROOT / f"docs/03-html/slides/slide-{index:03d}.html").read_text(encoding="utf-8")
            self.assertIn("CHAPTER 04", slide)
            self.assertIn("chapter-04", slide)
            self.assertNotIn("SECTION 4", slide)

        for start, end, chapter, css_class, stale in [
            (44, 53, "CHAPTER 05", "chapter-05", "SECTION 5"),
            (54, 66, "CHAPTER 06", "chapter-06", "SECTION 6"),
            (67, 79, "CHAPTER 07", "chapter-07", "SECTION 7"),
            (80, 88, "CHAPTER 08", "chapter-08", "SECTION 8"),
            (89, 92, "CHAPTER 09", "chapter-09", "SECTION 9"),
        ]:
            for index in range(start, end + 1):
                slide = (ROOT / f"docs/03-html/slides/slide-{index:03d}.html").read_text(encoding="utf-8")
                self.assertIn(chapter, slide)
                self.assertIn(css_class, slide)
                self.assertNotIn(stale, slide)

        self.assertIn("이렇게 하면 망한다", slide_046)
        self.assertIn("작업이 길어질 때 특히 위험한 이유", slide_048)
        self.assertIn("progression-card-map", slide_048)
        for snippet in ["1 단계", "95%", "첫 번째 결과물", "20 단계", "36%", "20 단계 뒤 결과물"]:
            self.assertIn(snippet, slide_048)
        for stale_snippet in ["긴 작업이 위험한 이유", "long-work-cost-map", "스무 단계 뒤 결과물", "긴 작업 사슬"]:
            self.assertNotIn(stale_snippet, slide_048)
        self.assertIn("컨텍스트가 길수록 항상 좋은 것은 아니다", slide_049)
        self.assertNotIn("컨텍스트가 클수록 항상 좋은 것은 아니다", slide_049)
        self.assertIn("AI Slop", slide_051)
        self.assertIn("Doom Loop", slide_051)
        self.assertIn("Shadow Agent", slide_051)
        self.assertIn("더 긴 컨텍스트보다 더 좋은 게이트", slide_055)
        self.assertIn("왜 하나의 에이전트만으로는 부족한가", slide_056)
        self.assertIn("결론: 실전 워크플로우의 중심은 운영 구조다", slide_081)
        self.assertIn("이 글과 발표가 만들어진 과정", slide_082)
        self.assertIn("내일부터", slide_094)

        slide_011 = (ROOT / "docs/03-html/slides/slide-011.html").read_text(encoding="utf-8")
        self.assertIn("evidence-card-grid", slide_011)
        self.assertNotIn("<table class=\"data-table\">", slide_011)
        self.assertNotIn("원문 사실", slide_011)
        slide_005 = (ROOT / "docs/03-html/slides/slide-005.html").read_text(encoding="utf-8")
        self.assertIn("컴파일러가 만든 코드가 사람보다 효율적일 리 없다!", slide_005)
        self.assertNotIn("기계어를 직접 다루지 않으면 진정한 개발이 아니다!", slide_005)
        self.assertIn("<p class=\"table-question\">직접하는 일을 줄고, 설계하는 일은 늘어난다</p>", (ROOT / "docs/03-html/slides/slide-010.html").read_text(encoding="utf-8"))

        css = (ROOT / "docs/03-html/shared/slide-base.css").read_text(encoding="utf-8")
        self.assertNotRegex(css, r"\.section-keyword \{")
        self.assertRegex(css, r"\.section-keyword-plain \{[^}]*color: rgba\(255, 255, 255, 0\.92\);")
        self.assertRegex(css, r"\.tool-network-line \{[^}]*stroke: var\(--color-signal\);")
        self.assertRegex(css, r"\.memory-artifact-grid \{[^}]*grid-template-columns:")
        self.assertRegex(css, r"\.cache-sequence-body \{[^}]*grid-template-columns:")
        self.assertRegex(css, r"\.quote-card-block \{[^}]*background: var\(--color-dark-surface\);")
        self.assertRegex(css, r"\.agent-component-grid \{[^}]*max-width: 690px;")
        self.assertRegex(css, r"\.context-quote-block \{[^}]*max-width: 700px;")
        self.assertRegex(css, r"\.mcp-context-card-body \{[^}]*grid-template-columns:")
        self.assertRegex(css, r"\.mcp-usage-card,[^}]*\.context7-mcp-card \{[^}]*box-shadow: var\(--shadow-card\);")
        self.assertNotIn(".mcp-usage-panel", css)
        self.assertNotIn(".context-hub-explainer-card", css)
        self.assertNotIn(".rag-context-decision", css)
        self.assertNotIn(".research-source-line", css)
        self.assertNotRegex(css, r"\.mcp-usage-stage \{[^}]*border-left:")
        self.assertRegex(css, r"\.rag-context-table-body \{[^}]*top:")
        self.assertRegex(css, r"\.rag-context-table \{[^}]*table-layout: fixed;")
        self.assertRegex(css, r"\.cache-quote-block \{[^}]*bottom:")

    def test_chapter_03_revision_5_focus(self) -> None:
        run_builder()

        slide_031 = SLIDE_031_PATH.read_text(encoding="utf-8")
        slide_032 = SLIDE_032_PATH.read_text(encoding="utf-8")
        slide_033 = SLIDE_033_PATH.read_text(encoding="utf-8")

        self.assertIn("<h1 class=\"title-placeholder statement-text\">TDD (Test-Driven Development)</h1>", slide_031)
        self.assertIn("tdd-control-lead", slide_031)
        for snippet in [
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
            self.assertIn(snippet, slide_031)

        self.assertIn("<h1 class=\"title-placeholder\">Waterfall vs SDD</h1>", slide_032)
        for snippet in [
            "Waterfall",
            "SDD",
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
            self.assertIn(snippet, slide_032)
        self.assertNotIn("Waterfall은 끝에서 제약이 드러나고, SDD는 스펙이 계획과 태스크를 만든다.", slide_032)
        self.assertNotIn("comparison-synthesis", slide_032)
        for forbidden in ["AI 시대 SDD + TDD", "앞단의 문서", "검증은", "실제 작동 원리", "문서의 성격", "검증 타이밍", "작동 방식", "검증 루프", "timing · storage · I/O"]:
            self.assertNotIn(forbidden, slide_032)

        self.assertIn("spec-tdd-subheading", slide_033)
        for snippet in [
            "SDD + TDD가 Harness로 이어지는 이유",
            "스펙 템플릿",
            "계획 문서",
            "TDD 루프",
            "Skills",
            "Hooks",
            "하네스",
            "이 시스템이 곧 하네스 엔지니어링",
        ]:
            self.assertIn(snippet, slide_033)
        self.assertNotIn("spec-tdd-thesis", slide_033)
        self.assertNotIn("Spec + TDD", slide_033)
        tdd_card = slide_033.split("<h2>TDD</h2>", maxsplit=1)[1].split("</article>", maxsplit=1)[0]
        self.assertNotIn("하네스", tdd_card)

    def test_chapter_03_revision_6_focus(self) -> None:
        run_builder()

        slide_030 = SLIDE_030_PATH.read_text(encoding="utf-8")
        slide_032 = SLIDE_032_PATH.read_text(encoding="utf-8")
        slide_033 = SLIDE_033_PATH.read_text(encoding="utf-8")
        css = (ROOT / "docs/03-html/shared/slide-base.css").read_text(encoding="utf-8")

        for snippet in [
            "spec-kit-workflow-body",
            "GitHub Copilot icon",
            "GitHub spec-kit",
            "/speckit.specify",
            "/speckit.plan",
            "/speckit.tasks",
        ]:
            self.assertIn(snippet, slide_030)

        self.assertIn("comparison-column-header is-focus", slide_032)
        self.assertNotIn("comparison-synthesis", slide_032)
        self.assertNotIn("Waterfall은 끝에서 제약이 드러나고, SDD는 스펙이 계획과 태스크를 만든다.", slide_032)

        self.assertIn("spec-tdd-subheading", slide_033)
        self.assertNotIn("spec-tdd-thesis", slide_033)
        self.assertNotIn("Spec + TDD", slide_033)
        tdd_card = slide_033.split("<h2>TDD</h2>", maxsplit=1)[1].split("</article>", maxsplit=1)[0]
        self.assertNotIn("하네스", tdd_card)

        self.assertRegex(css, r"\.spec-tdd-subheading \{[^}]*color: var\(--color-ink\);")
        self.assertRegex(css, r"\.spec-tdd-card-grid \{[^}]*left: 72px;[^}]*right: 72px;[^}]*grid-template-columns: minmax\(0, 1fr\) 34px minmax\(0, 1fr\);[^}]*gap: 16px;")
        self.assertRegex(css, r"\.spec-tdd-card \{[^}]*min-height: 88px;[^}]*padding: 16px 18px 14px;[^}]*gap: 10px;")
        self.assertRegex(css, r"\.spec-tdd-card h2 \{[^}]*font-size: 24px;")
        self.assertRegex(css, r"\.spec-tdd-card li \{[^}]*font-size: 16px;")
        self.assertRegex(css, r"\.comparison-column-headers \{[^}]*grid-template-columns: minmax\(170px, 0\.62fr\) minmax\(0, 1fr\) 24pt minmax\(0, 1fr\);")


if __name__ == "__main__":
    unittest.main()
