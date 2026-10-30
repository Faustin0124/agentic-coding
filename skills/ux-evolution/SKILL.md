---
name: ux-evolution
description: Fait évoluer un parcours, un écran ou une interaction qui existe déjà. Part de l'existant (captures d'écran, code, preview, données d'usage) et de problèmes utilisateur exprimés, observe l'écran avant de proposer, relie chaque problème à ses causes, compare 2–3 options, recommande une v1 et livre du concret (maquette texte, prompt Lovable, métriques, dépendances back). Délègue à product-designer, frontend-design, draft-spec et create-user-stories. Déclencheurs : "mon utilisateur ne comprend pas…", "il perd du temps à…", "quelles solutions lui apporter ?", "évol du parcours X", "améliore cet écran", "refonte de", "simplifier le tunnel", "les users bloquent à l'étape Y", captures d'écran accompagnées de problèmes utilisateur.
---

# UX Evolution

**D'un écran existant et d'un irritant utilisateur à une évolution prête à construire.**

Ce skill traite les évolutions **d'un parcours qui existe déjà**. On ne part pas d'une page blanche : l'écran actuel est la première source de preuves. La moitié du diagnostic se trouve dans ce qui est déjà affiché (compteurs contradictoires, libellés vagues, signaux visuels sans signification).

- Nouveau sujet ou problème encore flou → `product-flow`.
- Nouveaux écrans ou nouvelle navigation à concevoir → `product-designer`.
- Rendu visuel d'un écran déjà décidé → `frontend-design`.

## Entrée

`$ARGUMENTS` : en général, **des captures d'écran + un ou plusieurs problèmes utilisateur + une question** (« quelles solutions ? »). Formes acceptées :
- des captures d'écran ou une URL de preview ;
- le chemin d'une route ou d'un composant dans le code ;
- des verbatims, tickets de support, notes d'entretien ;
- des données d'usage (entonnoir Amplitude, taux d'abandon) si un connecteur est disponible.

Si aucune image ni aucun code n'est fourni, demande-les : sans l'écran réel, le diagnostic devient une supposition.

## Dossier de travail : `docs/<sujet>/`

Pour une demande rapide en conversation, réponds directement sans créer de fichiers. Si l'évolution doit partir en dev ou si l'utilisateur le demande, écris :

| Fichier | Contenu | Étape |
|---|---|---|
| `ux-diagnostic.md` | Inventaire de l'écran, incohérences, causes par problème | 1–2 |
| `ux-options.md` | Options, compromis, recommandation, maquettes texte | 3 |
| `ux-livrable.md` | Prompt Lovable / brief dev, métriques, dépendances, questions ouvertes | 4 |

Les gabarits sont dans [`references/livrables.md`](references/livrables.md).

## Parcours

### Étape 0. Cadrage (seulement si nécessaire)
Ne pose des questions que si l'entrée ne permet pas de répondre. Trois au plus :
- Qui est l'utilisateur, et que cherche-t-il à accomplir sur cet écran ?
- D'où vient le problème : observé, rapporté, mesuré, ou supposé ?
- Une contrainte forte (pas de changement côté back, délai, design system imposé) ?

Si le problème n'est qu'une intuition et que l'enjeu est gros, signale-le et propose `mom-test` pour le vérifier. Ne bloque pas pour autant : on peut avancer en le notant comme **supposé**.

### Étape 1. Observer avant de proposer
Décris l'écran **tel qu'il est**, sans encore juger :
- **Objectif de l'écran** : la tâche que l'utilisateur doit terminer ici.
- **Inventaire** : zones, actions (boutons, liens), statuts, compteurs, messages, couleurs ou pastilles et leur signification supposée.
- **Volumes** : nombre d'éléments, proportion à traiter par rapport au total, longueur de scroll.

Puis passe l'écran à la grille de [`references/grille-diagnostic.md`](references/grille-diagnostic.md). Relève en priorité les **incohérences internes** : deux compteurs qui ne disent pas le même nombre, un message qui contredit l'état d'un bouton, une couleur qui change de sens. Cite ce qu'on voit (« en haut : "13 lignes…", en bas : "1 ligne…" ») pour que l'utilisateur puisse vérifier.

Quand le code est accessible, vérifie ce que l'écran ne montre pas : états vide, chargement, erreur, conditions d'affichage, et **données réellement disponibles** (le back fournit-il ce dont la solution aura besoin ?).

