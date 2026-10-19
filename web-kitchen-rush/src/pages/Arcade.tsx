import { lazy, Suspense, useCallback, useEffect, useSyncExternalStore } from 'react';
import { ArrowLeft } from 'lucide-react';
import { engine } from '@/game/engine';
import { KitchenAudio } from '@/game/audio';
import { Briefing, GameHUD, HomeScreen, ResultsScreen, Toolbar } from '@/components/KitchenUI';

const KitchenScene = lazy(() => import('@/scene/KitchenScene'));

/** Standalone route for the classic Solo / Couch Co-op Arcade cooking mode. */
export default function Arcade() {
  const state = useSyncExternalStore(engine.subscribe, engine.getSnapshot);
  useEffect(() => {
    const audio = new KitchenAudio();
    return () => { audio.dispose(); engine.pause(true); };
  }, []);
  const go = useCallback((path: string) => {
    engine.setPhase(path === '/briefing' ? 'briefing' : 'menu');
  }, []);
  const start = useCallback((practice = false) => {
    engine.start(practice);
  }, []);
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
    </div>
  );
}
