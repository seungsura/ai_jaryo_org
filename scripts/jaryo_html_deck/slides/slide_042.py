from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        42,
        title="RAG vs Context 7",
        shell="evidence-table-shell",
        source_section="04",
        source_block="04-08",
        key_claim="검색 범위와 기준 시점의 차이",
        chapter_label="CHAPTER 04",
        notes_intent="RAG와 Context 7의 차이를 표로 비교",
        notes="RAG는 넓은 저장소 검색, Context 7은 최신/버전 지정 문서 확인",
        body={
            "variant": "rag-context-table",
            "columns": ["구분", "RAG", "Context 7"],
            "rows": [
                {
                    "axis": "대상",
                    "rag": "문서 저장소에서 검색된 관련 조각",
                    "context": "지정한 최신 문서나 공식 자료",
                },
                {
                    "axis": "강점",
                    "rag": "내부 위키, 정책 문서, 긴 참고 자료를 넓게 훑음",
                    "context": "최신 SDK, API, 변경이 잦은 공식 문서를 지금 기준으로 확인",
                },
                {
                    "axis": "기대",
                    "rag": "넓은 문서 집합에서 필요한 맥락을 찾음",
                    "context": "출처와 기준 시점이 더 분명함",
                },
                {
                    "axis": "문제점",
                    "rag": "오래된 조각, 낮은 관련도, 중복 정보가 섞일 수 있음",
                    "context": "연결 실패나 잘못된 소스 지정에 바로 흔들림",
                },
            ],
        },
    )
