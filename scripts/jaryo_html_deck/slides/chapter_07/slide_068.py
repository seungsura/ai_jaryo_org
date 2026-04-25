from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        68,
        title="OMC(Oh My Claude Code)",
        shell="process-flow-shell",
        source_section="07",
        source_block="07-02",
        key_claim="preset pack이 모드와 검증 루프를 먼저 고정",
        chapter_label="CHAPTER 07",
        notes_intent="preset command/routing map without canonical-only claims",
        notes="source lines 13-31, page 064/067 structure reference",
        body={
            "variant": "chapter-tool-gate-grid",
            "cards": [
                {"index": "01", "title": "역할 분리된 여러 에이전트", "text": "작업 성격에 맞는 역할"},
                {"index": "/model", "title": "모델 라우팅", "text": "모델 선택"},
                {"index": "/ralplan", "title": "Plan-Critic-Build 명령", "text": "계획과 비평 분리"},
                {"index": "/ultrapilot", "title": "병렬 worker", "text": "worker를 띄움"},
                {"index": "/ultraqa", "title": "QA와 검증 명령", "text": "test → fix → 재실행 루프"},
                {"index": "06", "title": "Git Worktree 기반 격리", "text": "이슈와 PR 연동"},
            ],
            "conclusion": "작업의 성격만 말하면 시스템이 모드, 역할, 모델, 검증 순서를 먼저 잡음",
        },
    )
