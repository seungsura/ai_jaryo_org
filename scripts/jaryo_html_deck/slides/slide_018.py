from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        18,
        title="1막: Copilot과 ChatGPT, 프롬프트의 시대",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-02",
        key_claim="자동완성에서 자연어 지시 인터페이스로",
        chapter_label="CHAPTER 02",
        notes_intent="프롬프트 시대의 출발점 비교",
        notes="source markdown의 초기 Copilot과 ChatGPT 전환",
        body={
            "variant": "prompt-era",
            "range": "2022~2024",
            "stages": [
                {
                    "title": "GitHub Copilot",
                    "text": "현재 파일 기반 다음 줄 제안",
                    "items": ["현재 파일", "암묵적 프롬프트", "자동완성"],
                },
                {
                    "title": "ChatGPT",
                    "text": "자연어 지시 기반 코드 생성",
                    "items": ["역할 부여", "예시", "단계별 요청"],
                },
            ],
            "thesis": "자연어 지시문이 새로운 프로그래밍 인터페이스처럼 보이던 시기",
        },
    )
