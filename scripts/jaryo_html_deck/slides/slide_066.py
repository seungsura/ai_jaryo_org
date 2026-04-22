from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        66,
        title="설계 원칙: 패턴보다 경계가 중요하다",
        shell="evidence-table-shell",
        source_section="06",
        source_block="06-11",
        key_claim="SOLID도 에이전트 중심으로 다시 읽힘",
        chapter_label="CHAPTER 06",
        notes_intent="SOLID reinterpretation table",
        notes="source lines 164-175",
        body={
            "variant": "chapter-solid-cards",
            "cards": [
                {"index": "S", "title": "단일 책임", "text": "코드: 클래스를 분리한다", "evidence": "에이전트: 역할과 도구를 분리한다"},
                {"index": "O", "title": "개방-폐쇄", "text": "코드: 수정 없이 확장한다", "evidence": "에이전트: 훅과 플러그인으로 확장한다"},
                {"index": "I", "title": "인터페이스 분리", "text": "코드: 불필요한 메서드 의존을 줄인다", "evidence": "에이전트: 불필요한 도구와 파일 권한을 노출하지 않는다"},
                {"index": "D", "title": "의존성 역전", "text": "코드: 추상화에 의존한다", "evidence": "에이전트: 하드코딩 프롬프트 대신 컨텍스트와 규칙을 외부화한다"},
            ],
        },
    )
