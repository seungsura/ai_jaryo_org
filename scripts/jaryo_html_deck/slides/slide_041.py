from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        41,
        title="MCP와 Context Hub",
        shell="process-flow-shell",
        source_section="04",
        source_block="04-07",
        key_claim="연결 방식을 표준화",
        chapter_label="CHAPTER 04",
        notes_intent="MCP native architecture와 Context Hub 연결 의미",
        notes="외부 도구와 최신 문서 연결은 컨텍스트 엔지니어링의 핵심 인프라",
        body={
            "variant": "mcp-context-architecture",
            "flow": [
                {"title": "에이전트", "text": "필요한 외부 컨텍스트 판단"},
                {"title": "MCP 클라이언트", "text": "서버 연결과 결과 형식 유지"},
                {"title": "MCP 서버", "text": "외부 도구·데이터 소스 제공"},
            ],
            "tools": ["GitHub", "Slack", "DB", "Filesystem", "Internal API"],
            "usage_note": "도구 결과가 컨텍스트 윈도우로 돌아와 다음 판단의 재료가 됨",
            "hub_title": "최신 문서를 읽힌 뒤 답하게 하는 통로",
            "principles": [
                {"label": "역할", "text": "최신 API 문서와 공식 자료를 필요할 때 가져옴"},
                {"label": "원리", "text": "모델 기억 대신 지금 기준 문서를 컨텍스트로 주입"},
                {"label": "효과", "text": "호출 방식과 결과 형식이 안정화"},
            ],
        },
    )
