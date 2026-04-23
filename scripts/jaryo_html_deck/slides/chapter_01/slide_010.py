from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        10,
        title="직접 하던 일의 감소",
        shell="evidence-table-shell",
        source_section="01",
        source_block="01-02",
        key_claim="직접 작성 부담의 지속적 위임",
        chapter_label="CHAPTER 01",
        notes_intent="시대별 위임 표와 질문 반전",
        notes="시대별 전환을 표로 압축하고, 변경된 source 질문을 독립된 한 줄로 배치한다.",
        body={
            "headers": ["시대", "전환", "위임한 것"],
            "rows": [
                ["1950s", "기계어 → 어셈블리", "이진 코드를 직접 작성하는 부담"],
                ["1960s", "어셈블리 → C", "레지스터와 명령어 최적화를 컴파일러에 위임"],
                ["1990s", "C/C++ → Java", "메모리 해제를 가비지 컬렉터에 위임"],
                ["2000s", "언어 → 프레임워크", "반복되는 보일러플레이트를 프레임워크에 위임"],
                ["2010s", "온프레미스 → 클라우드", "서버 운영과 확장을 클라우드에 위임"],
                ["2020s", "직접 코딩 → AI 에이전트", "코드 작성의 상당 부분과 작업 환경 설계"],
            ],
            "question": "직접하는 일을 줄고, 설계하는 일은 늘어난다",
        },
    )
