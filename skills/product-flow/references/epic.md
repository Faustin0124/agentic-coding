# Sujet de taille Epic

Un Epic se spécifie **une fois au niveau de l'Epic**, puis se découpe. Ne spécifie pas chaque story comme un spec à part.

| Étape | Sujet = story | Sujet = Epic |
|---|---|---|
| 1. Problème et intérêt | Problème du sujet | Idem, au niveau du problème global : l'Epic doit répondre à **un** problème |
| 2. Spec | Spec du sujet | Spec **de l'Epic** (problème, métriques, scope, hors scope, phases), puis **découpage en stories** |
| 3. Risques | Pre-mortem du sujet | Pre-mortem **de l'Epic** (les risques sont surtout là) |
| 4. Stories | 1 à quelques stories | Toutes les stories, groupées par phase |

## Découpage en stories (fin de l'étape 2)

Propose-le avant de rédiger les stories détaillées, et fais-le valider avec le spec :
- découpe par **parcours utilisateur** (des tranches qui marchent de bout en bout), pas par composant technique ;
- chaque story tient en un sprint et peut être livrée seule ; signale celles qui dépendent d'une autre ;
- inclus la story d'**état vide** et celles des **cas d'erreur** importants ;
- regroupe en **phases** (v1, v1.1…) si le scope est large ; la phase 1 doit déjà apporter de la valeur ;
- si une partie est trop floue pour être découpée, mets-la « à raffiner » plutôt que d'inventer des stories : elle repassera dans `product-flow` plus tard.

Présente le découpage en tableau : titre, phase, priorité proposée (P0 / P1 / P2), dépendances.

## Epic trop gros

Si l'Epic produit plus de ~10–12 stories, ou mélange plusieurs problèmes distincts, propose de le scinder en deux Epics et de faire un `product-flow` par Epic.
