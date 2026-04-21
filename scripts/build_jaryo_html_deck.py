#!/usr/bin/env python3
from __future__ import annotations

import html
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
HTML_ROOT = ROOT / "docs/03-html"
OUTLINE_PATH = HTML_ROOT / "outline/slide-outline.md"
MANIFEST_PATH = HTML_ROOT / "manifest.md"
SLIDES_ROOT = HTML_ROOT / "slides"
DECK_ROOT = HTML_ROOT / "deck"
DECK_PATH = DECK_ROOT / "index.html"
SCRIPT_PATH = DECK_ROOT / "script.md"
DATA_PATH = HTML_ROOT / "data/slide-specs.json"
SHARED_ROOT = HTML_ROOT / "shared"
TOKENS_CSS = SHARED_ROOT / "tokens.css"
BASE_CSS = SHARED_ROOT / "slide-base.css"

THEME = "theme-minimal-light"
FOOTER_LEFT = "Harness 잘 사용하기"
SOURCE_ROOT = ROOT / "docs/02-seminar/harness-rebuilt-md"

CODE_MACHINE = "10111000 00000001 00000000 00000000 00000000"

CODE_ASSEMBLY_MOV = "MOV EAX, 1"

CODE_ASSEMBLY_HELLO = """section .data
  msg db "Hello World", 10

section .text
  global _start

_start:
  mov rax, 1
  mov rdi, 1
  mov rsi, msg
  mov rdx, 12
  syscall
  mov rax, 60
  mov rdi, 0
  syscall"""

CODE_C_HELLO = """#include <stdio.h>

int main() {
    printf("Hello\\n");
    return 0;
}"""

CODE_C_POINT = """#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x;
    int y;
} Point;

int main() {
    Point* p = malloc(sizeof(Point));
    p->x = 10;
    p->y = 20;
    printf(
        "Point: %d, %d\\n",
        p->x,
        p->y
    );
    free(p);
    return 0;
}"""

CODE_JAVA_POINT = """class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    public static void main(String[] args) {
        Point p = new Point(10, 20);
        System.out.println(
            "Point: " + p.x + ", " + p.y
        );
        p = null;
    }
}"""

CODE_JAVA_HELLO = """public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}"""

CODE_PYTHON_HELLO = 'print("Hello, World!")'

PROMPT_AI_REFACTOR = """대상 함수 리팩터링
테스트 코드 작성
검증 결과 정리"""

SECTION_TARGETS = {
    "00": 3,
    "01": 11,
}

SHELL_TO_FAMILY = {
    "title-hero-shell": "title",
    "agenda-list-shell": "agenda",
    "section-divider-shell": "section",
    "statement-editorial-shell": "content",
    "process-flow-shell": "content",
    "split-compare-shell": "comparison",
    "evidence-table-shell": "content",
}

SHELL_TO_LAYOUT = {
    "title-hero-shell": "centered",
    "agenda-list-shell": "wide",
    "section-divider-shell": "centered",
    "statement-editorial-shell": "editorial",
    "process-flow-shell": "wide",
    "split-compare-shell": "split",
    "evidence-table-shell": "wide",
}

SHELL_TO_TYPE = {
    "title-hero-shell": "title",
    "agenda-list-shell": "agenda",
    "section-divider-shell": "section",
    "statement-editorial-shell": "statement",
    "process-flow-shell": "process",
    "split-compare-shell": "comparison",
    "evidence-table-shell": "table",
}


@dataclass
class SlideSpec:
    order: int
    slide_id: str
    file_name: str
    title: str
    slide_type: str
    layout: str
    shell: str
    family: str
    density: str
    source_section: str
    source_block: str
    key_claim: str
    notes_intent: str
    notes_status: str
    status: str
    chapter_label: str
    notes: str
    lead: str = ""
    footer_left: str = FOOTER_LEFT
    body: dict[str, Any] = field(default_factory=dict)


