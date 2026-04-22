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

## HTML Slide Policy

- 모든 HTML 관련 작업 전 `AGENTS.md`, `.codex/subagents/README.md`, `.codex/templates/subagent-task-template.md`, `docs/03-html/shared/slide-quality-rules.md`, `docs/03-html/shared/decision-log.md`를 먼저 읽고, 새 슬라이드 피드백은 `docs/03-html/shared/slide-quality-rules.md`에 먼저 기록합니다.
- HTML 관련 작업 범위에는 `docs/03-html/`의 outline, manifest, generator output, shared CSS, shared token, deck HTML, screenshot QA, PDF export QA가 모두 포함됩니다.
- 사용자와 대화하며 확정한 HTML slide 규칙은 기존 HTML stage 관례, design 문서, generator 관성보다 우선합니다.
- main session은 HTML orchestrator 역할만 수행합니다. 실제 HTML 작업은 project-local subagent `html-slide-pm`, `html-slide-builder`, `html-slide-qa`, `html-slide-reviewer`를 통해 조율합니다.
- HTML orchestrator는 `html-slide-pm` 결과를 기다린 뒤 builder 작업을 지시하고, `html-slide-reviewer` 결과를 기다린 뒤 종료/승인합니다. PM 또는 reviewer gate를 건너뛰지 않습니다.
- HTML 작업 subagent prompt에는 `docs/03-html/shared/slide-quality-rules.md`, `docs/03-html/shared/decision-log.md`, 대상 source markdown, 필요한 visual reference page, 관련 `scripts/jaryo_html_deck/slides/slide_XXX.py`, generated `slide-XXX.html`, outline, manifest 사전 확인을 명시합니다.
- 실제 HTML 구현 단위는 `scripts/jaryo_html_deck/slides/slide_XXX.py`입니다. generated `docs/03-html/slides/slide-XXX.html`은 artifact inspection 대상이며, 구현 source로 직접 수정하지 않습니다.
- `Kuneosu/make-slide`의 outline-first, theme/layout 분리, shell reuse, standalone deck, keyboard/touch, print/PDF 구조를 우선 적용합니다.
- HTML slide 문구와 시각 구조의 의미 단위는 source markdown 또는 사용자가 명시한 reference에서만 가져옵니다.
- source에 없는 비교 축, label, 의미, 예시, metric, 해설 문구를 새로 만들지 않습니다.
- deck은 `theme-minimal-light`, 기존/minimal-light palette, `720pt × 405pt`, Pretendard CDN, footer `Harness 잘 사용하기` 기준을 유지합니다.
- slide 문구는 명사형·구 단위 중심으로 쓰고, 공손체·서술형·명령형을 피합니다.
- HTML 수정 후 `check_slide_contract`, `check_slide_korean`, `check_deck_runtime`, 필요한 Playwright/PDF smoke를 규칙 기준으로 실행합니다.

## Local Skills

- `.codex/skills/local/jaryo-doc-reconstruction/SKILL.md`
- `.codex/skills/vendor/pdf/SKILL.md`

## Local Subagents

- `.codex/subagents/doc-editor-partner.yaml`
- `.codex/subagents/source-integrator.yaml`
- `.codex/subagents/source-curation-analyst.yaml`
- `.codex/subagents/seminar-writer-ko.yaml`
- `.codex/subagents/html-slide-pm.yaml`
- `.codex/subagents/html-slide-builder.yaml`
- `.codex/subagents/html-slide-qa.yaml`
- `.codex/subagents/html-slide-reviewer.yaml`

Use `.codex/subagents/README.md` for the intended order and `.codex/templates/subagent-task-template.md` for spawn prompts.
