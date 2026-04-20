# Jaryo Agent Guide

## Scope

This repository uses project-local skills and subagent specs under `.codex/`. Keep the setup local to this repository and prefer those local artifacts over global skills when the task is about document reconstruction.

## Default Source Policy

- Treat local markdown files as the only authoritative source for reconstruction work.
- Do not inspect `assets/`, JPG, PNG, or PDF files unless the user explicitly changes that rule.
- When content is missing, record it in `docs/01-sources/intake/open-questions.md` instead of guessing.
- Ask focused follow-up questions to the user after meaningful editorial passes instead of silently guessing.

## Documentation Language Policy

- Write new and revised documentation in Korean by default.
- Keep English for terms, technical vocabulary, product names, service names, library or framework names, API names, commands, paths, protocols, and other expressions where translation would reduce precision.
- When readability benefits from explanation, add a short Korean explanation without replacing the canonical English term.

## Seminar Voice Policy

- `docs/02-seminar/prose/`는 보고서, 강의안, 제품 문서 말투가 아니라 밀도 높은 기술 블로그 에세이 톤으로 씁니다.
- 문장은 직접적이고 단정적으로 씁니다. 과하게 비겁한 완곡어법, 사내 문서식 관료 문장, 안전한 요약문을 기본값으로 두지 않습니다.
- 문단은 주장과 대비가 앞으로 밀고 가는 리듬을 가져야 합니다. 필요한 경우 수사적 질문과 짧은 단문을 쓰되, 습관처럼 남발하지는 않습니다.
- 영어식 번역투와 방법론 직역체를 피합니다. 예: `상류/하류`, `강하게 호출된다`, `핵심은 ~ 데 있다`, `~의 측면에서`, `~라고 볼 수 있다` 같은 표현은 더 살아 있는 한국어가 있으면 교체합니다.
- 명사구만 무겁게 쌓는 문장, 설명문 냄새가 짙은 추상 문장, bullet을 줄글로 늘인 듯한 문장은 피합니다.
- 근거가 있는 강한 문장은 허용하지만, 밈체·허세체·과장된 인터넷체로 미끄러지면 안 됩니다.
## Local Skills

- `.codex/skills/local/jaryo-doc-reconstruction/SKILL.md`
- `.codex/skills/vendor/pdf/SKILL.md`

## Local Subagents

- `.codex/subagents/doc-editor-partner.yaml`
- `.codex/subagents/source-integrator.yaml`
- `.codex/subagents/source-curation-analyst.yaml`
- `.codex/subagents/seminar-writer-ko.yaml`

Use `.codex/subagents/README.md` for the intended order and `.codex/templates/subagent-task-template.md` for spawn prompts.