def make_slide(
    order: int,
    *,
    title: str,
    shell: str,
    source_section: str,
    source_block: str,
    key_claim: str,
    chapter_label: str,
    lead: str = "",
    density: str = "medium",
    notes_intent: str = "",
    notes: str = "",
    body: dict[str, Any] | None = None,
) -> SlideSpec:
    return SlideSpec(
        order=order,
        slide_id=f"S{order:03d}",
        file_name=f"slide-{order:03d}.html",
        title=title,
        slide_type=SHELL_TO_TYPE[shell],
        layout=SHELL_TO_LAYOUT[shell],
        shell=shell,
        family=SHELL_TO_FAMILY[shell],
        density=density,
        source_section=source_section,
        source_block=source_block,
        key_claim=key_claim,
        notes_intent=notes_intent or key_claim,
        notes_status="ready",
        status="built",
        chapter_label=chapter_label,
        notes=notes or key_claim,
        lead=lead,
        body=body or {},
    )


def build_all_specs() -> list[SlideSpec]:
    specs = [
        make_slide(
            1,
            title="Harness를 설계하는 법",
            shell="title-hero-shell",
            source_section="00",
            source_block="00-00",
            key_claim="에이전트가 일할 환경 설계",
            chapter_label="OPENING",
            lead="챗봇과 싸우지 않고, 에이전트가 일할 환경을 설계하는 방법",
            density="light",
            notes_intent="첫 장에서 제목, 부제, 발표자만 고정",
            notes="제목과 부제만 두고, 발표자는 게임플랫폼 1팀 라승수로 표시한다.",
            body={"presenter": "게임플랫폼 1팀 라승수"},
        ),
        make_slide(
            2,
            title="시작하며",
            shell="process-flow-shell",
            source_section="00",
            source_block="00-01",
            key_claim="AI에게 무엇을 말할까에서 AI가 일할 환경 설계로 이동",
            chapter_label="OPENING",
            notes_intent="챗봇 사용 경험과 도구 수렴을 Harness 문제로 연결",
            notes="좋은 결과는 한 번의 프롬프트보다 반복 가능한 구조에서 나온다는 흐름을 고정한다.",
            body={
                "thesis": "개발자의 핵심 역량: AI에게 할 말 → AI가 안전하게 일할 환경",
                "steps": [
                    {"index": "01", "title": "챗봇과 말씨름", "text": "맥락 충돌과 반복 설명"},
                    {"index": "02", "title": "도구들의 수렴", "text": "자동완성·채팅 UI·터미널 에이전트"},
                    {"index": "03", "title": "Harness", "text": "규칙·컨텍스트·권한·검증·상태 기록"},
                ],
            },
        ),
        make_slide(
            3,
            title="전체 목차",
            shell="agenda-list-shell",
            source_section="00",
            source_block="00-03",
            key_claim="Harness 관점으로 읽는 9개 장",
            chapter_label="OPENING",
            density="heavy",
            notes_intent="00-overview의 목차 표를 한 장에 압축",
            notes="전체 표를 한 장으로 보여 주고, 다음 장부터 각 항목을 순서대로 펼친다.",
            body={
                "items": [
                    {"number": "01", "topic": "코딩은 어디로 가고 있는가", "text": "개발자의 숙련 이동"},
                    {"number": "02", "topic": "왜 Claude Code인가", "text": "AI 코딩 도구의 구조 수렴"},
                    {"number": "03", "topic": "AI 시대의 개발 방법론", "text": "TDD·SDD·Spec-first 재부상"},
                    {"number": "04", "topic": "Harness", "text": "Prompt 이후의 에이전트 운영 구조"},
                    {"number": "05", "topic": "한계와 실패 패턴", "text": "긴 작업·보안·신뢰 문제"},
                    {"number": "06", "topic": "멀티 에이전트", "text": "역할과 컨텍스트 분리"},
                    {"number": "07", "topic": "워크플로우와 도구", "text": "명령어·게이트·워크트리·이슈"},
                    {"number": "08", "topic": "제작 과정", "text": "발표 제작 파이프라인 해부"},
                    {"number": "09", "topic": "다음에 해야 할 일", "text": "개인과 팀의 첫 변화"},
                ]
            },
        ),
        make_slide(
            4,
            title="코딩은 사라지는가",
            shell="section-divider-shell",
            source_section="01",
            source_block="01-00",
            key_claim="개발의 추상화 수준 상승",
            chapter_label="CHAPTER 01",
            density="light",
            notes_intent="01장의 질문을 챕터 단위로 고정",
            notes="코딩이 사라지는가보다 개발자가 직접 붙들 일이 어디로 이동하는가를 묻는다.",
            body={"keywords": []},
        ),
        make_slide(
            5,
            title="기계어 → 어셈블리",
            shell="split-compare-shell",
            source_section="01",
            source_block="01-01",
            key_claim="이진 코드 직접 작성에서 명령어 기호로",
            chapter_label="CHAPTER 01",
            notes_intent="언어 발전의 첫 추상화 사례",
            notes="기계어의 이진 표현이 어셈블리 명령어로 올라오며 직접 다루는 부담이 줄어든다.",
            body={
                "left_label": "기계어",
                "left_code": CODE_MACHINE,
                "right_label": "어셈블리",
                "right_code": CODE_ASSEMBLY_MOV,
                "opinion": "기계어를 모르면 진짜 개발자 아님",
            },
        ),
        make_slide(
            6,
            title="어셈블리 → C/Pascal",
            shell="split-compare-shell",
            source_section="01",
            source_block="01-01",
            key_claim="레지스터와 syscall에서 함수와 컴파일러로",
            chapter_label="CHAPTER 01",
            notes_intent="어셈블리와 C/Pascal의 표현량 차이",
            notes="Hello World 수준에서도 어셈블리와 C의 표현량 차이가 명확하다.",
            body={
                "left_label": "어셈블리",
                "left_code": CODE_ASSEMBLY_HELLO,
                "right_label": "C/Pascal",
                "right_code": CODE_C_HELLO,
                "opinion": "어셈블리를 모르면 진짜 개발자 아님",
            },
        ),
        make_slide(
            7,
            title="C → Java",
            shell="split-compare-shell",
            source_section="01",
            source_block="01-01",
            key_claim="수동 메모리 관리에서 GC로",
            chapter_label="CHAPTER 01",
            notes_intent="메모리 관리 책임의 이동",
            notes="C의 malloc/free와 Java의 객체 생성 및 GC를 비교한다.",
            body={
                "left_label": "C",
                "left_code": CODE_C_POINT,
                "right_label": "Java",
                "right_code": CODE_JAVA_POINT,
                "opinion": "메모리 직접 관리 없는 개발은 장난",
            },
        ),
        make_slide(
            8,
            title="Java → Python",
            shell="split-compare-shell",
            source_section="01",
            source_block="01-01",
            key_claim="보일러플레이트 축소와 표현 밀도 상승",
            chapter_label="CHAPTER 01",
            notes_intent="Java와 Python의 boilerplate 차이",
            notes="같은 Hello World라도 Java와 Python의 표현 밀도는 크게 다르다.",
            body={
                "left_label": "Java",
                "left_code": CODE_JAVA_HELLO,
                "right_label": "Python",
                "right_code": CODE_PYTHON_HELLO,
                "opinion": "보일러플레이트 없는 언어는 장난감",
            },
        ),
        make_slide(
            9,
            title="AI 개발",
            shell="split-compare-shell",
            source_section="01",
            source_block="01-01",
            key_claim="자연어 지시에서 작업 위임으로",
            chapter_label="CHAPTER 01",
            notes_intent="언어 발전 사례의 현재형",
            notes="AI 개발은 개발의 종말이 아니라 추상화 수준 상승으로 읽어야 한다.",
            body={
                "left_label": "직접 작성",
                "left_points": ["대상 코드 탐색", "수정 지점 선택", "테스트 작성", "결과 검토"],
                "right_label": "AI 개발",
                "right_code": PROMPT_AI_REFACTOR,
                "opinion": "자연어 지시는 개발이 아님",
            },
        ),
        make_slide(
            10,
            title="직접 하던 일의 감소",
            shell="evidence-table-shell",
            source_section="01",
            source_block="01-02",
            key_claim="직접 작성 부담의 지속적 위임",
            chapter_label="CHAPTER 01",
            notes_intent="시대별 위임 표와 질문 반전",
            notes="시대별 전환을 표로 압축하고, 개발자가 끝까지 붙들 일이 어디로 이동하는지 묻는다.",
            body={
                "headers": ["시대", "전환", "위임한 것"],
                "rows": [
                    ["1950s", "기계어 → 어셈블리", "이진 코드"],
                    ["1960s", "어셈블리 → C", "명령어 최적화"],
                    ["1990s", "C/C++ → Java", "메모리 해제"],
                    ["2000s", "언어 → 프레임워크", "보일러플레이트"],
                    ["2010s", "온프레미스 → 클라우드", "서버 운영·확장"],
                    ["2020s", "직접 코딩 → AI 에이전트", "코드 작성 일부"],
                ],
                "question": "개발자가 끝까지 직접 붙들 일의 이동 위치",
            },
        ),
        make_slide(
            11,
            title="숫자로 보는 변화",
            shell="evidence-table-shell",
            source_section="01",
            source_block="01-03",
            key_claim="타이핑 비중 감소의 현장 신호",
            chapter_label="CHAPTER 01",
            notes_intent="숫자 근거를 대형 카드와 표로 압축",
            notes="YC W25, OpenAI Codex 팀, Meta 엔지니어 사례를 큰 숫자 중심으로 보여 준다.",
            body={
                "metrics": [
                    {"value": "25%", "label": "YC W25", "text": "95% 이상 AI 코드베이스"},
                    {"value": "100만 줄", "label": "OpenAI Codex", "text": "수동 코드 없이 프로덕트 완성"},
                    {"value": "3개월+", "label": "Meta", "text": "직접 타이핑 중단 사례"},
                ],
                "headers": ["신호", "규모", "의미"],
                "rows": [
                    ["YC W25", "25%", "AI 작성 비중"],
                    ["Codex 팀", "100만 줄", "수동 코딩 감소"],
                    ["Meta 사례", "3개월+", "역할 변화"],
                ],
            },
        ),
        make_slide(
            12,
            title="문서의 코드화",
            shell="evidence-table-shell",
            source_section="01",
            source_block="01-04",
            key_claim="문서의 실행 경로 편입",
            chapter_label="CHAPTER 01",
            notes_intent="문서 역할 변화와 규칙 파일 예시",
            notes="AI 코딩 도구에서 문서는 사람이 읽는 참고 자료를 넘어 에이전트가 따르는 운영 규칙이 된다.",
            body={
                "headers": ["파일", "역할", "에이전트 기준"],
                "rows": [
                    ["README", "사람의 입구", "프로젝트 방향"],
                    ["CLAUDE.md", "세션 운영", "작업 방식"],
                    ["AGENTS.md", "역할과 금지선", "우선순위"],
                    ["Cursor Rules", "도구별 규칙", "편집 기준"],
                    ["copilot-instructions", "반복 기준", "코드 생성 습관"],
                ],
            },
        ),
        make_slide(
            13,
            title="컨텍스트를 설계하는 능력",
            shell="split-compare-shell",
            source_section="01",
            source_block="01-05",
            key_claim="개발자의 역할은 환경 설계와 결과 판단으로 이동",
            chapter_label="CHAPTER 01",
            notes_intent="Harness Engineer의 핵심 역량",
            notes="문제 분해, 컨텍스트 선택, 수용 기준, 검증, 권한 경계가 새로운 핵심 역량이 된다.",
            body={
                "left_label": "이전 역할",
                "left_points": ["코드 직접 작성", "버그 수정", "문서 사후 정리"],
                "right_label": "새 역할",
                "right_points": ["문제 분해", "컨텍스트 선택", "수용 기준", "검증 gate", "권한 경계"],
            },
        ),
        make_slide(
            14,
            title="기초의 중요성",
            shell="statement-editorial-shell",
            source_section="01",
            source_block="01-06",
            key_claim="타이핑은 줄고 시스템 판단은 남는다",
            chapter_label="CHAPTER 01",
            density="light",
            notes_intent="01장 결론 전환",
            notes="AI가 더 많은 코드를 만들수록 기본기는 사라지지 않고 판단 책임으로 더 무거워진다.",
            body={
                "tag": "BASICS",
                "statement": "타이핑 감소, 시스템 판단 책임",
                "support": "인증·동시성·DB·캐시·보안·비용·배포",
                "chips": ["Architecture", "Security", "Operations"],
            },
        ),
    ]

    assert len(specs) == sum(SECTION_TARGETS.values()), len(specs)
    return specs


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    header_row = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    body_rows = ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join([header_row, separator, *body_rows])


