#!/usr/bin/env python3
"""
Bootstrap Repository Harness Structure
Creates a clean, agent-ready repository harness following the AGENTS.md, SPEC.md, GOAL.md, and docs/WORKFLOW.md pattern.
"""

import os
import sys
from pathlib import Path

AGENTS_MD_TEMPLATE = """# AGENTS.md

## Repository Harness
Start with the requested outcome and use the repository as the single system of record.
Read `docs/WORKFLOW.md` and only the relevant product, architecture, design, and plan files.

### Core Working Rules:
1. **Repository is Authority:** Chat context is temporary; files in this repo are permanent. All decisions, goals, and contracts must exist in docs.
2. **Read-Only First:** Status checks, code audits, architecture reviews, and diagnoses must NOT modify any file.
3. **Progressive Disclosure:** Do not read the entire codebase upfront. Start from `AGENTS.md` -> `docs/WORKFLOW.md` -> `SPEC.md` -> `GOAL.md`.
4. **Authority Boundaries:** Do NOT invent product policy. If a material business requirement or design choice is ambiguous, STOP and ask before mutating code.
5. **Mechanical Verification:** Always prove changes with executable commands (exit code 0, lint/typecheck clean, test pass, curl 200). Never declare done without proof.
6. **No Manual Testing Imposed:** The agent must self-test and self-debug. Do not prompt the user for manual testing until automated criteria pass.
"""

WORKFLOW_MD_TEMPLATE = """# Repository Workflow

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
"""

EXEC_PLAN_TEMPLATE = """# Execution Plan: [Task Title]

Date: [YYYY-MM-DD]
Status: Active | Blocked | Completed

## 1. Outcome
Describe the exact, observable behavior this task will produce.

## 2. Authority & Context
- Reference documents: `SPEC.md`, `GOAL.md`, relevant architectural ADRs.
- Target files: List known files to modify.

## 3. Scope
- **In Scope:** What will be built/changed.
- **Non-Goals (Out of Scope):** What is explicitly NOT being done in this plan.

## 4. Mechanical Verification Plan
- [ ] Command 1: (e.g. `npm run typecheck` or `npm test`)
- [ ] Command 2: (e.g. `curl -I http://localhost:3000/api/health`)

## 5. Surgical Steps & Progress
- [ ] Step 1: ...
- [ ] Step 2: ...
- [ ] Step 3: Mechanical check verification.
"""

SPEC_MD_SKELETON = """# SPEC.md - Technical & Product Specification

## 1. Project Overview & Value Proposition
- **Product Name:** [Name]
- **Core Value:** [1-sentence problem-solution statement]
- **Target Audience:** [Primary Persona]

## 2. Tech Stack & Architecture
- **Frontend:** [Framework, UI Library, State Management]
- **Backend & API:** [Framework, Runtime, API Protocol]
- **Database & Storage:** [DB Engine, ORM/Client]
- **Deployment & Cloud:** [Hosting platform, CI/CD]

## 3. Core Features & Business Logic (MVP Scope)
- **Feature 1:** [User story & flow]
- **Feature 2:** [User story & flow]

## 4. Non-Goals (Scope Boundary)
- Feature X is NOT in MVP.
- Feature Y is postponed to V2.

## 5. UI/UX Invariants
- Dual Theme (Dark / Light) with WCAG AA contrast >= 4.5:1.
- Mobile First & PWA Responsive with safe-area padding (`env(safe-area-inset-bottom)`).
"""

GOAL_MD_SKELETON = """# GOAL.md - Milestones & Success Criteria

## Master Goal
Deliver an end-to-end working MVP with 0 console errors, passing all mechanical checks.

---

## Milestone 1: Foundation & Scaffold
- [ ] Initialize repository structure with Harness (`AGENTS.md`, `SPEC.md`, `GOAL.md`).
- [ ] Setup base configuration, linter, and typechecker.
- **Success Criteria:** `npm run build` or base test passes with exit code 0.

## Milestone 2: Core Data & API Layer
- [ ] Define database schema and migrations.
- [ ] Implement core API endpoints with input validation.
- **Success Criteria:** API endpoints return expected JSON schema, tests pass.

## Milestone 3: Frontend & User Flow
- [ ] Build key screens adhering to design tokens.
- [ ] Verify Dark/Light dual theme and mobile responsiveness.
- **Success Criteria:** 0 console errors on Chrome DevTools, UI renders clean on viewport 390px (mobile).

## Milestone 4: Hardening & Final Verification
- [ ] Edge-case handling and error boundary.
- [ ] End-to-end smoke test.
- **Success Criteria:** Full automated test suite passes with 0 failures.
"""

def init_harness(root_dir: Path):
    print(f"🚀 Initializing Repository Harness in: {root_dir}")
    
    # 1. Create directories
    docs_dir = root_dir / "docs"
    templates_dir = docs_dir / "templates"
    plans_active = docs_dir / "plans" / "active"
    plans_completed = docs_dir / "plans" / "completed"
    agents_skills = root_dir / ".agents" / "skills"

    for d in [templates_dir, plans_active, plans_completed, agents_skills]:
        d.mkdir(parents=True, exist_ok=True)
        print(f"  + Directory: {d.relative_to(root_dir)}")

    # 2. Write AGENTS.md if not exists
    agents_file = root_dir / "AGENTS.md"
    if not agents_file.exists():
        agents_file.write_text(AGENTS_MD_TEMPLATE, encoding="utf-8")
        print("  + Created: AGENTS.md")
    else:
        print("  . Kept existing: AGENTS.md")

    # 3. Write docs/WORKFLOW.md if not exists
    workflow_file = docs_dir / "WORKFLOW.md"
    if not workflow_file.exists():
        workflow_file.write_text(WORKFLOW_MD_TEMPLATE, encoding="utf-8")
        print("  + Created: docs/WORKFLOW.md")
    else:
        print("  . Kept existing: docs/WORKFLOW.md")

    # 4. Write docs/templates/exec-plan.md if not exists
    plan_template_file = templates_dir / "exec-plan.md"
    if not plan_template_file.exists():
        plan_template_file.write_text(EXEC_PLAN_TEMPLATE, encoding="utf-8")
        print("  + Created: docs/templates/exec-plan.md")
    else:
        print("  . Kept existing: docs/templates/exec-plan.md")

    # 5. Write SPEC.md if not exists
    spec_file = root_dir / "SPEC.md"
    if not spec_file.exists():
        spec_file.write_text(SPEC_MD_SKELETON, encoding="utf-8")
        print("  + Created: SPEC.md (Skeleton)")
    else:
        print("  . Kept existing: SPEC.md")

    # 6. Write GOAL.md if not exists
    goal_file = root_dir / "GOAL.md"
    if not goal_file.exists():
        goal_file.write_text(GOAL_MD_SKELETON, encoding="utf-8")
        print("  + Created: GOAL.md (Skeleton)")
    else:
        print("  . Kept existing: GOAL.md")

    print("\n✅ Repository Harness initialized successfully!")
    print("Next steps:")
    print("1. Run Goal Griller interview (`:hngoal` or `:hngriller`) to populate SPEC.md & GOAL.md.")
    print("2. Run Autonomous Harness Loop (`:hnloop` or `:hnok`) to implement and verify.")

if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    init_harness(target)
