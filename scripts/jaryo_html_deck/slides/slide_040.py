from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        40,
        title="Context Engineering",
        shell="process-flow-shell",
        source_section="04",
        source_block="04-06",
        key_claim="smallest set of high-signal tokens",
        chapter_label="CHAPTER 04",
        notes_intent="Write, Select, Compress, Isolate 네 전략",
        notes="좋은 컨텍스트는 넓은 컨텍스트가 아니라 선별된 컨텍스트",
        body={
            "variant": "context-quote",
            "steps": [
                {"index": "01", "title": "Write", "text": "역할, 목표, 금지, 출력, 검증 기준을 구조화"},
                {"index": "02", "title": "Select", "text": "지금 필요한 문서와 파일만 선택"},
                {"index": "03", "title": "Compress", "text": "결정, 남은 일, 증거 중심으로 압축"},
                {"index": "04", "title": "Isolate", "text": "대량 탐색과 로그 분석은 격리"},
            ],
            "thesis": "smallest set of high-signal tokens",
            "source_label": "Anthropic Research",
        },
    )
