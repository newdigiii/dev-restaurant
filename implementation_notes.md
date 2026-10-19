# Implementation Notes — Kitchen Rush (`dev-restaurant`)

## 1. Unspecified & Implicit Decisions
- **Asset Directory Layout (`public/assets/3d/` & `public/assets/aud/`):** Preserved the original UUID filenames when downloading the 9 `.glb` models and 5 `.mp3` audio tracks from Rork's CDN so any existing asset references or cache keys remain deterministic while serving 100% locally via Vite's `public/` static root.
- **Zero-Negative-Zero Normalization (`rotateStep`):** In JavaScript, negating `0` produces `-0`, which fails `Object.is` equality checks in Vitest (`toEqual`). `rotateStep` explicitly normalizes `{ x: x || 0, z: z || 0 }`.
- **Offline Replay Cap (`MAX_OFFLINE_SECONDS = 8 * 3600`):** Set to 8 hours (28,800 seconds = 288,000 fixed 0.1s ticks), matching the existing 8-hour stress test in `src/test/continuous-days.test.ts` while preventing unbounded multi-day catch-up loops. Upon completion, `s.lastActiveAt` is updated to `target` so the remaining skipped offline time is cleanly absorbed without re-triggering on reload.
- **Standard `<a href="/arcade">` Navigation in `ManagementGame.tsx`:** `src/test/restaurant.browser.test.tsx` mounts `<ManagementGame />` directly without a `<BrowserRouter>` wrapper. Using a native `<a href="/arcade">` inside the Settings dialog avoids requiring Router context in standalone component tests while providing clean navigation between `/` (Tycoon Mode) and `/arcade` (Arcade Cooking Mode).

## 2. Deviations from Specification
- None. All approved MVP slices (Zero-Hotlink Shield, Camera-Relative Furniture Movement, Offline Catch-Up Guard `MAX_OFFLINE_SECONDS`, and `/arcade` Mode Unlock) were executed surgically.

## 3. Considered Trade-offs
- **Lazy-Loading `/arcade` (`React.lazy` in `src/App.tsx`):** By lazy-loading `src/pages/Arcade.tsx`, the primary Tycoon bundle (`/`) does not pay the initial parse cost of `KitchenUI` and `KitchenScene`, while unlocking 100% of the previously unreachable Solo/Co-op Arcade Cooking engine and `ChefWardrobe`.

## 4. Maintenance Notes
- **Rollback Anchor:** Recorded in `CONTEXT.md` (`aa1cf6f9a0cb02afb1164f222171bd013a634694`).
- **Adding New 3D/Audio Assets:** Place new `.glb` files in `web-kitchen-rush/public/assets/3d/` and `.mp3` files in `web-kitchen-rush/public/assets/aud/`, and register them in `web-kitchen-rush/src/game/assets.ts` using root-relative `/assets/...` URLs. Never use external hotlinks.
- **Storage Keys Separation:** Tycoon Mode uses `kitchen-rush-restaurant-v1`; Arcade Mode uses `kitchen-rush-progress-v2` and `kitchen-rush-outfits-v1`. Resetting the restaurant in Tycoon Mode does not erase Arcade Mode records.
