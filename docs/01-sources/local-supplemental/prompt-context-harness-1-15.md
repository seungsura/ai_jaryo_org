# 프롬프트-컨텍스트-하네스 자료 정리

- Source PDF: `/Users/seungsu/Downloads/1-15_merged_with_source.pdf`
- Total pages: 15
- Generated at: `2026-04-16T02:48:33.042Z`
- Preservation strategy: each page section includes the rendered original page image and OCR transcription.
- Note: for tiny handwritten labels or decorative text, use the image as the source of truth if OCR is imperfect.

## Page 001

![Page 001](assets/prompt-context-harness-1-15/page-001.jpg)

### Transcription

```text
DATA FLOW INTEGRATION SYSTEM
WORKSPACE AGENT HARNESS SAFETY
CONTEXT WINDOW 챗봇과 싸우지 마라.
에이전트가 일할 환경을 설계하라. AL TOOLS
자율형 AI 도입을 위한 하네스 엔지니어링 실무 가이드
"stop fighting the chatbot.
RESTRICTIONS Start engineering the harness.
- Mitchell Hashimoto
AUTONOMY UNCONTROLLED MAput linkedin.com/in/hwang-minho 출처: 황민호 님 제작 (카카오)
```

## Page 002

![Page 002](assets/prompt-context-harness-1-15/page-002.jpg)

### Transcription

```text
프롬프트 -> 컨텍스트 -> 하네스: 관심사의 확장
하네스 프롬프트 : 어떻게 말할 것인가?
(명령어 품질)
컨텍스트
컨텍스트: 무엇을 보여줄 것인가?
(정보 품질)
프롬프트 하네스 : 무엇을 통제하고
방지할 것인가?
인전 데이터 보호 (시스템 안정성)
기준
프롬프트를 넘어, 에이전트가 신뢰성 있게 일할 수 있는
'구조적 체계'를 구축하는 시대로 전환되었습니다.
```

## Page 003

![Page 003](assets/prompt-context-harness-1-15/page-003.jpg)

### Transcription

```text
추상화의 역사: 직접 하는 일은 줄고, 설계하는 일은 늘어난다
직접 하는 일은 줄고, 설계하는 일은 늘어난다. AI 에이전트 (2020s)
- 코딩을 위임하고 '환경'을 설계
클라우드 (2010s) - 인프라 위임
GC 프레임워크 (2000s) - 보일러플레이트 위임
메모리 관리 (1990s) - 가비지 컬렉터(GC)에 위임
고급 언어 (1960s)- 컴파일러에 위임
어셈블리 (1950s)
```

## Page 004

![Page 004](assets/prompt-context-harness-1-15/page-004.jpg)

### Transcription

```text
하네스 없는 AI의 참사: 4가지 치명적 실패 모드
- 코드 보안 취약점 2.74배 증가 AI 슬롭 (Al Slop) -자기 작업 시 품질 70%에서 둠 루프 (Doom 100p) 23%로 추락
- 명시적 지시 무시, DB 삭제 사건 - 기업 73%가 모니터링 없이 Shadow Agent
1,200개 임원 기록 삭제 통제 불능 방치
```

## Page 005

![Page 005](assets/prompt-context-harness-1-15/page-005.jpg)

### Transcription

```text
해결책: 하네스의 5대 해부학 (The Anatomy)
⑤ 관측 가능성
① 안전장치 - 행동 트레이스 및 (Observability):
- 위험한 명령 차단 (Guardrails): 루프 모니터링.
및 권한 제한.
④ 상태 관리
② 명세 (State Management):
(Specification): - 세션 간 컨텍스트
- 의도와 작업 외부 유지.
분해 가이드.
③ 검증 루프 ⑤ 관측 가능성
(Verification): (Observability):
- 결정론적 린터와 - 행동 트레이스
테스트의 교차. 및 루프 모니터링,
```

## Page 006

![Page 006](assets/prompt-context-harness-1-15/page-006.jpg)

### Transcription

```text
15전 15승: 데이터로 증명된 하네스의 마법
Harness: 79.3점
(60% 향상) 최대 격차 차원:
•테스트 커버리지 (+4.9점)
• 아키텍처 (+4.4점)
Baseline: 49.5점 기능 구현 능력이 아니라,
방어적 프로그래밍과
구조 설계 강제가 품질을
결정했다. 병목은 AI의
능력이 아니라 환경에 있다.
기본 난이도(+23.8점)보다
초고난이도(+36.2점) 태스크에서 격차 극대화.
```

## Page 007

![Page 007](assets/prompt-context-harness-1-15/page-007.jpg)

### Transcription

```text
안전장치와 큐레이션: 적을수록 강하다
도구 15개 단 2개 핵심
과부하 도구 큐레이션
정확도 80%. 정확도 100%,
수많은 선택지 속에서 속도 3.5배 향상.
추론 능력 낭비(토큰 마비). (Vercel 실험 결과)
Stripe 사례: 400개 이상의 내부 도구 중, 태스크별로 오케스트레이터가 단 15개만 동적
큐레이션하여 주입. 에이전트는 사용하지 않는 인터페이스에 의존하지 말아야 한다.
```

## Page 008

![Page 008](assets/prompt-context-harness-1-15/page-008.jpg)

### Transcription

