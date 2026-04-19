---
name: jaryo-slide-evaluation
description: Evaluate the Jaryo seminar slide pipeline with explicit PASS, REVISE, or BLOCK gates. Use when auditing storyline flow, Korean slide tone, deck-level HTML consistency, or render-level HTML validation before allowing the next stage to proceed.
---

# Jaryo Slide Evaluation

## Overview

Use this skill for all review gates in the slide pipeline. It standardizes PASS / REVISE / BLOCK decisions across pre-HTML and post-HTML stages.

## Core Rules

- Every evaluator must return one of: `PASS`, `REVISE`, `BLOCK`.
- Review scope must be explicit:
  - chapter batch
  - exception slide set
  - full deck
- Do not rewrite assets while evaluating them.
- Pre-HTML gates judge storyline and Korean slide wording.
- Korean tone gates must catch report-style drift, translationese, and loss of the repository's direct Korean voice.
- Post-HTML gates judge deck consistency and slide-level rendering.
- Automated local checks can inform review, but they do not replace the gate decision.
- A later stage must not proceed when a required gate returns `REVISE` or `BLOCK`.

## Workflow

1. Confirm the review scope.
2. Choose the gate type:
   - storyline
   - Korean tone
   - HTML deck consistency
   - HTML render validation
3. Apply the gate checklist for that type and read automated check output when available.
4. Return:
   - gate decision
   - key findings
   - exact rework scope
   - next allowed action

## Output Expectations

- A strict gate decision
- Findings grouped by what actually blocks progress
- Clear rework scope rather than vague criticism
- Enough detail that the producing agent knows exactly what to fix, including whether the failure came from shell drift, tone drift, or render defects

## When To Load References

- Read [references/gate-contract.md](references/gate-contract.md) for the output shape and gate semantics.
- Read [references/checklists.md](references/checklists.md) for gate-specific review criteria.

## Guardrails

- Do not downgrade a real blocker into a vague note.
- Do not approve a batch just because it is mostly good.
- Do not blur chapter-batch review and full-deck review.
- Do not approve HTML that violates the design contract even if it technically renders.
