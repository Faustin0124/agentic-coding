---
name: mom-test
description: Prépare et évalue des conversations clients avec The Mom Test (Rob Fitzpatrick) pour obtenir du vrai signal plutôt que des politesses. À utiliser avant des entretiens utilisateurs (guide d'entretien), pour auditer des questions, ou après pour trier le vrai du faux signal dans des transcripts. Déclencheurs : "interview client", "comment parler aux users", "valider cette idée", "mom test", questions de recherche.
---

# The Mom Test

**Arrête de poser des questions auxquelles on peut te mentir.**

Tout le monde dit qu'il utiliserait ton produit et que l'idée est super. Presque aucun de ces retours n'est utile. Ce skill applique les règles du Mom Test pour concevoir des conversations qui extraient un signal vrai et exploitable, et pour évaluer si une recherche existante t'apprend vraiment quelque chose.

## Entrée

`$ARGUMENTS` : l'un des éléments suivants.
- l'idée ou l'hypothèse à valider par des conversations client ;
- des questions d'entretien à évaluer ;
- des transcripts ou notes d'entretien dont on veut juger la qualité du signal ;
- un segment client et les hypothèses à tester.

Si vide, demander lequel des quatre l'utilisateur fournit.

## Les trois règles

1. Parle de **leur vie**, pas de ton idée.
2. Demande des **faits précis dans le passé**, pas des généralités ni des opinions sur le futur.
3. Parle moins, écoute plus.

## Selon ce qui est fourni

### A. Une idée ou une hypothèse à valider → plan de conversation (20–30 min)

- **Ouverture (2 min)** : poser le contexte sans biaiser. Aucun pitch. Présente l'échange comme une découverte de leur workflow, pas un test de ton idée.
- **Leur monde (10 min)** : leur réalité actuelle.
  - À quoi ressemble leur workflow aujourd'hui ?
  - Où passent-ils le plus de temps, d'argent, d'effort ?
  - Qu'ont-ils déjà essayé pour résoudre ce problème ?
  - Comment gèrent-ils ça maintenant ? (S'ils ne font rien, c'est un signal.)
  - Pour chaque question, explique **pourquoi** elle marche : quel signal elle extrait, à quoi ressemble une bonne vs une mauvaise réponse.
- **Comportement passé précis (10 min)** :
  - « Raconte-moi la dernière fois où [tu as rencontré ce problème]… »
  - « Que s'est-il passé ? Déroule-moi ça. »
  - « Qu'as-tu fait ensuite ? »
  - « Combien de temps / d'argent ça t'a coûté ? »
- **Engagement et avancée (5 min)** : vérifier qu'ils mettent quelque chose en jeu. Accepteraient-ils un pilote ? De payer un accès anticipé ? De te présenter un collègue qui a le même problème ? Les compliments ne sont **pas** de l'engagement. « Ça a l'air cool » ne vaut rien ; « Je peux m'inscrire à la bêta ? » vaut quelque chose.

**Questions à ne JAMAIS poser** (et fournis pour chacune la réécriture Mom Test, centrée sur le comportement passé) :
- « Utiliserais-tu un produit qui fait X ? » (hypothétique, tout le monde dit oui)
- « Tu penses que c'est une bonne idée ? » (opinion, personne ne veut te vexer)
- « Combien paierais-tu pour ça ? » (prix hypothétique, inutile sans engagement)
- « Le recommanderais-tu à un ami ? » (intention future, peu fiable)

### B. Des questions d'entretien → audit

Évalue chaque question selon les règles :

| Question | Verdict | Problème | Réécriture Mom Test |
|---|---|---|---|
| [originale] | OK / KO | [pourquoi : hypothétique, cherche une opinion, orientée, pitch déguisé…] | [version réécrite] |

Schémas d'échec à repérer :
- **Hypothétiques** : « Est-ce que tu… » / « Si on construisait… » / « Tu pourrais t'imaginer… »
- **Opinions** : « Tu penses que… » / « Que ressens-tu face à… »
- **Orientées** : la question télégraphie la réponse souhaitée.
- **Pitch déguisé** : « Et s'il existait un produit qui [ton produit]… »
- **Promesses futures** : « Tu paierais… » / « Tu changerais… »
- **Trop génériques** : « Quels sont tes plus gros défis ? » (trop large sans relance)

Termine par un guide de conversation révisé, fluide et conforme aux règles.

### C. Des transcripts ou notes → évaluation du signal

**Vrai signal** (à pondérer fortement) :
- comportements et actions passés précis ;
- argent, temps ou effort déjà dépensés sur le problème ;
- contournements (workarounds) construits ;
- langage émotionnel sur des frustrations précises (pas des plaintes polies) ;
- actes d'engagement : inscription, paiement, introduction, temps réservé.

**Faux signal** (à décoter ou écarter) :
- compliments : « Super idée », « J'adore », « Très cool » ;
- promesses futures : « J'utiliserais clairement ça », « Je paierais pour ça » ;
- plaintes génériques : « Oui, c'est un vrai problème » ;
- scénarios hypothétiques : « Je pourrais voir un usage pour… » ;
- réponses socialement désirables : tout ce qui sonne comme ce qu'ils pensent que tu veux entendre.

Pour chaque constat : (1) la citation ou preuve exacte, (2) vrai ou faux signal et pourquoi, (3) l'insight sous-jacent si c'est vrai, ou la question qu'il aurait fallu poser si c'est faux.

**Synthèse :**
- Que sais-tu réellement après ces conversations ?
- Que crois-tu savoir sans le savoir ? (fausse confiance)
- Que reste-t-il à apprendre ?
- Quels engagements (pas compliments) as-tu obtenus ?

## Règles générales

- Les meilleures conversations client ne mentionnent pas ton idée. Tu apprends leur vie, puis tu juges si ton idée s'y insère.
- Si tu entends ce que tu veux entendre, tu poses probablement les mauvaises questions.
- Trois conversations solides avec des preuves comportementales valent mieux que 30 sondages d'opinions.
- Critère d'une bonne conversation : as-tu appris quelque chose qui pourrait changer ton plan ? Si tout confirme ce que tu crois déjà, tu n'apprends rien.

## Conseils

- À lancer **avant** de parler aux utilisateurs pour concevoir les bonnes questions, et **après** pour auditer le signal obtenu.
- Les entretiens les plus dangereux sont ceux qui se passent très bien. Si tout le monde a adoré l'idée, tu as sans doute pitché au lieu d'écouter.
- Utilise l'évaluation du signal pour décider si tu as assez de preuves pour passer à `craft-spec`, ou s'il te faut plus de conversations.
- Si tu réalises que tu ne comprends pas le monde du client, passe par `jobs-to-be-done`.
