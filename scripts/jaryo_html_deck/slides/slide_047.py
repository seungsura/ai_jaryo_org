from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        47,
        title="오류의 나비효과",
        shell="evidence-table-shell",
        source_section="05",
        source_block="05-01",
        key_claim="작은 오류가 다음 단계로 번진다",
        chapter_label="CHAPTER 05",
        notes_intent="작은 오해가 루프 전체로 누적되는 구조",
        notes="읽기-수정-실행-판단 루프와 단계별 성공률",
        body={
            "headers": ["단계 수", "전체 성공률"],
            "rows": [
                ["1 단계", "95%"],
                ["5 단계", "77%"],
                ["10 단계", "60%"],
                ["20 단계", "36%"],
                ["50 단계", "8%"],
            ],
            "callout": "계획 > 탐색 > 작성 > 테스트 > 수정 > 커밋",
            "question": "20 단계만 가도 2/3이 실패",
        },
    )
