from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        72,
        title="필요없는 도구는 덜어내라",
        shell="evidence-table-shell",
        source_section="07",
        source_block="07-04",
        key_claim="도구 큐레이션은 취향이 아니라 성능 문제",
        chapter_label="CHAPTER 07",
        notes_intent="tool curation과 gate 목록",
        notes="source lines 53-69",
        body={
            "variant": "chapter-principle-grid",
            "cards": [
                {"index": "01", "title": "tool curation", "text": "필요한 도구만 남김"},
                {"index": "02", "title": "lint / type check", "text": "기계가 닫는 문"},
                {"index": "03", "title": "테스트 / 리뷰 / 승인", "text": "검증과 승인"},
                {"index": "04", "title": "PreToolUse / PostToolUse", "text": "위험 명령 차단, 배포 전 human-in-the-loop"},
            ],
            "conclusion": "기계가 확인할 수 있는 것은 기계가 닫아야 함",
        },
    )
