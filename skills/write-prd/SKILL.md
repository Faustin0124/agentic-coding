---
name: write-prd
description: Rédaction guidée d'un PRD : recueille le contexte par conversation (3–5 questions ciblées), puis génère un spec structuré avec craft-spec. Point d'entrée recommandé pour passer d'une idée à un PRD. Déclencheurs : "écris un PRD", "write PRD", "j'ai une idée de feature", "aide-moi à spécifier", "définir le problème".
---

# Write PRD

**Transformer une idée brute en PRD structuré par une conversation guidée.**

## Déroulé

1. **Comprendre la fonctionnalité** : accepte l'entrée sous n'importe quelle forme (bullet points, threads Slack, notes brutes, description orale). Ne demande pas de la nettoyer.

2. **Recueillir le contexte** : pose 3 à 5 questions ciblées pour combler les trous. Couvre :
   - Quel problème résout-on, et pour qui ?
   - Comment sait-on que c'est un vrai problème ? (données, retours clients, intuition)
   - À quoi ressemble le succès ? Quelles métriques doivent bouger ?
   - Quelles contraintes existent ? (délai, technique, dépendances)
   - Qu'est-ce qui est explicitement hors scope ?

   Pose les questions en conversation, pas comme une checklist. Saute celles dont la réponse figure déjà dans l'entrée.
   Si la réponse à « comment sait-on que c'est un vrai problème ? » est « intuition » seulement, propose `mom-test` ou `jobs-to-be-done` avant d'écrire le PRD.

3. **Générer le PRD** : utilise le skill `craft-spec` (ou `draft-spec` si l'utilisateur veut un spec détaillé avec critères d'acceptation) pour produire un PRD avec :
   - Énoncé du problème
   - Objectifs et métriques de succès
   - Scope (dans / hors scope)
   - Solution proposée
   - User stories clés
   - Questions ouvertes

4. **Relire et itérer** : présente le brouillon et propose :
   - « Je resserre le scope ? »
   - « J'ajoute du détail dans une section ? »
   - « Je lance un `pre-mortem` pour tester les risques ? »
   - « Je découpe en stories avec `create-user-stories` pour l'envoyer au dev ? »

## Principes

- Scope serré plutôt que vague : si quelque chose est ambigu, signale-le.
- Les non-objectifs pèsent autant que les objectifs.
- Les métriques de succès doivent être précises et mesurables.
- Signale les hypothèses pour que l'utilisateur puisse les valider.
- Suggère un phasage quand le scope est large.

## Flux complet recommandé

`jobs-to-be-done` / `mom-test` (problème) → `amazon-working-backwards` (l'idée vaut-elle le coup ?) → `write-prd` / `craft-spec` / `draft-spec` (PRD) → `pre-mortem` (risques) → `create-user-stories` (passation au dev)
