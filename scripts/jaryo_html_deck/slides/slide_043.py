from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        43,
        title="Memory: 세션을 넘어서는 기억",
        shell="evidence-table-shell",
        source_section="04",
        source_block="04-09",
        key_claim="대화창을 기억 저장소로 착각하지 않는다",
        chapter_label="CHAPTER 04",
        notes_intent="외부 artifact map과 memory claim",
        notes="상태와 근거는 파일 시스템, Git, 이슈, PR, 문서로 나가야 함",
        body={
            "variant": "memory-artifact-map",
            "question": "대화창을 기억 저장소로 착각하지 않는다",
            "artifacts": [
                {"title": "CLAUDE.md / AGENTS.md", "text": "규칙 파일과 기준선"},
                {"title": "프로젝트 노트와 결정 기록", "text": "설계 의도와 합의"},
                {"title": "이슈와 PR 히스토리", "text": "작업 맥락과 리뷰 흔적"},
                {"title": "progress.txt / prd.json", "text": "진행 상태와 요구사항"},
                {"title": "벡터 DB / 코드 그래프", "text": "검색 가능한 프로젝트 지식"},
                {"title": "커밋 히스토리와 아키텍처 결정 기록", "text": "변경 이유와 구조 결정"},
            ],
        },
    )
