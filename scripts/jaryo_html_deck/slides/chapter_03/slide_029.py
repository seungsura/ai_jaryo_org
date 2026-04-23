from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        29,
        title="TDD (Test-Driven Development)",
        shell="statement-editorial-shell",
        source_section="03",
        source_block="03-03",
        key_claim="테스트를 먼저 쓰고, 통과하는 코드를 나중에 쓴다",
        chapter_label="CHAPTER 03",
        lead="테스트를 먼저 쓰고, 통과하는 코드를 나중에 쓴다. AI 시대에는 인간이 테스트, AI가 구현.",
        notes_intent="Page 028 TDD lead와 anti-cheat 규칙",
        notes="테스트가 에이전트의 자유를 제한하는 통제선",
        body={
            "variant": "tdd-control-layers",
            "flow": [
                {"title": "Red", "text": "인간이 실패 테스트 작성"},
                {"title": "Green", "text": "AI가 통과 코드 구현"},
                {"title": "Refactor", "text": "인간 리뷰 → AI가 리팩토링"},
            ],
            "controls": [
                {
                    "title": "왜 AI에게 특히 중요한가",
                    "text": 'AI는 "동작하는 것 같은" 코드를 자신 있게 만듦. 테스트 없으면 맞는지 틀린지 확인 불가.',
                },
                {
                    "title": "AI의 치팅에 주의",
                    "text": "테스트 수정 금지 규칙 필수. 테스트 코드 임의 수정 금지 · assert 조건 약화 · 실패 확인 전 구현 금지.",
                },
            ],
        },
    )
