# SPEC.md — Technical & Product Specification (`Kitchen Rush`)

## 1. Product Overview & Value Proposition
- **Product Name:** Kitchen Rush — Restaurant Stories (`kitchen-rush`)
- **Core Value:** A 100% standalone, offline-capable 3D WebGL / PWA dual-mode game combining a cozy rooftop **Restaurant Tycoon (` / `)** with a fast-paced Solo / Couch Co-op **Arcade Kitchen (`/arcade`)**.
- **Target Platforms:** Desktop & Mobile Web Browsers (WebGL 2) + Standalone Fullscreen PWA (`/manifest.webmanifest`).

## 2. Tech Stack & Architecture
- **Frontend & 3D Rendering:** React 19.2, TypeScript 5.9, Vite 8, Three.js 0.186, `@react-three/fiber` v9, `@react-three/drei` v10, Tailwind CSS 3.4, Radix UI.
- **Simulation Engines:**
  - `RestaurantEngine` (`src/management/engine.ts`): Fixed 0.1s timestep, deterministic seeded RNG, BFS grid pathfinding (`layout.ts`), offline catch-up capped at `MAX_OFFLINE_SECONDS = 28,800s` (8 hours), Zod-validated JSON save export/import (`exportSave` / `importSave`).
  - `KitchenEngine` (`src/game/engine.ts`): Frame-rate independent Solo & 2P Couch Co-op cooking shifts, 3 levels, `ChefWardrobe`, procedural Web Audio synthesis (`audio.ts`, `chopping-audio.ts`), and responsive Solo Touch Controls (`Arcade.tsx`).
- **Storage & Privacy:** 100% Client-Side `localStorage` (`kitchen-rush-restaurant-v1`, `kitchen-rush-progress-v2`, `kitchen-rush-outfits-v1`). Zero external API calls, zero telemetry, zero third-party CDNs.

## 3. Non-Goals (Frozen Scope Boundary — DO NOT IMPLEMENT UNLESS SPEC IS UPDATED)
1. **No Cloud Backend / Auth / Database:** The game is strictly local-first with JSON file Export/Import backup.
2. **No Engine Porting (Unity / Flutter / React Native):** Keep the single TypeScript + R3F WebGL codebase; if native store binaries are ever required later, wrap `dist/` with CapacitorJS.
3. **No Bulk Deletion of Unused `src/components/ui/*` Primitives:** Vite tree-shakes unused UI files at build time; leave them untouched to avoid churn.
4. **No Unsolicited Gameplay Scope Creep:** Do not invent new currencies, multiplayer servers, or extra game modes during routine maintenance audits.
