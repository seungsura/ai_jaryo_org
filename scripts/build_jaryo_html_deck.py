#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
PROSE_ROOT = ROOT / "docs/02-seminar/prose"
HTML_ROOT = ROOT / "docs/03-html"
OUTLINE_PATH = HTML_ROOT / "outline/slide-outline.md"
MANIFEST_PATH = HTML_ROOT / "manifest.md"
SLIDES_ROOT = HTML_ROOT / "slides"
DECK_ROOT = HTML_ROOT / "deck"
DECK_PATH = DECK_ROOT / "index.html"
SCRIPT_PATH = DECK_ROOT / "script.md"
DATA_PATH = HTML_ROOT / "data/slide-specs.json"
SHARED_ROOT = HTML_ROOT / "shared"
TOKENS_CSS = SHARED_ROOT / "tokens.css"
BASE_CSS = SHARED_ROOT / "slide-base.css"

THEME = "theme-minimal-light"
FOOTER_LEFT = "Harness 잘 사용하기"

SECTION_TARGETS = {
    "00": 6,
    "01": 14,
    "02": 14,
    "03": 13,
    "04": 15,
    "05": 12,
    "06": 14,
    "07": 15,
    "08": 10,
    "09": 11,
    "90": 8,
}

SECTION_ORDER = list(SECTION_TARGETS)

SECTION_META = {
    "00": {
        "path": PROSE_ROOT / "00-overview.md",
        "chapter": "OPENING",
        "agenda_topic": "문제의식",
        "agenda_text": "왜 지금 하네스가 앞에 오는가",
    },
    "01": {
        "path": PROSE_ROOT / "01-where-coding-is-going.md",
        "chapter": "CHAPTER 01",
        "agenda_topic": "이동",
        "agenda_text": "숙련이 손끝에서 운영 구조로 옮겨 간다",
    },
    "02": {
        "path": PROSE_ROOT / "02-why-claude-code.md",
        "chapter": "CHAPTER 02",
        "agenda_topic": "수렴",
        "agenda_text": "도구 경쟁은 결국 하네스 경쟁으로 좁혀진다",
    },
    "03": {
        "path": PROSE_ROOT / "03-ai-era-methodology.md",
        "chapter": "CHAPTER 03",
        "agenda_topic": "방법",
        "agenda_text": "Spec-first와 TDD가 다시 앞줄로 나온다",
    },
    "04": {
        "path": PROSE_ROOT / "04-harness-and-context-engineering.md",
        "chapter": "CHAPTER 04",
        "agenda_topic": "구조",
        "agenda_text": "Prompt를 넘어서 하네스를 설계한다",
    },
    "05": {
        "path": PROSE_ROOT / "05-limitations-and-failure-patterns.md",
        "chapter": "CHAPTER 05",
        "agenda_topic": "실패",
        "agenda_text": "실패는 대개 조용히 누적되고 뒤늦게 터진다",
    },
    "06": {
        "path": PROSE_ROOT / "06-multi-agent-patterns.md",
        "chapter": "CHAPTER 06",
        "agenda_topic": "분해",
        "agenda_text": "멀티 에이전트는 병렬화보다 handoff 설계다",
    },
    "07": {
        "path": PROSE_ROOT / "07-practical-workflow-and-tooling.md",
        "chapter": "CHAPTER 07",
        "agenda_topic": "운영",
        "agenda_text": "좋은 workflow는 생성이 아니라 운영 구조다",
    },
    "08": {
        "path": PROSE_ROOT / "08-how-this-presentation-was-made.md",
        "chapter": "CHAPTER 08",
        "agenda_topic": "사례",
        "agenda_text": "이 발표가 만들어진 경로 자체를 해부한다",
    },
    "09": {
        "path": PROSE_ROOT / "09-what-we-should-do-next.md",
        "chapter": "CHAPTER 09",
        "agenda_topic": "실천",
        "agenda_text": "작업 환경에 하네스 습관을 박아 넣는다",
    },
    "90": {
        "path": PROSE_ROOT / "90-appendix-references.md",
        "chapter": "APPENDIX",
        "agenda_topic": "출처",
        "agenda_text": "근거의 층위를 섞지 않고 다시 읽는다",
    },
}

SHELL_TO_FAMILY = {
    "title-hero-shell": "title",
    "agenda-list-shell": "agenda",
    "section-divider-shell": "section",
    "statement-editorial-shell": "content",
    "wide-bullets-shell": "content",
    "process-flow-shell": "content",
    "split-compare-shell": "comparison",
    "evidence-table-shell": "content",
    "closing-shell": "conclusion",
}

SHELL_TO_LAYOUT = {
    "title-hero-shell": "centered",
    "agenda-list-shell": "wide",
    "section-divider-shell": "centered",
    "statement-editorial-shell": "editorial",
    "wide-bullets-shell": "wide",
    "process-flow-shell": "wide",
    "split-compare-shell": "split",
    "evidence-table-shell": "wide",
    "closing-shell": "centered",
}

SHELL_TO_TYPE = {
    "title-hero-shell": "title",
    "agenda-list-shell": "agenda",
    "section-divider-shell": "section",
    "statement-editorial-shell": "statement",
    "wide-bullets-shell": "bullets",
    "process-flow-shell": "process",
    "split-compare-shell": "comparison",
    "evidence-table-shell": "table",
    "closing-shell": "closing",
}

