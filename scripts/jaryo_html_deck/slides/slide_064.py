from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        64,
        title="Sub-Agent와 Agent Team은 다르다",
        shell="evidence-table-shell",
        source_section="06",
        source_block="06-09",
        key_claim="단순한 심부름은 Sub-Agent, 양방향 토론은 Agent Team",
        chapter_label="CHAPTER 06",
        notes_intent="source table을 그대로 비교 표로 구성",
        notes="source lines 128-138, page 065 reference",
        body={
            "variant": "chapter-split-panels",
            "cards": [
                {
                    "title": "Sub-Agent",
                    "text": "메인이 작업을 던지고 결과를 받음 / 제한 범위, 요약 반환",
                    "evidence": "단방향 통신 / 로그 파싱, 파일 탐색, 단일 검증 / 낮은 요약 품질",
                },
                {
                    "title": "Agent Team",
                    "text": "서로 대화하며 수렴 / 별도 컨텍스트와 공유 맥락",
                    "evidence": "양방향 통신 / 관점 충돌, 기획, 아키텍처 토론 / 수렴 실패",
                },
            ],
            "conclusion": "양방향 토론이 필요한 경우에만 Agent Team",
        },
    )
