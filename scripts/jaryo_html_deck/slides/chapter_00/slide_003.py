from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        3,
        title="전체 목차",
        shell="agenda-list-shell",
        source_section="00",
        source_block="00-03",
        key_claim="Harness 관점으로 읽는 9개 장",
        chapter_label="OPENING",
        density="heavy",
        notes_intent="00-overview의 목차 표를 한 장에 압축",
        notes="전체 표를 한 장으로 보여 주고, 다음 장부터 각 항목을 순서대로 펼친다.",
        body={
            "items": [
                {"number": "01", "topic": "코딩은 어디로 가고 있는가", "text": "개발자의 숙련 이동"},
                {"number": "02", "topic": "왜 Claude Code인가", "text": "AI 코딩 도구의 구조 수렴"},
                {"number": "03", "topic": "AI 시대의 개발 방법론", "text": "TDD·SDD·Spec-first 재부상"},
                {"number": "04", "topic": "Harness", "text": "Prompt 이후의 에이전트 운영 구조"},
                {"number": "05", "topic": "한계와 실패 패턴", "text": "긴 작업·보안·신뢰 문제"},
                {"number": "06", "topic": "멀티 에이전트", "text": "역할과 컨텍스트 분리"},
                {"number": "07", "topic": "워크플로우와 도구", "text": "명령어·게이트·워크트리·이슈"},
                {"number": "08", "topic": "제작 과정", "text": "발표 제작 파이프라인 해부"},
                {"number": "09", "topic": "다음에 해야 할 일", "text": "개인과 팀의 첫 변화"},
            ]
        },
    )
