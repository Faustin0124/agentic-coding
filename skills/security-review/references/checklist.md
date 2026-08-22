# Ecosystem-Specific Security Grep Patterns

Concrete commands for the categories in `SKILL.md`, grouped by ecosystem. Extend this file
with new sections the same way if the project uses a stack not covered here — the categories
in `SKILL.md` generalize even where the exact command doesn't.

## JavaScript / TypeScript (Node, browser)

```bash
# Hardcoded-looking secrets
grep -rnE "(sk_live_|sk_test_|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36}|-----BEGIN.*PRIVATE KEY-----)" \
  --include="*.ts" --include="*.js" --include="*.env*" .

# String-built SQL
grep -rn "query(\`.*\${" --include="*.ts" --include="*.js" .
grep -rn "\.raw(\`.*\${" --include="*.ts" --include="*.js" .

# Raw HTML sinks
grep -rn "dangerouslySetInnerHTML\|\.innerHTML\s*=\|v-html" --include="*.tsx" --include="*.jsx" \
  --include="*.vue" .

# Token in browser-readable storage
grep -rn "localStorage\.setItem.*token\|sessionStorage\.setItem.*token" --include="*.ts" \
  --include="*.tsx" .

# Sensitive fields in logs
grep -rnE "console\.(log|error|info)\(.*\b(password|token|secret|cardNumber|cvv)\b" \
  --include="*.ts" --include="*.js" .

npm audit --json
npm outdated --json
```

## Python

```bash
grep -rnE "(sk_live_|AKIA[0-9A-Z]{16}|-----BEGIN.*PRIVATE KEY-----)" --include="*.py" .

# String-built SQL (f-strings / % / .format into execute())
grep -rn "execute(f[\"']" --include="*.py" .
grep -rn "execute(.*%\s*(" --include="*.py" .

# Unsafe deserialization / eval
grep -rn "pickle\.loads\|yaml\.load(\|eval(\|exec(" --include="*.py" .

pip-audit
pip list --outdated
```

## Go

```bash
grep -rnE "(sk_live_|AKIA[0-9A-Z]{16})" --include="*.go" .

# String-built SQL
grep -rn "fmt\.Sprintf.*SELECT\|fmt\.Sprintf.*INSERT" --include="*.go" .

# Command injection via unvalidated input
grep -rn "exec\.Command(" --include="*.go" .

govulncheck ./...
go list -u -m all
```

## Ruby / Rails

```bash
grep -rnE "(sk_live_|AKIA[0-9A-Z]{16})" --include="*.rb" .

# Raw SQL / mass assignment
grep -rn "\.where(\".*#{" --include="*.rb" .
grep -rn "permit!" --include="*.rb" .

bundler-audit check --update
```

## Rust

```bash
grep -rnE "(sk_live_|AKIA[0-9A-Z]{16})" --include="*.rs" .

# String-built SQL (when not using sqlx/diesel bound queries)
grep -rn "format!(.*SELECT\|format!(.*INSERT" --include="*.rs" .

cargo audit
cargo outdated
```

## Infra-as-code (any stack)

```bash
# Secrets committed in Terraform/CloudFormation/k8s manifests
grep -rnE "(password|secret|api_key)\s*=\s*[\"'][^\"']+[\"']" --include="*.tf" \
  --include="*.yaml" --include="*.yml" .

# Public storage buckets (Terraform example — adapt resource names to the provider in use)
grep -rn "acl\s*=\s*\"public-read\"" --include="*.tf" .
```