SECTION_KEYWORDS = {
    "00": ["Harness", "규칙", "검증"],
    "01": ["추상화", "문서", "역할"],
    "02": ["Prompt", "Context", "Harness"],
    "03": ["Spec-first", "TDD", "SDD"],
    "04": ["Agent", "Context", "Permissions"],
    "05": ["Long Context", "Rot", "Trust"],
    "06": ["Sub-Agent", "Parallel", "GAN"],
    "07": ["Write", "Select", "Compress"],
    "08": ["source", "outline", "Codex"],
    "09": ["rules", "gates", "Build to Delete"],
    "90": ["Public Source", "archive", "map"],
}

FILLER_TERMS = {
    "이 장은",
    "이 글은",
    "결국",
    "중요한 것은",
    "다만",
    "그래서",
    "즉",
    "하지만",
    "그리고",
    "또한",
    "여기서",
}


@dataclass
class ParsedBlock:
    section_id: str
    source_path: str
    heading: str
    level: int
    block_id: str
    paragraphs: list[str] = field(default_factory=list)
    lists: list[list[str]] = field(default_factory=list)
    tables: list[list[list[str]]] = field(default_factory=list)


@dataclass
class SlideSpec:
    order: int
    slide_id: str
    file_name: str
    title: str
    slide_type: str
    layout: str
    shell: str
    family: str
    density: str
    source_section: str
    source_block: str
    key_claim: str
    notes_intent: str
    notes_status: str
    status: str
    chapter_label: str
    notes: str
    lead: str = ""
    footer_left: str = FOOTER_LEFT
    body: dict[str, object] = field(default_factory=dict)


