# Contributing

Ce repo n'est qu'une chose : une bibliothèque de skills Claude Code génériques, copiables tels
quels dans n'importe quel projet. Pas d'agents, pas de commandes, pas de hooks — si un skill a
besoin de ça, il n'a pas sa place ici (voir `README.md`, section "Ajouter un nouveau skill").

## Critère d'entrée

Un skill est éligible seulement s'il est **100% générique** :

- Aucune référence à un projet, client, ou stack précis dans le contenu (noms de personnes,
  conventions internes, schéma de base spécifique, etc.)
- Aucune dépendance à un framework unique sauf si le skill *est* sur ce framework par
  construction (ex: un futur `react-testing` serait légitimement React-only) — dans ce cas le
  nom du skill doit le dire explicitement
- Si le skill touche plusieurs stacks possibles (DB, sécurité, tests...), il doit détecter le
  stack du repo cible plutôt que d'en supposer un — voir `tech-debt-manager` et
  `security-review` pour le pattern ("Phase 0 — Detect the Stack")

Un skill développé sur un projet spécifique migre ici seulement après nettoyage complet des
références au projet d'origine.

## Format d'un SKILL.md

```
skill-name/
├── SKILL.md          (obligatoire)
└── references/        (optionnel — détail chargé à la demande, pas au démarrage)
    └── *.md
```

### Frontmatter

```yaml
---
name: skill-name
description: >
  Ce que fait le skill, formulé de façon un peu "pushy" pour éviter le sous-déclenchement —
  liste les contextes et formulations qui doivent le déclencher, même implicites. Termine par
  "Trigger on: ..." avec des exemples de phrases réalistes.
---
```

Le `description` est le seul mécanisme de déclenchement automatique — tout ce qui concerne le
"quand utiliser ce skill" va là, pas dans le corps du fichier.

### Corps

- Nom du fichier et du dossier : `lowercase-with-hyphens`
- Contenu en anglais (convention actuelle des skills existants), README et docs du repo en
  français
- Style impératif, orienté action — pas de prose théorique. Regarder `tech-debt-manager` ou
  `bug-diagnostics` comme référence de ton et de structure (phases numérotées, checklists,
  sections "Output" qui disent exactement quoi produire à la fin)
- Garder `SKILL.md` sous ~500 lignes. Au-delà, extraire le détail spécifique-au-stack ou
  peu-consulté dans `references/*.md` et y renvoyer explicitement depuis le corps
- Expliquer le *pourquoi* d'une règle plutôt que d'empiler des MUST/NEVER en majuscules — un
  agent suit mieux une contrainte dont il comprend la raison

### Chargement progressif

Un skill se charge en trois couches : `name` + `description` (toujours en contexte),
`SKILL.md` (chargé au déclenchement), `references/` (chargé seulement si le corps y renvoie).
Mettre dans `references/` tout ce qui est volumineux et consulté occasionnellement (patterns
spécifiques à un langage, exemples de grep par écosystème) plutôt que de tout mettre dans
`SKILL.md`.

## Ajouter un skill : checklist

- [ ] Le skill est générique (voir critère d'entrée ci-dessus)
- [ ] `description` couvre les formulations naturelles, pas juste le nom du skill
- [ ] Pas de secret, token, ou donnée réelle dans les exemples
- [ ] Section "Output" claire si le skill produit un livrable (fichier, backlog, rapport)
- [ ] Entrée ajoutée au tableau dans `README.md`

## Itérer sur un skill existant

Utiliser le skill `skill-creator` de ce repo lui-même — il couvre la boucle
draft → test → évaluation → révision, y compris l'optimisation du `description` pour le
déclenchement.
