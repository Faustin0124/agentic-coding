---
name: product-flow
description: Chef d'orchestre du raffinement produit. Part d'un sujet du backlog Notion (note créée avec product-notes) ou d'un problème brut, et déroule les bons skills dans l'ordre (mom-test / jobs-to-be-done, amazon-working-backwards, write-prd / draft-spec, pre-mortem, create-user-stories) avec des questions et une porte de validation à chaque étape. Écrit le travail dans docs/<sujet>/ puis l'exporte dans Notion. Déclencheurs : "raffine ce sujet", "construis le plan de", "prends l'item X du backlog", "on part de ce problème", "de l'idée au PRD", "prépare ça pour le dev".
---

# Product Flow

**Du sujet brut au lot prêt pour le dev, une porte de validation à la fois.**

Ce skill orchestre, il ne fait pas le travail des autres. Chaque étape appelle un skill existant ; ici on décide **par où entrer, quand passer à la suite, et où écrire le résultat**. Il garde la même logique que `product-notes` : on lit la vraie structure de Notion, on ne suppose rien, on ne modifie jamais le backlog sans confirmation.

`product-notes` capture les idées (étape amont). `product-flow` les raffine (étape aval).

## Entrée

`$ARGUMENTS` : un sujet. Trois formes possibles.
1. **Un item du backlog Notion** (titre, lien ou « le prochain à raffiner ») → le retrouver (`notion-search` / `notion-fetch`) et lire sa page. Si l'utilisateur ne précise pas, lister les items en statut le plus amont (découverte / à raffiner) et lui demander lequel prendre.
2. **Un problème brut** donné en conversation.
3. **Un dossier `docs/<sujet>/` existant** → reprendre où on s'était arrêté (voir « Reprise »).

## Fichier de suivi : `docs/<sujet>/`

Source de travail, versionnée. `<sujet>` = slug court du titre.

| Fichier | Contenu | Écrit à l'étape |
|---|---|---|
| `brief.md` | Source (lien Notion), problème, preuves, hypothèses, décisions, journal des portes | 0 → 5 |
| `prd.md` | PRD (craft-spec ou draft-spec) | 3 |
| `risques.md` | Sortie du pre-mortem | 4 |
| `stories.md` | User stories prêtes pour le dev | 5 |

`brief.md` commence par un en-tête d'état, mis à jour à chaque porte :

```yaml
---
sujet: <titre>
notion: <lien de l'item d'origine ou "aucun">
etape: 0-5
statut: en cours | validé | abandonné
mis_a_jour: JJ/MM/AAAA
---
```

Suit un journal : pour chaque porte franchie, la date, la décision, ce qui est **su** vs **supposé**.

## Parcours

### Étape 0. Cadrage et point d'entrée
Lis l'item ou le problème. Pose au plus 3–4 questions, en sautant celles dont la réponse est déjà dans la note :
- Qui a ce problème, et dans quelle situation concrète ?
- Quelle preuve que c'est réel (faits observés, retours, données) ou seulement une intuition ?
- Qu'est-ce qui a déjà été essayé ou contourné ?
- Pourquoi maintenant ? Que se passe-t-il si on ne fait rien ?

Puis **choisis le point d'entrée** et annonce-le avec une phrase de justification :

| Situation | Entrée |
|---|---|
| Idée floue, aucune preuve | Étape 1 (`mom-test` en mode plan de conversation) |
| Retours ou entretiens existants à évaluer | Étape 1 (`mom-test` en mode évaluation du signal) |
| Problème réel, motivations à clarifier | Étape 1 (`jobs-to-be-done`) |
| Problème solide, doute sur l'intérêt de construire | Étape 2 |
| Problème et idée clairs | Étape 3 |
| PRD déjà écrit | Étape 4 |
| PRD validé et risques traités | Étape 5 |
| Évolution d'un écran ou parcours existant, irritants identifiés | `ux-evolution` (reprendre ici à l'étape 3 ou 5 si un spec ou des stories sont nécessaires) |

