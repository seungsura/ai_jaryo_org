# Subagent Task Template

Use this wrapper when spawning a project subagent.

```text
목표
<what the subagent must achieve>

범위
<files or sections it may read or edit>

입력 파일
<specific markdown/doc paths>

HTML 관련 작업 필수 입력
- `AGENTS.md`
- `.codex/subagents/README.md`
- `.codex/templates/subagent-task-template.md`
- `docs/03-html/shared/slide-quality-rules.md`
- `docs/03-html/shared/decision-log.md`
- 대상 source markdown
- 작업에 필요한 사용자 승인 visual reference page
- 관련 `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py`
- 관련 generated `docs/03-html/slides/slide-XXX.html`
- 관련 `docs/03-html/outline/slide-outline.md` entry
- 관련 `docs/03-html/manifest.md` row

HTML orchestration gate
- main session은 HTML orchestrator 역할만 수행
- `html-slide-pm` 결과를 기다린 뒤 builder 작업 지시
- `html-slide-reviewer` 결과를 기다린 뒤 종료/승인 판단
- 실제 HTML 구현은 `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py`에서 수행
- generated `slide-XXX.html`은 artifact inspection 대상이며 구현 source로 직접 수정하지 않음

출력 형식
<exact expected deliverable>

사용자에게 물을 질문
<1~3 focused questions only if needed>

금지사항
- JPG, PNG, PDF 참조 금지 unless the user explicitly overrides it
- 추정으로 빈 내용을 메우지 말 것
- 범위를 벗어난 파일 수정 금지
- 넓고 막연한 질문 남발 금지
- HTML 관련 작업에서 `docs/03-html/shared/slide-quality-rules.md` 미확인 상태로 구현 금지
- HTML 관련 작업에서 `docs/03-html/shared/decision-log.md`와 필요한 visual reference page 미확인 상태로 구현 금지
- HTML orchestrator가 PM 또는 reviewer gate를 건너뛰지 말 것
- HTML 구현에서 generated `slide-XXX.html`을 source로 직접 수정하지 말 것
- HTML slide 문구와 구조에 source/reference 밖의 의미, label, 예시, metric 추가 금지

기본 프롬프트
<paste the default_prompt from the chosen .codex/subagents/*.yaml file>
```
