from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        26,
        title="3막: 하네스의 시대",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-09",
        key_claim="작업 환경 전체를 품기 시작한 코딩 도구",
        chapter_label="CHAPTER 02",
        notes_intent="Harness era signs without chapter 4 mechanics",
        notes="source markdown의 Claude Code 구성 요소와 하네스 시대 전환",
        body={
            "variant": "harness-era-signs",
            "statement": "작업 환경 전체를 품기 시작한 코딩 도구",
            "cards": [
                {"title": "터미널 네이티브", "text": "파일 읽기 · 셸 실행 · 테스트 확인"},
                {"title": "구성 요소의 묶음", "text": "독립 기능이 실행 환경으로 결합"},
                {"title": "내 환경에 맞는 도구", "text": "플러그인 · 스킬 · 노하우 · 교육자료"},
            ],
            "components": ["Plan Mode", "승인 체계", "CLAUDE.md", "Skills", "Hooks", "MCP", "Plugins", "Subagents"],
        },
    )
