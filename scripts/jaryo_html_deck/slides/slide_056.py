from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        56,
        title="왜 하나의 에이전트만으로는 부족한가",
        shell="evidence-table-shell",
        source_section="06",
        source_block="06-01",
        key_claim="멀티 에이전트는 세 가지 벽을 줄이기 위한 구조",
        chapter_label="CHAPTER 06",
        notes_intent="단일 에이전트의 세 가지 문제를 3-card 구조로 압축",
        notes="source lines 3-11, page 063 structure-only reference",
        body={
            "variant": "chapter-wall-cards",
            "cards": [
                {
                    "index": "01",
                    "title": "컨텍스트의 벽",
                    "text": "탐색·구현·로그 분석·리뷰·문서 작성이 같은 창에 쌓임",
                    "evidence": "무관한 정보가 판단을 오염",
                },
                {
                    "index": "02",
                    "title": "역할의 벽",
                    "text": "계획·구현·리뷰·테스트 해석이 한 손에 집중",
                    "evidence": "자기 답을 자기가 채점",
                },
                {
                    "index": "03",
                    "title": "신뢰성의 벽",
                    "text": "탐색만 해야 하는 작업에 쓰기 권한까지 열림",
                    "evidence": "민감 데이터를 볼 필요가 없는 작업까지 전체 컨텍스트 수신",
                },
            ],
            "conclusion": "멀티 에이전트는 이 문제를 줄이기 위한 구조",
        },
    )
