from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        63,
        title="설계 원칙: 패턴보다 경계가 중요하다",
        shell="evidence-table-shell",
        source_section="06",
        source_block="06-10",
        key_claim="컨텍스트, 역할, 검증을 쪼개는 경계 설계",
        chapter_label="CHAPTER 06",
        notes_intent="다섯 설계 원칙을 source 문구로 카드화",
        notes="source lines 142-162, page 068 reference",
        body={
            "variant": "chapter-principle-grid",
            "cards": [
                {"index": "01", "title": "필요한 것만 받기", "text": "컨텍스트를 많이 주는 것은 친절이 아님"},
                {"index": "02", "title": "역할과 금지 행동", "text": "무엇을 하고 무엇을 안 하는지 먼저 결정"},
                {"index": "03", "title": "출력 계약 구조화", "text": "완료 기준과 반환 형식을 먼저 고정"},
                {"index": "04", "title": "생성자와 검증자 분리", "text": "자기 결과를 자기가 통과시키지 않기"},
                {"index": "05", "title": "중단 조건과 수렴 조건", "text": "몇 번 재시도할지, 언제 넘길지 미리 정하기"},
            ],
            "conclusion": "패턴 이름보다 중요한 것은 경계 설계",
        },
    )
