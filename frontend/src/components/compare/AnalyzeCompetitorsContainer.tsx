import React, { useEffect, useState } from 'react';
import { fetchAuditReport } from '../../lib/api';
import type { AuditReport } from '../../lib/mockData';
import ScoreGauge from '../report/ScoreGauge';

type CompetitorState =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'error'; message: string }
  | { status: 'ready'; reports: AuditReport[] };

function readQueryParam(): string {
  if (typeof window === 'undefined') return '';
  return new URLSearchParams(window.location.search).get('urls') || '';
}

function CompactCompetitorCard({ report, index }: { report: AuditReport; index: number }) {
  const colors = ['text-accent-teal', 'text-accent-warning', 'text-accent-success', 'text-accent-danger', 'text-text-primary'];
  const labelColor = colors[index % colors.length];
  const criticalCount = report.recommendations.filter((r) => r.priority === 'critical').length;

  return (
    <div className="rounded-xl border border-border bg-bg-surface p-5">
      <div className="mb-4 pb-3 border-b border-border">
        <span className={`text-[10px] font-mono font-semibold uppercase tracking-wider ${labelColor}`}>
          Competitor {index + 1}
        </span>
        <p className="mt-1 text-sm text-text-primary font-medium truncate">{report.url}</p>
      </div>

      <div className="flex flex-col items-center mb-4">
        <ScoreGauge score={report.geoScore} label="GEO Score" />
      </div>

      <div className="space-y-2 text-sm">
        <div className="flex items-center justify-between">
          <span className="text-text-muted">Citability</span>
          <span className="font-mono font-semibold text-text-primary">{report.citabilityScore}/100</span>
        </div>
        <div className="flex items-center justify-between">
          <span className="text-text-muted">Grade</span>
          <span className="font-mono font-semibold text-text-primary uppercase">{report.grade}</span>
        </div>
        <div className="flex items-center justify-between">
          <span className="text-text-muted">Categories active</span>
          <span className="font-mono font-semibold text-text-primary">{report.categories.filter((c) => c.score > 0).length}/{report.categories.length}</span>
        </div>
        <div className="flex items-center justify-between">
          <span className="text-text-muted">Recommendations</span>
          <span className="font-mono font-semibold text-text-primary">{report.recommendations.length}</span>
        </div>
        {criticalCount > 0 && (
          <div className="flex items-center justify-between">
            <span className="text-text-muted">Critical</span>
            <span className="font-mono font-semibold text-accent-danger">{criticalCount}</span>
          </div>
        )}
      </div>

      <div className="mt-4 pt-3 border-t border-border">
        <h3 className="text-[10px] font-mono font-semibold uppercase tracking-wider text-text-muted mb-2">Top issues</h3>
        <ul className="space-y-1.5">
          {report.recommendations.slice(0, 3).map((rec) => (
            <li key={rec.id} className="text-xs text-text-secondary leading-snug">
              <span
                className={`inline-block w-1.5 h-1.5 rounded-full mr-1.5 align-middle ${
                  rec.priority === 'critical'
                    ? 'bg-accent-danger'
                    : rec.priority === 'high'
                      ? 'bg-accent-warning'
                      : 'bg-text-muted'
                }`}
              />
              {rec.title}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default function AnalyzeCompetitorsContainer() {
  const [urlsInput, setUrlsInput] = useState(readQueryParam);
  const [state, setState] = useState<CompetitorState>({ status: 'idle' });

  useEffect(() => {
    const raw = readQueryParam();
    if (!raw.trim()) {
      setState({ status: 'idle' });
      return;
    }
    const urls = raw
      .split(',')
      .map((u) => u.trim())
      .filter((u) => u.startsWith('http'));
    if (urls.length === 0) {
      setState({ status: 'idle' });
      return;
    }
    setUrlsInput(raw);
    setState({ status: 'loading' });

    Promise.all(urls.map((u) => fetchAuditReport(u)))
      .then((results) => {
        const errors = results.filter((r) => r.error);
        if (errors.length > 0) {
          setState({
            status: 'error',
            message: `${errors.length} audit(s) failed: ${errors.map((e) => e.error).join('; ')}`,
          });
          return;
        }
        const reports = results.map((r) => r.report).filter(Boolean) as AuditReport[];
        if (reports.length === 0) {
          setState({ status: 'error', message: 'No valid reports returned.' });
          return;
        }
        setState({ status: 'ready', reports });
      })
      .catch((e) => setState({ status: 'error', message: e.message || 'Network error' }));
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const trimmed = urlsInput.trim();
    if (!trimmed) return;
    const u = new URL(window.location.href);
    u.searchParams.set('urls', trimmed);
    window.location.href = u.toString();
  };

  if (state.status === 'loading') {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 py-12 text-center">
        <div className="inline-flex items-center gap-2 text-sm text-text-muted">
          <svg className="animate-spin w-4 h-4 text-accent-teal" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" className="opacity-20" />
            <path d="M22 12a10 10 0 0 1-10 10" stroke="currentColor" strokeWidth="4" strokeLinecap="round" />
          </svg>
          Running competitor audits...
        </div>
      </div>
    );
  }

  if (state.status === 'error') {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 py-12">
        <div className="p-5 rounded-xl border border-accent-danger/20 bg-accent-danger/5 text-accent-danger text-sm">
          <div className="font-semibold mb-1">Analysis failed</div>
          {state.message}
        </div>
        <button
          onClick={() => setState({ status: 'idle' })}
          className="mt-4 inline-flex items-center gap-2 rounded-lg border border-border px-4 py-2 text-sm font-medium text-text-primary hover:border-accent-teal/30 transition-colors"
        >
          Back to form
        </button>
      </div>
    );
  }

  if (state.status === 'ready') {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 py-6 md:py-8 space-y-6">
        <div className="flex items-center justify-between">
          <h2 className="font-display text-lg font-bold text-text-primary">Competitor analysis</h2>
          <button
            onClick={() => {
              const u = new URL(window.location.href);
              u.search = '';
              window.location.href = u.toString();
            }}
            className="inline-flex items-center gap-2 rounded-lg border border-border px-3 py-1.5 text-sm font-medium text-text-secondary hover:text-text-primary hover:border-accent-teal/30 transition-colors"
          >
            New analysis
          </button>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {state.reports.map((report, i) => (
            <CompactCompetitorCard key={report.id} report={report} index={i} />
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6">
      <div className="p-6 md:p-8 rounded-xl border border-border bg-bg-surface">
        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label htmlFor="urls" className="block text-sm font-medium mb-2">Competitor URLs (comma-separated, max 5)</label>
            <input
              id="urls"
              type="text"
              required
              placeholder="https://competitor1.com, https://competitor2.com"
              value={urlsInput}
              onChange={(e) => setUrlsInput(e.target.value)}
              className="w-full px-4 py-3 rounded-lg border border-border bg-bg-base text-sm text-text-primary placeholder:text-text-muted focus:outline-none focus:ring-2 focus:ring-accent-teal transition-shadow"
            />
            <p className="mt-1.5 text-xs text-text-muted">Enter one or more URLs separated by commas.</p>
          </div>
          <button
            type="submit"
            className="px-6 py-3 rounded-lg bg-accent-teal text-white font-medium text-sm hover:bg-accent-teal-dark transition-colors"
          >
            Analyze
          </button>
        </form>
      </div>
    </div>
  );
}
