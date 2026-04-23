from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        77,
        title="세션이 아니라 이슈가 상태를 들고 간다",
        shell="process-flow-shell",
        source_section="07",
        source_block="07-11",
        key_claim="이슈는 세션보다 오래가는 상태 저장소",
        chapter_label="CHAPTER 07",
        notes_intent="issue -> worktree -> session -> PR -> verification chain",
        notes="source lines 156-169, page 074 reference",
        body={
            "variant": "chapter-issue-hub",
            "center": "이슈",
            "center_text": "세션보다 오래가는 상태 저장소",
            "spokes": [
                {"index": "01", "title": "작업 목적과 수용 기준", "text": "Linear/PMS/GitHub Issue"},
                {"index": "02", "title": "Worktree 생성", "text": "이슈에서 시작"},
                {"index": "03", "title": "에이전트 세션", "text": "해당 이슈 범위만"},
                {"index": "04", "title": "작은 커밋", "text": "변경 단위 기록"},
                {"index": "05", "title": "이슈와 PR에 증거 첨부", "text": "검증 결과 연결"},
                {"index": "06", "title": "완료 판단", "text": "수용 기준과 검증 증거"},
            ],
            "conclusion": "이슈 → Worktree → 세션 → PR → 검증",
        },
    )
