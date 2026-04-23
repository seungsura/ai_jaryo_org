from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        2,
        title="시작하며",
        shell="process-flow-shell",
        source_section="00",
        source_block="00-01",
        key_claim="AI에게 무엇을 말할까에서 AI가 일할 환경 설계로 이동",
        chapter_label="OPENING",
        notes_intent="챗봇 사용 경험과 도구 수렴을 Harness 문제로 연결",
        notes="좋은 결과는 한 번의 프롬프트보다 반복 가능한 구조에서 나온다는 흐름을 고정한다.",
        body={
            "thesis": "개발자의 핵심 역량: AI에게 할 말 → AI가 안전하게 일할 환경",
            "steps": [
                {"index": "01", "title": "챗봇과 말씨름", "text": "맥락 충돌과 반복 설명"},
                {"index": "02", "title": "도구들의 수렴", "text": "자동완성·채팅 UI·터미널 에이전트"},
                {"index": "03", "title": "Harness", "text": "규칙·컨텍스트·권한·검증·상태 기록"},
            ],
        },
    )
