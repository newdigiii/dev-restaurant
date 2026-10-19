# Project Context & Rollback Anchor — Kitchen Rush (`dev-restaurant`)

## 1. Rollback Anchor
- **Initial Commit Hash (Pre-Modification):** `aa1cf6f9a0cb02afb1164f222171bd013a634694` (`aa1cf6f`)
- **Branch:** `main`
- **Rollback Command:** `git reset --hard aa1cf6f9a0cb02afb1164f222171bd013a634694`

## 2. Domain Architecture & Single Source of Truth
- **Core Simulation (Tycoon Mode — `/`):** `web-kitchen-rush/src/management/engine.ts` (`RestaurantEngine`) — deterministic 0.1s fixed-step simulation, seeded RNG, offline catch-up in 1,000-step chunks capped at `MAX_OFFLINE_SECONDS` (`28,800s` = 8 hours), persisted under `localStorage["kitchen-rush-restaurant-v1"]`.
- **Core Simulation (Arcade Mode — `/arcade`):** `web-kitchen-rush/src/game/engine.ts` (`KitchenEngine`) & `web-kitchen-rush/src/pages/Arcade.tsx` — Overcooked-style solo/co-op cooking campaign (`LEVELS`, `ChefWardrobe`, `KitchenScene`, `KitchenUI`), persisted under `localStorage["kitchen-rush-progress-v2"]` and `localStorage["kitchen-rush-outfits-v1"]`.
- **Grid & Pathfinding:** `web-kitchen-rush/src/management/layout.ts` — 10×10 (expandable to 14×10) rooftop grid, 4-way BFS (`findPath`) validating all guest/staff access points before placement.
- **UI Shell:** `web-kitchen-rush/src/management/ManagementGame.tsx` — owner HUD, Build/Team/Menu/Ledger panels, camera zoom/rotation (`angle: 0..3`), Settings dialog with direct navigation to `/arcade`.
- **3D Scene:** `web-kitchen-rush/src/management/RestaurantScene.tsx` (Tycoon) & `web-kitchen-rush/src/scene/KitchenScene.tsx` (Arcade) — React Three Fiber orthographic three-quarter scenes with procedural animal rigs (`src/scene/*`).

## 3. Surgical Hardening Scope (Executed MVP Slices)
1. **Zero-Hotlink Shield (Gate 9.3 Compliance):**
   - Downloaded all 9 `.glb` 3D models and 5 `.mp3` audio files from `https://4t92512aiqitifoedg47w.rork.app/~assets/...` into `web-kitchen-rush/public/assets/3d/` and `web-kitchen-rush/public/assets/aud/`.
   - Updated `web-kitchen-rush/src/game/assets.ts` and `web-kitchen-rush/src/management/CityLife.tsx` to load from local static paths (`/assets/3d/...`, `/assets/aud/...`).
2. **Camera-Relative Movement Fix (Collision Matrix Gate 3.1):**
   - Rotated keyboard (`ArrowUp/Down/Left/Right`) and on-screen D-pad movement vectors by camera `angle` (`0..3`) via `rotateStep` in `web-kitchen-rush/src/management/build-grid.ts` and `web-kitchen-rush/src/management/ManagementGame.tsx`.
3. **Offline Catch-Up Guard (`MAX_OFFLINE_SECONDS` — Blind Spot #1):**
   - Capped `RestaurantEngine.resume()` replay at `MAX_OFFLINE_SECONDS = 8 * 3600` (`288,000` ticks max) in `web-kitchen-rush/src/management/engine.ts` and advanced `lastActiveAt` to `target` on completion so multi-day absences or system clock jumps cannot freeze the browser main thread.
4. **Unlock Hidden Arcade Cooking Mode (`/arcade` — Blind Spot #3):**
   - Created `web-kitchen-rush/src/pages/Arcade.tsx` wrapping `KitchenScene` and `KitchenUI`, lazy-loaded at `/arcade` in `web-kitchen-rush/src/App.tsx`, with a cross-navigation link in `ManagementGame.tsx` Settings Dialog.
