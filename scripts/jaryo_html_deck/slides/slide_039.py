from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        39,
        title="하네스의 도구",
        shell="evidence-table-shell",
        source_section="04",
        source_block="04-05",
        key_claim="책임과 도구는 1:1이 아니다",
        chapter_label="CHAPTER 04",
        notes_intent="책임 anchor와 도구 node의 다대다 관계 지도",
        notes="기능 블록과 도구 레이어는 1:1로 대응하지 않음",
        body={
            "variant": "tool-relation-map",
            "responsibilities": [
                {"title": "Guardrails", "tools": ["CLAUDE.md / AGENTS.md", "Hooks", "Plugins"]},
                {"title": "Specification", "tools": ["CLAUDE.md / AGENTS.md", "Skills", "이슈 / PR / 진행 파일"]},
                {"title": "Verification", "tools": ["Hooks", "pytest / CI / PR 체크", "CLAUDE.md / AGENTS.md"]},
                {"title": "State Management", "tools": ["Git Worktree", "이슈 / PR / 진행 파일", "CLAUDE.md / AGENTS.md"]},
                {"title": "Observability", "tools": ["실행 로그 / trace", "MCP / Context 7", "pytest / CI / PR 체크"]},
            ],
            "tools": [
                {"title": "CLAUDE.md / AGENTS.md"},
                {"title": "Skills"},
                {"title": "Hooks"},
                {"title": "MCP / Context 7"},
                {"title": "Plugins"},
                {"title": "Git Worktree"},
                {"title": "pytest / CI / PR 체크"},
                {"title": "이슈 / PR / 진행 파일"},
                {"title": "실행 로그 / trace"},
            ],
        },
    )
