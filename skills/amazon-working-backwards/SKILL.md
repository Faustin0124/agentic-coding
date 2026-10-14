---
name: amazon-working-backwards
description: Rédige un PR/FAQ (communiqué de presse + FAQ) selon le processus Working Backwards d'Amazon, en partant du client pour remonter vers ce qu'il faut construire. À utiliser pour valider qu'une idée vaut la peine d'être construite avant d'écrire le spec. Déclencheurs : "PR/FAQ", "working backwards", "ça vaut le coup de le construire ?", "écris le communiqué d'abord", idée floue à cristalliser.
---

# Amazon Working Backwards

**Pars du client. Écris le communiqué de presse avant d'écrire le code.**

Tu as une idée : nouveau produit, grosse fonctionnalité ou pari stratégique. Avant d'investir dans specs, designs et ingénierie, ce skill te force à dire ce que tu construis, pour qui et pourquoi, du point de vue du client. Si tu n'arrives pas à écrire un communiqué convaincant, l'idée n'est pas prête.

## Entrée

`$ARGUMENTS` : l'idée, le concept de feature ou le pari stratégique.
Si vide, demander : « Colle ton idée : notes brutes, threads Slack, résultats de brainstorm ou une seule phrase. »

## Consigne

Tu es un responsable produit expérimenté qui applique le Working Backwards d'Amazon. Rédige un PR/FAQ avec cette structure.

### COMMUNIQUÉ DE PRESSE

- **Titre** : nom du produit, clair et orienté client (pas de nom de code interne).
- **Sous-titre** : une phrase sur qui est le client et quel bénéfice il obtient.
- **Date & ville** : date de lancement future plausible et lieu.
- **Paragraphe d'ouverture** : produit et bénéfice en 3–4 phrases. Commence par le problème client, puis la solution. Écris comme pour un vrai communiqué public, sans jargon interne.
- **Paragraphe problème** : la douleur actuelle du client en termes vifs et précis. Que fait-il aujourd'hui ? Pourquoi c'est pénible ? Des scénarios concrets, pas des énoncés abstraits. Le lecteur doit ressentir la douleur.
- **Paragraphe solution** : comment le produit résout le problème. Centré sur l'expérience client, pas la technologie. Que peut-il faire maintenant qu'il ne pouvait pas avant ?
- **Citation d'un dirigeant** : pourquoi c'est stratégiquement important. Force à formuler le « pourquoi maintenant » et le point de vue de l'entreprise.
- **Comment ça marche** : 3–5 phrases sur l'expérience client, le chemin nominal en termes simples.
- **Citation d'un client** : fictive mais réaliste, qui décrit le bénéfice avec ses mots. Force à imaginer à quoi ressemble le succès vu de l'extérieur.
- **Appel à l'action** : comment démarrer, en une phrase.

### FAQ

- **FAQ externes** (côté client, 4–6 questions) : prix/disponibilité, comparaison avec les alternatives, pour qui c'est (et pour qui ce n'est PAS), données/vie privée, objections « oui mais… ».
- **FAQ internes** (côté équipe, 4–6 questions) : taille de marché et business case, faisabilité technique et délai, dépendances et risques, pourquoi maintenant, ce qu'on ne construit PAS, comment on mesurera le succès.

### ÉVALUATION WORKING BACKWARDS

1. **Test de clarté** : un non-technicien comprend-il ce que fait le produit ? Sinon l'idée est encore floue.
2. **Test de différenciation** : un concurrent pourrait-il remplir les trous ? Si oui, la valeur unique n'est pas assez nette.
3. **Test client** : le client fictif dirait-il vraiment cette citation ? Si elle sonne forcée, le bénéfice n'est pas assez réel.
4. **Test FAQ interne** : les réponses sont-elles convaincantes ? Signale celles où tu bluffes : ce sont tes plus gros risques.
5. **Test d'arrêt** : cette idée doit-elle avancer, être retravaillée ou être abandonnée ? Tranche.

## Règles

- Rédige le communiqué à un niveau de lecture de collégien. S'il faut du jargon, l'idée n'est pas assez claire.
- Le paragraphe problème est la section la plus importante. Si la douleur n'est pas vive et précise, tout le reste sera vague.
- Ne tergiverse pas. « Ça pourrait aider certains utilisateurs parfois » signale une idée pas prête. Affirme clairement et laisse les FAQ traiter les nuances.
- Les FAQ internes doivent contenir au moins une question à laquelle tu n'as pas encore de bonne réponse : c'est la partie honnête.
- L'évaluation doit être brutalement honnête. Un PR/FAQ qui révèle une idée faible vaut plus qu'un qui masque les fissures.

## Conseils

- Le PR/FAQ est un outil de réflexion, pas un support marketing : il sert à exposer les pensées floues avant d'investir.
- Si tu bloques sur le paragraphe problème, tu ne comprends probablement pas assez le client : lance `jobs-to-be-done` ou `mom-test` d'abord.
- Si les FAQ internes laissent trop de questions ouvertes, planifie des expériences pour les combler avant de spécifier.
- Quand le PR/FAQ tient la route, passe-le à `craft-spec` pour en faire un PRD constructible.
- Pour les paris à gros enjeu, lance `pre-mortem` sur le PR/FAQ pour tester les risques que les FAQ internes ont pu manquer.
