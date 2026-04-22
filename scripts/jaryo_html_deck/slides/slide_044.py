from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        44,
        title="Stable Prefix와 Variable Suffix",
        shell="split-compare-shell",
        source_section="04",
        source_block="04-10",
        key_claim="잘 쓰는 것 못지않게 안 바꾸는 것도 능력",
        chapter_label="CHAPTER 04",
        notes_intent="prefix/suffix diagram",
        notes="자주 변하지 않는 것은 앞쪽에, 최신 입력과 도구 결과는 뒤쪽에 둠",
        body={
            "variant": "prefix-suffix-cache",
            "left_label": "Stable Prefix",
            "left_badges": ["KV-cache", "고정", "재사용"],
            "left_points": ["시스템 프롬프트", "도구 정의", "장기 규칙"],
            "left_note": "앞쪽의 안정 접두어",
            "right_label": "Variable Suffix",
            "right_badges": ["동적 접미어", "갈아 끼움"],
            "right_points": ["최신 사용자 입력", "도구 결과", "뒤에서 갈아 끼움"],
            "right_note": "최신 입력과 도구 결과",
            "quote": "최신 입력과 도구 결과만 뒤에서 갈아 끼워야 KV-cache hit rate가 살아납니다.",
            "attribution": "Manus Research",
        },
    )
