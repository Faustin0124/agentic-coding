---
name: feature-scoping
description: >
  Cadrage d'une feature simple avant de la coder, sur le modèle de bug-diagnostics : 5 phases
  dans l'ordre (besoin et taille → ancrage dans le code → impact → plan d'implémentation →
  ticket et décision). Lit le code pour savoir où la feature se loge, ce qu'on peut réutiliser
  et ce qu'elle risque de casser, puis produit un ticket prêt pour le dev et demande s'il faut
  coder maintenant, créer le ticket, ou les deux. Déclencheurs : "ajoute une feature",
  "je veux pouvoir…", "il faudrait que l'utilisateur puisse…", "cadre cette feature",
  "comment on implémente…", "nouvelle fonctionnalité", "petite feature", "ajoute un bouton /
  un filtre / un champ / un export", "prépare cette story pour le code". Pour un gros sujet ou
  un Epic, renvoie vers product-flow ; pour un bug, vers bug-diagnostics.
---

# Feature Scoping

Un cadrage en 5 phases. Fais-les dans l'ordre, sans en sauter : chaque phase nourrit la
suivante, et coder directement est la façon la plus sûre de livrer une feature qui duplique
l'existant ou casse un écran voisin.

| Skill | Quand |
|---|---|
| `bug-diagnostics` | Quelque chose ne marche pas comme prévu |
| `feature-scoping` | Ajouter ou changer un comportement, sujet simple |
| `quick-evol` | Cadrage produit seulement (fiche + Notion), sans lire le code |
| `product-flow` | Gros sujet, Epic, problème encore à valider |

---

## Phase 1 — Besoin et taille

### 1.1 Recueillir le contexte minimal

S'il manque des éléments, pose les questions **toutes en une fois** (pas une par une) et
saute celles dont la réponse est déjà là :

- Qui a besoin de la feature, et dans quelle situation ?
- Que doit-il pouvoir faire une fois livrée ? (le résultat attendu, pas la solution)
- D'où vient la demande : retour client, besoin interne, idée ?
- Une contrainte : délai, écran imposé, pas de changement côté back ?

### 1.2 Reformuler et classer la taille

Reformule le besoin en une phrase : « En tant que <rôle>, je veux <action> afin de
<bénéfice>. » Puis classe la taille :

| Taille | Critères | Suite |
|---|---|---|
| 🟢 **S** | Un écran ou une règle, pas de changement de données, quelques heures | Continuer |
| 🟡 **M** | Un parcours, éventuellement un champ ou une table simple, quelques jours | Continuer |
| 🔴 **L** | Plusieurs parcours, nouveau modèle de données, intégration externe, plus d'un sprint | Proposer `product-flow` |

**Affiche la reformulation et la taille avec leur justification avant de continuer.** Si
c'est un L, dis pourquoi et propose de basculer ; continue seulement si l'utilisateur le
demande.

---

## Phase 2 — Ancrage dans le code

### 2.1 Trouver où la feature se loge

Utilise les outils de recherche et de lecture pour repérer :

- l'**écran, la route ou le composant** concernés ;
- la **source des données** (requêtes, hooks, types, tables) ;
- les **règles métier** déjà en place sur ce sujet.

```bash
# Repérer l'écran ou le composant
grep -rn "NomDeLEcran\|libellé visible à l'écran" src/ -l

# Repérer la donnée
grep -rn "nom_de_table\|NomDuType" src/ supabase/ -l
```

Adapte les dossiers (`src/`, `app/`, `supabase/`, etc.) à la structure réelle du projet.

### 2.2 Chercher ce qui existe déjà

Avant de proposer du neuf, cherche ce qu'on peut **réutiliser** :

- une feature proche ailleurs dans l'app (un filtre, un export, une modale du même genre) ;
- les composants du design system ou de la librairie UI déjà utilisés ;
- des utilitaires, hooks ou fonctions back qui font déjà une partie du travail.

### 2.3 Résumer l'ancrage

En 3 à 5 lignes : où la feature va vivre, ce qu'on réutilise, et ce qui manque vraiment.
Si tu n'as pas accès au code, dis-le clairement et marque cette phase comme **supposée**.

---

## Phase 3 — Impact

### 3.1 Lister ce que la feature touche

Cherche activement ce qui pourrait être affecté :

