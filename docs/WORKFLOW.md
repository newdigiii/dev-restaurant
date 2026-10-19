# Repository Workflow

This repository uses the Harness Engineering pattern. Every task falls into one of three work shapes:

## 1. Work Shape Classification

### A. Read-Only Request
- **Trigger:** "Explain X", "Where is Y?", "Audit Z", "Why is this failing?"
- **Action:** Inspect the minimal necessary surface. Answer with evidence. Change NO files.

### B. Bounded Change (Small Bug / Minor Polish)
- **Trigger:** Single file edit, typo, targeted bug fix, styling tweak.
- **Action:**
  1. Inspect affected behavior and existing tests.
  2. Implement surgical change (Karpathy Guidelines: touch only what's needed).
  3. Run relevant mechanical check (typecheck/linter/test).
  4. Output concrete proof.

### C. Coordinated / Multi-Session Change (Feature / MVP Milestone)
- **Trigger:** New feature, architectural change, database migration, API addition, MVP inception.
- **Action:**
  1. Ensure `SPEC.md` covers the requirement. If missing or ambiguous, run the Goal Griller interview first.
  2. Create an execution plan in `docs/plans/active/<plan-name>.md` using `docs/templates/exec-plan.md`.
  3. Update `GOAL.md` progress as sub-tasks complete.
  4. Move validated plan to `docs/plans/completed/` once mechanical verification passes 100%.

## 2. Invariant & Verification Protocol
- Local rules: Unit tests / Linter / Typechecker (`tsc --noEmit`, `flake8`, `go test`, `pytest`).
- API contracts: `curl` or automated endpoint checks.
- UI/UX rules: WCAG AA contrast check, Dual-theme verification, Mobile responsive safe-area checks.
- Output: Every completed task MUST provide execution log evidence.
