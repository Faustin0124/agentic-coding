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
| `tdd` | Boucle red-green-refactor : bons tests vs anti-patterns, seams pré-accordés, un slice à la fois |
| `diagnosing-bugs` | Diagnostic de bugs difficiles en 6 phases : boucle de feedback → repro/minimise → hypothèses → instrumentation → fix → nettoyage |
| `code-review` | Review du diff sur deux axes indépendants (Standards + baseline Fowler / Spec), lancés en sous-agents parallèles |
| `codebase-design` | Vocabulaire partagé pour les modules "deep" : interface, seam, adapter, leverage, locality |
| `resolving-merge-conflicts` | Résout un merge/rebase conflit par conflit en retrouvant l'intention de chaque source, jamais d'`--abort` |
| `product-flow` | Chef d'orchestre : part d'un item du backlog Notion (ou d'un problème brut), déroule les skills produit avec une porte de validation par étape, écrit `docs/<sujet>/` puis exporte dans Notion |
| `write-prd` | Point d'entrée PRD : questions ciblées puis génération du spec, avec le flux complet recommandé |
| `jobs-to-be-done` | Jobs fonctionnels, sociaux et émotionnels derrière le comportement client : bien définir le problème |
| `mom-test` | Guide d'entretien, audit de questions et tri vrai/faux signal dans des transcripts |
| `amazon-working-backwards` | PR/FAQ pour tester si une idée vaut la peine d'être construite avant de spécifier |
| `craft-spec` | Notes en vrac → PRD structuré (problème, métriques, scope, solution, stories, questions ouvertes) |
| `draft-spec` | Spec détaillé : exploration de solutions, parcours précis, critères d'acceptation testables |
| `pre-mortem` | Imaginer l'échec avant de livrer : Tigres, Tigres de papier, Éléphants |
| `create-user-stories` | PRD → user stories prêtes pour le dev avec critères Given/When/Then |

Les huit skills produit (`write-prd` … `create-user-stories`, orchestrés par `product-flow`) sont issus de [amplitude/builder-skills](https://github.com/amplitude/builder-skills) (plugin `product-skills`), traduits en français et débarrassés de leurs dépendances à Amplitude. `product-notes` capture les idées dans le backlog Notion ; `product-flow` les raffine ensuite : `jobs-to-be-done` / `mom-test` → `amazon-working-backwards` → `write-prd` → `pre-mortem` → `create-user-stories`, puis export dans Notion.

Ces cinq derniers viennent de [mattpocock/skills](https://github.com/mattpocock/skills) (bucket `engineering`, skills model-invoked), adaptés ici en enlevant leur dépendance à son propre workflow (tracker d'issues, `/setup-matt-pocock-skills`) pour rester autonomes.

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
