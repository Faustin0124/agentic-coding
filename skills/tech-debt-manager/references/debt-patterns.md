# Common Debt Patterns — React/TypeScript + Backend-as-a-Service Stack

Patterns worth checking for on top of the generic Phase 1 greps in SKILL.md, written for a
React 18 + TypeScript + Vite + Supabase-style stack since that's the best-understood example
here. If the project uses a different framework, data layer, or backend, the *categories*
below still apply — typing debt, data-fetching debt, backend/RLS debt, test-coverage
prioritization, build/perf debt, CI debt — even where the exact grep commands need substituting
for the equivalent tool in that stack.

---

## React + TypeScript

### Patterns to detect

**Implicit `any` in props**
```tsx
// Debt
const MyComponent = ({ data }: { data: any }) => ...

// Fix
const MyComponent = ({ data }: { data: SomeDomainType }) => ...
```

**`useEffect` with missing or empty dependencies**
```tsx
// Common debt — masks stale-closure bugs
useEffect(() => {
  fetchData(userId); // userId used but missing from deps
}, []);

// Detect with:
grep -rn "useEffect" src/ --include="*.tsx" | grep "\[\]"
```

**Components over ~200 lines**
- Signal: business logic mixed with UI in the same component
- Fix: extract logic into a `src/hooks/use{Domain}.ts` hook

**Context used for server state**
- Anti-pattern: caching backend data in React Context instead of a data-fetching library
- Fix: migrate to TanStack Query (or whatever data-fetching library the project already has)

```bash
grep -rn "createContext\|useContext" src/ --include="*.tsx" --include="*.ts" | grep -v "hooks\|provider" | head -20
```

---

## TanStack React Query (or equivalent)

### Patterns to detect

**No `staleTime` configured (defaults to 0)**
```bash
# Queries without explicit staleTime = unnecessary refetch on every focus
grep -rn "useQuery\|useMutation" src/ --include="*.tsx" --include="*.ts" | grep -v "staleTime" | wc -l
```

**Over-broad invalidation (`queryClient.invalidateQueries()` with no filter)**
```bash
grep -rn "invalidateQueries()" src/
```

**Missing error handling on critical mutations** (payments, auth, anything user-money-facing)
```bash
grep -rn "useMutation" src/ --include="*.tsx" -A 10 | grep -L "onError"
```

---

## Zod + React Hook Form (or equivalent validation stack)

### Patterns to detect

**Validation schemas duplicated between frontend and backend**
```bash
# Compare schema definitions on both sides
grep -rn "z\.object" src/ -l
grep -rn "z\.object" <backend-functions-dir>/ -l
```

**Missing validation in backend handlers**
```bash
# Any handler reading a request body without a schema parse
grep -rL "\.parse\|\.safeParse" <backend-functions-dir>/*/index.ts
```

**Redundant validation schemas across similar domain variants** — if the project has several
structurally-similar entities (multiple product tiers, multiple document types, multiple
calculation modes), their schemas are a common duplication site; a candidate for extraction
into one shared schema module.

---

## Backend-as-a-Service (Supabase-style)

### Critical patterns (P0/P1)

**Missing or incomplete row-level security**
```bash
grep -l "CREATE TABLE" supabase/migrations/*.sql | while read f; do
  if ! grep -q "ENABLE ROW LEVEL SECURITY" "$f"; then
    echo "Missing RLS: $f"
  fi
done
```

**Generated types out of sync with the schema**
```bash
echo "Generated types:" && stat src/integrations/supabase/types.ts | grep Modify
echo "Latest migration:" && ls -la supabase/migrations/ | tail -2
```
If the migration is newer, regenerate: `supabase gen types typescript --local > src/integrations/supabase/types.ts`

**Direct backend calls inside components (bypassing hooks)**
```bash
# Anti-pattern: no caching, no retry, hard to test
grep -rn "supabase\.from\|supabase\.auth" src/components/ --include="*.tsx" -l
```

**Edge/serverless functions missing CORS handling**
```bash
grep -rL "_shared/cors\|corsHeaders" supabase/functions/*/index.ts 2>/dev/null
```

**Irreversible migrations without a comment explaining why**
```bash
grep -rn "DROP TABLE\|DROP COLUMN" supabase/migrations/ | head -10
```

---

## Test Coverage Priorities

**P0 — Core business logic (zero tolerance for gaps)**
- Anything under a `lib/`, `domain/`, or `calculations/` directory that computes a
  user-facing result (pricing, eligibility, scoring, financial or legal output)

**P1 — Business hooks**
- Hooks that call the backend or perform a calculation

**P2 — Critical components**
- Complex forms, payment-flow components

**Example unit test for a pure function:**
```typescript
import { describe, it, expect } from 'vitest';
import { computeDiscount } from '../pricing';

describe('computeDiscount', () => {
  it('applies a 10% discount above the threshold', () => {
    const result = computeDiscount({ amount: 1000, threshold: 500 });
    expect(result.finalAmount).toBe(900);
  });
});
```

---

## i18n (if the project is localized)

**Hardcoded strings in JSX instead of translation keys**
```bash
grep -rn '"[A-Z][a-z ]\{15,\}"' src/components/ --include="*.tsx" | head -20
```

**Translation keys defined but never used**
```bash
find src/ -name "*.json" -path "*/locales/*" | head -5
```

---

## Build / Performance

**Non-tree-shaken imports**
```bash
grep -rn "import \* as" src/ --include="*.ts" --include="*.tsx" | grep -v "// "
```

**Heavy components without lazy loading**
```bash
grep -rn "React.lazy\|lazy(" src/ --include="*.tsx" | wc -l
grep -rn "<Route" src/ --include="*.tsx" | wc -l   # compare against route count
```

---

## CI

**Unpinned GitHub Actions (supply-chain risk)**
```bash
grep -rn "uses:" .github/workflows/ | grep -v "@v[0-9]\|@[a-f0-9]\{40\}" | head -10
```

**Unused or redundant secrets**
```bash
grep -rn "\${{ secrets\." .github/workflows/ | sed 's/.*secrets\.\([A-Z_]*\).*/\1/' | sort -u
```
