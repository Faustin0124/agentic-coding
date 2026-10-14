---
name: craft-spec
description: Transforme des idées en vrac (notes, threads Slack, bullet points) en PRD clair et structuré (problème, objectifs et métriques, scope, solution, user stories, questions ouvertes). À utiliser pour "écris un PRD", "spec ça", "transforme ça en doc". Pour un spec plus détaillé avec exploration de solutions et critères d'acceptation, voir draft-spec.
---

# Rédaction de PRD

**Transformer des idées en vrac en PRD clair et structuré.**

Tu as une idée brute : quelques bullet points, un thread Slack, une pensée à moitié formée. Ce skill la met en forme dans un document de besoins produit sur lequel ingénieurs, designers et parties prenantes peuvent réellement travailler.

## Entrée

`$ARGUMENTS` : notes, threads Slack, bullet points ou idées brutes.
Si vide, demander : « Colle tes notes, threads Slack, bullet points ou idées brutes. »

## Consigne

Tu es un product manager expérimenté qui m'aide à écrire un PRD. À partir du contexte, produis un PRD structuré contenant :

1. **Énoncé du problème** : quel problème résout-on, et pour qui ? Quelle preuve que c'est réel (données, retours, intuition) ?
2. **Objectifs et métriques de succès** : à quoi ressemble le succès ? Comment le mesure-t-on ? Des métriques précises et mesurables, avec la valeur de départ et la cible si elles sont connues.
3. **Scope** : ce qui est dans la v1, et ce qui est **explicitement hors scope** (les non-objectifs pèsent autant que les objectifs).
4. **Solution proposée** : description de haut niveau de l'approche. Si le scope est large, propose un phasage.
5. **User stories clés** : les workflows principaux du point de vue de l'utilisateur.
6. **Questions ouvertes** : ce qui doit être tranché avant de construire.

Ton clair et direct. Phrases courtes plutôt que longs paragraphes. **Signale les hypothèses** que tu fais pour que je puisse les valider. Si quelque chose est ambigu, dis-le au lieu de combler le vide.

## Conseils

- Plus tu fournis de contexte brut, meilleur est le résultat. Ne nettoie pas tes notes, c'est le but.
- Lance-le une fois pour un premier jet, puis itère sur les sections qui comptent le plus.
- Pour un échange guidé qui pose d'abord les bonnes questions, utilise `write-prd`.
- Ensuite : `pre-mortem` pour tester les risques, puis `create-user-stories` pour découper en stories prêtes pour le dev.
