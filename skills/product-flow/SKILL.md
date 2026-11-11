---
name: product-flow
description: Chef d'orchestre du raffinement produit pour les sujets moyens à gros (plusieurs stories, Epic, problème encore à vérifier). Part d'un item du backlog Notion (créé avec product-notes) ou d'un problème brut, et répond à quatre questions dans l'ordre, une validation à chaque fois - le problème est-il réel et ça vaut le coup ? qu'est-ce qu'on construit ? qu'est-ce qui pourrait mal tourner ? est-ce prêt pour le dev ? - en appelant les skills existants (mom-test, jobs-to-be-done, amazon-working-backwards, write-prd, pre-mortem, create-user-stories, feature-scoping). Notion fait foi ; un brouillon local sert seulement à reprendre le travail. Renvoie les petites features vers feature-scoping et les évols d'écran existant vers ux-evolution. Déclencheurs : "raffine ce sujet", "construis le plan de", "prends l'item X du backlog", "on part de ce problème", "de l'idée au PRD", "prépare cet Epic pour le dev".
---

# Product Flow

**Du sujet brut aux stories prêtes pour le dev, en quatre questions.**

Ce skill orchestre, il ne fait pas le travail des autres : chaque étape appelle un skill existant. Ici on décide **par où entrer, quand passer à la suite, et où écrire le résultat**. Comme `product-notes`, on lit la vraie structure de Notion, on ne suppose rien, et on ne modifie jamais le backlog sans confirmation.

## Entrée

`$ARGUMENTS` : un sujet, sous l'une de ces formes :
1. **Un item du backlog Notion** (titre, lien ou « le prochain à raffiner ») → le retrouver (`notion-search` / `notion-fetch`) et lire sa page. Si rien n'est précisé, lister les items en statut le plus amont et demander lequel prendre.
2. **Un problème brut** donné en conversation.
3. **Un brouillon existant** `docs/<sujet>.md` → reprendre où on s'était arrêté (voir « Reprise »).

## Où vit le travail

- **Notion fait foi.** Le résultat final (synthèse, stories) va dans Notion, sur confirmation. Le détail de l'export est dans [`references/export-notion.md`](references/export-notion.md).
- **Un seul brouillon local**, `docs/<sujet>.md` (`<sujet>` = titre court en minuscules avec des tirets). Il sert à garder le fil et à reprendre plus tard. Il commence par cet en-tête, mis à jour à chaque validation :

  ```yaml
  ---
  sujet: <titre>
  notion: <lien de l'item d'origine ou "aucun">
  etape: 0-4
  statut: en cours | exporté vers Notion | abandonné
  mis_a_jour: JJ/MM/AAAA
  ---
  ```

  Puis une section par étape (problème, spec, risques, stories) et un journal : pour chaque validation, la date, la décision, ce qui est **su** et ce qui est **supposé**.
- **Après l'export**, passe le statut à « exporté vers Notion » et ajoute en tête : « Notion fait foi depuis le JJ/MM/AAAA. » Ne modifie plus le brouillon ensuite.
- **Sans Notion**, le brouillon devient le document de référence.

## Parcours

### Étape 0. De quoi parle-t-on, et par où commencer ?
Lis l'item ou le problème. Pose **au plus 3–4 questions**, en sautant celles dont la réponse est déjà là :
- Qui a ce problème, et dans quelle situation concrète ?
- Qu'est-ce qui prouve que c'est réel (faits observés, retours, données), ou est-ce une intuition ?
- Qu'est-ce qui a déjà été essayé ou contourné ?
- Pourquoi maintenant ? Que se passe-t-il si on ne fait rien ?

Puis **choisis le point d'entrée** et annonce-le avec une phrase de justification :

