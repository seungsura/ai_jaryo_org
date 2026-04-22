from __future__ import annotations

from .model import SlideSpec

def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    header_row = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    body_rows = ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join([header_row, separator, *body_rows])

def render_outline(specs: list[SlideSpec]) -> str:
    lines = [
        "# Slide Outline",
        "",
        "- status: 00/01/02/03/04 45-slide make-slide rebuild",
        "- canonical source: `docs/02-seminar/harness-rebuilt-md/00-overview.md`, `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`, `docs/02-seminar/harness-rebuilt-md/02-왜 Claude Code인가, 그리고 왜 Harness 인가.md`, `docs/02-seminar/harness-rebuilt-md/03-AI 시대의 개발 방법론.md`, `docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`",
        "- output deck: `docs/03-html/deck/index.html`",
        "- output script: `docs/03-html/deck/script.md`",
        "- theme: `minimal-light`",
        "- runtime policy: single-file deck, keyboard navigation, touch/swipe, active slide switching, print CSS",
        "- rejected chrome: progress bar, fullscreen UI, slide counter UI, notes UI, keyboard hint",
        "",
        "## Section Targets",
        "",
        markdown_table(
            ["section", "source", "target slides"],
            [
                ["00", "`docs/02-seminar/harness-rebuilt-md/00-overview.md`", "3"],
                ["01", "`docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`", "11"],
                ["02", "`docs/02-seminar/harness-rebuilt-md/02-왜 Claude Code인가, 그리고 왜 Harness 인가.md`", "13"],
                ["03", "`docs/02-seminar/harness-rebuilt-md/03-AI 시대의 개발 방법론.md`", "6"],
                ["04", "`docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`", "12"],
            ],
        ),
        "",
        "## Slide Registry",
        "",
    ]

    for spec in specs:
        lines.extend(
            [
                f"### {spec.slide_id}. {spec.title}",
                f"- file: `docs/03-html/slides/{spec.file_name}`",
                f"- slide type: `{spec.slide_type}`",
                f"- layout: `{spec.layout}`",
                f"- shell: `{spec.shell}`",
                f"- source section: `{spec.source_section}`",
                f"- source paragraph block: `{spec.source_block}`",
                f"- key claim: {spec.key_claim}",
                f"- notes intent: {spec.notes_intent}",
                f"- notes status: `{spec.notes_status}`",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"

def render_manifest(specs: list[SlideSpec]) -> str:
    rows = [
        [
            str(spec.order),
            f"`{spec.slide_id}`",
            f"`{spec.file_name}`",
            spec.title,
            f"`{spec.slide_type}`",
            f"`{spec.layout}`",
            f"`{spec.shell}`",
            f"`{spec.source_section}`",
            f"`{spec.source_block}`",
            f"`{spec.notes_status}`",
            spec.status,
        ]
        for spec in specs
    ]

    return "\n".join(
        [
            "# HTML Manifest",
            "",
            "- current status: 00/01/02/03/04 45-slide deck built",
            "- active theme: `theme-minimal-light`",
            "- slide id format: `S001`-`S045`",
            "- slide file format: `slide-001.html`-`slide-045.html`",
            "- output deck: `docs/03-html/deck/index.html`",
            "- output script: `docs/03-html/deck/script.md`",
            "",
            "## Slide Registry",
            "",
            markdown_table(
                [
                    "order",
                    "slide id",
                    "file",
                    "title",
                    "slide type",
                    "layout",
                    "shell",
                    "source section",
                    "source paragraph block",
                    "notes status",
                    "status",
                ],
                rows,
            ),
            "",
        ]
    )

def render_script(specs: list[SlideSpec]) -> str:
    parts = [
        "# Seminar Script",
        "",
        "- target deck: `docs/03-html/deck/index.html`",
        "- scope: 00 overview + 01/02/03/04 chapters",
        "",
    ]
    for spec in specs:
        parts.extend(
            [
                f"## {spec.slide_id} {spec.title}",
                f"- intent: {spec.notes_intent}",
                f"- opening: {spec.key_claim}",
                f"- bridge: {spec.notes}",
                "",
            ]
        )
    return "\n".join(parts).rstrip() + "\n"
