from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        25,
        title="3막: 하네스의 시대",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-09",
        key_claim="터미널 네이티브 실행 환경",
        chapter_label="CHAPTER 02",
        notes_intent="Claude Code harness components",
        notes="source markdown의 Claude Code 구성 요소 bullet list",
        body={
            "variant": "component-clusters",
            "context": "Claude Code · Codex · OpenCode",
            "tiers": [
                {
                    "label": "기초",
                    "items": [
                        {"title": "CLAUDE.md", "text": "모든 세션에서 로드되는 프로젝트 컨텍스트", "primary": True},
                    ],
                },
                {
                    "label": "자동화",
                    "items": [
                        {"title": "Skills", "text": "재사용 가능한 워크플로우"},
                        {"title": "Hooks", "text": "이벤트 기반 검증과 차단"},
                    ],
                },
                {
                    "label": "연결",
                    "items": [
                        {"title": "MCP", "text": "외부 도구와 데이터 연결"},
                    ],
                },
                {
                    "label": "확장",
                    "items": [
                        {"title": "Subagents", "text": "역할과 컨텍스트 분리"},
                        {"title": "승인/샌드박스", "text": "위험 행동 권한 경계"},
                    ],
                },
            ],
            "steps": [
                {"index": "01", "title": "CLAUDE.md", "text": "프로젝트 상시 규칙"},
                {"index": "02", "title": "Skills", "text": "재사용 작업 지식"},
                {"index": "03", "title": "Hooks", "text": "이벤트 기반 검증과 차단"},
                {"index": "04", "title": "MCP", "text": "외부 도구와 데이터 연결"},
                {"index": "05", "title": "Subagents", "text": "역할과 컨텍스트 분리"},
                {"index": "06", "title": "승인/샌드박스", "text": "위험 행동 권한 경계"},
            ],
        },
    )