**Niveau de l'item.** Détecte s'il s'agit d'une story ou d'un Epic : lis `Type` sur l'item Notion, sinon juge sur la taille (plusieurs workflows indépendants, ou plus de 2–3 semaines de travail = Epic). Note-le dans `brief.md` ; il détermine la sortie des étapes 3 à 5 et l'export (voir « Item de taille Epic »).

Écris `brief.md` (étape 0) et passe la porte 0 : « Voici ce que j'ai compris, par où je propose de commencer. OK ? »

### Étape 1. Comprendre le problème
Appelle `mom-test` et/ou `jobs-to-be-done` selon le tableau. Si l'étape consiste à aller parler à des utilisateurs, **mets le flux en pause** : donne le guide d'entretien, sauvegarde l'état et dis explicitement ce qu'il faut rapporter pour reprendre.

> **Porte 1. Le problème est-il réel et précis ?** Résume : ce qu'on sait (preuves), ce qu'on suppose. Propose : *avancer* / *creuser encore* (quoi, comment) / *abandonner*.

### Étape 2. Valider l'idée
Appelle `amazon-working-backwards`. Passe-la si le problème est solide et la solution évidente (dis-le et demande confirmation de la sauter).

> **Porte 2. Ça vaut la peine d'être construit ?** Reprends le verdict du « test d'arrêt » et les questions des FAQ internes restées sans réponse. Propose : *avancer* / *retravailler* / *abandonner*.

### Étape 3. Spécifier
Appelle `write-prd` (questions + `craft-spec`). Propose `draft-spec` si le sujet touche une interface, plusieurs parcours ou des cas limites : demande-lui le niveau de détail voulu. Écris `prd.md`.

> **Porte 3. Le PRD te convient-il ?** Relis avec l'utilisateur : scope et hors-scope, métriques, hypothèses signalées, questions ouvertes. Aucune question ouverte bloquante ne doit rester implicite.

### Étape 4. Sécuriser
Appelle `pre-mortem` sur le PRD. Écris `risques.md`. Si un Tigre révèle une hypothèse non testée, **retour à l'étape 1** pour la valider (voir « Retours en arrière »).

> **Porte 4. Les Tigres bloquants sont-ils traités ?** Liste-les avec mitigation, responsable et échéance. Propose : *avancer* / *traiter d'abord X*.

### Étape 5. Passer au dev
Appelle `create-user-stories` à partir de `prd.md` et `risques.md` (intègre les mitigations comme critères ou stories). Écris `stories.md`.

> **Porte 5. Prêt pour le dev ?** Vérifie : chaque story tient en un sprint, a des critères testables, inclut chemins d'erreur et état vide ; les P0 couvrent le lancement.

## Item de taille Epic

Un Epic se raffine **une fois au niveau Epic**, puis se découpe. Ne spécifie pas chaque story comme un PRD à part.

| Étape | Sujet = story | Sujet = Epic |
|---|---|---|
| 1–2 | Problème et idée | Idem, au niveau du problème global : l'Epic doit répondre à **un** problème |
| 3 | `prd.md` du sujet | `prd.md` **de l'Epic** : problème, métriques, scope, hors-scope, phasage |
| 3 bis | — | **Découpage en stories** (voir ci-dessous) |
| 4 | Pre-mortem du sujet | Pre-mortem **de l'Epic** (les risques sont surtout là) |
| 5 | `stories.md` (1 à quelques stories) | `stories.md` : toutes les stories, groupées par phase |

**Découpage (étape 3 bis).** Propose-le avant de rédiger les stories, et fais-le valider (porte 3 bis) :
- découpe par **workflow utilisateur** (tranches verticales de bout en bout), pas par composant technique ;
- chaque story tient en un sprint et peut être livrée seule ; signale celles qui dépendent d'une autre ;
- inclus la story d'**état vide** et les stories de **chemins d'erreur** significatifs ;
- regroupe en **phases** (v1 / v1.1…) si le scope est large ; la phase 1 doit déjà avoir de la valeur ;
- si une partie est trop floue pour être découpée, mets-la en « à raffiner » plutôt que d'inventer des stories ; elle repartira dans `product-flow` plus tard.

