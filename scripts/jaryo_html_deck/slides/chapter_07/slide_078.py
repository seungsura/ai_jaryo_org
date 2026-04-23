from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        78,
        title="첫 주에 바로 세울 수 있는 최소 워크플로우",
        shell="evidence-table-shell",
        source_section="07",
        source_block="07-12",
        key_claim="대화창의 기준을 작업 환경의 일부로 만드는 첫 단계",
        chapter_label="CHAPTER 07",
        notes_intent="six minimal habits",
        notes="source lines 173-182",
        body={
            "variant": "chapter-principle-grid",
            "cards": [
                {"index": "01", "title": "CLAUDE.md / AGENTS.md", "text": "반복 지시 세 가지"},
                {"index": "02", "title": "위험 명령 차단", "text": "훅이나 승인 규칙"},
                {"index": "03", "title": "lint / type check", "text": "필수 게이트 하나"},
                {"index": "04", "title": "이슈 하나와 Worktree 하나", "text": "긴 작업 묶기"},
                {"index": "05", "title": "계획과 승인", "text": "구현 전 계획, 승인 후 수정"},
                {"index": "06", "title": "결정과 남은 일", "text": "파일이나 이슈에 남김"},
            ],
            "conclusion": "대화창에 떠다니는 기준을 작업 환경의 일부로 만드는 첫 단계",
        },
    )
