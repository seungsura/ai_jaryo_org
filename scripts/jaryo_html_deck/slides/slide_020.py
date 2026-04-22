from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide

def build() -> SlideSpec:
    return make_slide(
        20,
        title="Self-Refine / Reflexion",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-03",
        key_claim="출력 이후의 피드백 루프",
        chapter_label="CHAPTER 02",
        notes_intent="Self-Refine / Reflexion native feedback-loop diagrams",
        notes="source markdown의 Self-Refine, Reflexion row",
        body={
            "variant": "feedback-pair",
            "patterns": [
                {
                    "title": "Self-Refine",
                    "text": "자기 출력을 다시 비판하고 수정",
                    "meaning": "출력 이후의 피드백 루프",
                    "class": "self-refine-diagram",
                    "nodes": ["자기 출력", "비판", "수정", "피드백 루프"],
                },
                {
                    "title": "Reflexion",
                    "text": "자기 출력을 다시 비판하고 수정",
                    "meaning": "출력 이후의 피드백 루프",
                    "class": "reflexion-diagram",
                    "nodes": ["자기 출력", "비판", "수정", "피드백 루프"],
                },
            ],
        },
    )