| Situation | Entrée |
|---|---|
| Petite feature : une story, un parcours, problème connu, pas de nouveau modèle de données | **`feature-scoping`** (on sort de `product-flow`) |
| Évol d'un écran ou d'un parcours existant, irritants identifiés | **`ux-evolution`** (revenir ici à l'étape 2 ou 4 si un spec ou des stories sont nécessaires) |
| Idée floue, aucune preuve, ou retours à évaluer | Étape 1 |
| Problème solide et idée claire | Étape 2 |
| Spec déjà écrit | Étape 3 |
| Spec validé et risques traités | Étape 4 |

**Story ou Epic ?** Lis `Type` sur l'item Notion ; sinon, juge sur la taille (plusieurs parcours indépendants, ou plus de 2–3 semaines de travail = Epic). Note-le dans le brouillon. Pour un Epic, suis aussi [`references/epic.md`](references/epic.md) aux étapes 2 et 4.

Écris le brouillon, puis **validation 0** : « Voici ce que j'ai compris et par où je propose de commencer. OK ? »

### Étape 1. Le problème est-il réel, et ça vaut le coup de le construire ?
- **Le problème** (skills `mom-test` ou `jobs-to-be-done`) :
  - aucune preuve → `mom-test` pour préparer les questions à poser aux utilisateurs ;
  - des retours ou des entretiens existent → `mom-test` pour trier les vrais signaux des faux ;
  - le problème est réel mais les motivations sont floues → `jobs-to-be-done`.

  S'il faut aller parler à des utilisateurs, **mets le flux en pause** : donne le guide d'entretien, sauvegarde le brouillon et dis exactement ce qu'il faut rapporter pour reprendre.
- **L'intérêt de construire** (skill `amazon-working-backwards`) : **facultatif**. Ne le lance que s'il reste un doute sur la valeur (gros investissement, solution pas évidente, idée qui pourrait ne servir à personne). Sinon, dis en une phrase pourquoi tu le passes.

> **Validation 1. Le problème est réel et ça vaut le coup ?** Résume ce qu'on sait (preuves) et ce qu'on suppose ; si `amazon-working-backwards` a tourné, reprends son verdict et les questions restées sans bonne réponse. Propose : *avancer* / *creuser encore* (quoi, comment) / *abandonner*.

### Étape 2. Qu'est-ce qu'on construit exactement ?
Appelle `write-prd` (questions puis `craft-spec`). Propose `draft-spec` si le sujet touche une interface, plusieurs parcours ou des cas limites, en demandant le niveau de détail voulu. Écris le spec dans le brouillon.

Pour un Epic : spec au niveau de l'Epic, puis **proposition de découpage en stories** avant de les détailler (voir [`references/epic.md`](references/epic.md)).

> **Validation 2. Le spec te convient ?** Relis ensemble : ce qui est dans le scope et ce qui n'y est pas, les métriques, les hypothèses, les questions ouvertes. Aucune question bloquante ne doit rester implicite. Pour un Epic, valide aussi le découpage (titre, phase, priorité, dépendances).

### Étape 3. Qu'est-ce qui pourrait mal tourner ?
Appelle `pre-mortem` sur le spec. Il classe les risques en **risques réels** (à traiter), **fausses alertes** (à écarter) et **non-dits** (ce que personne n'ose dire). Écris le résultat dans le brouillon. Si un risque réel repose sur une hypothèse jamais vérifiée, **reviens à l'étape 1** pour la vérifier.

> **Validation 3. Les risques bloquants ont une parade ?** Liste-les avec la parade, le responsable et l'échéance. Propose : *avancer* / *traiter d'abord X*.

### Étape 4. Est-ce prêt pour le dev ?
Appelle `create-user-stories` à partir du spec et des risques (les parades deviennent des critères ou des stories). Écris les stories dans le brouillon.

Puis propose, pour **chaque story P0**, un cadrage technique avec `feature-scoping` (où elle se loge dans le code, ce qu'on réutilise, l'impact, le plan). Lance-le story par story, seulement si l'utilisateur le veut.

> **Validation 4. Prêt pour le dev ?** Vérifie : chaque story tient en un sprint, a des critères testables, couvre les cas d'erreur et l'état vide ; les P0 suffisent pour lancer. Puis propose l'export vers Notion.

## Retours en arrière

Le parcours n'est pas linéaire. Si une étape remet en cause une précédente (hypothèse non vérifiée au pre-mortem, question restée sans réponse à l'étape 1, spec qui contredit les preuves), **dis-le, reviens à l'étape concernée** et note-le dans le journal.

Si le sujet est abandonné à une validation, propose de consigner la décision et la raison dans la page Notion d'origine (statut changé seulement sur confirmation).

## Reprise

Si `docs/<sujet>.md` existe : lis l'en-tête et le journal, résume en trois lignes où on en est et ce qui était attendu, puis demande s'il faut reprendre ou repartir d'une étape. S'il est marqué « exporté vers Notion », repars de la page Notion, pas du brouillon.

## Règles

- **Chaque étape répond à sa question** : annonce-la en clair, le nom du skill appelé vient après.
- **Trois à quatre questions au plus par étape**, jamais celles dont la réponse est déjà connue.
- **Une seule question de décision par validation**, avec ta recommandation.
- **Sépare toujours le su du supposé** dans le brouillon et les résumés.
- **Saute ce qui n'apporte rien** (et dis-le), mais jamais la validation 2 ni l'export sans confirmation.
- **Un Epic se spécifie une fois au niveau de l'Epic**, puis se découpe : pas un spec par story.
- **Délègue** : ne réécris pas ici la logique des skills appelés.
- **Notion en écriture seulement sur confirmation** ; jamais de suppression, de fusion ou de changement de sprint.
