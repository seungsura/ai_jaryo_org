from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        46,
        title="작업이 길어질 때 특히 위험한 이유",
        shell="statement-editorial-shell",
        source_section="05",
        source_block="05-02",
        key_claim="작업이 길어질수록 기준이 달라진다",
        chapter_label="CHAPTER 05",
        notes_intent="첫 번째 결과물에서 20 단계 결과물까지의 성공률 하락",
        notes="1 단계 95%에서 20 단계 36%로 내려가는 카드형 진행",
        body={
            "variant": "progression-card-map",
            "cards": [
                {"step": "1 단계", "percent": "95%", "result": "첫 번째 결과물"},
                {"step": "5 단계", "percent": "77%", "result": "5 단계 결과물"},
                {"step": "10 단계", "percent": "60%", "result": "10 단계 결과물"},
                {"step": "20 단계", "percent": "36%", "result": "20 단계 뒤 결과물"},
            ],
            "gates": [
                "작업 분해",
                "검증",
                "고정 지점",
            ],
        },
    )
