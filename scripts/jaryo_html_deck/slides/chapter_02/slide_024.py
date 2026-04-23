from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        24,
        title="3막: 하네스의 시대",
        shell="evidence-table-shell",
        source_section="02",
        source_block="02-09",
        key_claim="Harness가 해내야 하는 것 · Harness를 이루는 것들",
        chapter_label="CHAPTER 02",
        notes_intent="해야 하는 것과 이루는 것의 relation map",
        notes="source markdown 3막 paragraph + user-requested relation remap",
        body={
            "variant": "tool-relation-map",
            "responsibilities": [
                {
                    "title": "무엇을 보는지",
                    "text": "컨텍스트",
                    "tools": [
                        "Plan Mode · 승인 체계",
                        "CLAUDE.md · Skills · Hooks",
                        "MCP · Plugins · Subagents",
                    ],
                },
                {
                    "title": "무엇을 할 수 있는지",
                    "text": "도구, 권한",
                    "tools": [
                        "Plan Mode · 승인 체계",
                        "CLAUDE.md · Skills · Hooks",
                        "MCP · Plugins · Subagents",
                    ],
                },
                {
                    "title": "언제 멈추는지",
                    "text": "제약",
                    "tools": [
                        "Plan Mode · 승인 체계",
                        "CLAUDE.md · Skills · Hooks",
                        "MCP · Plugins · Subagents",
                    ],
                },
                {
                    "title": "잘못되었을 때",
                    "text": "복구",
                    "tools": [
                        "Plan Mode · 승인 체계",
                        "CLAUDE.md · Skills · Hooks",
                        "MCP · Plugins · Subagents",
                    ],
                },
            ],
            "tools": [
                {"title": "Plan Mode · 승인 체계"},
                {"title": "CLAUDE.md · Skills · Hooks"},
                {"title": "MCP · Plugins · Subagents"},
            ],
        },
    )
