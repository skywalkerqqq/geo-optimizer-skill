import React, { useEffect, useState } from 'react';
import { loadScores } from '../../lib/scoreHistory';
import type { ScoreEntry } from '../../lib/scoreHistory';

const gradeColor: Record<string, string> = {
  excellent: '#059669',
  good: '#0D9488',
  foundation: '#D97706',
  critical: '#DC2626',
};

interface ScoreHistoryProps {
  url: string;
  currentScore: number;
}

export default function ScoreHistory({ url, currentScore }: ScoreHistoryProps) {
  const [entries, setEntries] = useState<ScoreEntry[]>([]);

  useEffect(() => {
    setEntries(loadScores(url));
  }, [url, currentScore]);

  if (entries.length < 2) return null;

  const oldest = entries[entries.length - 1];
  const delta = currentScore - oldest.score;
  const deltaPositive = delta > 0;

  return (
    <div className="p-4 rounded-xl border border-border bg-bg-surface">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-[10px] font-mono font-semibold uppercase tracking-wider text-text-muted">
          Score History
        </h3>
        <span className={`text-xs font-mono font-semibold tabular-nums ${deltaPositive ? 'text-accent-success' : delta < 0 ? 'text-accent-danger' : 'text-text-muted'}`}>
          {deltaPositive ? '+' : ''}{delta} vs first
        </span>
      </div>

      <div className="flex items-end gap-1 h-10">
        {[...entries].reverse().map((entry, i) => {
          const isLast = i === entries.length - 1;
          const heightPct = Math.max(8, (entry.score / 100) * 100);
          const color = gradeColor[entry.grade] ?? '#6B7280';
          return (
            <div key={i} className="flex-1 flex flex-col items-center gap-0.5 group relative">
              <div
                className={`w-full rounded-sm transition-all ${isLast ? 'ring-1 ring-accent-teal/50' : ''}`}
                style={{ height: `${heightPct}%`, backgroundColor: color, opacity: isLast ? 1 : 0.5 }}
              />
              <div className="absolute -top-7 left-1/2 -translate-x-1/2 hidden group-hover:flex bg-bg-surface border border-border rounded px-1.5 py-0.5 text-[10px] font-mono text-text-primary whitespace-nowrap shadow-sm z-10">
                {entry.score} · {new Date(entry.timestamp).toLocaleDateString('en', { month: 'short', day: 'numeric' })}
              </div>
            </div>
          );
        })}
      </div>

      <div className="mt-2 flex items-center justify-between text-[10px] text-text-muted">
        <span>{new Date(oldest.timestamp).toLocaleDateString('en', { month: 'short', day: 'numeric' })}</span>
        <span>Today</span>
      </div>
    </div>
  );
}