- **Données** : changement de schéma, migration, données existantes à reprendre ?
- **Droits et sécurité** : qui peut voir ou faire quoi (rôles, règles d'accès aux lignes) ?
- **Autres écrans** : composants ou requêtes partagés avec d'autres parties de l'app ?
- **Calculs et règles métier** : un résultat affiché ailleurs peut-il changer ?
- **États** : vide, chargement, erreur, gros volumes.

### 3.2 Tableau des zones touchées

```
| Fichier / zone | Nature de l'impact | Risque | Notes |
|----------------|--------------------|--------|-------|
| src/...        | Modifié            | Faible | ...   |
| supabase/...   | Nouvelle colonne   | Moyen  | ...   |
```

Signale les **fichiers sensibles** (calculs financiers ou légaux, auth, paiement,
migrations) : ils demandent une confirmation avant d'être modifiés. Si le projet a un
CLAUDE.md ou une doc de conventions qui les nomme, suis-la ; sinon, demande une fois.

Si l'impact est limité, dis-le explicitement : « Impact limité à X, aucune autre zone
touchée trouvée. » Ne laisse pas croire que tu as cherché plus large que tu ne l'as fait.

---

## Phase 4 — Plan d'implémentation

### 4.1 Proposer l'approche

- Décris la solution retenue, avec du code si c'est utile.
- S'il existe deux approches vraiment différentes, présente-les avec leurs compromis et
  recommande-en une.
- Écris les **critères d'acceptation** : 3 à 5, au format « Étant donné…, quand…, alors… »,
  dont au moins un état d'erreur ou un cas limite.
- Précise le **hors scope** : ce que la feature ne fait pas.

### 4.2 Estimer l'effort

| Dimension | Estimation |
|-----------|------------|
| ⏱️ Temps | X heures / X jours |
| 🔧 Complexité | Faible / Moyenne / Élevée |
| 🗄️ Changement de données | Oui / Non — lequel |
| 🧪 Tests à écrire | Lesquels |
| 🚀 Livrable seul | Oui / Non (dépendances) |

### 4.3 Ordre des étapes

```
1. [DONNÉES] Migration : ajouter la colonne X (si besoin)
2. [BACK] Exposer X dans la requête Y
3. [FRONT] Ajouter le filtre dans le composant Z
4. [TESTS] Cas nominal + état vide + erreur
```

---

## Phase 5 — Ticket et décision

### 5.1 Générer le ticket

Mets le cadrage en forme avec le gabarit de
[`references/ticket-template.md`](references/ticket-template.md). Il est indépendant de
l'outil : d'abord affiché dans la conversation, ensuite adapté à la destination.

### 5.2 Proposer le choix

**Pose toujours cette question après le ticket :**

```
📋 Cadrage terminé. Que veux-tu faire ?

A) 🚀 Coder maintenant — je commence l'implémentation
B) 📤 Créer le ticket — je le classe et je m'arrête là
C) 📤 + 🚀 Les deux — je crée le ticket ET je commence
```

Si l'implémentation se fait dans Lovable, propose aussi un prompt prêt à coller, construit à
partir du plan (une modification par point numéroté, libellés exacts, ce qui ne change pas).

### 5.3 Classer le ticket (si B ou C)

La destination dépend de ce qui est disponible. Vérifie dans l'ordre :
1. Notion connecté ? → applique la logique de `product-notes` : trouver la base backlog, lire
   son schéma réel, rattacher à l'Epic existant, statut le plus amont. Si une story existe déjà
   pour cette feature, ajoute le cadrage à sa page plutôt que d'en créer une nouvelle.
2. Dépôt GitHub avec outils d'issues ? → crée une issue avec le même contenu.
3. Rien de disponible, ou pas de préférence ? → enregistre le ticket en markdown local
   (`FEAT-<slug>.md`) et dis où il se trouve.

Confirme ensuite :
```
✅ Ticket créé : [lien ou chemin du fichier]
```

---

## Règles

- **Toujours afficher la taille** de la phase 1 avant de continuer.
- **Lire le code avant de proposer** : la phase 2 n'est pas facultative quand le code est
  accessible.
- **Réutiliser avant de créer** : un composant ou une règle existante l'emporte sur du neuf.
- **Être factuel sur l'impact** : sans accès complet au code, le dire clairement.
- **Ne jamais modifier** les fichiers sensibles, le schéma de données ou faire un refactoring
  d'architecture sans confirmation explicite.
- **Toujours proposer** le choix A/B/C de la phase 5 : ne jamais coder directement sans
  demander, même si la feature paraît évidente.
- Si la feature s'avère plus grosse en cours de route (taille L), **arrête et propose
  `product-flow`**, en reprenant le cadrage déjà fait comme point de départ.
