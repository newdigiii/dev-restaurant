# Implementation Notes — Kitchen Rush (`dev-restaurant`)

## 1. Unspecified & Implicit Decisions
- **Asset Directory Layout (`public/assets/3d/` & `public/assets/aud/`):** Preserved the original UUID filenames when downloading the 9 `.glb` models and 5 `.mp3` audio tracks so any existing asset references or cache keys remain deterministic while serving 100% locally via Vite's `public/` static root.
- **Zero-Negative-Zero Normalization (`rotateStep`):** In JavaScript, negating `0` produces `-0`, which fails `Object.is` equality checks in Vitest (`toEqual`). `rotateStep` explicitly normalizes `{ x: x || 0, z: z || 0 }`.
- **Offline Replay Cap (`MAX_OFFLINE_SECONDS = 8 * 3600`):** Set to 8 hours (28,800 seconds = 288,000 fixed 0.1s ticks), matching the existing 8-hour stress test in `src/test/continuous-days.test.ts` while preventing unbounded multi-day catch-up loops. Upon completion, `s.lastActiveAt` is updated to `target` so the remaining skipped offline time is cleanly absorbed without re-triggering on reload.
- **Save Backup Validation (`exportSave` / `importSave`):** `importSave(raw)` reuses `restaurantSchema.safeParse`, `layoutError`, and challenge-day checks before mutating `this.state`, resets `this.state.lastActiveAt = this.now()`, and calls `form.reset({ name: restaurant.state.name })` in `ManagementGame.tsx` so the Settings input reflects the restored restaurant name immediately.
- **Non-Overlapping Solo Touch Controls in `/arcade`:** `Arcade.tsx` renders `<section aria-label="Touch controls">` only when `state.phase === 'playing' && !state.paused && state.mode === 'solo'`, clears `activeInput?.clear()` whenever `state.phase !== 'playing' || state.paused`, moves the compact `Chef 1` status pill to `bottom-52` in `solo` mode (`KitchenUI.tsx`), and hides the duplicate static `DashStatus` card below `xl` (`1280px`) in `solo` mode where `DashButton` is already displayed.

## 2. Deviations from Specification
- None. All approved slices and project-scope harness files (`AGENTS.md`, `SPEC.md`, `GOAL.md`, `docs/WORKFLOW.md`, `.agents/skills/`) were executed strictly within `/Users/digiii/Documents/workdigi/dev-restaurant/`.

## 3. Considered Trade-offs
- **Repository Harness vs CodeGraph:** For an 85-file flat TypeScript codebase, a deterministic Repository Harness (`AGENTS.md` + `SPEC.md` + `GOAL.md` + `CONTEXT.md`) provides instant file resolution and a strict mechanical stop condition without the overhead of maintaining a local graph database.

## 4. Maintenance Notes
- **Rollback Anchor:** Recorded in `CONTEXT.md` (`aa1cf6f9a0cb02afb1164f222171bd013a634694`).
- **Storage Keys Separation:** Tycoon Mode uses `kitchen-rush-restaurant-v1`; Arcade Mode uses `kitchen-rush-progress-v2` and `kitchen-rush-outfits-v1`.