### Étape 2. Relier chaque problème à ses causes
Pour chaque problème exprimé, liste les **causes visibles à l'écran** qui l'expliquent. Ce sont elles qu'on va traiter, pas le symptôme. Un problème a souvent plusieurs causes, et une cause peut alimenter deux problèmes.

Distingue toujours :
- **constaté** (visible sur la capture ou dans le code) ;
- **supposé** (déduit, à confirmer : « je suppose que "À relire" correspond à un score de confiance bas »).

> **Porte 1. Le diagnostic te parle-t-il ?** En conversation rapide, enchaîne directement sur les options en gardant cette question en fin de réponse. Sinon, attends la réponse.

### Étape 3. Options et recommandation
Propose **2 à 3 options** qui diffèrent vraiment (pas trois variantes du même bouton). Pour chacune :
- quelles causes elle traite (renvoyer aux problèmes de l'étape 2) ;
- une **maquette texte** de l'élément clé (bloc de code ASCII, 5–10 lignes) ;
- son coût (front seul ou back aussi) et son risque.

Puis **recommande une v1** (souvent la combinaison des options les moins chères qui traitent toutes les causes) et ce qui peut venir ensuite.

Principes qui reviennent souvent dans les évolutions UX :
- **Rendre l'incertitude explicite** : si on demande de confirmer, montrer *sur quoi* porte le doute et proposer un choix plutôt qu'un « Confirmer » abstrait.
- **Montrer d'abord ce qui reste à faire** : un filtre « À traiter » par défaut, l'élément traité qui sort de la file, une progression.
- **Une seule source de vérité par information** : un même compteur, le même libellé partout.
- **Dire clairement ce qui bloque et ce qui ne bloque pas**.
- **Montrer l'impact du choix** pour l'utilisateur (montant, délai, conséquence), pas le jargon interne.

Pour une évolution de structure (nouvel écran, navigation), appuie-toi sur `product-designer`. Pour les libellés, garde la voix du produit et sois précis plutôt que générique.

> **Porte 2. Quelle option retiens-tu ?** Une seule question, avec ta recommandation.

### Étape 4. Livrable concret
Pour l'option retenue, livre ce qui permet de construire tout de suite :
1. **Prompt Lovable** (ou brief pour le dev) prêt à coller : numéroté, une modification par point, précisant ce qui ne change pas, et finissant par « respecte le design system existant » ou par le renvoi au `design.md`.
2. **Métriques** : 2 ou 3, chacune reliée à un problème (ex. temps entre l'ouverture et la validation, part des propositions modifiées, taux d'abandon), avec l'événement à tracker s'il n'existe pas.
3. **Dépendances et risques** : ce que le back doit fournir, ce qu'il faut vérifier dans le code, les cas limites (zéro élément à traiter, tous traités, très gros volumes).
4. **Questions ouvertes** qui demandent une décision produit.

Si l'implémentation se fait dans ce repo plutôt que dans Lovable, passe la main à `frontend-design` en lui transmettant l'option retenue, et vérifie la conformité au `design.md`.

> **Porte 3. On le passe en dev ?** Propose au choix : coller le prompt dans Lovable, écrire le spec (`draft-spec`), ou découper en stories (`create-user-stories`).

## Exemple travaillé

[`references/exemple-relecture.md`](references/exemple-relecture.md) : un panneau de relecture de lignes classées par une IA, deux irritants (« je ne comprends pas ce que je dois confirmer », « je scrolle sur des lignes déjà bonnes »), du diagnostic jusqu'au prompt Lovable. Il sert de référence pour le niveau de détail attendu et de cas de test du skill.

## Règles

- **Observer avant de proposer** : pas de solution avant l'inventaire et les causes.
- **Citer l'écran** : chaque incohérence est appuyée par ce qu'on y lit.
- **Séparer le constaté du supposé**, toujours.
- **2–3 options vraiment différentes, puis une recommandation** : pas de catalogue.
- **Concret à la fin** : maquette texte, prompt prêt à coller, métriques. Pas de « il faudrait améliorer la clarté ».
- **Vérifier la faisabilité côté données** avant de recommander une option qui en dépend, ou la signaler comme dépendance.
- **Trois questions au plus**, jamais celles dont la réponse est dans l'entrée.
- **Délègue** : ne réécris pas ici la logique de `product-designer`, `frontend-design`, `draft-spec` ou `create-user-stories`.
