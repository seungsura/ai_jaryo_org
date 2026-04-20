from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_ROOT = ROOT / "docs/02-seminar/harness-rebuilt-md"
DEFAULT_OUTPUT_ROOT = ROOT / "docs/03-html/harness-rebuilt"
DEFAULT_PDF_OUTPUT = ROOT / "output/pdf/harness-rebuilt-deck.pdf"
SHARED_THEME_ROOT = ROOT / "docs/03-html/shared"
FOOTER_LABEL = "Harness 잘 사용하기"
ICON_CLUSTER_ITEMS = [
    ("CC", "Claude Code"),
    ("CX", "Codex"),
    ("OC", "OpenCode"),
]

CHAPTER_REVIEW_FOCUS = {
    "00": "문제의식과 전체 덱의 리듬이 첫 장부터 곧바로 보이는지 확인",
    "01": "추상화의 역사와 역할 이동이 선언이 아니라 증거로 읽히는지 확인",
    "02": "프롬프트에서 하네스로 이동하는 구조가 제품 소개처럼 보이지 않는지 확인",
    "03": "Spec-first, TDD, SDD의 관계가 도식이 아니라 실행 규율로 읽히는지 확인",
    "04": "Harness를 유행어가 아니라 실행 구조로 설명하는 데 성공했는지 확인",
    "05": "실패 패턴이 공포 마케팅이 아니라 설계 결함의 결과로 보이는지 확인",
    "06": "멀티 에이전트 패턴이 병렬화 자랑이 아니라 handoff 설계로 보이는지 확인",
    "07": "명령어, 게이트, 상태 외부화가 실전 workflow로 이어지는지 확인",
    "08": "이 발표의 제작 과정이 하네스 원리를 그대로 증명하는지 확인",
    "09": "행동 항목이 FOMO를 자극하지 않고 바로 옮길 습관으로 남는지 확인",
}

SHELL_CONTRACTS = {
    "cover-title-shell": ["icon-cluster", "cover-title", "cover-subtitle", "cover-author", "footer"],
    "chapter-transition-shell": ["icon-cluster", "transition-title", "footer"],
    "content-essay-shell": ["icon-cluster", "content-title", "content-body", "footer"],
    "content-card-shell": ["icon-cluster", "content-title", "card-grid", "card-item", "footer"],
    "content-emphasis-shell": ["icon-cluster", "content-title", "emphasis-line", "footer"],
}

POLITE_ENDING_RE = re.compile(r"(습니다|입니다|했습니다|되었습니다|하십시오|하세요|드립니다|합니다)(?:[.?!]|$)")
REPORT_STYLE_RE = re.compile(r"(또한|따라서|한편|통하여|위하여|관련하여)")
ENDING_RE = re.compile(
    r"(입니다|합니다|했습니다|되었습니다|있었습니다|였습니다|하십시오|하세요|드립니다|한다|된다|있다|없다|이다|였다|보인다|의미한다|설명한다)(?:[.?!]|$)"
)
FOOTNOTE_REF_RE = re.compile(r"\[\^([^\]]+)\]")
FOOTNOTE_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:\s*(.+)$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


@dataclass
class SourceBlock:
    chapter_id: str
    block_id: str
    heading: str
    paragraphs: list[str] = field(default_factory=list)
    list_items: list[str] = field(default_factory=list)
    table_rows: list[list[str]] = field(default_factory=list)
    code_blocks: list[str] = field(default_factory=list)
    quotes: list[str] = field(default_factory=list)
    footnote_refs: list[str] = field(default_factory=list)


@dataclass
class SourceChapter:
    chapter_id: str
    title: str
    source_path: str
    blocks: list[SourceBlock]
    footnotes: dict[str, list[str]]
    keywords: list[str]


@dataclass
class SlideSpec:
    order: int
    slide_id: str
    file_name: str
    title: str
    slide_kind: str
    shell: str
    chapter_id: str
    chapter_label: str
    source_path: str
    source_block: str
    key_claim: str
    lead: str
    review_hint: str
    shell_reason: str
    family: str
    layout: str
    density: str
    footnote_assets: list[str] = field(default_factory=list)
    body: dict[str, object] = field(default_factory=dict)


