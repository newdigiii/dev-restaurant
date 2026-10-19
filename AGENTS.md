# AGENTS.md — Repository Harness & Authority Contract (`dev-restaurant`)

## 1. Repository Harness & Single System of Record
Start with the requested outcome and use this repository as the single system of record.
Read `docs/WORKFLOW.md`, `SPEC.md`, `GOAL.md`, and `CONTEXT.md` before proposing or executing changes.

### Core Working Rules
1. **Project-Scope Isolation:** All skills, rules, and workflows for this project reside inside `/Users/digiii/Documents/workdigi/dev-restaurant/.agents/skills/`. **NEVER modify global skills (`~/.gemini/config/skills/`).**
2. **Read-Only First:** Status checks, code audits, architecture reviews, and diagnoses must NOT modify any file (`Zero Action`).
3. **Stop Condition Enforcement (No Infinite Audit Loop):** `SPEC.md` and `GOAL.md` define the frozen MVP scope and Non-Goals. When all checkboxes in `GOAL.md` are `[x]` and mechanical verification passes, **STOP** — do not invent new speculative features or open-ended gaps unless the user explicitly defines a new Milestone in `GOAL.md`.
4. **No Manual Testing Imposed:** The agent must self-test and self-debug using `npx tsc -p tsconfig.app.json --noEmit`, `npx vitest run`, `npm run build`, and `chrome-devtools-mcp` / subagents. Never ask the user to manually test broken or unverified code.
5. **Subagent Cross-Verification:** Before declaring any multi-file milestone complete, invoke a read-only `research` subagent or mechanical verification suite to audit the diff for layout collisions, stuck state, or regressions.

## 2. Quick Architecture Map
- **App Entry & Routing:** `web-kitchen-rush/src/App.tsx` (`/` -> Tycoon Mode `ManagementGame`, `/arcade` -> Lazy-loaded Arcade Mode `Arcade.tsx`).
- **Tycoon Engine (`/`):** `web-kitchen-rush/src/management/engine.ts` (`RestaurantEngine`), `layout.ts` (`findPath` BFS), `build-grid.ts` (`rotateStep`), `ManagementGame.tsx`, `RestaurantScene.tsx`.
- **Arcade Engine (`/arcade`):** `web-kitchen-rush/src/game/engine.ts` (`KitchenEngine`), `input.ts` (`KitchenInput`, `activeInput`), `src/pages/Arcade.tsx`, `src/components/KitchenUI.tsx`, `src/scene/KitchenScene.tsx`.
- **Static Local Assets:** `web-kitchen-rush/public/assets/3d/*.glb` (9 models) & `web-kitchen-rush/public/assets/aud/*.mp3` (5 audio tracks), referenced in `src/game/assets.ts` and `src/management/CityLife.tsx`.
