# Gabarits des livrables

Utilisés tels quels dans la réponse en conversation, ou écrits dans `docs/<sujet>/` quand l'évolution part en dev.

## `ux-diagnostic.md`

```markdown
---
sujet: <titre>
ecran: <nom de l'écran / route>
sources: <captures, code, verbatims, données>
statut: en cours | validé
mis_a_jour: JJ/MM/AAAA
---

# Diagnostic : <écran>

## Objectif de l'écran
<La tâche que l'utilisateur doit terminer ici, en une phrase.>

## Inventaire
- Zones : …
- Actions : …
- Statuts / compteurs / messages : …
- Volumes : <n éléments, dont x à traiter>

## Incohérences relevées
| Constat | Où | Constaté / supposé |
|---|---|---|

## Problème 1 : « <verbatim utilisateur> »
Causes :
- …

## Problème 2 : « … »
Causes :
- …
```

## `ux-options.md`

```markdown
# Options : <écran>

## Option A : <nom court> (traite : P1)
<Principe en 2–3 lignes.>

    <maquette texte, 5–10 lignes>

Coût : front seul | front + back. Risque : …

## Option B : …

## Recommandation
v1 : <options retenues>, parce que <causes couvertes, coût>.
Ensuite : <option différée et condition pour la lancer>.
```

## `ux-livrable.md`

```markdown
# Livrable : <écran>

## Prompt Lovable (ou brief dev)
> Dans <écran> : (1) … ; (2) … ; (3) … Ne change pas <…>. Respecte le design system existant.

## Métriques
| Métrique | Problème visé | Événement à tracker | Valeur actuelle → cible |
|---|---|---|---|

## Dépendances et cas limites
- Back : …
- À vérifier dans le code : …
- Cas limites : zéro élément à traiter, tous traités, gros volume.

## Questions ouvertes
- …
```

## Bonnes pratiques pour le prompt Lovable

- Une modification par point numéroté, formulée comme un comportement observable.
- Nommer les éléments avec les **libellés réels** de l'écran pour que l'agent les retrouve.
- Dire ce qui **ne change pas** (données, autres sections, design system).
- Donner les textes exacts des nouveaux libellés plutôt que « un message clair ».
- Si la solution dépend d'une donnée que le back ne fournit peut-être pas, demander d'abord en `plan_mode` à l'agent Lovable de vérifier.
