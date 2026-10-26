const STORAGE_KEY = 'geo_score_history';
const MAX_ENTRIES = 5;

export interface ScoreEntry {
  url: string;
  score: number;
  grade: string;
  timestamp: string;
}

function storageKey(domain: string): string {
  return `${STORAGE_KEY}:${domain}`;
}

function extractDomain(url: string): string {
  try {
    return new URL(url).hostname;
  } catch {
    return url;
  }
}

export function saveScore(entry: ScoreEntry): void {
  if (typeof localStorage === 'undefined') return;
  const domain = extractDomain(entry.url);
  const key = storageKey(domain);
  const existing = loadScores(entry.url);
  const updated = [entry, ...existing].slice(0, MAX_ENTRIES);
  try {
    localStorage.setItem(key, JSON.stringify(updated));
  } catch {
    // quota exceeded — skip silently
  }
}

export function loadScores(url: string): ScoreEntry[] {
  if (typeof localStorage === 'undefined') return [];
  const domain = extractDomain(url);
  const key = storageKey(domain);
  try {
    const raw = localStorage.getItem(key);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    if (!Array.isArray(parsed)) return [];
    return parsed as ScoreEntry[];
  } catch {
    return [];
  }
}

export function clearScores(url: string): void {
  if (typeof localStorage === 'undefined') return;
  const domain = extractDomain(url);
  localStorage.removeItem(storageKey(domain));
}