def clean_text(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    text = re.sub(r"_([^_]+)_", r"\1", text)
    text = LINK_RE.sub(r"\1", text)
    text = FOOTNOTE_REF_RE.sub("", text)
    text = re.sub(r"^[#>\-\*\d.\s]+", "", text)
    text = text.replace("→", " ").replace("—", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_phrase(text: str, *, limit: int = 44) -> str:
    text = clean_text(text)
    text = re.sub(r"\([^)]*\)", "", text).strip()
    text = POLITE_ENDING_RE.sub("", text).strip()
    text = ENDING_RE.sub("", text).strip()
    text = text.strip(" .,:;!?\"'“”‘’")
    if len(text) <= limit:
        return text
    shortened = text[:limit].rstrip()
    if " " in shortened:
        shortened = shortened.rsplit(" ", 1)[0]
    return shortened.strip(" .,:;!?\"'“”‘’")


def unique_phrases(items: Iterable[str], *, limit: int = 44, max_items: int | None = None) -> list[str]:
    phrases: list[str] = []
    seen: set[str] = set()
    for item in items:
        phrase = normalize_phrase(item, limit=limit)
        if len(phrase) < 2 or phrase in seen:
            continue
        seen.add(phrase)
        phrases.append(phrase)
        if max_items is not None and len(phrases) >= max_items:
            break
    return phrases


def split_sentences(items: Iterable[str]) -> list[str]:
    sentences: list[str] = []
    for item in items:
        cleaned = clean_text(item)
        if not cleaned:
            continue
        parts = re.split(r"(?<=[.!?])\s+|\n+", cleaned)
        sentences.extend(part.strip() for part in parts if part.strip())
    return sentences


def chapter_label(chapter_id: str) -> str:
    if chapter_id == "00":
        return "OPENING"
    return f"CHAPTER {chapter_id}"


def parse_chapter_title(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        if line.startswith("# "):
            return normalize_phrase(line[2:], limit=80)
    stem = path.stem
    stem = re.sub(r"^\d+-", "", stem)
    return normalize_phrase(stem, limit=80)


def extract_footnotes(lines: list[str]) -> dict[str, list[str]]:
    footnotes: dict[str, list[str]] = {}
    for line in lines:
        match = FOOTNOTE_DEF_RE.match(line.strip())
        if not match:
            continue
        assets = [target for _, target in LINK_RE.findall(match.group(2))]
        footnotes[match.group(1)] = assets
    return footnotes


def parse_blocks(chapter_id: str, title: str, lines: list[str]) -> list[SourceBlock]:
    blocks: list[SourceBlock] = []
    current_heading = title
    current_heading_raw = title
    current_lines: list[str] = []
    block_index = 0

    def flush() -> None:
        nonlocal block_index, current_lines, current_heading, current_heading_raw
        useful = [line for line in current_lines if line.strip() and not FOOTNOTE_DEF_RE.match(line.strip())]
        if not useful:
            current_lines = []
            return

        block_index += 1
        paragraphs: list[str] = []
        list_items: list[str] = []
        table_rows: list[list[str]] = []
        code_blocks: list[str] = []
        quotes: list[str] = []
        footnote_refs: list[str] = FOOTNOTE_REF_RE.findall(current_heading_raw)

        cursor = 0
        while cursor < len(current_lines):
            raw = current_lines[cursor]
            stripped = raw.strip()
            if not stripped or FOOTNOTE_DEF_RE.match(stripped):
                cursor += 1
                continue
            footnote_refs.extend(FOOTNOTE_REF_RE.findall(stripped))

            if stripped.startswith("```"):
                code_lines: list[str] = []
                cursor += 1
                while cursor < len(current_lines) and not current_lines[cursor].strip().startswith("```"):
                    code_lines.append(current_lines[cursor].rstrip())
                    cursor += 1
                code = "\n".join(line.rstrip() for line in code_lines if line.strip())
                if code:
                    code_blocks.append(code)
                cursor += 1
                continue

            if stripped.startswith("|"):
                rows: list[str] = []
                while cursor < len(current_lines) and current_lines[cursor].strip().startswith("|"):
                    rows.append(current_lines[cursor].strip())
                    cursor += 1
                parsed_rows: list[list[str]] = []
                for row in rows:
                    cells = [clean_text(cell) for cell in row.strip("|").split("|")]
                    if cells and set("".join(cells)) == {"-"}:
                        continue
                    parsed_rows.append(cells)
                if parsed_rows:
                    table_rows.extend(parsed_rows)
                continue

            if re.match(r"^(-|\*|\d+\.)\s+", stripped):
                item = re.sub(r"^(-|\*|\d+\.)\s+", "", stripped)
                list_items.append(clean_text(item))
                cursor += 1
                continue

            if stripped.startswith(">"):
                quotes.append(clean_text(stripped[1:]))
                cursor += 1
                continue

            paragraph_lines = [stripped]
            cursor += 1
            while cursor < len(current_lines):
                next_line = current_lines[cursor].strip()
                if not next_line or next_line.startswith("```") or next_line.startswith("|") or re.match(
                    r"^(-|\*|\d+\.)\s+", next_line
                ) or next_line.startswith(">"):
                    break
                paragraph_lines.append(next_line)
                cursor += 1
            paragraphs.append(clean_text(" ".join(paragraph_lines)))

        blocks.append(
            SourceBlock(
                chapter_id=chapter_id,
                block_id=f"{chapter_id}-{block_index:02d}",
                heading=normalize_phrase(current_heading, limit=80) or title,
                paragraphs=[part for part in paragraphs if part],
                list_items=[item for item in list_items if item],
                table_rows=table_rows,
                code_blocks=code_blocks,
                quotes=[quote for quote in quotes if quote],
                footnote_refs=sorted(set(footnote_refs)),
            )
        )
        current_lines = []

    for raw_line in lines:
        if raw_line.startswith("# "):
            continue
        if raw_line.startswith("## "):
            flush()
            current_heading_raw = raw_line[3:].strip()
            current_heading = clean_text(current_heading_raw)
            current_lines = []
            continue
        if raw_line.startswith("### "):
            flush()
            current_heading_raw = raw_line[4:].strip()
            current_heading = clean_text(current_heading_raw)
            current_lines = []
            continue
        current_lines.append(raw_line)

    flush()
    return blocks


def chapter_keywords(title: str, blocks: list[SourceBlock]) -> list[str]:
    candidates = [title]
    for block in blocks[:3]:
        candidates.append(block.heading)
        candidates.extend(block.list_items[:3])
    return unique_phrases(candidates, limit=18, max_items=4)


def load_chapters(source_root: Path) -> list[SourceChapter]:
    chapters: list[SourceChapter] = []
    for path in sorted(source_root.glob("*.md")):
        chapter_id = path.name.split("-", 1)[0]
        lines = path.read_text(encoding="utf-8").splitlines()
        title = parse_chapter_title(path)
        footnotes = extract_footnotes(lines)
        blocks = parse_blocks(chapter_id, title, lines)
        chapters.append(
            SourceChapter(
                chapter_id=chapter_id,
                title=title,
                source_path=str(path.relative_to(ROOT)),
                blocks=blocks,
                footnotes=footnotes,
                keywords=chapter_keywords(title, blocks),
            )
        )
    return chapters


def snippets_for_block(block: SourceBlock) -> list[str]:
    items: list[str] = [block.heading]
    items.extend(split_sentences(block.paragraphs))
    items.extend(block.list_items)
    items.extend(block.quotes)
    for row in block.table_rows[:8]:
        items.append(" / ".join(cell for cell in row if cell))
    for code_block in block.code_blocks[:4]:
        first_line = next((line.strip() for line in code_block.splitlines() if line.strip()), "")
        if first_line:
            items.append(first_line)
    return unique_phrases(items, limit=72)


def detail_lines_for_block(block: SourceBlock) -> list[str]:
    items: list[str] = []
    items.extend(block.paragraphs)
    items.extend(block.list_items)
    items.extend(block.quotes)
    for row in block.table_rows[1:6] or block.table_rows[:4]:
        items.append(" / ".join(cell for cell in row if cell))
    for code in block.code_blocks[:3]:
        lines = [line.strip() for line in code.splitlines() if line.strip()]
        if lines:
            items.append(" / ".join(lines[:2]))
    return unique_phrases(items, limit=72)


def block_assets(chapter: SourceChapter, block: SourceBlock) -> list[str]:
    assets: list[str] = []
    for ref in block.footnote_refs:
        assets.extend(chapter.footnotes.get(ref, []))
    return sorted(set(assets))


def chunked(items: list[str], size: int) -> list[list[str]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def shell_frame(shell: str) -> tuple[str, str, str]:
    if shell in {"cover-title-shell", "chapter-transition-shell"}:
        return "cover", "centered", "tight"
    if shell == "content-emphasis-shell":
        return "content", "wide", "tight"
    return "content", "wide", "medium"


def block_complexity(block: SourceBlock) -> int:
    return (
        len(block.paragraphs) * 2
        + len(block.list_items)
        + len(block.table_rows)
        + len(block.code_blocks) * 2
        + len(block.quotes)
    )


def plan_slide_count(chapter: SourceChapter, block: SourceBlock) -> int:
    if chapter.chapter_id == "01" and block.block_id == "01-01":
        return 5
    score = block_complexity(block)
    count = 1
    if score >= 7:
        count += 1
    if score >= 15:
        count += 1
    if score >= 27:
        count += 1
    return max(1, min(count, 5))


def cards_for_block(block: SourceBlock, *, offset: int = 0) -> list[dict[str, str]]:
    candidates: list[str] = []
    candidates.extend(block.list_items)
    candidates.extend(block.quotes)
    for row in block.table_rows[1:6] or block.table_rows[:4]:
        candidates.append(" / ".join(cell for cell in row if cell))
    candidates.extend(snippets_for_block(block))
    phrases = unique_phrases(candidates, limit=68)
    titles = unique_phrases([block.heading, *phrases], limit=26)
    cards: list[dict[str, str]] = []
    source = phrases[offset : offset + 6] or phrases[:3] or [block.heading]
    for index, phrase in enumerate(source[:3], start=1):
        title_source = titles[offset + index - 1] if offset + index - 1 < len(titles) else phrase
        cards.append(
            {
                "title": normalize_phrase(title_source, limit=28),
                "copy": normalize_phrase(phrase, limit=76),
            }
        )
    while len(cards) < 2:
        cards.append(
            {
                "title": normalize_phrase(block.heading, limit=28),
                "copy": normalize_phrase(block.heading, limit=76),
            }
        )
    return cards[:3]


def emphasis_line_for_block(block: SourceBlock) -> str:
    candidates = [
        *(block.quotes or []),
        *(list(reversed(block.paragraphs))[:2]),
        *(list(reversed(block.list_items))[:2]),
        block.heading,
    ]
    phrases = unique_phrases(candidates, limit=68, max_items=3)
    return phrases[0] if phrases else normalize_phrase(block.heading, limit=68)


def essay_lines_for_block(block: SourceBlock, *, offset: int = 0) -> list[str]:
    lines = detail_lines_for_block(block)
    group = lines[offset : offset + 2]
    if not group:
        group = lines[:2]
    if not group:
        group = [normalize_phrase(block.heading, limit=72)]
    return group[:2]


def make_slide(
    order: int,
    *,
    title: str,
    slide_kind: str,
    shell: str,
    chapter: SourceChapter,
    block: SourceBlock,
    key_claim: str,
    lead: str,
    review_hint: str,
    shell_reason: str,
    body: dict[str, object],
) -> SlideSpec:
    family, layout, density = shell_frame(shell)
    return SlideSpec(
        order=order,
        slide_id=f"S{order:03d}",
        file_name=f"slide-{order:03d}.html",
        title=normalize_phrase(title, limit=72),
        slide_kind=slide_kind,
        shell=shell,
        chapter_id=chapter.chapter_id,
        chapter_label=chapter_label(chapter.chapter_id),
        source_path=chapter.source_path,
        source_block=block.block_id,
        key_claim=normalize_phrase(key_claim, limit=88),
        lead=normalize_phrase(lead, limit=88),
        review_hint=review_hint,
        shell_reason=shell_reason,
        family=family,
        layout=layout,
        density=density,
        footnote_assets=block_assets(chapter, block),
        body=body,
    )


def build_cover(chapter: SourceChapter, order: int) -> SlideSpec:
    snippets: list[str] = []
    for block in chapter.blocks[:3]:
        snippets.extend(snippets_for_block(block))
    subtitle = normalize_phrase(
        snippets[1] if len(snippets) > 1 else "에이전트가 일할 환경을 설계하는 발표",
        limit=72,
    )
    family, layout, density = shell_frame("cover-title-shell")
    return SlideSpec(
        order=order,
        slide_id=f"S{order:03d}",
        file_name=f"slide-{order:03d}.html",
        title=chapter.title,
        slide_kind="cover",
        shell="cover-title-shell",
        chapter_id=chapter.chapter_id,
        chapter_label=chapter_label(chapter.chapter_id),
        source_path=chapter.source_path,
        source_block=chapter.blocks[0].block_id if chapter.blocks else f"{chapter.chapter_id}-00",
        key_claim="챗봇이 아니라 에이전트가 일할 구조를 설계한다",
        lead=subtitle,
        review_hint=CHAPTER_REVIEW_FOCUS[chapter.chapter_id],
        shell_reason="opening deck cover",
        family=family,
        layout=layout,
        density=density,
        footnote_assets=[],
        body={"subtitle": subtitle, "author": "게임플랫폼 1팀 라승수"},
    )


def build_chapter_transition(chapter: SourceChapter, order: int) -> SlideSpec:
    first_block = chapter.blocks[0]
    family, layout, density = shell_frame("chapter-transition-shell")
    return SlideSpec(
        order=order,
        slide_id=f"S{order:03d}",
        file_name=f"slide-{order:03d}.html",
        title=chapter.title,
        slide_kind="chapter-transition",
        shell="chapter-transition-shell",
        chapter_id=chapter.chapter_id,
        chapter_label=chapter_label(chapter.chapter_id),
        source_path=chapter.source_path,
        source_block=first_block.block_id,
        key_claim=normalize_phrase(first_block.heading, limit=72),
        lead=normalize_phrase(first_block.heading, limit=72),
        review_hint=CHAPTER_REVIEW_FOCUS[chapter.chapter_id],
        shell_reason="chapter transition anchor",
        family=family,
        layout=layout,
        density=density,
        footnote_assets=[],
        body={},
    )


def build_special_chapter_01(chapter: SourceChapter, block: SourceBlock, order: int) -> list[SlideSpec]:
    phrases = snippets_for_block(block)
    detail_lines = detail_lines_for_block(block)
    cards = cards_for_block(block)
    code_rows: list[str] = []
    for code in block.code_blocks[:5]:
        lines = [line.strip() for line in code.splitlines() if line.strip()]
        if lines:
            code_rows.append(normalize_phrase(" / ".join(lines[:2]), limit=76))
    while len(code_rows) < 2:
        code_rows.append("직접 타이핑은 줄고 더 큰 구조를 설계")

    slides = [
        make_slide(
            order,
            title="직접 붙들던 층은 계속 위로 밀려났다",
            slide_kind="content",
            shell="content-essay-shell",
            chapter=chapter,
            block=block,
            key_claim="추상화는 개발을 지우지 않고 개발자가 붙드는 층을 바꾼다",
            lead=detail_lines[0] if detail_lines else block.heading,
            review_hint=CHAPTER_REVIEW_FOCUS["01"],
            shell_reason="chapter 01 opening thesis",
            body={"lines": essay_lines_for_block(block, offset=0)},
        ),
        make_slide(
            order + 1,
            title="반발의 문장은 시대만 바뀌고 반복됐다",
            slide_kind="content",
            shell="content-card-shell",
            chapter=chapter,
            block=block,
            key_claim="기계어에서 AI까지 진짜 개발자 담론은 늘 같은 모양으로 돌아왔다",
            lead=phrases[1] if len(phrases) > 1 else block.heading,
            review_hint=CHAPTER_REVIEW_FOCUS["01"],
            shell_reason="chapter 01 resistance cards",
            body={"cards": cards},
        ),
        make_slide(
            order + 2,
            title="코드 예시는 역할 이동을 가장 빨리 보여 준다",
            slide_kind="content",
            shell="content-essay-shell",
            chapter=chapter,
            block=block,
            key_claim="새 추상화는 작성량을 줄이고 판단의 범위를 넓혔다",
            lead=code_rows[0],
            review_hint=CHAPTER_REVIEW_FOCUS["01"],
            shell_reason="chapter 01 code evolution evidence",
            body={"lines": code_rows[:2]},
        ),
        make_slide(
            order + 3,
            title="AI도 예외가 아니라 같은 흐름의 다음 장면이다",
            slide_kind="content",
            shell="content-essay-shell",
            chapter=chapter,
            block=block,
            key_claim="자연어로 지시한다고 개발이 끝나는 것이 아니라 추상화가 다시 올라간다",
            lead=detail_lines[2] if len(detail_lines) > 2 else block.heading,
            review_hint=CHAPTER_REVIEW_FOCUS["01"],
            shell_reason="chapter 01 ai shift bridge",
            body={"lines": essay_lines_for_block(block, offset=2)},
        ),
        make_slide(
            order + 4,
            title="타이핑보다 설계와 검증이 더 무거워진다",
            slide_kind="content",
            shell="content-emphasis-shell",
            chapter=chapter,
            block=block,
            key_claim="개발의 중심은 직접 입력보다 판단과 검증으로 옮겨 간다",
            lead=emphasis_line_for_block(block),
            review_hint=CHAPTER_REVIEW_FOCUS["01"],
            shell_reason="chapter 01 synthesis emphasis",
            body={"line": "직접 치는 손보다 설계와 검증이 더 무거워진다"},
        ),
    ]
    return slides


def choose_single_shell(block: SourceBlock) -> tuple[str, str]:
    if "결론" in block.heading or block.quotes:
        return "content-emphasis-shell", "single emphasis close"
    if len(block.list_items) >= 4 or len(block.table_rows) >= 4:
        return "content-card-shell", "parallel evidence fits card shell"
    return "content-essay-shell", "default compressed essay"


def shells_for_block(block: SourceBlock, count: int) -> list[tuple[str, str]]:
    if count <= 1:
        shell, reason = choose_single_shell(block)
        return [(shell, reason)]

    has_parallel = len(block.list_items) >= 3 or len(block.table_rows) >= 4
    shells: list[tuple[str, str]] = [("content-essay-shell", "block opening claim")]
    if has_parallel:
        shells.append(("content-card-shell", "parallel evidence split"))
    else:
        shells.append(("content-essay-shell", "second compressed essay split"))

    while len(shells) < count - 1:
        if has_parallel and len(shells) % 2 == 1:
            shells.append(("content-card-shell", "additional evidence split"))
        else:
            shells.append(("content-essay-shell", "additional essay split"))

    shells.append(("content-emphasis-shell", "block synthesis emphasis"))
    return shells[:count]


def segment_title(block: SourceBlock, shell: str, phrases: list[str], segment_index: int) -> str:
    if segment_index == 0:
        return block.heading
    candidate_index = min(segment_index, len(phrases) - 1) if phrases else 0
    candidate = phrases[candidate_index] if phrases else block.heading
    if shell == "content-emphasis-shell":
        return normalize_phrase(block.heading, limit=72)
    return normalize_phrase(candidate, limit=72) or block.heading


def build_generic_block_slides(chapter: SourceChapter, block: SourceBlock, order: int) -> list[SlideSpec]:
    slide_count = plan_slide_count(chapter, block)
    phrases = snippets_for_block(block)
    shells = shells_for_block(block, slide_count)
    essay_groups = chunked(detail_lines_for_block(block), 2)
    card_offset = 0
    slides: list[SlideSpec] = []

    for segment_index, (shell, reason) in enumerate(shells):
        title = segment_title(block, shell, phrases, segment_index)
        claim = phrases[segment_index] if segment_index < len(phrases) else block.heading
        lead = (
            detail_lines_for_block(block)[segment_index]
            if segment_index < len(detail_lines_for_block(block))
            else claim
        )
        if shell == "content-card-shell":
            body = {"cards": cards_for_block(block, offset=card_offset)}
            card_offset += 2
        elif shell == "content-emphasis-shell":
            body = {"line": emphasis_line_for_block(block)}
        else:
            lines = essay_groups[segment_index] if segment_index < len(essay_groups) else essay_lines_for_block(block)
            body = {"lines": lines}

        slides.append(
            make_slide(
                order + segment_index,
                title=title,
                slide_kind="content",
                shell=shell,
                chapter=chapter,
                block=block,
                key_claim=claim,
                lead=lead,
                review_hint=CHAPTER_REVIEW_FOCUS[chapter.chapter_id],
                shell_reason=reason,
                body=body,
            )
        )
    return slides


def build_block_slides(chapter: SourceChapter, order_start: int) -> tuple[list[SlideSpec], dict[str, list[str]]]:
    slides: list[SlideSpec] = []
    special_rules: dict[str, list[str]] = defaultdict(list)
    order = order_start
    for block in chapter.blocks:
        if chapter.chapter_id == "01" and block.block_id == "01-01":
            built = build_special_chapter_01(chapter, block, order)
            slides.extend(built)
            special_rules[block.block_id].append("chapter_01_special_decomposition")
            order += len(built)
            continue

        built = build_generic_block_slides(chapter, block, order)
        if len(built) > 1:
            special_rules[block.block_id].append("heuristic_multi_slide_decomposition")
        slides.extend(built)
        order += len(built)

    return slides, special_rules


def build_chapter_review_meta(
    chapter: SourceChapter,
    transition: SlideSpec | None,
    content_slides: list[SlideSpec],
    special_rules: dict[str, list[str]],
) -> dict[str, object]:
    coverage: list[dict[str, object]] = []
    slides_by_block: dict[str, list[SlideSpec]] = defaultdict(list)
    for slide in content_slides:
        slides_by_block[slide.source_block].append(slide)

    chapter_footnotes: set[str] = set()
    chapter_shells: Counter[str] = Counter()
    chapter_slide_ids: list[str] = []
    for slide in content_slides:
        chapter_slide_ids.append(slide.slide_id)
        chapter_shells[slide.shell] += 1
        chapter_footnotes.update(slide.footnote_assets)
    if transition is not None:
        chapter_slide_ids.insert(0, transition.slide_id)
        chapter_shells[transition.shell] += 1
        chapter_footnotes.update(transition.footnote_assets)

    for block in chapter.blocks:
        block_slides = slides_by_block[block.block_id]
        coverage.append(
            {
                "block_id": block.block_id,
                "heading": block.heading,
                "slide_count": len(block_slides),
                "slide_ids": [slide.slide_id for slide in block_slides],
            }
        )

    flattened_rules = sorted({rule for rules in special_rules.values() for rule in rules})
    return {
        "chapter_id": chapter.chapter_id,
        "title": chapter.title,
        "source_path": chapter.source_path,
        "transition_slide_id": transition.slide_id if transition else None,
        "slide_ids": chapter_slide_ids,
        "section_coverage": coverage,
        "footnote_assets": sorted(chapter_footnotes),
        "review_focus": CHAPTER_REVIEW_FOCUS[chapter.chapter_id],
        "special_rules": flattened_rules,
        "shell_mix": dict(chapter_shells),
    }


def build_specs(chapters: list[SourceChapter]) -> tuple[list[SlideSpec], dict[str, dict[str, object]]]:
    chapter_map = {chapter.chapter_id: chapter for chapter in chapters}
    specs: list[SlideSpec] = []
    review_meta: dict[str, dict[str, object]] = {}
    order = 1

    opening = chapter_map["00"]
    specs.append(build_cover(opening, order))
    order += 1
    opening_slides, opening_special = build_block_slides(opening, order)
    specs.extend(opening_slides)
    order += len(opening_slides)
    review_meta["00"] = build_chapter_review_meta(opening, None, opening_slides, opening_special)

    for chapter in chapters:
        if chapter.chapter_id == "00":
            continue
        transition = build_chapter_transition(chapter, order)
        specs.append(transition)
        order += 1
        content_slides, special_rules = build_block_slides(chapter, order)
        specs.extend(content_slides)
        order += len(content_slides)
        review_meta[chapter.chapter_id] = build_chapter_review_meta(chapter, transition, content_slides, special_rules)

    return specs, review_meta


def render_footer(spec: SlideSpec) -> str:
    return (
        '<footer class="footer">'
        f'<span class="footer-left">{html.escape(FOOTER_LABEL)}</span>'
        f'<span class="footer-center">{html.escape(spec.chapter_label)}</span>'
        f'<span class="footer-right">{spec.order}</span>'
        "</footer>"
    )


def render_assets(spec: SlideSpec) -> str:
    if not spec.footnote_assets:
        return ""
    chips = "".join(
        f'<li class="asset-chip" data-asset-path="{html.escape(asset)}">{html.escape(Path(asset).name)}</li>'
        for asset in spec.footnote_assets
    )
    return f'<ul class="footnote-assets">{chips}</ul>'


def render_icon_cluster() -> str:
    items = "".join(
        '<li class="icon-cluster-item">'
        f'<span class="icon-cluster-glyph">{html.escape(glyph)}</span>'
        f'<span class="icon-cluster-label">{html.escape(label)}</span>'
        "</li>"
        for glyph, label in ICON_CLUSTER_ITEMS
    )
    return f'<ul class="icon-cluster" aria-label="tool icons">{items}</ul>'


def render_shell(spec: SlideSpec) -> str:
    if spec.shell == "cover-title-shell":
        return (
            '<section class="cover-shell">'
            f'<h1 class="cover-title">{html.escape(spec.title)}</h1>'
            f'<p class="cover-subtitle">{html.escape(str(spec.body["subtitle"]))}</p>'
            f'<p class="cover-author">{html.escape(str(spec.body["author"]))}</p>'
            "</section>"
        )
    if spec.shell == "chapter-transition-shell":
        return (
            '<section class="transition-shell">'
            f'<h1 class="transition-title">{html.escape(spec.title)}</h1>'
            "</section>"
        )
    if spec.shell == "content-card-shell":
        cards = "".join(
            '<article class="card-item">'
            f'<h2 class="card-title">{html.escape(card["title"])}</h2>'
            f'<p class="card-copy">{html.escape(card["copy"])}</p>'
            "</article>"
            for card in spec.body["cards"]
        )
        return (
            '<section class="content-shell">'
            f'<h1 class="content-title">{html.escape(spec.title)}</h1>'
            f'<div class="card-grid">{cards}</div>'
            f"{render_assets(spec)}"
            "</section>"
        )
    if spec.shell == "content-emphasis-shell":
        return (
            '<section class="content-shell content-shell-emphasis">'
            f'<h1 class="content-title">{html.escape(spec.title)}</h1>'
            f'<p class="emphasis-line">{html.escape(str(spec.body["line"]))}</p>'
            f"{render_assets(spec)}"
            "</section>"
        )

    lines = "".join(f"<p>{html.escape(line)}</p>" for line in spec.body["lines"])
    return (
        '<section class="content-shell">'
        f'<h1 class="content-title">{html.escape(spec.title)}</h1>'
        f'<div class="content-body">{lines}</div>'
        f"{render_assets(spec)}"
        "</section>"
    )


def render_slide_markup(spec: SlideSpec) -> str:
    return (
        f'<main class="slide family-{html.escape(spec.family)} layout-{html.escape(spec.layout)} density-{html.escape(spec.density)}" '
        f'data-slide-id="{html.escape(spec.slide_id)}" '
        f'data-shell="{html.escape(spec.shell)}" '
        f'data-slide-kind="{html.escape(spec.slide_kind)}" '
        f'data-chapter="{html.escape(spec.chapter_id)}" '
        f'data-source-block="{html.escape(spec.source_block)}" '
        'data-footer="default">'
        f"{render_icon_cluster()}"
        f"{render_shell(spec)}"
        f"{render_footer(spec)}"
        "</main>"
    )


def load_shared_css() -> tuple[str, str]:
    tokens = (SHARED_THEME_ROOT / "tokens.css").read_text(encoding="utf-8")
    slide_base = (SHARED_THEME_ROOT / "slide-base.css").read_text(encoding="utf-8")
    return tokens, slide_base


def deck_css() -> str:
    return """
.slide {
  padding: 76px 88px 88px;
  background: var(--color-paper);
}

.slide::before {
  content: "";
  position: absolute;
  inset: 24px;
  border: 1px solid var(--color-line-soft);
  pointer-events: none;
}

.icon-cluster {
  position: absolute;
  top: 40px;
  right: 48px;
  display: flex;
  gap: 10px;
}

.icon-cluster-item {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  border-radius: var(--radius-pill);
  background: var(--color-surface);
  border: 1px solid var(--color-line-soft);
  box-shadow: var(--shadow-card);
  font-size: 14px;
  font-weight: 700;
  color: var(--color-ink);
}

.icon-cluster-glyph {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 26px;
  height: 26px;
  border-radius: 999px;
  background: var(--color-signal-soft);
  color: var(--color-signal);
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 800;
}

.cover-shell,
.transition-shell,
.content-shell {
  position: relative;
  max-width: 930px;
}

.family-cover.layout-centered .cover-shell,
.family-cover.layout-centered .transition-shell {
  position: absolute;
  left: 88px;
  right: 220px;
  top: 144px;
}

.cover-title,
.transition-title,
.content-title {
  letter-spacing: -0.04em;
  word-break: keep-all;
}

.cover-title {
  font-size: 78px;
  line-height: 0.98;
  font-weight: 800;
  max-width: 820px;
}

.cover-subtitle {
  margin-top: 28px;
  max-width: 760px;
  font-size: 28px;
  line-height: 1.34;
  font-weight: 600;
  color: var(--color-mute);
}

.cover-author {
  margin-top: 32px;
  font-size: 18px;
  line-height: 1.2;
  font-weight: 800;
  letter-spacing: 0.06em;
  color: var(--color-signal);
}

.transition-title {
  font-size: 68px;
  line-height: 1.02;
  font-weight: 800;
  max-width: 860px;
}

.family-content.layout-wide .content-shell {
  margin-top: 54px;
}

.content-title {
  max-width: 920px;
  font-size: 56px;
  line-height: 1.06;
  font-weight: 800;
}

.content-body {
  display: grid;
  gap: 16px;
  margin-top: 28px;
  max-width: 860px;
}

.content-body p {
  font-size: 28px;
  line-height: 1.36;
  font-weight: 600;
  color: var(--color-mute);
  word-break: keep-all;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
  margin-top: 32px;
}

.card-item {
  min-height: 220px;
  padding: 24px;
  border-radius: var(--radius-card);
  background: var(--color-surface);
  border: 1px solid var(--color-line-soft);
  box-shadow: var(--shadow-card);
}

.card-title {
  font-size: 28px;
  line-height: 1.12;
  font-weight: 800;
  letter-spacing: -0.03em;
}

.card-copy {
  margin-top: 16px;
  font-size: 23px;
  line-height: 1.34;
  font-weight: 600;
  color: var(--color-mute);
}

.content-shell-emphasis {
  max-width: 980px;
}

.emphasis-line {
  margin-top: 34px;
  max-width: 960px;
  font-size: 62px;
  line-height: 1.02;
  font-weight: 800;
  letter-spacing: -0.04em;
  word-break: keep-all;
}

.footnote-assets {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 24px;
}

.asset-chip {
  padding: 8px 12px;
  border-radius: var(--radius-pill);
  border: 1px solid var(--color-line-soft);
  background: var(--color-surface-muted);
  font-size: 14px;
  font-weight: 700;
  color: var(--color-mute);
}

.deck {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: var(--color-paper);
}

.deck-slide {
  position: absolute;
  inset: 0;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.deck-slide.active {
  display: flex;
}

.deck-slide .slide {
  transform: scale(var(--deck-scale));
  transform-origin: top left;
}

@media print {
  html,
  body {
    width: auto;
    height: auto;
    overflow: visible;
  }

  .deck {
    display: block;
    width: auto;
    height: auto;
    overflow: visible;
  }

  .deck-slide {
    position: relative;
    display: block !important;
    padding: 0;
    break-after: page;
    page-break-after: always;
  }

  .deck-slide .slide {
    transform: none;
  }
}
"""


def render_slide_html(spec: SlideSpec) -> str:
    return "\n".join(
        [
            "<!DOCTYPE html>",
            '<html lang="ko">',
            "<head>",
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            f"<title>{html.escape(spec.slide_id)} {html.escape(spec.title)}</title>",
            '<link rel="stylesheet" href="../shared/tokens.css">',
            '<link rel="stylesheet" href="../shared/slide-base.css">',
            '<link rel="stylesheet" href="../shared/deck.css">',
            "</head>",
            '<body class="theme-minimal-light">',
            render_slide_markup(spec),
            "</body>",
            "</html>",
            "",
        ]
    )


def render_deck_html(specs: list[SlideSpec]) -> str:
    tokens, slide_base = load_shared_css()
    wrappers = []
    for index, spec in enumerate(specs):
        active = " active" if index == 0 else ""
        wrappers.append(f'<section class="deck-slide{active}" data-slide-id="{html.escape(spec.slide_id)}">{render_slide_markup(spec)}</section>')
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Harness Rebuilt Deck</title>
  <style>
{tokens}
{slide_base}
{deck_css()}
:root {{
  --deck-scale: 1;
}}
html, body {{
  width: 100%;
  height: 100%;
  margin: 0;
  overflow: hidden;
  background: var(--color-paper);
}}
body {{
  width: 100vw;
  height: 100vh;
}}
  </style>
</head>
<body class="theme-minimal-light">
  <div class="deck">
    {''.join(wrappers)}
  </div>
  <script>
const slides = Array.from(document.querySelectorAll('.deck-slide'));
let currentIndex = 0;
let touchStartX = 0;

function updateScale() {{
  const usableWidth = window.innerWidth - 48;
  const usableHeight = window.innerHeight - 48;
  const scale = Math.min(usableWidth / 1280, usableHeight / 720, 1);
  document.documentElement.style.setProperty('--deck-scale', String(scale));
}}

function goTo(index) {{
  currentIndex = Math.max(0, Math.min(index, slides.length - 1));
  slides.forEach((slide, slideIndex) => {{
    slide.classList.toggle('active', slideIndex === currentIndex);
  }});
}}

window.addEventListener('resize', updateScale);
window.addEventListener('keydown', (event) => {{
  if (event.key === 'ArrowRight' || event.key === 'PageDown' || event.key === ' ') {{
    goTo(currentIndex + 1);
  }}
  if (event.key === 'ArrowLeft' || event.key === 'PageUp') {{
    goTo(currentIndex - 1);
  }}
}});
window.addEventListener('touchstart', (event) => {{
  touchStartX = event.changedTouches[0].clientX;
}});
window.addEventListener('touchend', (event) => {{
  const delta = event.changedTouches[0].clientX - touchStartX;
  if (delta < -50) goTo(currentIndex + 1);
  if (delta > 50) goTo(currentIndex - 1);
}});
updateScale();
goTo(0);
  </script>
</body>
</html>
"""


def render_outline(specs: list[SlideSpec]) -> str:
    lines = ["# Harness Rebuilt Outline", ""]
    current_chapter = None
    for spec in specs:
        if spec.chapter_id != current_chapter:
            current_chapter = spec.chapter_id
            lines.append(f"## {spec.chapter_label} · {spec.chapter_id}")
        lines.append(f"- {spec.slide_id} | {spec.slide_kind} | {spec.shell} | {spec.title} | {spec.key_claim}")
    lines.append("")
    return "\n".join(lines)


def render_manifest(output_root: Path, specs: list[SlideSpec], chapter_groups: dict[str, list[SlideSpec]]) -> str:
    lines = [
        "# Harness Rebuilt Manifest",
        "",
        f"- slide count: {len(specs)}",
        f"- output deck: `{(output_root / 'deck/index.html').resolve()}`",
        f"- active theme: `theme-minimal-light`",
        "",
        "## Chapter Files",
        "",
    ]
    for chapter_id in sorted(chapter_groups):
        lines.append(f"- chapter `{chapter_id}` brief: `briefs/chapter-{chapter_id}.md`")
        lines.append(f"- chapter `{chapter_id}` copy: `copy/chapter-{chapter_id}.md`")
    lines.extend(
        [
            "",
            "## Slide Registry",
            "",
            "| order | slide id | kind | shell | chapter | source block | file | title | footnote assets |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for spec in specs:
        assets = ", ".join(Path(asset).name for asset in spec.footnote_assets) or "-"
        lines.append(
            f"| {spec.order} | `{spec.slide_id}` | `{spec.slide_kind}` | `{spec.shell}` | `{spec.chapter_id}` | `{spec.source_block}` | `{spec.file_name}` | {spec.title} | {assets} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_brief(chapter: SourceChapter, slides: list[SlideSpec]) -> str:
    lines = [f"# {chapter_label(chapter.chapter_id)} Brief", "", f"- title: {chapter.title}", ""]
    for spec in slides:
        lines.extend(
            [
                f"## {spec.slide_id} {spec.title}",
                f"- kind: `{spec.slide_kind}`",
                f"- shell: `{spec.shell}`",
                f"- family/layout/density: `{spec.family}` / `{spec.layout}` / `{spec.density}`",
                f"- claim: {spec.key_claim}",
                f"- shell reason: {spec.shell_reason}",
                f"- footnote assets: {', '.join(spec.footnote_assets) if spec.footnote_assets else '-'}",
                "",
            ]
        )
    return "\n".join(lines)


def render_copy(chapter: SourceChapter, slides: list[SlideSpec]) -> str:
    lines = [f"# {chapter_label(chapter.chapter_id)} Copy", "", f"- title: {chapter.title}", ""]
    for spec in slides:
        lines.extend(
            [
                f"## {spec.slide_id} {spec.title}",
                f"- lead: {spec.lead}",
                f"- claim: {spec.key_claim}",
            ]
        )
        if spec.shell == "content-card-shell":
            lines.append("- cards:")
            for card in spec.body["cards"]:
                lines.append(f"  - {card['title']} | {card['copy']}")
        elif spec.shell == "content-emphasis-shell":
            lines.append(f"- emphasis: {spec.body['line']}")
        elif spec.shell == "content-essay-shell":
            lines.append("- body:")
            for line in spec.body["lines"]:
                lines.append(f"  - {line}")
        elif spec.shell == "cover-title-shell":
            lines.append(f"- subtitle: {spec.body['subtitle']}")
        lines.append("")
    return "\n".join(lines)


def specs_by_chapter(specs: list[SlideSpec]) -> dict[str, list[SlideSpec]]:
    groups: dict[str, list[SlideSpec]] = defaultdict(list)
    for spec in specs:
        groups[spec.chapter_id].append(spec)
    return groups


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_outputs(output_root: Path, chapters: list[SourceChapter], specs: list[SlideSpec], review_meta: dict[str, dict[str, object]]) -> None:
    if output_root.exists():
        shutil.rmtree(output_root)
    (output_root / "slides").mkdir(parents=True, exist_ok=True)
    (output_root / "deck").mkdir(parents=True, exist_ok=True)
    (output_root / "data").mkdir(parents=True, exist_ok=True)
    (output_root / "briefs").mkdir(parents=True, exist_ok=True)
    (output_root / "copy").mkdir(parents=True, exist_ok=True)
    (output_root / "outline").mkdir(parents=True, exist_ok=True)
    (output_root / "shared").mkdir(parents=True, exist_ok=True)

    chapter_groups = specs_by_chapter(specs)
    tokens, slide_base = load_shared_css()

    write(output_root / "shared/tokens.css", tokens)
    write(output_root / "shared/slide-base.css", slide_base)
    write(output_root / "shared/deck.css", deck_css())
    write(output_root / "outline/slide-outline.md", render_outline(specs))
    write(output_root / "manifest.md", render_manifest(output_root, specs, chapter_groups))
    write(output_root / "deck/index.html", render_deck_html(specs))
    write(output_root / "data/slide-specs.json", json.dumps([asdict(spec) for spec in specs], ensure_ascii=False, indent=2))
    write(output_root / "data/chapter-review-metadata.json", json.dumps(review_meta, ensure_ascii=False, indent=2))

    for spec in specs:
        write(output_root / "slides" / spec.file_name, render_slide_html(spec))

    chapter_map = {chapter.chapter_id: chapter for chapter in chapters}
    for chapter_id, chapter_specs in chapter_groups.items():
        chapter = chapter_map[chapter_id]
        write(output_root / "briefs" / f"chapter-{chapter_id}.md", render_brief(chapter, chapter_specs))
        write(output_root / "copy" / f"chapter-{chapter_id}.md", render_copy(chapter, chapter_specs))


def resolve_chapter_scope(
    chapters: list[SourceChapter],
    *,
    through_chapter: str | None,
    chapters_arg: str | None,
) -> list[SourceChapter]:
    chapter_map = {chapter.chapter_id: chapter for chapter in chapters}
    ordered_ids = [chapter.chapter_id for chapter in chapters]

    if through_chapter and through_chapter not in chapter_map:
        raise ValueError(f"unknown chapter id for --through-chapter: {through_chapter}")
    if chapters_arg:
        requested = [chunk.strip() for chunk in chapters_arg.split(",") if chunk.strip()]
        missing = [chapter_id for chapter_id in requested if chapter_id not in chapter_map]
        if missing:
            raise ValueError(f"unknown chapter ids for --chapters: {', '.join(missing)}")
        requested_set = set(requested)
        requested_set.add("00")
        return [chapter_map[chapter_id] for chapter_id in ordered_ids if chapter_id in requested_set]
    if through_chapter:
        selected: list[SourceChapter] = []
        for chapter in chapters:
            selected.append(chapter)
            if chapter.chapter_id == through_chapter:
                break
        return selected
    return chapters


def build_pipeline(
    source_root: Path,
    output_root: Path,
    *,
    through_chapter: str | None = None,
    chapters_arg: str | None = None,
) -> tuple[list[SlideSpec], dict[str, dict[str, object]]]:
    chapters = load_chapters(source_root)
    selected_chapters = resolve_chapter_scope(chapters, through_chapter=through_chapter, chapters_arg=chapters_arg)
    specs, review_meta = build_specs(selected_chapters)
    write_outputs(output_root, selected_chapters, specs, review_meta)
    return specs, review_meta


def load_specs(output_root: Path) -> list[dict[str, object]]:
    return json.loads((output_root / "data/slide-specs.json").read_text(encoding="utf-8"))


def load_review_meta(output_root: Path) -> dict[str, dict[str, object]]:
    return json.loads((output_root / "data/chapter-review-metadata.json").read_text(encoding="utf-8"))


def parse_cli(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--through-chapter", default=None)
    scope.add_argument("--chapters", default=None, help="Comma-separated chapter ids. Opening chapter 00 is included automatically.")
    return parser.parse_args(argv)
