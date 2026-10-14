---
name: draft-spec
description: Rédige un spec détaillé : contexte du problème en 3 phrases, exploration de plusieurs solutions avant de choisir, parcours utilisateur très concret, et critères d'acceptation testables (fonctionnels, cas limites, hors scope). À utiliser quand craft-spec est trop léger et que le spec doit être assez précis pour partir en dev sans ambiguïté.
---

# Draft Spec

**Un spec détaillé, assez précis pour que l'équipe de dev n'ait pas à deviner.**

Plus poussé que `craft-spec` : il impose de bien poser le problème, d'explorer l'espace des solutions avant de s'engager, de décrire l'expérience pas à pas et d'écrire des critères d'acceptation testables.

## Entrée

`$ARGUMENTS` : idée, notes, PRD existant ou PR/FAQ à détailler.
Si vide, demander ce qu'il faut spécifier. En cas de doute sur le problème, le public ou le « pourquoi maintenant », pose d'abord 3–5 questions ciblées plutôt que d'inventer.

## Format de sortie

*Mis à jour : @date du jour au format JJ/MM/AAAA*

### Contexte du problème

Un seul paragraphe actionnable et concis sur le problème et sa motivation : quels problèmes centraux on résout, ou quelles opportunités on débloque.
- Pourquoi le construire maintenant ? Pourquoi sommes-nous bien placés pour gagner sur ce sujet ?
- Le paragraphe doit être autonome (compréhensible sans contexte supplémentaire) et limité à **3 phrases maximum**.
- Commence par le persona client le plus pertinent (ex. : « Les gérants de petites entreprises ont besoin de… »). **Jamais de noms de personnes ni d'entreprises** précis dans ce paragraphe.

### Conception de la solution

**Explore l'espace des solutions** avant de t'engager. Envisage plusieurs solutions candidates et évalue-les selon des angles stratégiques et d'expérience.

Identifie les leviers stratégiques qui comptent le plus pour cette solution et creuse-les :
- avantages de coût par économies d'échelle ;
- effets de réseau (la valeur croît avec le nombre de participants) ;
- contre-positionnement (une capacité que les concurrents ne peuvent pas copier sans bousculer leur propre stratégie) ;
- coûts de changement (rendre le départ moins attractif) ;
- marque (identité et lien émotionnel durable) ;
- ressources exclusives (données propriétaires, partenariats, capacités uniques) ;
- processus supérieurs ou workflows propriétaires.

Pour une expérience simple et agréable, applique ces principes au parcours :
- Simplifie sans relâche : retire les étapes et éléments superflus. Chaque élément doit mériter sa place.
- Assure la continuité : guide l'utilisateur du début à la fin avec une charge cognitive minimale et sans impasse.
- Soigne les détails : typographie, transitions, espacements et textes reflètent un vrai soin.
- Ajoute de petites touches mémorables qui dépassent le simple fonctionnel.
- Quand tu ne sais pas comment concevoir un composant, inspire-toi de produits de référence de la catégorie.

N'énonce pas ces principes explicitement : intègre-les dans ton raisonnement quand tu explores puis choisis la solution.

Après avoir exploré et retenu la meilleure stratégie, fournis un déroulé concis de ce que fait la fonctionnalité, comment elle résout les douleurs de l'utilisateur et en quoi elle lui plaît, sans préambule inutile :
- Décris très précisément comment l'utilisateur interagit avec le produit : interface, chaque étape du parcours, comment on améliore l'utilisabilité et la simplicité.
- Présente le scénario d'usage réel attendu après le lancement, ancré dans un vrai utilisateur à un vrai moment. Exemple : « Quand Frank visite des startups à Paris, il utilise [feature X] pour noter les besoins et les suivre dans [feature Y] au fil des rencontres… »
- Souligne ce qui distingue cette solution des alternatives du marché.
- Un paragraphe court par aspect de l'expérience, séparés par des sauts de ligne.

La meilleure solution maximise **ICE** : fort impact, forte confiance, faible effort. Indique brièvement l'impact, la confiance et l'effort de la solution retenue, et pourquoi elle bat les alternatives écartées.

### Critères d'acceptation

Chaque critère décrit une condition précise et testable avec un résultat attendu clair. Les critères décrivent des **résultats voulus, pas des choix d'implémentation**. Ils sont **MECE** (mutuellement exclusifs, collectivement exhaustifs) et couvrent tout ce qui est nécessaire pour que le travail soit terminé.

**Fonctionnel :**
- [Comportement utilisateur observable → réponse ou résultat attendu du système]

**Cas limites et gestion d'erreurs :**
- [Que se passe-t-il quand la saisie est invalide, un service tombe, des données manquent, l'utilisateur atteint un état inattendu ?]

**Hors scope :**
- [Ce que ce travail n'inclut explicitement PAS, pour éviter le sur-développement]

Exemples de bons critères :
- Quand l'utilisateur tape dans la barre de recherche, les résultats se mettent à jour en direct après un debounce de 300 ms, avec nom du produit, image et prix dans une liste classée.
- L'utilisateur peut aller dans Paramètres > Modifier le profil et changer prénom, nom, e-mail et téléphone. Les changements persistent à l'enregistrement et se reflètent partout sans rechargement.
- Si la requête d'enregistrement échoue (timeout ou 5xx), un message en ligne s'affiche : « Une erreur est survenue. Réessaie. » Le formulaire conserve la saisie non enregistrée.
- Soumettre une recherche vide renvoie la liste par défaut, sans erreur ni état vide.
- Cela n'inclut PAS l'édition de profil en masse, l'export CSV ni les changements de permissions admin.

## Conseils

- Si le problème n'est pas solide, retourne à `jobs-to-be-done` ou `mom-test` avant de spécifier.
- Après le spec : `pre-mortem` puis `create-user-stories`.
