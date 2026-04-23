from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        59,
        title="3. Parallel: 같은 목표를 평면으로 벌리고 나중에 합친다",
        shell="process-flow-shell",
        source_section="06",
        source_block="06-06",
        key_claim="좋은 병렬은 서로를 더럽히지 않는 구조",
        chapter_label="CHAPTER 06",
        notes_intent="독립 lane과 merge 조건을 source 예시로 압축",
        notes="source lines 80-92, page 064 parallel lanes reference",
        body={
            "variant": "chapter-lanes",
            "lanes": [
                {"index": "A", "title": "대안 비교", "text": "세 가지 라이브러리 대안"},
                {"index": "B", "title": "설계안 생성", "text": "같은 요구사항에 여러 설계안"},
                {"index": "C", "title": "독립 점검", "text": "서로 다른 파일 묶음"},
            ],
            "merge": "Git Worktree · 별도 브랜치 · 별도 작업 디렉터리 · 출력 계약",
            "conclusion": "좋은 병렬은 서로를 더럽히지 않는 구조",
        },
    )
