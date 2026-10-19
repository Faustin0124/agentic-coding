# agentic-coding

Skills Claude Code réutilisables pour coder sur n'importe quel projet — génériques,
sans dépendance à un stack ou un client en particulier.

## Contenu

### Code et ingénierie

| Skill | Usage |
|---|---|
| `test-architect` | Stratégie de tests : pyramide de tests, isolation, tests par propriété, quality gates |
| `database-optimizer` | Optimisation de perf DB, tuning de requêtes |
| `database-schema-design` | Modélisation de données, migrations, relations |
| `database-migrations` | Évolution de schéma sans downtime, rollback |
| `supabase-security` | RLS, sécurité multi-tenant, tokens Supabase |
| `skill-creator` | Créer et itérer sur des skills Claude Code |
| `frontend-design` | UI/composants front anti-slop : lit `design.md` en priorité, sinon infère le goût (dials, anti-clichés, pre-flight) |
| `bug-diagnostics` | Diagnostic de bug en 5 phases : triage → cause racine → propagation → plan → ticket (Notion/GitHub/local) |
| `tech-debt-manager` | Audit dette technique (deps, types, code smells, tests, sécurité) → backlog exécutable scoré |
| `tdd` | Boucle red-green-refactor : bons tests vs anti-patterns, seams pré-accordés, un slice à la fois |
| `diagnosing-bugs` | Diagnostic de bugs difficiles en 6 phases : boucle de feedback → repro/minimise → hypothèses → instrumentation → fix → nettoyage |
| `code-review` | Review du diff sur deux axes indépendants (Standards + baseline Fowler / Spec), lancés en sous-agents parallèles |
| `codebase-design` | Vocabulaire partagé pour les modules "deep" : interface, seam, adapter, leverage, locality |
| `resolving-merge-conflicts` | Résout un merge/rebase conflit par conflit en retrouvant l'intention de chaque source, jamais d'`--abort` |

Les cinq skills `tdd`, `diagnosing-bugs`, `code-review`, `codebase-design` et `resolving-merge-conflicts` viennent de [mattpocock/skills](https://github.com/mattpocock/skills) (bucket `engineering`, skills model-invoked), adaptés ici en enlevant leur dépendance à son propre workflow (tracker d'issues, `/setup-matt-pocock-skills`) pour rester autonomes.

### Product management

| Skill | Usage |
|---|---|
| `product-notes` | Convertit une note en vrac en Epic/User Story structurée dans un backlog Notion, sans base figée |
| `product-flow` | Chef d'orchestre : part d'un item du backlog Notion (ou d'un problème brut), déroule les skills produit avec une porte de validation par étape, écrit `docs/<sujet>/` puis exporte dans Notion |
| `jobs-to-be-done` | Jobs fonctionnels, sociaux et émotionnels derrière le comportement client : bien définir le problème |
| `mom-test` | Guide d'entretien, audit de questions et tri vrai/faux signal dans des transcripts |
| `amazon-working-backwards` | PR/FAQ pour tester si une idée vaut la peine d'être construite avant de spécifier |
| `write-prd` | Point d'entrée PRD : questions ciblées puis génération du spec, avec le flux complet recommandé |
| `craft-spec` | Notes en vrac → PRD structuré (problème, métriques, scope, solution, stories, questions ouvertes) |
| `draft-spec` | Spec détaillé : exploration de solutions, parcours précis, critères d'acceptation testables |
| `pre-mortem` | Imaginer l'échec avant de livrer : Tigres, Tigres de papier, Éléphants |
| `create-user-stories` | PRD → user stories prêtes pour le dev avec critères Given/When/Then |
| `product-designer` | Flows, architecture de l'info, navigation, code UI structurel — complémentaire de `frontend-design` pour le goût visuel |

Les huit skills de `jobs-to-be-done` à `create-user-stories` (hors `product-notes`, `product-flow` et `product-designer`) sont issus de [amplitude/builder-skills](https://github.com/amplitude/builder-skills) (plugin `product-skills`), traduits en français et débarrassés de leurs dépendances à Amplitude.

#### Workflow produit : de l'idée au dev

`product-notes` capture une idée dans le backlog Notion ; `product-flow` la raffine ensuite, étape par étape, avec une porte de validation à chaque fois :

```
product-notes (capture dans Notion)
        │
product-flow ── 0. cadrage ──► choisit le point d'entrée
        │  1. jobs-to-be-done / mom-test       → problème réel et précis ?
        │  2. amazon-working-backwards         → ça vaut le coup de construire ?
        │  3. write-prd (craft-spec / draft-spec) → PRD validé ?
        │  4. pre-mortem                       → risques bloquants traités ?
        │  5. create-user-stories              → prêt pour le dev ?
        ▼
docs/<sujet>/ (brief, prd, risques, stories)  +  export Notion (Epic puis stories)
```

- Un item de taille Epic est raffiné au niveau Epic (un seul PRD), puis découpé en stories validées avant écriture.
- Chaque skill reste utilisable seul (`/mom-test`, `/pre-mortem`…) sans passer par `product-flow`.
- **Prérequis** : le connecteur Notion pour la capture et l'export (`product-notes`, `product-flow`). Sans Notion, `product-flow` fonctionne avec un problème donné en conversation et les fichiers `docs/<sujet>/`.
- **Installation** : `product-flow` appelle les autres skills du groupe, copie-les ensemble :

```bash
for s in product-notes product-flow jobs-to-be-done mom-test amazon-working-backwards \
         write-prd craft-spec draft-spec pre-mortem create-user-stories; do
  cp -R skills/$s /chemin/vers/projet/.claude/skills/
done
```

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
