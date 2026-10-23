# Exemple travaillé : panneau de relecture de lignes classées par une IA

Cas réel anonymisé. Sert de référence pour le niveau de détail attendu et de cas de test du skill.

## Entrée

Quatre captures d'un panneau latéral « proposition d'immobilisations » dans une application de comptabilité. Une IA a classé une soixantaine de lignes de factures en catégories (immobilisations par durée d'amortissement, ou charges de l'exercice). L'utilisateur doit relire puis valider la proposition.

Prompt de l'utilisateur :

> Mon utilisateur a 2 problématiques :
> - Il ne comprend pas pourquoi il doit confirmer certaines lignes et pas d'autres, il ne comprend pas ce qu'il doit confirmer.
> - Il doit tout scroller et passe plein d'éléments déjà confirmés = perte de temps.
>
> Quelles solutions lui apporter ?

## Étape 1. Inventaire

- **Objectif de l'écran** : vérifier le classement proposé par l'IA, puis valider.
- **Structure** : groupes (« Agencements · 10 ans », « Travaux · 10 ans », « Mobilier · 7 ans », « Charges de l'exercice ») → sous-catégories repliables → lignes (libellé, justification en gris, montant).
- **Deux types de lignes** : « À relire » avec les boutons « Confirmer » et « Modifier » ; les autres avec un simple lien « Modifier ».
- **Actions globales** : « Relire la ligne suivante » (en haut), « Ligne suivante » et « Valider la proposition » (en pied, ce dernier d'apparence désactivée), « Amortir toute la catégorie » (dans un groupe).
- **Volumes** : ~60 lignes, dont une douzaine à relire.

## Étapes 1–2. Incohérences et causes

**P1 : « Je ne comprends pas ce que je dois confirmer »**
- *Constaté* : « À relire » ne dit pas sur quoi porte le doute. La justification grise explique le classement, pas l'hésitation. « Confirmer » n'a pas d'objet visible.
- *Constaté* : trois compteurs différents. En haut « 13 lignes avec hésitation », en pied « 1 ligne incertaine à relire », sur un groupe « 6 à relire ».
- *Constaté* : contradiction entre « à relire, sans bloquer la validation » et un bouton « Valider » d'apparence désactivée accompagné de « confirmez ou modifiez ».
- *Constaté* : pastille orange sur un groupe, grise ailleurs, sans légende.
- *Constaté* : trois noms pour le même concept : « à relire », « incertaine », « avec hésitation ».
- *Supposé* : « À relire » correspond à un score de confiance bas sans alternative exposée.

**P2 : « Je scrolle sur des lignes déjà bonnes »**
- *Constaté* : lignes sûres et lignes à relire mélangées, toutes les catégories dépliables au même niveau.
- *Constaté* : une ligne confirmée reste à sa place.
- *Constaté* : « Ligne suivante » saute dans une longue liste, sans indication de progression.

## Étape 3. Options

**A. Rendre le doute explicite : un choix plutôt que « Confirmer »** (traite P1)

```
PIPE FLEXIBLE WC 280-400                                  19 €
L'IA hésite : où classer cette dépense ?
  ( Installations techniques · amorti 10 ans )   ← proposé
  ( Charge d'entretien · déduite en 2026 )
Pourquoi : petite pièce de remplacement, mais achetée pendant les travaux.
```
Plus une phrase de cadrage en haut (« L'IA a classé 58 lignes. Elle hésite sur 13 : choisis le bon traitement. Le reste est prêt. »), un seul compteur « x / n relues » partout, un seul terme, et un « Valider » toujours actif qui indique combien de lignes gardent la proposition de l'IA.
Coût : front + back (le moteur doit fournir l'alternative, pas seulement un score).

**B. Mode « À relire » par défaut** (traite P2)
Filtre « À relire (13) / Tout (58) », catégories sans doute repliées sur leur total, ligne traitée qui sort de la file avec un toast « Annuler », barre de progression, résumé puis « Valider ».
Coût : front seul.

**C. Relecture une ligne à la fois** (traite P2, en partie P1)
Une carte par ligne incertaine, raccourcis `1`/`2` pour choisir, `→` pour passer.
Coût : front seul, mais change beaucoup l'écran.

**Recommandation** : A + B en v1, qui couvrent toutes les causes. C ensuite si les volumes augmentent.

## Étape 4. Livrable

**Prompt Lovable**
> Dans le panneau de relecture des immobilisations : (1) ajoute un filtre « À relire (n) / Tout (n) », actif par défaut sur « À relire », et replie les catégories sans ligne à relire en n'affichant que leur total ; (2) sur chaque ligne à relire, remplace « Confirmer / Modifier » par deux options : le classement proposé (catégorie + durée ou « charge de l'exercice ») et l'alternative, avec une ligne « Pourquoi l'IA hésite » ; (3) une ligne traitée sort de la liste filtrée, avec un toast « Annuler » ; (4) un seul compteur « x / n relues », identique en haut, sur les groupes et en pied de panneau ; (5) le bouton « Valider la proposition » est toujours actif et indique combien de lignes gardent la proposition de l'IA. Respecte le design system existant.

**Métriques**
| Métrique | Problème visé |
|---|---|
| Temps entre l'ouverture du panneau et la validation | P2 |
| Part des propositions modifiées par l'utilisateur | P1 (choix réel ou confirmation à l'aveugle) |
| Taux d'abandon de la relecture | P1 + P2 |

**Dépendance** : vérifier que le moteur de classement renvoie l'alternative pour chaque ligne incertaine. Sinon, l'option A demande d'abord une évolution côté back.
