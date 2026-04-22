from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        78,
        title="cmux와 Git Worktree",
        shell="process-flow-shell",
        source_section="07",
        source_block="07-10",
        key_claim="창과 작업 디렉터리를 나누어 메인 컨텍스트를 보호",
        chapter_label="CHAPTER 07",
        notes_intent="four-window workspace map",
        notes="source lines 139-152, page 073 reference",
        body={
            "variant": "chapter-workspace-map",
            "windows": [
                {"index": "창 1", "title": "메인 구현 세션", "text": "결정과 통합"},
                {"index": "창 2", "title": "조사와 탐색 전용", "text": "코드베이스 탐색과 문서 검색"},
                {"index": "창 3", "title": "테스트와 감시 로그", "text": "테스트·빌드 로그 확인"},
                {"index": "창 4", "title": "이슈와 PR 정리", "text": "이슈 확인, PR 생성"},
            ],
            "conclusion": "Git Worktree는 이 분리를 파일 시스템 수준에서 고정",
        },
    )
