from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        93,
        title="증폭되는 경험 - 세 개의 증언",
        shell="statement-editorial-shell",
        source_section="09",
        source_block="09-02",
        key_claim="AI 시대의 경험 - 축소가 아니라 증폭",
        chapter_label="CHAPTER 09",
        notes_intent="Page 085 testimony cards and bottom support line",
        notes="source 09 lines 9-17; canonical Page 085",
        body={
            "variant": "experience-testimony",
            "lead": "세 사람이 거의 같은 말을 한다.",
            "cards": [
                {
                    "speaker": "KENT BECK",
                    "role": "TDD 창시자 · 52년",
                    "quote": "프로그래밍은 여전히 프로그래밍이고, AI는 더 중요한 결정을 더 빨리 내리게 하는 도구다",
                },
                {
                    "speaker": "SIMON WILLISON",
                    "role": "Vibe Engineering",
                    "quote": "AI는 기존 전문성을 증폭한다. 경험이 많을수록 더 빠르고 더 좋은 결과를 얻는다",
                },
                {
                    "speaker": "MARTIN FOWLER",
                    "role": "Thoughtworks",
                    "quote": "AI는 주니어의 산출물은 복제할 수 있어도 시니어의 경험과 판단은 복제하지 못한다",
                },
            ],
            "statement": "AI 시대의 경험 - 축소가 아니라 증폭",
            "support": "Spec-first · TDD · Plan-Critic · 검증 분리",
        },
    )
