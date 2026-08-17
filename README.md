# agentic-coding

Skills Claude Code réutilisables pour coder sur n'importe quel projet — génériques,
sans dépendance à un stack ou un client en particulier.

## Contenu

| Skill | Usage |
|---|---|
| `test-architect` | Stratégie de tests : pyramide de tests, isolation, tests par propriété, quality gates |
| `database-optimizer` | Optimisation de perf DB, tuning de requêtes |
| `database-schema-design` | Modélisation de données, migrations, relations |
| `database-migrations` | Évolution de schéma sans downtime, rollback |
| `supabase-security` | RLS, sécurité multi-tenant, tokens Supabase |
| `skill-creator` | Créer et itérer sur des skills Claude Code |
| `frontend-design` | UI/composants front anti-slop : lit `design.md` en priorité, sinon infère le goût (dials, anti-clichés, pre-flight) |
| `product-designer` | Flows, architecture de l'info, navigation, code UI structurel — complémentaire de `frontend-design` pour le goût visuel |
| `bug-diagnostics` | Diagnostic de bug en 5 phases : triage → cause racine → propagation → plan → ticket (Notion/GitHub/local) |
| `tech-debt-manager` | Audit dette technique (deps, types, code smells, tests, sécurité) → backlog exécutable scoré |
| `product-notes` | Convertit une note en vrac en Epic/User Story structurée dans un backlog Notion, sans base figée |

## Réutiliser un skill dans un nouveau projet

Copier le dossier du skill dans `.claude/skills/` du projet :

```bash
cp -R skills/<nom-du-skill> /chemin/vers/projet/.claude/skills/
```

Ou, pour toujours avoir la dernière version sans dupliquer :

```bash
ln -s /chemin/vers/agentic-coding/skills/<nom-du-skill> /chemin/vers/projet/.claude/skills/<nom-du-skill>
```

## Ajouter un nouveau skill

Un skill générique développé sur un projet spécifique (ex: Pradio) mérite sa place ici
seulement s'il ne contient aucune référence au projet d'origine (stack précis, noms de
personnes, conventions internes, etc.). Sinon il reste dans le repo du projet.
