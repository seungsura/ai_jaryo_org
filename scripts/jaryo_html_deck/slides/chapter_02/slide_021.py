from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide

def build() -> SlideSpec:
    return make_slide(
        21,
        title="2막: Cursor와 컨텍스트의 시대",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-06",
        key_claim="현재 파일에서 전체 코드베이스로",
        chapter_label="CHAPTER 02",
        notes_intent="초기 Copilot과 Cursor 계열 도구 비교",
        notes="source markdown의 Cursor 비교 표, Tools 문장, Context Engineering 문단",
        body={
            "variant": "cursor-tools",
            "left": {
                "title": "초기 Copilot",
                "items": ["현재 파일 중심", "검색 없음 또는 제한", "한 줄 또는 한 블록"],
            },
            "right": {
                "title": "Cursor 계열 도구",
                "items": ["전체 코드베이스", "RAG · AST · 시맨틱 검색", "멀티파일 수정과 Tools"],
            },
            "tools": ["채팅", "Composer", "Agent Mode", "Context Engineering"],
        },
    )
