from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        1,
        title="Harness 잘 사용하기",
        shell="title-hero-shell",
        source_section="00",
        source_block="00-00",
        key_claim="에이전트가 일할 환경 설계",
        chapter_label="OPENING",
        lead="챗봇과 싸우지 않고, 에이전트가 일할 환경을 설계하는 방법",
        density="light",
        notes_intent="첫 장에서 제목, 부제, 발표자만 고정",
        notes="제목과 부제만 두고, 발표자는 게임플랫폼 1팀 라승수로 표시한다.",
        body={"presenter": "게임플랫폼 1팀 라승수"},
    )
