from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        16,
        title="에이전틱 코딩의 실제 성과",
        shell="evidence-table-shell",
        source_section="02",
        source_block="02-01",
        key_claim="속도, 온보딩, 불가능하던 작업의 변화",
        chapter_label="CHAPTER 02",
        notes_intent="page-017 reference 기반 성과 metric cards",
        notes="source markdown의 에이전틱 코딩 실제 성과와 page-017 reference",
        body={
            "variant": "metric-impact-cards",
            "reference": "tall",
            "cards": [
                {
                    "value": "2주",
                    "label": "CTO 추정 4~8개월",
                    "text": "프로젝트 완료",
                    "meta": "카카오 AI 팀 내부 공유 사례",
                },
                {
                    "value": "1~2일",
                    "label": "신규 개발자 온보딩",
                    "text": "기존 수주~수개월에서 단축",
                    "meta": "첫날부터 의미 있는 기여",
                },
                {
                    "value": "불가능하던 작업 실현",
                    "label": "기술 부채 해결",
                    "text": "즉각 피드백과 작업 실현",
                    "meta": "문서화된 작업 환경",
                },
            ],
        },
    )
