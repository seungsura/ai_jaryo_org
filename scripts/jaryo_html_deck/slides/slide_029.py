from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        29,
        title="왜 지금 방법론",
        shell="evidence-table-shell",
        source_section="03",
        source_block="03-01",
        key_claim="AI에게 무엇을 시킬지, 어떻게 검증할 것인지",
        chapter_label="CHAPTER 03",
        notes_intent="AI 코딩 방법론 재부상 연대기",
        notes="생성 속도에서 검증 절차로 생각이 이동한 흐름",
        body={
            "headers": ["시기", "현상", "대표 키워드/도구", "핵심 질문"],
            "rows": [
                ["2025.02", "AI 코딩의 대중화와 문화적 전환점", "Vibe Coding", "일단 빨리 만들어 보자"],
                ["2025 중반", "생성 코드의 품질, 보안, 유지보수 문제 부각", "구조화된 검토, 검증 루프", "이 결과를 믿어도 되나?"],
                ["2025 하반기", "구현 전에 방향을 고정하려는 업계 대응", "SDD, Spec-first, GitHub Spec Kit", "애초에 무엇을 만들라고 할 것인가?"],
                ["2026 초", "구현 뒤 검증 체계와 문맥 통제가 다시 중요해짐", "TDD, Context Engineering", "정말 그 스펙대로 동작하는가?"],
            ],
            "question": "AI에게 무엇을 시킬지, 어떻게 검증할 것인지",
        },
    )
