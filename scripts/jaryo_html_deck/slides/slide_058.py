from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        58,
        title="1. Sub-Agent: 중간 작업을 격리하는 기본형",
        shell="process-flow-shell",
        source_section="06",
        source_block="06-03",
        key_claim="서브 에이전트는 메인 컨텍스트를 지키는 격리 패턴",
        chapter_label="CHAPTER 06",
        notes_intent="Main -> Sub-Agent -> summary 흐름과 least privilege 원칙",
        notes="source lines 28-51, page 066 structure reference",
        body={
            "variant": "chapter-map-side",
            "main": {"title": "Main", "text": "결과 요약과 결론만 수신"},
            "sub": {"title": "Sub", "text": "격리된 워커"},
            "artifacts": ["file", "log", "test", "api"],
            "side_cards": [
                {"title": "컨텍스트 격리", "text": "파일을 많이 읽고 수만 토큰을 써도 메인 컨텍스트는 오염되지 않음"},
                {"title": "least privilege", "text": "필요한 파일, 질문, 출력 형식, 권한만 전달"},
                {"title": "좋은 지시", "text": "목적, 읽을 범위, 출력 형식, 근거 표시 방식, 금지 행동"},
            ],
            "conclusion": "Sub-Agent는 메인 컨텍스트를 지키는 데 특히 강함",
        },
    )
