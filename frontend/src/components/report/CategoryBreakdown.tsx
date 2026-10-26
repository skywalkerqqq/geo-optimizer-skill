import React from 'react';
import type { CategoryScore } from '../../lib/mockData';

const gradeConfig = {
  excellent: { color: '#059669', bg: 'rgba(5, 150, 105, 0.08)', label: 'Excellent' },
  good: { color: '#0D9488', bg: 'rgba(13, 148, 136, 0.08)', label: 'Good' },
  foundation: { color: '#D97706', bg: 'rgba(217, 119, 6, 0.08)', label: 'Foundation' },
  critical: { color: '#DC2626', bg: 'rgba(220, 38, 38, 0.08)', label: 'Critical' },
};

const CATEGORY_LABELS: Record<string, string> = {
  llms: 'llms.txt',
  schema: 'Schema JSON-LD',
  content: 'Content Quality',
  ai_discovery: 'AI Discovery',
  brand_entity: 'Brand & Entity',
};

const CATEGORY_MAX_SCORES: Record<string, number> = {
  llms: 18,
  schema: 16,
  content: 12,
  ai_discovery: 6,
  brand_entity: 10,
};

interface LockedCardProps {
  slug: string;
}

function LockedCard({ slug }: LockedCardProps) {
  return (
    <div className="relative p-4 rounded-lg border border-border bg-bg-surface overflow-hidden">
      {/* Blurred content background */}
      <div className="blur-[3px] pointer-events-none select-none" aria-hidden="true">
        <div className="flex items-center justify-between gap-2 mb-2">
          <span className="text-xs font-medium text-text-secondary truncate">
            {CATEGORY_LABELS[slug] ?? slug}
          </span>
          <span className="shrink-0 text-[10px] font-mono font-semibold px-1.5 py-0.5 rounded bg-bg-subtle text-text-muted">
            —
          </span>
        </div>
        <div className="flex items-baseline gap-1.5 mb-2.5">
          <span className="font-mono text-xl font-bold tabular-nums text-text-muted">??</span>
          <span className="font-mono text-xs text-text-muted">/ {CATEGORY_MAX_SCORES[slug] ?? '?'}</span>
        </div>
        <div className="h-1 rounded-full bg-bg-subtle overflow-hidden">
          <div className="h-full w-1/3 rounded-full bg-text-muted/30" />
        </div>
        <ul className="mt-2.5 space-y-1">
          {[1, 2, 3].map((i) => (
            <li key={i} className="h-3 rounded bg-bg-subtle" />
          ))}
        </ul>
      </div>

      {/* Lock overlay */}
      <div className="absolute inset-0 flex flex-col items-center justify-center bg-bg-surface/70 backdrop-blur-[1px] p-3 text-center">
        <div className="w-7 h-7 rounded-full bg-accent-teal/10 flex items-center justify-center mb-2">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" className="text-accent-teal">
            <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
            <path d="M7 11V7a5 5 0 0 1 10 0v4" />
          </svg>
        </div>
        <span className="text-[10px] font-mono font-semibold text-accent-teal uppercase tracking-wider leading-tight">
          Pro
        </span>
      </div>
    </div>
  );
}

interface CategoryBreakdownProps {
  categories: CategoryScore[];
  lockedSlugs?: string[];
}

export default function CategoryBreakdown({ categories, lockedSlugs = [] }: CategoryBreakdownProps) {
  const lockedSet = new Set(lockedSlugs);

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
      {categories.map((cat) => {
        if (lockedSet.has(cat.slug)) {
          return <LockedCard key={cat.slug} slug={cat.slug} />;
        }

        const config = gradeConfig[cat.grade];
        const pct = (cat.score / cat.maxScore) * 100;
        const isEmpty = cat.score === 0;

        return (
          <div
            key={cat.slug}
            className={`p-4 rounded-lg border bg-bg-surface transition-colors ${
              isEmpty ? 'border-border opacity-75' : 'border-border hover:border-accent-teal/25'
            }`}
          >
            <div className="flex items-center justify-between gap-2 mb-2">
              <span className="text-xs font-medium text-text-secondary truncate">{cat.name}</span>
              <span
                className="shrink-0 text-[10px] font-mono font-semibold px-1.5 py-0.5 rounded"
                style={{ color: config.color, backgroundColor: config.bg }}
              >
                {config.label}
              </span>
            </div>

            <div className="flex items-baseline gap-1.5 mb-2.5">
              <span className="font-mono text-xl font-bold tabular-nums" style={{ color: config.color }}>
                {cat.score}
              </span>
              <span className="font-mono text-xs text-text-muted">/ {cat.maxScore}</span>
            </div>

            <div className="h-1 rounded-full bg-bg-subtle overflow-hidden">
              <div
                className="h-full rounded-full transition-all duration-700 ease-out"
                style={{ width: `${pct}%`, backgroundColor: config.color }}
              />
            </div>

            {cat.signals.length > 0 && (
              <ul className="mt-2.5 space-y-1">
                {cat.signals.slice(0, 3).map((signal, i) => (
                  <li key={i} className="flex items-start gap-1.5 text-xs text-text-muted">
                    <span className="w-1 h-1 rounded-full mt-[5px] shrink-0" style={{ backgroundColor: config.color }} />
                    <span className="leading-snug">{signal}</span>
                  </li>
                ))}
              </ul>
            )}
          </div>
        );
      })}
    </div>
  );
}
