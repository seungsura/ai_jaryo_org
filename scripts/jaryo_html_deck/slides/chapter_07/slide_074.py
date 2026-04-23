from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        74,
        title="암묵지를 파일로 뽑아내라",
        shell="evidence-table-shell",
        source_section="07",
        source_block="07-08",
        key_claim="암묵지가 파일로 옮겨지는 순간 하네스가 됨",
        chapter_label="CHAPTER 07",
        notes_intent="four numbered steps and closing source",
        notes="source lines 114-123, page 054 structure-only reference",
        body={
            "variant": "chapter-principle-grid",
            "cards": [
                {"index": "01", "title": "결정의 이유", "text": "결과만 남기지 않음"},
                {"index": "02", "title": "Post-Mortem → 규칙", "text": "갈라진 지점을 한 줄로 승화"},
                {"index": "03", "title": "피드백마다 규칙 성장", "text": "반복 피드백은 파일로 이동"},
                {"index": "04", "title": "취향 encode", "text": "전용 에이전트나 규칙 파일"},
            ],
            "conclusion": "머릿속 판단이 파일로 옮겨지는 순간 하네스가 됩니다",
        },
    )
