from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        42,
        title="RAG vs Context Hub",
        shell="evidence-table-shell",
        source_section="04",
        source_block="04-08",
        key_claim="넓게 찾는가, 지금 맞는 문서를 지정하는가",
        chapter_label="CHAPTER 04",
        notes_intent="RAG 논문과 MCP/Context Hub 문서 조사 기반 비교",
        notes="RAG는 넓은 검색 인덱스, Context Hub MCP는 최신/버전 지정 문서 주입",
        body={
            "variant": "rag-context-researched",
            "cards": [
                {
                    "label": "RAG",
                    "title": "넓은 저장소에서 passage 검색",
                    "items": [
                        "질문마다 관련 조각을 생성 입력에 주입",
                        "벡터 인덱스와 retriever 품질이 결과를 좌우",
                        "내부 위키·정책·긴 참고 자료에 적합",
                    ],
                },
                {
                    "label": "Context Hub MCP",
                    "title": "지정한 최신 문서를 컨텍스트로 주입",
                    "items": [
                        "공식·버전별 API 문서를 필요할 때 가져옴",
                        "라이브러리 ID·버전·언어로 범위를 좁힘",
                        "SDK/API 변경이 잦은 작업에 적합",
                    ],
                },
            ],
            "decision_label": "선택 기준",
            "decision": "넓게 찾을 때는 RAG, 지금 맞는 문서를 확인할 때는 Context Hub",
            "source_label": "Sources: Lewis et al. 2020 · MCP Docs · Context Hub / Context7",
        },
    )
