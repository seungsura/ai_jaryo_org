from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        73,
        title="Approval, Auto-accept, Plan Mode",
        shell="evidence-table-shell",
        source_section="07",
        source_block="07-05",
        key_claim="위험도에 따라 모드를 나눔",
        chapter_label="CHAPTER 07",
        notes_intent="source table exact-mode mapping",
        notes="source lines 73-82",
        body={
            "variant": "chapter-risk-matrix",
            "cards": [
                {
                    "index": "01",
                    "title": "문서 초안, 로그 요약",
                    "text": "비교적 넓은 자율성",
                    "evidence": "실패 비용이 낮고 되돌리기 쉬움",
                },
                {
                    "index": "02",
                    "title": "테스트 보강, 작은 리팩터링",
                    "text": "제한적 auto-accept + 검증",
                    "evidence": "반복 작업이지만 검증 필요",
                },
                {
                    "index": "03",
                    "title": "아키텍처 변경, DB 마이그레이션",
                    "text": "Plan Mode + 승인",
                    "evidence": "잘못되면 비용이 큼",
                },
                {
                    "index": "04",
                    "title": "삭제, 배포, 권한 변경",
                    "text": "수동 승인 필수",
                    "evidence": "상태 변경과 사고 위험이 큼",
                },
            ],
            "conclusion": "작업별로 신뢰 수준을 조절하는 구조",
        },
    )