```text
상태 관리: 에이전트의 기억을 윈도우 밖으로 빼라 12-Factor
App의
Before After 무상태 원칙 적용
외부 아티팩트
claude-progress.bit
컨텍스트
윈도우
문제: 에이전트는 이산적 세션에서 일하며, 해결: 상태를 에이전트 외부 아티팩트(파일 시스템, Git 히스토리)에 영속화.
윈도우가 닫히면 기억은 리셋된다. 수십 번의 세션을 넘나드는 일관성 유지.
```

## Page 009

![Page 009](assets/prompt-context-harness-1-15/page-009.jpg)

### Transcription

```text
엄격함의 재배치: 결정론적 제어와 확률적 제어의 분리
계산적 제어 (기계/ 신호등) 추론적 제어 (AI/ 교통경찰)
결정론적 특성 확률론적 특성
(빨간불은 절대 멈춤) (상황에 따른 유연한 판단)
린터, 타입 체커, 훅(Hooks) 에이전트 코드 리뷰, 아키텍처 설계
예외 없이 100% 기계적으로 강제 컨텍스트 기반의
AI는 결정론적 게이트를 유연한 추론
건너될 수 없다.
Keep Quality Left:
기계가 확인할 수 있는 것은
기계에게 맡기고, AI는 판단만 하라.
```

## Page 010

![Page 010](assets/prompt-context-harness-1-15/page-010.jpg)

### Transcription

```text
레퍼런스 아키텍처: Stripe와 Claude의 수렴 DEPLOY
Ceoel
독립적인 회사들이 인간 검토 APPOONTD
'6계층 하네스 구조'에 하나의 건축 구조인 E2E 테스트 게이트 V X V TESTING...
완전히 수렴했다. AI 코드 생성 Function eeL() Ceneet E 1Beee (
이것은 취향의 문제가 기계적 린트 게이트 @ PASS
아니라, X FAIL
프로덕션 환경의
요구사항이 만들어낸 동적 도구 큐레이션
아키텍처적 필연이다. 격리 VM
(안전 샌드박스)
```

## Page 011

![Page 011](assets/prompt-context-harness-1-15/page-011.jpg)

### Transcription

```text
하이브리드 워크플로: 창의성과 엄격함의 교차
1 확률적 생성 2
(코드 작성) 에러 메시지가
AI의 다음 프롬프트가 됨
결정론적 검증 (Lint-as-Instruction)
(린트/테스트)
4 확률적 수정
0 3
결정론적 결정론적 게이트를 건너뒬 수 없다. 핵심 원칙: AI는 결코
검증 확률론과 결정론이 반복 교차하며
품질을 보장한다.
```

## Page 012

![Page 012](assets/prompt-context-harness-1-15/page-012.jpg)

### Transcription

```text
전통적 아키텍처 원칙의 재해석 (SOLID 변환)
원칙 과거 현재
(코드 중심) (에이전트 중심)
S (단일 책임) 클래스 분리 에이전트/도구 역할 제한 (코더와 리뷰어 분리)
0 (개방-폐쇄) 코드 수정 불가/ 확장 가능 플러그인(Hooks)으로 검증 확장 코어 로직 건드리지 않고
1(인터페이스 분리) 불필요한 메서드 불필요한 도구(MCP) 및
의존 금지 파일 권한 노출 금지
D (의존성 역전) 추상화 의존 컨텍스트(CLAUDE.md)를 능동 주입 하드코딩 탈피, 하네스가
```

## Page 013

![Page 013](assets/prompt-context-harness-1-15/page-013.jpg)

### Transcription

```text
조직 거버넌스 성숙도: 카오스에서 혁신으로
4단계: 최적화
3단계: 표준화 캐시 및 모델 분리로
프로젝트별 공통 최적화 완료.
하네스 템플릿 5단계: 혁신
월$7,000/팀 비용 폭발: 2단계: 인식 도입. 조직의 기본 인프라화. 자가 조정 하네스.
1단계: 카오스 가이드라인 도입. 개인별
섀도우 에이전트 위험. 하네스 없음. 비용 82% 절감:
월 S1,230/팀
```

## Page 014

![Page 014](assets/prompt-context-harness-1-15/page-014.jpg)

### Transcription

```text
새로운 엔지니어의 탄생: 타이피스트에서 지휘자로
전통적 엔지니어 현대의 하네스 엔지니어
코드를 직접 작성하고 에이전트가 코드를 잘 짤 수 있도록 환경을 설계하고,
버그를 직접 수정하는 사람 결과물의 맛(Taste)을 감별하는 아키텍처 게이트키퍼
시니어 엔지니어의 판단력과 통찰은
코딩 능력이 대체될수록 오히려 그 가치가 급증한다.
```

## Page 015

![Page 015](assets/prompt-context-harness-1-15/page-015.jpg)

### Transcription

```text
하네스의 미래: 삭제를 위해 구축하라 (Build to Delete)
Richard Sutton의 'Bitter Lesson':
모델이 발전할수록 정교한 수작업
인프라는 불필요해진다.
오늘 에이전트의 실수를 막기 위해 만든
복잡한 하네스는, 내일 더 똑똑해진
에이전트에게 족쇄가 될 수 있다.
최고의 하네스는 에이전트가 성장함에 따라
삭제 조건을 명시하라. 점진적으로 지워지는 것이다. Legacy
소프트웨어 엔지니어링은 사라지지 않는다.
환경 설계로 진화할 뿐이다.
```
