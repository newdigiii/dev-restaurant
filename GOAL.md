# GOAL.md — Frozen Milestones & Mechanical Stop Criteria (`Kitchen Rush`)

## Master Goal & Stop Condition
Deliver a 100% standalone, zero-hotlink, dual-mode 3D Web/PWA game (`/` Tycoon Mode & `/arcade` Arcade Mode) passing all mechanical checks with 0 errors.
**STOP CONDITION:** When all checkboxes below are `[x]` and the verification commands exit with code `0`, the MVP is **COMPLETE AND FROZEN**.

---

## Milestone 1: 100% Standalone & Zero-Hotlink Shield
- [x] Download all 9 `.glb` 3D models and 5 `.mp3` audio files into `web-kitchen-rush/public/assets/` and serve via local static paths (`/assets/3d/*`, `/assets/aud/*`).
- [x] Remove all Rork metadata (`rork.json`), `.vitest-attachments/`, and third-party Rork git remotes (`alexngdev99`); rename package to `kitchen-rush`; migrate Vite/Vitest configs to `import.meta.dirname`.
- **Mechanical Criteria:** `grep -rnI -iE "rork|alexngdev" web-kitchen-rush/src web-kitchen-rush/package.json web-kitchen-rush/vite*.ts` returns 0 matches; `git remote -v` contains 0 `alexngdev99`/`rork` URLs.

## Milestone 2: Core Simulation Hardening & Save Backup
- [x] Rotate furniture placement keyboard and D-pad steps by camera `angle` (`rotateStep` in `src/management/build-grid.ts`).
- [x] Cap offline catch-up simulation at `MAX_OFFLINE_SECONDS = 8 * 3600` in `RestaurantEngine.resume()` to prevent main-thread freezes on multi-day absences.
- [x] Add Zod-validated `exportSave()` and `importSave(raw)` in `RestaurantEngine` and wire Export/Import buttons + form name reset in `ManagementGame.tsx` Settings Dialog.
- **Mechanical Criteria:** `npx vitest run src/test/continuous-days.test.ts src/test/restaurant-grid.test.ts` passes 100%.

## Milestone 3: Dual-Mode Unlock (`/arcade`), Mobile Touch & Anti-Bounce Shield
- [x] Expose lazy-loaded `/arcade` route in `src/App.tsx` and `src/pages/Arcade.tsx` with 1-tap switcher in `ManagementGame.tsx` header & Settings dialog.
- [x] Wire Solo Touch Controls (`D-Pad`, `Pick / Place`, `Hold Work`, `DashButton`) in `Arcade.tsx` without overlapping `GameHUD` elements in `KitchenUI.tsx`, and auto-clear `activeInput` on pause/unmount/phase change.
- [x] Add `public/manifest.webmanifest`, `viewport-fit=cover`, `overscroll-none`, and `touch-action: manipulation` in `index.html` and `src/index.css`.
- **Mechanical Criteria:** `npx tsc -p tsconfig.app.json --noEmit && npx vitest run && npm run build` exits `0` (`37/37` test files, `487/487` tests passed, `0` console errors in Chrome DevTools).

## Milestone 4: Project-Scope Harness Isolation
- [x] Populate `/Users/digiii/Documents/workdigi/dev-restaurant/.agents/skills/` with core engineering skills in project scope without touching global skills.
- [x] Lock `AGENTS.md`, `SPEC.md`, `GOAL.md`, `docs/WORKFLOW.md`, `CONTEXT.md`, and `implementation_notes.md`.
