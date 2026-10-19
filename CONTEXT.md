# Project Context & Rollback Anchor — Kitchen Rush (`dev-restaurant`)

## 1. Rollback Anchor
- **Initial Commit Hash (Pre-Modification):** `aa1cf6f9a0cb02afb1164f222171bd013a634694` (`aa1cf6f`)
- **Hardened Milestone Commit Hash:** `4ce51d3` (`branch: feature/hardening-and-arcade-route`)
- **Rollback Command:** `git reset --hard aa1cf6f9a0cb02afb1164f222171bd013a634694`

## 2. Project-Scope Harness Structure
- **Authority Contract:** `AGENTS.md`
- **Frozen Specification & Non-Goals:** `SPEC.md`
- **Milestones & Mechanical Stop Condition:** `GOAL.md` (Status: **100% COMPLETE & FROZEN**)
- **Project-Scope Skills:** `.agents/skills/` (`harness-engineering`, `vibe-engineering-workflow`, `ai-copilot-alignment`, `behavior-model-debugger`, `karpathy-guidelines`, `diagnosing-bugs`, `code-review`, `tdd`).

## 3. Domain Architecture & Single Source of Truth
- **Core Simulation (Tycoon Mode — `/`):** `web-kitchen-rush/src/management/engine.ts` (`RestaurantEngine`) — deterministic 0.1s fixed-step simulation, seeded RNG, offline catch-up in 1,000-step chunks capped at `MAX_OFFLINE_SECONDS` (`28,800s` = 8 hours), `exportSave()` / `importSave(raw)` JSON backup with Zod + layout validation, persisted under `localStorage["kitchen-rush-restaurant-v1"]`.
- **Core Simulation (Arcade Mode — `/arcade`):** `web-kitchen-rush/src/game/engine.ts` (`KitchenEngine`) & `web-kitchen-rush/src/pages/Arcade.tsx` — Overcooked-style solo/co-op cooking campaign (`LEVELS`, `ChefWardrobe`, `KitchenScene`, `KitchenUI`) with non-overlapping Solo Mobile Touch Controls (`activeInput.touch` + `DashButton`) and automatic input reset on pause/phase transitions.

## 4. What Was Done (All 4 Milestones Complete)
1. **Zero-Hotlink Shield & 100% Standalone De-Rork:** Local static `.glb` & `.mp3` assets in `public/assets/`, removed `rork.json` and external git remotes, migrated Vite/Vitest configs to `import.meta.dirname`.
2. **Camera-Relative Movement & Offline Cap:** Added `rotateStep(step, angle)` in `build-grid.ts` and capped offline replay at `MAX_OFFLINE_SECONDS` in `RestaurantEngine.resume()`.
3. **Save Backup & Mobile PWA Anti-Bounce:** Added `exportSave` / `importSave` (with `form.reset` sync), `manifest.webmanifest`, `viewport-fit=cover`, and `overscroll-none`.
4. **Dual-Mode `/arcade` & Subagent Regression Fixes:** Unlocked `/arcade` with 1-tap header switch, resolved HUD vs Touch Controls overlap (`bottom-52` for Chef 1 prompt in solo mode, `hidden xl:flex` for static `DashStatus` in solo mode), and cleared `activeInput` on pause/unmount.
