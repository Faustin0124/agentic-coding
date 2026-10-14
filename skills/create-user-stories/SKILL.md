---
name: create-user-stories
description: Découpe un PRD ou une description de fonctionnalité en user stories implémentables avec critères d'acceptation Given/When/Then. À utiliser pour la passation à l'ingénierie ou la planification de sprint. Déclencheurs : "découpe ça", "envoie au dev", "user stories", "critères d'acceptation", "sprint planning".
---

# Créer des user stories

**Transformer un spec en stories sur lesquelles les ingénieurs peuvent construire.**

Tu as un PRD ou une description de fonctionnalité à découper en user stories : assez petites pour tenir dans un sprint, assez claires pour que les ingénieurs n'aient pas à deviner, assez testables pour que le QA sache quand c'est fini.

## Entrée

`$ARGUMENTS` : PRD, description de la fonctionnalité, liens de maquettes ou besoins bruts.
Si vide, demander : « Colle ton PRD, la description de la fonctionnalité, des liens de design ou des besoins bruts. »

## Consigne

Tu es un product manager expérimenté qui découpe une fonctionnalité en user stories pour l'ingénierie. Pour chaque story :

**Titre :** nom court et descriptif.

**Story :** En tant que [rôle utilisateur précis], je veux [action], afin de [bénéfice/résultat].

**Critères d'acceptation :**
- [ ] Étant donné [précondition], quand [action], alors [résultat attendu]
- [ ] Inclure cas limites, états d'erreur et conditions aux bornes
- [ ] 4 à 6 critères par story : assez pour être clair, pas assez pour devenir un mini-spec

**Priorité :** P0 (indispensable au lancement), P1 (souhaitable) ou P2 (confort / plus tard).

**Notes :** dépendances, références de design, considérations techniques ou questions ouvertes.

Applique ces principes :
- Chaque story doit être réalisable en un seul sprint. Trop grosse ? Découpe.
- Les stories sont indépendantes : évite les chaînes où B ne peut démarrer qu'après la livraison de A.
- Écris les critères comme des comportements testables, pas des descriptions vagues. « L'utilisateur voit un message de succès », pas « l'utilisateur a une bonne expérience ».
- Inclus les chemins non nominaux : que se passe-t-il quand l'API échoue, quand l'utilisateur n'a aucune donnée, quand il atteint une limite de débit ?
- Regroupe les stories par workflow utilisateur, pas par composant technique.
- Signale toute story qui requiert un apport de design, des changements d'API ou des dépendances inter-équipes.

## Conseils

- Alimente-le avec la sortie de `craft-spec` ou `draft-spec` pour un pipeline PRD → stories propre.
- Si les stories sortent toujours trop grosses, le spec contient sans doute du scope à phaser d'abord.
- Les meilleurs critères se lisent comme un script de test : un QA doit pouvoir vérifier chacun sans poser de question.
- N'oublie pas la story d'**état vide** (que voit l'utilisateur avant d'avoir des données ?) : c'est presque toujours oublié.
