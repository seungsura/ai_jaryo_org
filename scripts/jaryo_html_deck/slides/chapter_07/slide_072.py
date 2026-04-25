from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        72,
        title="반복의 자산화",
        shell="process-flow-shell",
        source_section="07",
        source_block="07-06",
        key_claim="반복되는 지침은 시스템 바깥에 있어야 할 지식",
        chapter_label="CHAPTER 07",
        notes_intent="/context, /compact, /clear와 Skills/Hooks/Commands/AGENTS mapping",
        notes="source lines 86-102, page 066/067 split reference",
        body={
            "variant": "chapter-command-artifacts",
            "commands": [
                {"index": "/context", "title": "지금 무엇이 얼마나 쌓였는지", "text": "컨텍스트 확인"},
                {"index": "/compact", "title": "이어갈 결정과 상태만", "text": "압축"},
                {"index": "/clear", "title": "다른 작업으로 넘어갈 때", "text": "세션 비움"},
            ],
            "artifacts": [
                {"title": "Skills", "text": "반복 지시"},
                {"title": "Hooks", "text": "우회하면 안 되는 규칙"},
                {"title": "Custom Commands", "text": "자주 쓰는 루프"},
                {"title": "CLAUDE.md / AGENTS.md", "text": "프로젝트 공통 기준"},
                {"title": "이슈나 진행 파일", "text": "특정 태스크의 상태"},
            ],
            "conclusion": "개인 메모에서 리포지토리와 팀 설정으로 올라가면 표준이 됩니다",
        },
    )
