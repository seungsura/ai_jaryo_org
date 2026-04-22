from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        24,
        title="Cursor 아키텍처",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-07",
        key_claim="긴 프롬프트가 아니라 검색기와 편집기",
        chapter_label="CHAPTER 02",
        notes_intent="Cursor architecture native system map",
        notes="source markdown의 Cursor 아키텍처 text diagram과 approved 06 asset 구조",
        body={
            "variant": "cursor-architecture-native",
            "request": "사용자 요청",
            "index": "파일 · 심볼 · AST · 문서",
            "context": "관련 파일 · 규칙 · 히스토리",
            "tools": ["채팅", "Composer", "Agent Mode", "명령 실행"],
            "feedback": "verify",
            "steps": [
                {"index": "01", "title": "사용자 요청", "text": "질문 자체의 전환"},
                {"index": "02", "title": "indexing", "text": "파일 · 심볼 · AST · 문서"},
                {"index": "03", "title": "retrieval", "text": "관련 파일 · 규칙 · 히스토리"},
                {"index": "04", "title": "context assembly", "text": "필요 정보 선별"},
                {"index": "05", "title": "edit/run", "text": "편집과 명령 실행"},
                {"index": "06", "title": "verify", "text": "테스트 · 린트 · 로그"},
            ],
        },
    )
