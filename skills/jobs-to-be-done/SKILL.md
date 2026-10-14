---
name: jobs-to-be-done
description: Révèle les "jobs" fonctionnels, sociaux et émotionnels qui expliquent le comportement des clients. À utiliser pour comprendre pourquoi les clients adoptent, changent ou abandonnent un produit, au-delà de ce qu'ils demandent. Déclencheurs : "pourquoi ils churnent", "qu'est-ce qu'ils veulent vraiment", "quel job ça résout", motivations, demandes de features à creuser, définition du problème avant un PRD.
---

# Jobs to Be Done

**Révéler les jobs fonctionnels, sociaux et émotionnels qui expliquent le comportement des clients.**

Les clients n'achètent pas des produits : ils les « embauchent » pour progresser dans leur vie ou leur travail. Ce skill aide à dépasser les demandes de features pour atteindre les motivations qui pilotent l'adoption, la rétention et le churn.

## Entrée

`$ARGUMENTS` : recherche client, notes d'entretiens, données de churn, demandes de features ou description du produit.
Si vide, demander : « Colle ici tes notes de recherche client, entretiens, données de churn, demandes de features ou une description du produit. »

## Consigne

Tu es un stratège produit expérimenté qui applique le cadre Jobs to Be Done. Analyse le contexte et produis :

1. **Jobs fonctionnels** : les tâches que le client essaie d'accomplir. Que cherche-t-il à faire ? À quoi ressemble son workflow aujourd'hui ? Mesure : gain de temps, réduction d'effort, précision, débit.
2. **Jobs sociaux** : comment le client veut être perçu par les autres. Quelle identité professionnelle ou quel statut veut-il projeter ? Souvent non dit, mais moteur puissant d'adoption et de consentement à payer.
3. **Jobs émotionnels** : les sentiments recherchés ou évités. Quelles angoisses l'approche actuelle crée-t-elle ? Quelle confiance ou quel soulagement la solution idéale apporterait-elle ? Souvent le plus fort levier de fidélité, mais le moins exprimé.
4. **Frustrations actuelles** : pour chaque job, les obstacles, le temps/l'argent/l'effort gaspillé, les erreurs causées par l'approche actuelle, les lacunes des solutions existantes.
5. **Gains attendus** : pour chaque job, ce qui dépasserait les attentes, les gains d'efficacité chiffrables, les nouvelles capacités débloquées, le confort apporté.
6. **Priorisation des jobs** : classe-les par intensité (à quel point c'est ressenti), fréquence (à quelle fréquence ça arrive) et sous-service (à quel point les solutions actuelles répondent mal).
7. **Implications** : que faut-il construire, positionner ou changer ? Quels jobs faut-il ignorer ?

**Sépare toujours ce que les clients ont dit de ce que tu infères.** Cite-les directement quand c'est possible. Signale où il faut plus de recherche.

## Conseils

- Le test classique : « Les clients ne veulent pas une perceuse, ils veulent un trou. » Continue à creuser derrière la demande de feature jusqu'au job sous-jacent.
- Les jobs sociaux et émotionnels sont là où se joue la vraie différenciation. Les jobs fonctionnels se banalisent, les jobs émotionnels créent la fidélité.
- À combiner avec un travail de synthèse si tu as des transcripts bruts à traiter d'abord.
- Si tu n'as que des demandes de features (pas de recherche), ce skill fait ressortir les hypothèses que tu fais, donc ce qu'il faut aller valider (voir `mom-test`).
- Une fois les jobs clairs, passe à `amazon-working-backwards` ou `write-prd`.
