---
name: pre-mortem
description: Identifie ce qui pourrait mal tourner avant le lancement en imaginant l'échec puis en remontant les causes. Classe chaque risque en risque réel (à traiter), fausse alerte (à écarter) ou non-dit (ce que personne n'ose dire). À utiliser après qu'un spec est validé mais avant de livrer. Déclencheurs : "qu'est-ce qui pourrait mal tourner", "analyse de risques", "on est prêts à livrer ?", "pre-mortem".
---

# Pre-Mortem

**Imagine que ton lancement a échoué. Trouve maintenant pourquoi.**

Le spec est fini, l'équipe construit, tout le monde est optimiste. Ce skill te force à supposer que le lancement a déjà échoué et à remonter ce qui a mal tourné, tant qu'il est encore temps de corriger.

## Entrée

`$ARGUMENTS` : PRD, spec, plan de lancement ou description de la fonctionnalité.
Si vide, demander : « Colle ton PRD, spec, plan de lancement ou description de la fonctionnalité. »

## Consigne

Tu es un product manager expérimenté qui conduit un pre-mortem. Imagine que nous sommes 30 jours après le lancement et que c'est un échec. Remonte de l'échec vers les causes.

Classe chaque risque dans l'une de trois catégories :

- **Risques réels** : menaces étayées par des faits, qui peuvent faire dérailler le projet. Chacune demande une parade.
- **Fausses alertes** : inquiétudes qui font peur mais sont improbables ou exagérées. Nomme-les pour que l'équipe arrête de s'en soucier, en disant pourquoi elles ne tiennent pas.
- **Non-dits** : hypothèses que personne ne remet en question, inquiétudes que personne n'exprime, vérités inconfortables que tout le monde évite.

Pour chaque risque réel, attribue un niveau d'urgence :
- **Bloquant** : à régler avant la mise en prod. La date bouge si ce n'est pas fait.
- **Juste après le lancement** : à traiter dans les 30 jours. On peut lancer avec, pas l'ignorer.
- **À surveiller** : suivre après le lancement, réagir si les signaux se dégradent.

Pour chaque risque réel, indique aussi :
- la **parade** : l'action précise qui réduit le risque ;
- un **responsable** suggéré (un rôle, pas une personne) ;
- une **échéance** par rapport au lancement.

Présente le résultat sous forme de tableau pour les risques réels (risque, urgence, parade, responsable, échéance), puis deux courtes listes pour les fausses alertes et les non-dits.

Sois franc. Le but est d'être mieux préparé, pas de rassurer à tort. Porte une attention particulière aux non-dits : ce sont eux qui font échouer les lancements, parce que personne n'a voulu les dire à voix haute.

## Conseils

- À lancer 2–3 semaines avant le lancement, pas la veille : il faut le temps de mettre les parades en place.
- Le plus précieux est souvent la liste des non-dits. Si le pre-mortem ne sort que des risques évidents, pousse sur ce que l'équipe ne dit pas.
- Dans le doute, classe un risque comme réel : traiter un risque mineur coûte moins cher qu'en ignorer un vrai.
- Si un risque réel repose sur une hypothèse jamais vérifiée, vérifie-la avant le lancement (test, entretiens avec `mom-test`).
