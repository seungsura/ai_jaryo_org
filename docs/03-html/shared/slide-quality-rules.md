# HTML Slide Quality Rules

이 문서는 `docs/03-html/` 작업 전 먼저 읽는 대화 기반 규칙 기록이다.

## 우선순위

- 사용자와 대화하며 확정한 HTML slide 규칙이 기존 HTML stage 관례보다 우선
- `Kuneosu/make-slide` 방식 우선: outline-first, theme/layout 분리, shell reuse, standalone deck, keyboard/touch navigation, print/PDF 친화 CSS
- 비채택 UI chrome 유지: fullscreen UI, slide counter UI, notes UI, progress bar, keyboard hint, demo chrome
- theme class 유지: `theme-minimal-light`
- palette 유지: 기존 프로젝트 palette 또는 minimal-light palette
- slide 규격 유지: `720pt × 405pt`
- Font 유지: Pretendard CDN

## 고정 레이아웃 규칙

- footer 고정: 좌하단 `Harness 잘 사용하기`, 우하단 page number
- 첫 장 전용 tool mark: 우상단 `claude-code`, `codex`, `opencode` icon-only mark
- 일반 슬라이드 tool mark 금지
- text pill 형태 tool 표기 금지
- 첫 장 발표자 표기: `게임플랫폼 1팀 라승수`, 하단 우측 영역
- 카드 규칙: nested card 금지, slide당 핵심 카드 1~3개, radius 8px 이하
- 강조 3단계: theme accent, bold/ink, muted metadata
- 제목 아래 subtitle/lead 기본 금지, 필요한 경우만 예외
- 전체 목차 한 장 구성: compact agenda, subtitle 제거, 하단 footer safe margin 확보
- 챕터 전환: dark divider, 일반 content page와 명확한 구분
- 요약/전환 content page: chapter divider shell 금지

## 문구 규칙

- 종결어미: 명사형 또는 구 단위
- 금지: 공손체, 서술형, 명령형
- slide title, lead, body copy 모두 압축 문구 중심
- code syntax는 원문 보존
- code block 내부 주석 추가 금지
- 예시 code block 축약 금지, 전체 예시 내용 첨부
- 부정적 의견 quote는 짧은 구 단위 문구

## 구성 규칙

- 섹션마다 최소 1장
- 큰 섹션은 최대 5장까지 허용
- 패턴, 도표, architecture 설명은 시각 요소 필수
- 같은 인접 주제라도 같은 shell 반복 금지 검토
- 특히 S012/S013처럼 연속되는 역할/문서 설명은 서로 다른 shell 우선
- 실패한 review 결과는 실패 slide id와 수정 범위만 다음 작업자에게 전달

## 판단 로그

### 2026-04-21 00/01 14장 revision

- text pill tool 표시 제거, icon-only mark로 변경  
  판단: 사용자는 tool 이름 pill이 아니라 mark를 요구, cover identity만 필요

- tool mark를 S001 전용으로 제한  
  판단: 모든 장의 우상단 반복은 본문 집중도 저하, cover page signature로 충분

- 목차 subtitle 제거와 compact agenda 규칙 추가  
  판단: 9개 장 전체 표를 한 장에 담기 위해 세로 공간 회수와 footer 안전 영역 필요

- chapter divider dark shell 적용  
  판단: 일반 content slide와 전환 slide의 시각적 혼동 제거

- language-transition 예시에 부정적 의견 quote 추가  
  판단: `assets/claude-code-seminar-kakao/page-006.png`의 반대 의견 rhythm 재현

- 예시 code block 전체화, code comment 금지  
  판단: 축약 bullet은 언어 추상화 비교 설득력 부족, code block 안 주석은 시각 noise 증가

- S009 regular comparison page 전환  
  판단: AI 개발 예시는 summary나 chapter divider가 아니라 언어 발전의 현재형 사례

- S012/S013 shell 분리  
  판단: 인접 슬라이드가 같은 process-flow 리듬이면 내용 차이가 약해짐

- 대부분 subtitle/lead 제거  
  판단: 제목 아래 보조문 반복은 핵심 요점 압축 규칙과 충돌

- S014 문장형 statement 수정  
  판단: `남는다` 같은 서술형 종결 대신 명사형 claim 필요

- S010/S012/S014 visible sentence title 정리  
  판단: source heading의 의미는 유지하되 slide 표면 문구는 명사형·구 단위 우선

- S002 핵심문장 보강  
  판단: 사용자가 지정한 핵심 전환을 유지하기 위해 `개발자의 핵심 역량`과 `AI가 안전하게 일할 환경`을 thesis line에 명시
