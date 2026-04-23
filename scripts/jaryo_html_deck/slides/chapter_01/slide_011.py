from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        11,
        title="숫자로 보는 변화",
        shell="evidence-table-shell",
        source_section="01",
        source_block="01-03",
        key_claim="수동 코드 작성 비중 감소의 현장 신호",
        chapter_label="CHAPTER 01",
        notes_intent="source 숫자 사실만 압축",
        notes="source markdown의 YC W25, OpenAI Codex 팀, Meta 엔지니어 사례",
        body={
            "variant": "evidence-cards",
            "cards": [
                {"value": "25%", "label": "YC W25", "text": "코드베이스 95% 이상 AI"},
                {"value": "100만 줄", "label": "OpenAI Codex 팀", "text": "수동 코드 한 줄 없음"},
                {"value": "3개월+", "label": "Meta 엔지니어", "text": "직접 코드 타이핑 없음"},
            ],
        },
    )
