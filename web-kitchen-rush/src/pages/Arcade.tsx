import { lazy, Suspense, useCallback, useEffect, useSyncExternalStore } from 'react';
import { ArrowDown, ArrowLeft, ArrowRight, ArrowUp, Hand, Utensils } from 'lucide-react';
import { engine } from '@/game/engine';
import { KitchenAudio } from '@/game/audio';
import { Briefing, GameHUD, HomeScreen, ResultsScreen, Toolbar } from '@/components/KitchenUI';
import { DashButton } from '@/components/DashStatus';
import { activeInput } from '@/game/input';

const KitchenScene = lazy(() => import('@/scene/KitchenScene'));

/** Standalone route for the classic Solo / Couch Co-op Arcade cooking mode. */
export default function Arcade() {
  const state = useSyncExternalStore(engine.subscribe, engine.getSnapshot);
  useEffect(() => {
    const audio = new KitchenAudio();
    return () => { audio.dispose(); activeInput?.clear(); engine.pause(true); };
  }, []);
  useEffect(() => {
    if (state.phase !== 'playing' || state.paused) activeInput?.clear();
  }, [state.phase, state.paused]);
  const go = useCallback((path: string) => {
    engine.setPhase(path === '/briefing' ? 'briefing' : 'menu');
  }, []);
  const start = useCallback((practice = false) => {
    engine.start(practice);
  }, []);
  const setMove = (x: number, y: number) => {
    if (activeInput) { activeInput.touch.x = x; activeInput.touch.y = y; }
  };
  return (
    <div className="relative min-h-[100svh] overflow-hidden bg-teal text-ink">
      <div className="fixed inset-0 z-0">
        <Suspense fallback={<div className="grid h-full place-items-center font-display text-xl text-paper">Setting the tables…</div>}>
          <KitchenScene state={state} />
        </Suspense>
      </div>
      {state.phase !== 'playing' && (
        <a
          href="/"
          className="pointer-events-auto fixed left-5 top-5 z-30 flex min-h-11 items-center gap-2 rounded-xl border border-paper/60 bg-paper/90 px-3.5 text-xs font-extrabold text-teal shadow-md transition hover:bg-paper"
        >
          <ArrowLeft className="size-4" />
          Tycoon Mode
        </a>
      )}
      <Toolbar state={state} go={go} start={start} />
      <div className="relative z-10">
        {state.phase === 'menu' && <HomeScreen state={state} go={go} start={start} />}
        {state.phase === 'briefing' && <Briefing state={state} go={go} start={start} />}
        {state.phase === 'playing' && <GameHUD state={state} />}
        {state.phase === 'results' && <ResultsScreen state={state} go={go} start={start} />}
      </div>
      {state.phase === 'playing' && !state.paused && state.mode === 'solo' && (
        <section
          aria-label="Touch controls"
          className="pointer-events-none fixed inset-x-4 bottom-24 z-30 flex items-end justify-between xl:hidden"
        >
          <div className="pointer-events-auto grid grid-cols-3 gap-1.5 select-none touch-none">
            <span />
            <button
              type="button"
              aria-label="Move up"
              className="grid size-12 place-items-center rounded-xl border border-paper/50 bg-ink/85 text-paper active:bg-teal"
              onPointerDown={() => setMove(0, 1)}
              onPointerUp={() => setMove(0, 0)}
              onPointerCancel={() => setMove(0, 0)}
              onPointerLeave={() => setMove(0, 0)}
            >
              <ArrowUp className="size-5" />
            </button>
            <span />
            <button
              type="button"
              aria-label="Move left"
              className="grid size-12 place-items-center rounded-xl border border-paper/50 bg-ink/85 text-paper active:bg-teal"
              onPointerDown={() => setMove(-1, 0)}
              onPointerUp={() => setMove(0, 0)}
              onPointerCancel={() => setMove(0, 0)}
              onPointerLeave={() => setMove(0, 0)}
            >
              <ArrowLeft className="size-5" />
            </button>
            <button
              type="button"
              aria-label="Move down"
              className="grid size-12 place-items-center rounded-xl border border-paper/50 bg-ink/85 text-paper active:bg-teal"
              onPointerDown={() => setMove(0, -1)}
              onPointerUp={() => setMove(0, 0)}
              onPointerCancel={() => setMove(0, 0)}
              onPointerLeave={() => setMove(0, 0)}
            >
              <ArrowDown className="size-5" />
            </button>
            <button
              type="button"
              aria-label="Move right"
              className="grid size-12 place-items-center rounded-xl border border-paper/50 bg-ink/85 text-paper active:bg-teal"
              onPointerDown={() => setMove(1, 0)}
              onPointerUp={() => setMove(0, 0)}
              onPointerCancel={() => setMove(0, 0)}
              onPointerLeave={() => setMove(0, 0)}
            >
              <ArrowRight className="size-5" />
            </button>
          </div>
          <div className="pointer-events-auto flex flex-col items-end gap-2 select-none touch-none">
            <div className="flex gap-2">
              <button
                type="button"
                aria-label="Pick up or place"
                className="game-button min-h-11 px-3.5 py-2 text-sm"
                onClick={() => { if (activeInput) activeInput.touch.pick = true; }}
              >
                <Hand className="size-4" />Pick / Place
              </button>
              <button
                type="button"
                aria-label="Hold to work"
                className="game-button min-h-11 px-3.5 py-2 text-sm active:bg-gold"
                onPointerDown={() => { if (activeInput) activeInput.touch.work = true; }}
                onPointerUp={() => { if (activeInput) activeInput.touch.work = false; }}
                onPointerCancel={() => { if (activeInput) activeInput.touch.work = false; }}
                onPointerLeave={() => { if (activeInput) activeInput.touch.work = false; }}
              >
                <Utensils className="size-4" />Hold Work
              </button>
            </div>
            <DashButton
              chef={state.chefs[0]}
              paused={state.paused}
              onDash={() => { if (activeInput) activeInput.touch.dash = true; }}
            />
          </div>
        </section>
      )}
    </div>
  );
}
