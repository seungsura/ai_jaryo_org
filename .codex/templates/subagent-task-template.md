# Subagent Task Template

Use this wrapper when spawning a project subagent.

```text
목표
<what the subagent must achieve>

범위
<files or sections it may read or edit>

입력 파일
<specific markdown/doc paths>

출력 형식
<exact expected deliverable>

사용자에게 물을 질문
<1~3 focused questions only if needed>

금지사항
- JPG, PNG, PDF 참조 금지 unless the user explicitly overrides it
- 추정으로 빈 내용을 메우지 말 것
- 범위를 벗어난 파일 수정 금지
- 넓고 막연한 질문 남발 금지

기본 프롬프트
<paste the default_prompt from the chosen .codex/subagents/*.yaml file>
```
