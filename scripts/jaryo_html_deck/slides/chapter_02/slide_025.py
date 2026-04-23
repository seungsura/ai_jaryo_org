from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide

def build() -> SlideSpec:
    return make_slide(
        25,
        title="3막: Claude Code, Codex, OpenCode 와 하네스의 시대",
        shell="evidence-table-shell",
        source_section="02",
        source_block="02-11",
        key_claim="Agent = Model + Harness",
        chapter_label="CHAPTER 02",
        notes_intent="2장 결론 관계식을 source heading 중심으로 고정",
        notes="source markdown 3막 heading + 시대 구분 표 + 포함 관계 문장",
        body={
            "variant": "era-native",
            "headers": ["시대", "핵심 질문", "주안점"],
            "rows": [
                ["Prompt Engineering", "어떤 말을 해야 하나", "자연어 지시문과 기법"],
                ["Context Engineering", "어떤 정보를 넣어야 하나", "코드베이스와 구조화 정보"],
                ["Harness Engineering", "어떤 시스템을 만들어야 하나", "권한 · 피드백 루프 · 검증"],
            ],
            "cards": [
                {"range": "2022~2024", "title": "Prompt Engineering", "question": "어떤 말을 해야 하나"},
                {"range": "2025 중반~", "title": "Context Engineering", "question": "어떤 정보를 넣어야 하나"},
                {"range": "2026~", "title": "Harness Engineering", "question": "어떤 시스템을 만들어야 하나"},
            ],
            "question": "하네스 안에 컨텍스트가 있고, 컨텍스트 안에 프롬프트가 있다",
            "formula": "Agent = Model + Harness",
            "relationship": "Prompt ⊂ Context ⊂ Harness",
        },
    )
