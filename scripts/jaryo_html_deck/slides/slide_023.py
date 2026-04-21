from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide

def build() -> SlideSpec:
    return make_slide(
        23,
        title="Cursor 아키텍처",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-07",
        key_claim="긴 프롬프트가 아니라 검색기와 편집기",
        chapter_label="CHAPTER 02",
        notes_intent="Cursor architecture asset and process",
        notes="source markdown의 Cursor 아키텍처 text diagram과 02-v04 asset",
        body={
            "variant": "cursor-architecture-native",
            "request": "사용자 요청",
            "index": "파일 · 심볼 · 문서 · PR",
            "context": "관련 파일 · 규칙 · 변경 이력",
            "tools": ["SearchCode", "Read", "EditFile", "명령 실행"],
            "feedback": "테스트 · 린트 · 로그 확인",
            "steps": [
                {"index": "01", "title": "인덱싱", "text": "파일 · 심볼 · AST · 문서"},
                {"index": "02", "title": "검색", "text": "파일 · 규칙 · 히스토리"},
                {"index": "03", "title": "조립", "text": "Composer · Agent Mode"},
                {"index": "04", "title": "수정·실행", "text": "멀티파일 수정 · 명령 실행"},
                {"index": "05", "title": "검증", "text": "테스트 · 린트 · 로그"},
            ],
        },
    )