def strip_markdown(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("—", " ").replace("→", " ")
    return re.sub(r"\s+", " ", text).strip()


def clean_heading(heading: str) -> str:
    text = strip_markdown(heading)
    text = re.sub(r"^\d+\.\s*", "", text).strip()
    if ":" in text:
        left, right = [part.strip() for part in text.split(":", 1)]
        if 4 <= len(right) <= 30:
            return right
        return f"{left} {right}".strip()
    return text


def sentence_split(text: str) -> list[str]:
    cleaned = strip_markdown(text)
    parts = re.split(r"(?<=[.!?])\s+|\n+", cleaned)
    return [part.strip() for part in parts if part.strip()]


def trim_phrase(text: str, limit: int = 28) -> str:
    text = strip_markdown(text)
    text = re.sub(r"\([^)]*\)", "", text).strip()
    text = re.sub(r"^[\"'“”‘’]+|[\"'“”‘’]+$", "", text).strip()
    text = re.sub(
        r"(입니다|합니다|했습니다|되었습니다|있었습니다|였습니다|한다|된다|있다|없다|이다|였다|보인다|의미한다|설명한다)\.?$",
        "",
        text,
    )
    for filler in FILLER_TERMS:
        if text.startswith(filler):
            text = text[len(filler) :].strip()
    for token in [",", ";", ":", " - ", " — ", " / "]:
        if token in text:
            candidate = text.split(token, 1)[0].strip()
            if 4 <= len(candidate) <= limit:
                text = candidate
                break
    if len(text) <= limit:
        return text
    shortened = text[:limit].rstrip()
    if " " in shortened:
        shortened = shortened.rsplit(" ", 1)[0]
    return shortened.strip(" ,.;:-")


def unique_phrases(items: Iterable[str], *, limit: int = 28, max_items: int = 4) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        phrase = trim_phrase(item, limit=limit)
        if len(phrase) < 4 or phrase in seen:
            continue
        seen.add(phrase)
        result.append(phrase)
        if len(result) == max_items:
            break
    return result


def even_groups(items: list[str], groups: int) -> list[list[str]]:
    if groups <= 0:
        return []
    if not items:
        return [[] for _ in range(groups)]
    base, extra = divmod(len(items), groups)
    result: list[list[str]] = []
    cursor = 0
    for index in range(groups):
        size = base + (1 if index < extra else 0)
        if size == 0:
            result.append([])
            continue
        result.append(items[cursor : cursor + size])
        cursor += size
    return result


def parse_blocks(section_id: str, path: Path) -> tuple[str, list[ParsedBlock]]:
    title = ""
    blocks: list[ParsedBlock] = []
    current_heading = ""
    current_level = 2
    current_lines: list[str] = []
    block_index = 0

    def flush() -> None:
        nonlocal block_index, current_lines
        if not current_heading:
            current_lines = []
            return

        block_index += 1
        paragraphs: list[str] = []
        lists: list[list[str]] = []
        tables: list[list[list[str]]] = []

        lines = current_lines[:]
        cursor = 0
        while cursor < len(lines):
            line = lines[cursor].rstrip()
            stripped = line.strip()
            if not stripped:
                cursor += 1
                continue

            if stripped.startswith("|"):
                table_lines: list[str] = []
                while cursor < len(lines) and lines[cursor].strip().startswith("|"):
                    table_lines.append(lines[cursor].strip())
                    cursor += 1
                row_matrix: list[list[str]] = []
                for table_line in table_lines:
                    cells = [strip_markdown(cell) for cell in table_line.strip("|").split("|")]
                    if cells and set("".join(cells)) == {"-"}:
                        continue
                    if cells:
                        row_matrix.append(cells)
                if row_matrix:
                    tables.append(row_matrix)
                continue

            if re.match(r"^(-|\*|\d+\.)\s+", stripped):
                bullet_lines: list[str] = []
                while cursor < len(lines) and re.match(r"^(-|\*|\d+\.)\s+", lines[cursor].strip()):
                    bullet_lines.append(re.sub(r"^(-|\*|\d+\.)\s+", "", lines[cursor].strip()))
                    cursor += 1
                if bullet_lines:
                    lists.append(bullet_lines)
                continue

            paragraph_lines = [stripped]
            cursor += 1
            while cursor < len(lines):
                next_line = lines[cursor].strip()
                if not next_line:
                    cursor += 1
                    break
                if next_line.startswith("|") or re.match(r"^(-|\*|\d+\.)\s+", next_line):
                    break
                paragraph_lines.append(next_line)
                cursor += 1
            paragraphs.append(" ".join(paragraph_lines))

        blocks.append(
            ParsedBlock(
                section_id=section_id,
                source_path=str(path.relative_to(ROOT)),
                heading=clean_heading(current_heading),
                level=current_level,
                block_id=f"{section_id}-{block_index:02d}",
                paragraphs=paragraphs,
                lists=lists,
                tables=tables,
            )
        )
        current_lines = []

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if raw_line.startswith("# "):
            title = clean_heading(raw_line[2:])
            continue
        if raw_line.startswith("## "):
            flush()
            current_heading = raw_line[3:].strip()
            current_level = 2
            current_lines = []
            continue
        if raw_line.startswith("### "):
            flush()
            current_heading = raw_line[4:].strip()
            current_level = 3
            current_lines = []
            continue
        current_lines.append(raw_line)

    flush()
    return title, blocks


def block_weight(block: ParsedBlock) -> int:
    sentence_count = sum(len(sentence_split(paragraph)) for paragraph in block.paragraphs)
    list_weight = sum(len(items) for items in block.lists)
    table_weight = sum(len(rows) for rows in block.tables) * 2
    return max(1, sentence_count + list_weight + table_weight)


def allocate_slots(blocks: list[ParsedBlock], total: int) -> list[int]:
    allocations = [1] * len(blocks)
    remaining = total - len(blocks)
    if remaining <= 0:
        return allocations

    scores = [block_weight(block) for block in blocks]
    while remaining > 0:
        best_index = max(
            range(len(blocks)),
            key=lambda index: (scores[index] / allocations[index], scores[index], -index),
        )
        allocations[best_index] += 1
        remaining -= 1
    return allocations


def sentences_for_block(block: ParsedBlock) -> list[str]:
    sentences: list[str] = []
    for paragraph in block.paragraphs:
        sentences.extend(sentence_split(paragraph))
    for items in block.lists:
        sentences.extend(strip_markdown(item) for item in items)
    return sentences


def source_lines(block: ParsedBlock, groups: int) -> list[list[str]]:
    sentences = sentences_for_block(block)
    if not sentences:
        sentences = [block.heading]
    return even_groups(sentences, groups)


def chunk_title(block: ParsedBlock, lines: list[str], index: int) -> str:
    base = clean_heading(block.heading)
    if index == 0:
        return trim_phrase(base, limit=26)
    for line in lines:
        phrase = trim_phrase(line, limit=24)
        if phrase and phrase != base:
            return phrase
    return trim_phrase(base, limit=26)


def chunk_claim(block: ParsedBlock, lines: list[str]) -> str:
    candidates = [block.heading, *lines]
    phrases = unique_phrases(candidates, limit=34, max_items=1)
    return phrases[0] if phrases else trim_phrase(block.heading, limit=34)


def extract_points(lines: list[str], block: ParsedBlock, count: int = 3) -> list[str]:
    points = unique_phrases(lines, limit=26, max_items=count)
    if len(points) >= count:
        return points[:count]
    fallback = unique_phrases(block.paragraphs + [block.heading], limit=26, max_items=count)
    for item in fallback:
        if item not in points:
            points.append(item)
        if len(points) == count:
            break
    while len(points) < count:
        points.append(trim_phrase(block.heading, limit=24))
    return points[:count]


def intro_slide_specs(
    order: int, section_titles: dict[str, str], blocks_by_section: dict[str, list[ParsedBlock]]
) -> list[SlideSpec]:
    cover_points = [
        "코딩보다 운영 구조가 먼저 온다",
        "도구 경쟁은 하네스 경쟁으로 좁혀진다",
        "실패 패턴과 workflow까지 같이 본다",
    ]
    cover = SlideSpec(
        order=order,
        slide_id=f"S{order:03d}",
        file_name=f"slide-{order:03d}.html",
        title=section_titles["00"],
        slide_type="title",
        layout="centered",
        shell="title-hero-shell",
        family="title",
        density="light",
        source_section="00",
        source_block="00-00",
        key_claim="좋은 모델보다 좋은 하네스가 앞에 선다",
        notes_intent="문제의식과 발표 범위를 한 번에 고정",
        notes_status="ready",
        status="built",
        chapter_label=SECTION_META["00"]["chapter"],
        notes="오늘의 질문은 모델 성능이 아니다. 에이전트가 일할 구조를 어떻게 설계하는지가 핵심이라는 점부터 잠근다.",
        lead="챗봇과 씨름하는 대신, 에이전트가 일할 구조를 짠다",
        body={"points": cover_points},
    )

    agenda_items = [
        {
            "number": f"{index:02d}",
            "topic": SECTION_META[section_id]["agenda_topic"],
            "text": SECTION_META[section_id]["agenda_text"],
        }
        for index, section_id in enumerate(["01", "02", "03", "04", "05", "06", "07", "08", "09", "90"], start=1)
    ]
    agenda = SlideSpec(
        order=order + 1,
        slide_id=f"S{order + 1:03d}",
        file_name=f"slide-{order + 1:03d}.html",
        title="전체 구조",
        slide_type="agenda",
        layout="wide",
        shell="agenda-list-shell",
        family="agenda",
        density="medium",
        source_section="00",
        source_block="00-00",
        key_claim="이 덱은 이동, 수렴, 방법, 구조, 실패, 분해, 운영, 사례, 실천, 출처 순으로 읽힌다",
        notes_intent="청중이 132장 전체 지도를 먼저 잡게 만든다",
        notes_status="ready",
        status="built",
        chapter_label=SECTION_META["00"]["chapter"],
        notes="장수가 많아도 흐름은 단순하다. 전체 지도를 먼저 잡아 두면 뒤의 세부 슬라이드는 길을 잃지 않는다.",
        lead="이동에서 실천까지, 그리고 마지막에 출처로 닫는다",
        body={"items": agenda_items},
    )

    overview_blocks = blocks_by_section["00"]
    section_map: list[SlideSpec] = []
    order_cursor = order + 2
    for index, block in enumerate(overview_blocks, start=1):
        lines = sentences_for_block(block)
        if index == 2:
            shell = "statement-editorial-shell"
            title = "운영 구조가 앞선다"
            body = {
                "tag": "KEY MESSAGE",
                "statement": chunk_claim(block, lines),
                "support": trim_phrase("프롬프트와 컨텍스트만으로는 긴 작업을 버티지 못한다", limit=32),
                "chips": extract_points(lines, block, count=3),
            }
        elif index == 3:
            shell = "process-flow-shell"
            title = "앞으로 다룰 이야기"
            items = [
                {"index": "01", "title": "이동", "text": "코딩의 중심이 어디로 가는가"},
                {"index": "02", "title": "수렴", "text": "왜 도구가 Harness로 모이는가"},
                {"index": "03", "title": "운영", "text": "실패와 workflow를 어떻게 다루는가"},
                {"index": "04", "title": "실천", "text": "이 구조를 작업 습관으로 옮기는 법"},
            ]
            body = {"steps": items}
        else:
            shell = "wide-bullets-shell"
            title = clean_heading(block.heading)
            body = {
                "callout": chunk_claim(block, lines),
                "points": extract_points(lines, block, count=4),
            }

        section_map.append(
            SlideSpec(
                order=order_cursor,
                slide_id=f"S{order_cursor:03d}",
                file_name=f"slide-{order_cursor:03d}.html",
                title=title,
                slide_type=SHELL_TO_TYPE[shell],
                layout=SHELL_TO_LAYOUT[shell],
                shell=shell,
                family=SHELL_TO_FAMILY[shell],
                density="medium" if shell != "statement-editorial-shell" else "light",
                source_section="00",
                source_block=block.block_id,
                key_claim=chunk_claim(block, lines),
                notes_intent="opening narrative를 짧은 리듬으로 쪼갠다",
                notes_status="ready",
                status="built",
                chapter_label=SECTION_META["00"]["chapter"],
                notes=f"{trim_phrase(block.heading, limit=30)}를 먼저 고정한다. 세부 근거는 뒤 슬라이드에서 더 잘게 펼친다.",
                lead=trim_phrase(block.paragraphs[0] if block.paragraphs else block.heading, limit=34),
                body=body,
            )
        )
        order_cursor += 1

    section_map.append(
        SlideSpec(
            order=order_cursor,
            slide_id=f"S{order_cursor:03d}",
            file_name=f"slide-{order_cursor:03d}.html",
            title="더 나은 Harness",
            slide_type="statement",
            layout="editorial",
            shell="statement-editorial-shell",
            family="content",
            density="light",
            source_section="00",
            source_block="00-03",
            key_claim="경쟁력은 더 좋은 모델보다 더 나은 하네스에서 갈린다",
            notes_intent="opening chapter를 한 문장으로 봉합",
            notes_status="ready",
            status="built",
            chapter_label=SECTION_META["00"]["chapter"],
            notes="서론의 마지막에서는 질문을 다시 한 문장으로 닫는다. 뒤의 100장 넘는 세부도 결국 이 문장을 증명하는 과정이라는 점을 다시 박아 둔다.",
            lead="도구보다 운영 구조가 앞에 선다",
            body={
                "tag": "THESIS",
                "statement": "좋은 모델보다 좋은 하네스",
                "support": "문맥, 권한, 검증, 상태 기록이 결과를 바꾼다",
                "chips": ["Context", "Permissions", "Verify"],
            },
        )
    )

    return [cover, agenda, *section_map]


def section_divider(order: int, section_id: str, title: str, blocks: list[ParsedBlock]) -> SlideSpec:
    keywords = SECTION_KEYWORDS[section_id]
    first_block = blocks[0]
    short_line = trim_phrase(first_block.paragraphs[0] if first_block.paragraphs else first_block.heading, limit=34)
    return SlideSpec(
        order=order,
        slide_id=f"S{order:03d}",
        file_name=f"slide-{order:03d}.html",
        title=trim_phrase(title, limit=30),
        slide_type="section",
        layout="centered",
        shell="section-divider-shell",
        family="section",
        density="light",
        source_section=section_id,
        source_block=f"{section_id}-00",
        key_claim=trim_phrase(title, limit=34),
        notes_intent=f"{section_id}장의 질문을 챕터 단위로 고정",
        notes_status="ready",
        status="built",
        chapter_label=SECTION_META[section_id]["chapter"],
        notes=f"{title}에서 무엇을 묻는지 먼저 잠근다. 지금부터는 세부 논지를 2~3문장 단위로 분해해 본다.",
        lead=short_line,
        body={"keywords": keywords},
    )


def determine_shell(block: ParsedBlock, lines: list[str], index: int, total_chunks: int, section_id: str) -> str:
    heading = block.heading
    if block.tables and index == 0:
        return "evidence-table-shell"
    if block.lists and 3 <= len(block.lists[0]) <= 5:
        return "process-flow-shell"
    if any(token in heading for token in ["연대기", "순서", "원칙", "패턴", "네 동사", "세 단계", "다섯", "5대", "루프", "워크플로우"]):
        return "process-flow-shell"
    if any(token in heading for token in ["다른가", "경쟁", "층위", "비교", "지도", "맵", "전환"]):
        return "split-compare-shell"
    if "결론" in heading or "정리" in heading:
        return "statement-editorial-shell"
    if section_id == "90" and ("근거" in heading or "map" in heading.lower()):
        return "split-compare-shell"
    if total_chunks == 1 and len(lines) <= 2:
        return "statement-editorial-shell"
    return "wide-bullets-shell"


def build_process_steps(block: ParsedBlock, lines: list[str]) -> list[dict[str, str]]:
    if block.lists:
        raw_items = block.lists[0][:4]
    elif block.tables:
        raw_items = [" / ".join(row[:2]) for row in block.tables[0][1:5]]
    else:
        raw_items = extract_points(lines, block, count=4)
    steps: list[dict[str, str]] = []
    for index, item in enumerate(raw_items, start=1):
        steps.append(
            {
                "index": f"{index:02d}",
                "title": trim_phrase(item, limit=18),
                "text": trim_phrase(item, limit=24),
            }
        )
    while len(steps) < 3:
        index = len(steps) + 1
        steps.append({"index": f"{index:02d}", "title": trim_phrase(block.heading, limit=18), "text": trim_phrase(block.heading, limit=24)})
    return steps


def build_compare_columns(block: ParsedBlock, lines: list[str]) -> dict[str, object]:
    points = extract_points(lines, block, count=4)
    left_points = points[:2]
    right_points = points[2:] if len(points) > 2 else points[:2]
    labels = ("축 A", "축 B")
    heading = block.heading
    if any(token in heading for token in ["전", "이전", "Before"]):
        labels = ("이전", "이후")
    elif "층위" in heading:
        labels = ("바깥 기준", "안쪽 기준")
    elif "경쟁" in heading:
        labels = ("표면", "실제 축")
    return {
        "left_label": labels[0],
        "left_points": left_points,
        "right_label": labels[1],
        "right_points": right_points,
    }


def build_table(block: ParsedBlock, lines: list[str]) -> dict[str, object]:
    if block.tables:
        table = block.tables[0]
        headers = [trim_phrase(cell, limit=18) for cell in table[0][:3]]
        rows = [[trim_phrase(cell, limit=18) for cell in row[:3]] for row in table[1:5]]
        return {"headers": headers, "rows": rows}
    points = extract_points(lines, block, count=4)
    rows = [[str(index), point, trim_phrase(block.heading, limit=18)] for index, point in enumerate(points, start=1)]
    return {"headers": ["#","포인트","섹션"], "rows": rows}


def build_chunk_slide(
    order: int,
    section_id: str,
    block: ParsedBlock,
    lines: list[str],
    index: int,
    total_chunks: int,
) -> SlideSpec:
    shell = determine_shell(block, lines, index, total_chunks, section_id)
    title = chunk_title(block, lines, index)
    claim = chunk_claim(block, lines)
    lead = trim_phrase(lines[0] if lines else block.heading, limit=34)
    body: dict[str, object]

    if shell == "statement-editorial-shell":
        body = {
            "tag": SECTION_META[section_id]["agenda_topic"].upper(),
            "statement": claim,
            "support": trim_phrase(lines[1] if len(lines) > 1 else block.heading, limit=30),
            "chips": extract_points(lines, block, count=3),
        }
    elif shell == "process-flow-shell":
        body = {"steps": build_process_steps(block, lines)}
    elif shell == "split-compare-shell":
        body = build_compare_columns(block, lines)
    elif shell == "evidence-table-shell":
        body = build_table(block, lines)
    else:
        body = {
            "callout": claim,
            "points": extract_points(lines, block, count=4),
        }

    return SlideSpec(
        order=order,
        slide_id=f"S{order:03d}",
        file_name=f"slide-{order:03d}.html",
        title=title,
        slide_type=SHELL_TO_TYPE[shell],
        layout=SHELL_TO_LAYOUT[shell],
        shell=shell,
        family=SHELL_TO_FAMILY[shell],
        density="medium" if shell not in {"statement-editorial-shell", "closing-shell"} else "light",
        source_section=section_id,
        source_block=block.block_id,
        key_claim=claim,
        notes_intent=f"{clean_heading(block.heading)}를 slide 단위 주장으로 분해",
        notes_status="ready",
        status="built",
        chapter_label=SECTION_META[section_id]["chapter"],
        notes=f"{claim}를 먼저 말한다. 이어서 {trim_phrase(block.heading, limit=24)}의 근거를 짧게 보강한다.",
        lead=lead,
        body=body,
    )


def build_section_slides(
    start_order: int,
    section_id: str,
    section_title: str,
    blocks: list[ParsedBlock],
) -> list[SlideSpec]:
    target = SECTION_TARGETS[section_id]
    slides = [section_divider(start_order, section_id, section_title, blocks)]
    content_target = target - 1
    allocations = allocate_slots(blocks, content_target)
    order = start_order + 1

    for block, allocation in zip(blocks, allocations):
        groups = source_lines(block, allocation)
        for index, group in enumerate(groups):
            slides.append(build_chunk_slide(order, section_id, block, group, index, len(groups)))
            order += 1

    if section_id == "90":
        slides[-1].shell = "closing-shell"
        slides[-1].slide_type = "closing"
        slides[-1].layout = "centered"
        slides[-1].family = "conclusion"
        slides[-1].density = "light"
        slides[-1].title = "다시 열어볼 로컬 지도"
        slides[-1].key_claim = "근거의 층위를 섞지 않는 읽기 습관이 마지막 안전장치다"
        slides[-1].lead = "공개 근거를 앞줄에, 로컬 지도는 뒤줄에 둔다"
        slides[-1].body = {
            "points": [
                "공개 근거를 먼저 세운다",
                "내부 맥락은 뒤에서 보강한다",
                "로컬 map은 연결망으로만 쓴다",
            ]
        }
        slides[-1].notes = "마지막 슬라이드는 새 주장 추가가 아니다. 어디를 먼저 읽고 어디를 나중에 읽을지, 읽기 순서 자체를 다시 고정한다."

    return slides


def build_all_specs() -> list[SlideSpec]:
    titles: dict[str, str] = {}
    blocks_by_section: dict[str, list[ParsedBlock]] = {}
    for section_id in SECTION_ORDER:
        title, blocks = parse_blocks(section_id, SECTION_META[section_id]["path"])
        titles[section_id] = title
        blocks_by_section[section_id] = blocks

    specs = intro_slide_specs(1, titles, blocks_by_section)
    next_order = len(specs) + 1
    for section_id in SECTION_ORDER[1:]:
        section_specs = build_section_slides(next_order, section_id, titles[section_id], blocks_by_section[section_id])
        specs.extend(section_specs)
        next_order = len(specs) + 1

    assert len(specs) == sum(SECTION_TARGETS.values()), len(specs)
    return specs


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    header_row = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    body_rows = ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join([header_row, separator, *body_rows])


def render_outline(specs: list[SlideSpec]) -> str:
    lines = [
        "# Slide Outline",
        "",
        "- status: 132-slide make-slide rebuild",
        "- canonical prose source: `docs/02-seminar/prose/`",
        "- output deck: `docs/03-html/deck/index.html`",
        "- output script: `docs/03-html/deck/script.md`",
        "- theme: `minimal-light`",
        "- runtime policy: single-file deck, keyboard navigation, active slide switching, print CSS, `data-notes`",
        "",
        "## Section Targets",
        "",
        markdown_table(
            ["section", "source", "target slides"],
            [
                [section_id, f"`{SECTION_META[section_id]['path'].relative_to(ROOT)}`", str(SECTION_TARGETS[section_id])]
                for section_id in SECTION_ORDER
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

    lines = [
        "# HTML Manifest",
        "",
        "- current status: 132-slide deck built",
        "- active theme: `theme-minimal-light`",
        "- slide id format: `S001`-`S132`",
        "- slide file format: `slide-001.html`-`slide-132.html`",
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
    return "\n".join(lines)


def render_script(specs: list[SlideSpec]) -> str:
    parts = ["# Seminar Script", "", "- target deck: `docs/03-html/deck/index.html`", ""]
    for spec in specs:
        points = []
        if "points" in spec.body:
            points = list(spec.body["points"])[:3]
        elif "steps" in spec.body:
            points = [step["text"] for step in spec.body["steps"]][:3]
        elif "left_points" in spec.body:
            points = list(spec.body["left_points"])[:2] + list(spec.body["right_points"])[:2]
        elif "rows" in spec.body:
            points = [" / ".join(row) for row in spec.body["rows"][:3]]
        else:
            points = [spec.key_claim]

        parts.extend(
            [
                f"## {spec.slide_id} {spec.title}",
                f"- intent: {spec.notes_intent}",
                f"- opening: {spec.key_claim}부터 말한다.",
                f"- bridge: {spec.notes}",
                "- beats:",
                *[f"  - {point}" for point in points[:3]],
                "",
            ]
        )
    return "\n".join(parts).rstrip() + "\n"


def attr_escape(text: str) -> str:
    return html.escape(text, quote=True)


def text_node(tag: str, class_name: str, text: str) -> str:
    return f'<{tag} class="{class_name}">{html.escape(text)}</{tag}>'


def render_footer(spec: SlideSpec) -> str:
    return (
        '<footer class="footer">'
        f'<span class="footer-left">{html.escape(spec.footer_left)}</span>'
        f'<span class="footer-right">{spec.order}</span>'
        "</footer>"
    )


def render_shell(spec: SlideSpec) -> str:
    if spec.shell == "title-hero-shell":
        points = "".join(
            f'<li class="hero-point">{html.escape(point)}</li>'
            for point in spec.body.get("points", [])
        )
        return (
            '<section class="cover-main">'
            '<div class="cover-rule"></div>'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f'<p class="lead-placeholder">{html.escape(spec.lead)}</p>'
            f'<ul class="hero-points">{points}</ul>'
            "</section>"
        )

    if spec.shell == "agenda-list-shell":
        items = "".join(
            '<li class="agenda-item">'
            f'<span class="agenda-number">{html.escape(item["number"])}</span>'
            f'<span class="agenda-topic">{html.escape(item["topic"])}</span>'
            f'<span class="agenda-text">{html.escape(item["text"])}</span>'
            "</li>"
            for item in spec.body.get("items", [])
        )
        return (
            '<section class="agenda-header">'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f'<p class="lead-placeholder">{html.escape(spec.lead)}</p>'
            "</section>"
            f'<ol class="agenda-list">{items}</ol>'
        )

    if spec.shell == "section-divider-shell":
        keywords = "".join(
            f'<li class="section-keyword">{html.escape(keyword)}</li>'
            for keyword in spec.body.get("keywords", [])
        )
        return (
            '<section class="section-main">'
            f'<p class="chapter-marker">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f'<p class="short-line">{html.escape(spec.lead)}</p>'
            f'<ul class="section-keywords">{keywords}</ul>'
            "</section>"
        )

    if spec.shell == "statement-editorial-shell":
        chips = "".join(
            f'<li class="statement-chip">{html.escape(chip)}</li>'
            for chip in spec.body.get("chips", [])
        )
        return (
            '<section class="statement-panel">'
            f'<p class="statement-tag">{html.escape(spec.body.get("tag", spec.chapter_label))}</p>'
            f'<h1 class="statement-text">{html.escape(spec.body.get("statement", spec.key_claim))}</h1>'
            f'<p class="statement-support">{html.escape(spec.body.get("support", spec.lead))}</p>'
            f'<ul class="statement-chips">{chips}</ul>'
            "</section>"
        )

    if spec.shell == "process-flow-shell":
        steps = "".join(
            '<li class="process-step">'
            f'<span class="step-index">{html.escape(step["index"])}</span>'
            f'<span class="step-title">{html.escape(step["title"])}</span>'
            f'<span class="step-copy">{html.escape(step["text"])}</span>'
            "</li>"
            for step in spec.body.get("steps", [])
        )
        return (
            '<section class="top-band">'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f'<p class="lead-placeholder">{html.escape(spec.lead)}</p>'
            "</section>"
            '<section class="body-area">'
            f'<ol class="process-track">{steps}</ol>'
            "</section>"
        )

    if spec.shell == "split-compare-shell":
        left_points = "".join(
            f'<li class="compare-point">{html.escape(point)}</li>'
            for point in spec.body.get("left_points", [])
        )
        right_points = "".join(
            f'<li class="compare-point">{html.escape(point)}</li>'
            for point in spec.body.get("right_points", [])
        )
        return (
            '<section class="top-band">'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f'<p class="lead-placeholder">{html.escape(spec.lead)}</p>'
            "</section>"
            '<section class="compare-grid">'
            '<article class="compare-col">'
            f'<p class="compare-label">{html.escape(spec.body.get("left_label", "축 A"))}</p>'
            f'<ul class="compare-list">{left_points}</ul>'
            "</article>"
            '<article class="compare-col is-focus">'
            f'<p class="compare-label">{html.escape(spec.body.get("right_label", "축 B"))}</p>'
            f'<ul class="compare-list">{right_points}</ul>'
            "</article>"
            "</section>"
        )

    if spec.shell == "evidence-table-shell":
        headers = "".join(f"<th>{html.escape(header)}</th>" for header in spec.body.get("headers", []))
        rows = "".join(
            "<tr>" + "".join(f"<td>{html.escape(cell)}</td>" for cell in row) + "</tr>"
            for row in spec.body.get("rows", [])
        )
        return (
            '<section class="top-band">'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f'<p class="lead-placeholder">{html.escape(spec.lead)}</p>'
            "</section>"
            '<section class="table-wrap">'
            f'<div class="table-callout">{html.escape(spec.key_claim)}</div>'
            '<table class="data-table">'
            f"<thead><tr>{headers}</tr></thead>"
            f"<tbody>{rows}</tbody>"
            "</table>"
            "</section>"
        )

    if spec.shell == "closing-shell":
        points = "".join(
            f'<li class="closing-point">{html.escape(point)}</li>'
            for point in spec.body.get("points", [])
        )
        return (
            '<section class="closing-main">'
            '<div class="cover-rule"></div>'
            f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
            f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
            f'<p class="lead-placeholder">{html.escape(spec.lead)}</p>'
            f'<ul class="closing-points">{points}</ul>'
            "</section>"
        )

    points = "".join(
        f'<li class="bullet-item">{html.escape(point)}</li>'
        for point in spec.body.get("points", [])
    )
    return (
        '<section class="top-band">'
        f'<p class="chapter-label">{html.escape(spec.chapter_label)}</p>'
        f'<h1 class="title-placeholder">{html.escape(spec.title)}</h1>'
        f'<p class="lead-placeholder">{html.escape(spec.lead)}</p>'
        "</section>"
        '<section class="body-area">'
        f'<div class="callout-card">{html.escape(spec.body.get("callout", spec.key_claim))}</div>'
        f'<ul class="bullet-list">{points}</ul>'
        "</section>"
    )


def render_slide_markup(spec: SlideSpec) -> str:
    return (
        f'<main class="slide family-{spec.family} layout-{spec.layout} density-{spec.density}" '
        f'data-slide-id="{spec.slide_id}" '
        f'data-shell="{spec.shell}" '
        f'data-notes="{attr_escape(spec.notes)}" '
        'data-footer="default">'
        f"{render_shell(spec)}"
        f"{render_footer(spec)}"
        "</main>"
    )


def render_slide_file(spec: SlideSpec) -> str:
    return "\n".join(
        [
            "<!DOCTYPE html>",
            '<html lang="ko">',
            "<head>",
            '<meta charset="UTF-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            f"<title>{html.escape(spec.title)}</title>",
            '<link rel="stylesheet" href="../shared/tokens.css">',
            '<link rel="stylesheet" href="../shared/slide-base.css">',
            "</head>",
            f'<body class="{THEME}">',
            render_slide_markup(spec),
            "</body>",
            "</html>",
            "",
        ]
    )


def render_deck(specs: list[SlideSpec]) -> str:
    tokens = TOKENS_CSS.read_text(encoding="utf-8")
    base = BASE_CSS.read_text(encoding="utf-8")
    wrappers = []
    for spec in specs:
        active = " active" if spec.order == 1 else ""
        wrappers.append(f'<section class="deck-slide{active}" data-slide-id="{spec.slide_id}">{render_slide_markup(spec)}</section>')

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Harness를 설계하는 법</title>
<style>
{tokens}
{base}
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
.deck {{
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}}
.deck-slide {{
  position: absolute;
  inset: 0;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 24px;
  overflow: hidden;
}}
.deck-slide.active {{
  display: flex;
}}
.deck-slide .slide {{
  transform: scale(var(--deck-scale));
  transform-origin: center center;
  box-shadow: 0 24px 80px rgba(0, 0, 0, 0.08);
}}
@media print {{
  html, body {{
    overflow: visible;
    height: auto;
    background: #fff;
  }}
  .deck {{
    height: auto;
    overflow: visible;
  }}
  .deck-slide {{
    position: relative;
    display: block !important;
    page-break-after: always;
    page-break-inside: avoid;
    padding: 0;
  }}
  .deck-slide .slide {{
    transform: none !important;
    box-shadow: none;
  }}
  @page {{
    size: landscape;
    margin: 0;
  }}
}}
</style>
</head>
<body>
<div class="deck">
{''.join(wrappers)}
</div>
<script>
const slides = Array.from(document.querySelectorAll('.deck-slide'));
let currentIndex = 0;
let touchStartX = 0;

function updateScale() {{
  const widthScale = window.innerWidth / 1280;
  const heightScale = window.innerHeight / 720;
  const scale = Math.min(widthScale, heightScale);
  document.documentElement.style.setProperty('--deck-scale', String(scale));
}}

function goTo(index) {{
  const bounded = Math.max(0, Math.min(index, slides.length - 1));
  slides[currentIndex].classList.remove('active');
  currentIndex = bounded;
  slides[currentIndex].classList.add('active');
}}

window.addEventListener('resize', updateScale);
window.addEventListener('keydown', (event) => {{
  if (event.key === 'ArrowRight' || event.key === ' ') {{
    event.preventDefault();
    goTo(currentIndex + 1);
  }}
  if (event.key === 'ArrowLeft') {{
    event.preventDefault();
    goTo(currentIndex - 1);
  }}
}});

window.addEventListener('touchstart', (event) => {{
  touchStartX = event.changedTouches[0].clientX;
}});

window.addEventListener('touchend', (event) => {{
  const delta = event.changedTouches[0].clientX - touchStartX;
  if (delta < -40) goTo(currentIndex + 1);
  if (delta > 40) goTo(currentIndex - 1);
}});

updateScale();
</script>
</body>
</html>
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def clean_generated_slides() -> None:
    SLIDES_ROOT.mkdir(parents=True, exist_ok=True)
    for path in SLIDES_ROOT.glob("slide-*.html"):
        path.unlink()


def main() -> None:
    specs = build_all_specs()
    clean_generated_slides()

    for spec in specs:
        write(SLIDES_ROOT / spec.file_name, render_slide_file(spec))

    write(OUTLINE_PATH, render_outline(specs))
    write(MANIFEST_PATH, render_manifest(specs))
    write(SCRIPT_PATH, render_script(specs))
    write(DECK_PATH, render_deck(specs))
    write(DATA_PATH, json.dumps([asdict(spec) for spec in specs], ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