def render_outline(specs: list[SlideSpec]) -> str:
    lines = [
        "# Slide Outline",
        "",
        "- status: 00/01 14-slide make-slide rebuild",
        "- canonical source: `docs/02-seminar/harness-rebuilt-md/00-overview.md`, `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`",
        "- output deck: `docs/03-html/deck/index.html`",
        "- output script: `docs/03-html/deck/script.md`",
        "- theme: `minimal-light`",
        "- runtime policy: single-file deck, keyboard navigation, touch/swipe, active slide switching, print CSS",
        "- rejected chrome: progress bar, fullscreen UI, slide counter UI, notes UI, keyboard hint",
        "",
        "## Section Targets",
        "",
        markdown_table(
            ["section", "source", "target slides"],
            [
                ["00", "`docs/02-seminar/harness-rebuilt-md/00-overview.md`", "3"],
                ["01", "`docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`", "11"],
            ],
        ),
        "",
        "## Slide Registry",
        "",
    ]

    for spec in specs:
        lines.extend(
            [
                f"### {spec.slide_id}. {spec.title}",
                f"- file: `docs/03-html/slides/{spec.file_name}`",
                f"- slide type: `{spec.slide_type}`",
                f"- layout: `{spec.layout}`",
                f"- shell: `{spec.shell}`",
                f"- source section: `{spec.source_section}`",
                f"- source paragraph block: `{spec.source_block}`",
                f"- key claim: {spec.key_claim}",
                f"- notes intent: {spec.notes_intent}",
                f"- notes status: `{spec.notes_status}`",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def render_manifest(specs: list[SlideSpec]) -> str:
    rows = [
        [
            str(spec.order),
            f"`{spec.slide_id}`",
            f"`{spec.file_name}`",
            spec.title,
            f"`{spec.slide_type}`",
            f"`{spec.layout}`",
            f"`{spec.shell}`",
            f"`{spec.source_section}`",
            f"`{spec.source_block}`",
            f"`{spec.notes_status}`",
            spec.status,
        ]
        for spec in specs
    ]

    return "\n".join(
        [
            "# HTML Manifest",
            "",
            "- current status: 00/01 14-slide deck built",
            "- active theme: `theme-minimal-light`",
            "- slide id format: `S001`-`S014`",
            "- slide file format: `slide-001.html`-`slide-014.html`",
            "- output deck: `docs/03-html/deck/index.html`",
            "- output script: `docs/03-html/deck/script.md`",
            "",
            "## Slide Registry",
            "",
            markdown_table(
                [
                    "order",
                    "slide id",
                    "file",
                    "title",
                    "slide type",
                    "layout",
                    "shell",
                    "source section",
                    "source paragraph block",
                    "notes status",
                    "status",
                ],
                rows,
            ),
            "",
        ]
    )


def render_script(specs: list[SlideSpec]) -> str:
    parts = [
        "# Seminar Script",
        "",
        "- target deck: `docs/03-html/deck/index.html`",
        "- scope: 00 overview + 01 chapter",
        "",
    ]
    for spec in specs:
        parts.extend(
            [
                f"## {spec.slide_id} {spec.title}",
                f"- intent: {spec.notes_intent}",
                f"- opening: {spec.key_claim}",
                f"- bridge: {spec.notes}",
                "",
            ]
        )
    return "\n".join(parts).rstrip() + "\n"


def attr_escape(text: str) -> str:
    return html.escape(text, quote=True)


def render_footer(spec: SlideSpec) -> str:
    return (
        '<footer class="footer">'
        f'<span class="footer-left">{html.escape(spec.footer_left)}</span>'
        f'<span class="footer-right">{spec.order}</span>'
        "</footer>"
    )


def render_tool_icons() -> str:
    return (
        '<aside class="tool-icons" aria-label="toolchain">'
        '<span class="tool-icon tool-icon-claude" aria-label="claude-code">'
        '<svg viewBox="0 0 24 24" aria-hidden="true">'
        '<path d="M12 3.5v17M3.5 12h17M6 6l12 12M18 6 6 18"/>'
        "</svg>"
        "</span>"
        '<span class="tool-icon tool-icon-codex" aria-label="codex">'
        '<svg viewBox="0 0 24 24" aria-hidden="true">'
        '<path d="M12 3.5 19.5 8v8L12 20.5 4.5 16V8Z"/>'
        '<path d="M8.5 9.5 12 7.5l3.5 2v5L12 16.5l-3.5-2Z"/>'
        "</svg>"
        "</span>"
        '<span class="tool-icon tool-icon-opencode" aria-label="opencode">'
        '<svg viewBox="0 0 24 24" aria-hidden="true">'
        '<path d="m9 6-5 6 5 6M15 6l5 6-5 6M13 4 11 20"/>'
        "</svg>"
        "</span>"
        "</aside>"
    )


def render_lead(lead: str) -> str:
    return f'<p class="lead-placeholder">{html.escape(lead)}</p>' if lead else ""


def render_short_line(lead: str) -> str:
    return f'<p class="short-line">{html.escape(lead)}</p>' if lead else ""


def render_code_block(code: str) -> str:
    return f'<pre class="code-block"><code>\n{html.escape(code)}\n</code></pre>'


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
            '<section class="agenda-header">'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f"{render_lead(spec.lead)}"
            "</section>"
            f'<ol class="agenda-list">{items}</ol>'
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
        chips = "".join(f'<li class="statement-chip">{html.escape(chip)}</li>' for chip in spec.body.get("chips", []))
        return (
            '<section class="statement-panel">'
            f'<p class="statement-tag">{html.escape(spec.body.get("tag", spec.chapter_label))}</p>'
            f'<h1 class="statement-text">{html.escape(spec.body.get("statement", spec.key_claim))}</h1>'
            f'<p class="statement-support">{html.escape(spec.body.get("support", spec.lead))}</p>'
            f'<ul class="statement-chips">{chips}</ul>'
            "</section>"
        )

    if spec.shell == "process-flow-shell":
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
            thesis = f'<p class="flow-thesis">{html.escape(spec.body["thesis"])}</p>'
        return (
            '<section class="top-band">'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f"{render_lead(spec.lead)}"
            "</section>"
            '<section class="body-area flow-body">'
            f'<ol class="process-track">{steps}</ol>'
            f"{thesis}"
            "</section>"
        )

    if spec.shell == "split-compare-shell":
        left_content = render_compare_content(spec, "left")
        right_content = render_compare_content(spec, "right")
        opinion = ""
        if spec.body.get("opinion"):
            opinion = f'<p class="negative-opinion">{html.escape(spec.body["opinion"])}</p>'
        return (
            '<section class="top-band">'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f"{render_lead(spec.lead)}"
            "</section>"
            '<section class="compare-grid">'
            '<article class="compare-col">'
            f'<p class="compare-label">{html.escape(spec.body.get("left_label", "축 A"))}</p>'
            f"{left_content}"
            "</article>"
            '<article class="compare-col is-focus">'
            f'<p class="compare-label">{html.escape(spec.body.get("right_label", "축 B"))}</p>'
            f"{right_content}"
            "</article>"
            "</section>"
            f"{opinion}"
        )

    if spec.shell == "evidence-table-shell":
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
    return (
        f'<main class="slide family-{spec.family} layout-{spec.layout} density-{spec.density}" '
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
<title>Harness를 설계하는 법</title>
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


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def clean_generated_slides() -> None:
    SLIDES_ROOT.mkdir(parents=True, exist_ok=True)
    for path in SLIDES_ROOT.glob("slide-*.html"):
        path.unlink()


def main() -> None:
    specs = build_all_specs()
    clean_generated_slides()

    for spec in specs:
        write(SLIDES_ROOT / spec.file_name, render_slide_file(spec))

    write(OUTLINE_PATH, render_outline(specs))
    write(MANIFEST_PATH, render_manifest(specs))
    write(SCRIPT_PATH, render_script(specs))
    write(DECK_PATH, render_deck(specs))
    write(DATA_PATH, json.dumps([asdict(spec) for spec in specs], ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