**Un Epic au résultat trop gros.** Si l'Epic produit plus de ~10–12 stories ou plusieurs problèmes distincts, propose de le scinder en deux Epics et de faire un `product-flow` par Epic.

> **Porte 3 bis. Ce découpage te convient-il ?** Montre la liste (titre, phase, priorité proposée, dépendances) avant d'écrire les stories détaillées.

## Export vers Notion

À la fin (ou à la demande à n'importe quelle étape), propose l'export et **demande confirmation avant d'écrire**. Comme `product-notes`, lis d'abord le schéma réel de la base (`notion-fetch`), copie les valeurs de sélection caractère pour caractère, ne devine ni ID ni vocabulaire.

1. **Mettre à jour l'item d'origine** (`notion-update-page`) : ajouter à sa page une section de synthèse (problème, preuves, décision, scope, métriques, risques majeurs, liens vers les fichiers `docs/<sujet>/`). Ne pas écraser le contenu existant.
2. **Créer les stories** (`notion-create-pages`) dans la même base, avec le même Epic parent que l'item (ou la relation que la base utilise), `Type` = `User Story`, une page par story avec contexte, énoncé et critères d'acceptation issus de `stories.md`.
3. **Statut et priorité** : ne pas les modifier d'office. Propose le changement (ex. passer l'item à « prêt pour le dev », priorités P0/P1/P2 des stories) et applique-le seulement si l'utilisateur confirme.
4. **Sujet de taille Epic** :
   - si l'item d'origine **est déjà** un Epic (`Type` = `Epic`) : le mettre à jour avec la synthèse du PRD (point 1), puis créer les stories rattachées à lui ;
   - si l'item d'origine était une **story trop grosse** : proposer de la convertir en Epic (changer son `Type`, sur confirmation) ou d'en créer un nouveau et de laisser l'ancienne en lien ; ne rien supprimer ;
   - si le sujet n'a **pas d'Epic** correspondant : proposer un nom, demander confirmation, créer l'Epic **d'abord**, puis les stories qui pointent vers lui ;
   - le PRD complet reste dans `docs/<sujet>/prd.md` ; la page de l'Epic en porte la synthèse et les liens ;
   - copie le nom de l'Epic caractère pour caractère si c'est une propriété de sélection, pour ne pas créer une option parasite.
5. **Doublons** : si une story existante recoupe une nouvelle, signale-la sans fusionner ni supprimer.
6. Termine par une courte liste : pages mises à jour/créées avec leur lien.

Si le sujet est abandonné à une porte, propose de consigner la décision et la raison dans la page Notion d'origine (statut à ajuster seulement sur confirmation).

## Retours en arrière

Le parcours n'est pas linéaire. Si une étape invalide une précédente (hypothèse non validée au pre-mortem, question ouverte du PR/FAQ, PRD qui contredit les preuves), **dis-le, reviens à l'étape concernée** et note-le dans le journal du brief.

## Reprise

Si `docs/<sujet>/brief.md` existe : lis l'en-tête et le journal, résume en trois lignes où on en est et ce qui était attendu, puis demande s'il faut reprendre ou repartir d'une étape.

## Règles

- **Trois à quatre questions max par étape**, jamais celles dont la réponse est déjà connue. Pas de checklist récitée.
- **Une seule question de décision par porte**, avec ta recommandation.
- **Sépare toujours le su du supposé** dans le brief et les résumés de porte.
- **N'empile pas des étapes inutiles** : saute celles qui n'apportent rien (et dis-le), mais jamais la porte 3 ni l'export sans confirmation.
- **Un Epic se raffine au niveau Epic**, puis se découpe : pas un PRD par story.
- **Délègue** : ne réécris pas ici la logique des skills appelés.
- **Notion en écriture seulement sur confirmation** ; jamais de suppression, de fusion ou de changement de sprint.
