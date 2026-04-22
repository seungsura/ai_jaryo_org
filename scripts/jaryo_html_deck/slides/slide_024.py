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
        notes_intent="Cursor architecture raw asset with source-backed arrow flow",
        notes="사용자 승인 예외: approved 06 asset raw embed + source text arrow graph",
        body={
            "variant": "cursor-architecture-asset",
            "asset": "assets/evolution-of-ai-agentic-patterns/06-cursor-ai-code-editor-architecture.png",
            "flow": [
                {"title": "사용자 요청"},
                {"title": "코드베이스 인덱싱", "detail": "(파일, 심볼, AST, 문서)"},
                {"title": "관련 파일 / 규칙 / 히스토리 검색"},
                {"title": "컨텍스트 조립"},
                {"title": "Composer / Agent Mode"},
                {"title": "멀티파일 수정 + 명령 실행"},
                {"title": "테스트 / 린트 / 로그 확인"},
            ],
        },
    )
