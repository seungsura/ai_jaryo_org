from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        12,
        title="문서가 코드",
        shell="process-flow-shell",
        source_section="01",
        source_block="01-04",
        key_claim="에이전트가 매 세션 읽고 따라야 할 운영 규칙",
        chapter_label="CHAPTER 01",
        lead="이름은 다르지만 역할은 동일",
        notes_intent="page-011 reference 기반 문서 card layout",
        notes="source markdown의 규칙 파일 네 가지",
        body={
            "variant": "document-grid",
            "steps": [
                {"index": "01", "tool": "Claude Code", "title": "CLAUDE.md", "icon": "claude"},
                {"index": "02", "tool": "Cursor", "title": "Cursor Rules", "icon": "cursor"},
                {"index": "03", "tool": "GitHub Copilot", "title": "copilot-instructions.md", "icon": "copilot"},
                {"index": "04", "tool": "Codex", "title": "AGENTS.md", "icon": "codex"},
            ],
        },
    )
