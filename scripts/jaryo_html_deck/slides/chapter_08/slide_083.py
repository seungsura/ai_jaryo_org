from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        83,
        title="재료 1 source 수집",
        shell="evidence-table-shell",
        source_section="08",
        source_block="08-03",
        key_claim="불확실한 부분은 억지로 메우지 않았습니다",
        chapter_label="CHAPTER 08",
        notes_intent="source 계층과 중요도 분리",
        notes="source 08 lines 32-38; canonical Page 078",
        body={
            "variant": "source-boundary-cards",
            "cards": [
                {
                    "value": "유튜브 · 링크드인 · 인터넷 커뮤니티",
                    "label": "자료 수집",
                    "text": "서로 다른 계층",
                },
                {
                    "value": "공식 사이트 · 공개 문헌",
                    "label": "자료 수집",
                    "text": "서로 다른 중요도",
                },
                {
                    "value": "직접 수집한 마크다운 · PDF",
                    "label": "자료 수집",
                    "text": "불확실한 부분을 억지로 메우지 않는 구분",
                },
            ],
        },
    )
