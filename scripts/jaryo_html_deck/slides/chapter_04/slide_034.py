from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        34,
        title="Agent = Model + Harness",
        shell="evidence-table-shell",
        source_section="04",
        source_block="04-02",
        key_claim="모델이 아닌 것은 전부 하네스입니다.",
        chapter_label="CHAPTER 04",
        notes_intent="공식, 인용구, 여섯 구성 요소를 한 장에 배치",
        notes="Agent 공식과 하네스의 여섯 구성 요소",
        body={
            "variant": "agent-harness-quote",
            "quote": "모델이 아닌 것은 전부 하네스입니다.",
            "attribution": "LangChain, Vivek Trivedy",
            "components": [
                {"title": "Context Engineering", "text": "모델이 봐야 할 정보와 버려야 할 정보"},
                {"title": "Tool Orchestration", "text": "도구 호출 순서와 권한"},
                {"title": "State & Memory", "text": "세션을 넘어 남는 파일과 기록"},
                {"title": "Verification Loop", "text": "테스트, 린트, 리뷰"},
                {"title": "Error Recovery", "text": "실패 감지와 재시도, 우회, 중단"},
                {"title": "Human-in-the-Loop Control", "text": "사람 승인과 개입 지점"},
            ],
        },
    )
