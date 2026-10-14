---
name: pre-mortem
description: Identifie ce qui pourrait mal tourner avant le lancement en imaginant l'échec puis en remontant les causes (Tigres, Tigres de papier, Éléphants). À utiliser après qu'un spec est validé mais avant de livrer. Déclencheurs : "qu'est-ce qui pourrait mal tourner", "analyse de risques", "on est prêts à livrer ?", "pre-mortem".
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

- **Tigres** : menaces réelles, étayées par des preuves, qui peuvent faire dérailler le projet. Elles exigent un plan de mitigation.
- **Tigres de papier** : inquiétudes qui font peur mais sont improbables ou exagérées. Nomme-les pour que l'équipe arrête de s'en soucier.
- **Éléphants** : les risques non dits. Hypothèses que personne ne questionne, inquiétudes que personne n'exprime, vérités inconfortables que tout le monde évite.

Pour chaque Tigre, attribue un niveau d'urgence :
- **Bloquant pour le lancement** : à résoudre avant la mise en prod. La date bouge si ce n'est pas traité.
- **Fast-follow** : à traiter dans les 30 jours après lancement. On peut lancer avec, pas l'ignorer.
- **Suivi** : à surveiller après lancement, à escalader si les signaux se dégradent.

Pour chaque Tigre, indique aussi :
- une action de mitigation précise ;
- un responsable suggéré (un rôle, pas une personne) ;
- une échéance relative au lancement.

Sois brutalement honnête. Le but est d'améliorer la préparation, pas de fabriquer une fausse confiance. Porte une attention particulière aux Éléphants : ce sont les risques qui coulent les lancements parce que personne n'a voulu les dire à voix haute.

## Conseils

- À lancer 2–3 semaines avant le lancement, pas la veille : il faut le temps de mitiger les Tigres.
- Le plus précieux est souvent la liste des Éléphants. Si le pre-mortem ne sort que des risques évidents, pousse sur ce que l'équipe ne dit pas.
- Dans le doute, classe un risque en Tigre : mitiger un risque mineur coûte moins cher qu'ignorer un risque réel.
- Si un Tigre révèle une hypothèse non testée, valide-la avant le lancement (test, entretiens avec `mom-test`).
