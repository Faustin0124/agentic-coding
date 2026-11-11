# Gabarit du ticket de feature

La structure à générer en phase 5. Garde ces champs, dans cet ordre, quelle que soit la
destination (conversation, Notion, issue GitHub, fichier local) : seule la mise en forme change.

---

## Format d'affichage (conversation / fichier local)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ FEATURE — [TITRE COURT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 INFOS GÉNÉRALES
  Taille       : 🟢 S | 🟡 M | 🔴 L
  Statut       : 🆕 À faire
  Date         : [date du jour]
  Origine      : Retour client / Besoin interne / Idée

🎯 BESOIN
  En tant que [rôle], je veux [action] afin de [bénéfice].
  Contexte     : [situation concrète, 1–2 phrases]

📍 ANCRAGE DANS LE CODE
  Écran / route : [chemin]
  Données       : [tables, requêtes, types]
  Réutilisé     : [composants, hooks, règles existants]

📡 IMPACT
  Zones touchées :
    - src/... → [nature de l'impact]
  Changement de données : Oui (lequel) / Non
  Fichiers sensibles    : [liste, ou « aucun »]

🔧 PLAN
  Approche     : [description de la solution]
  Étapes       :
    1. [...]
    2. [...]
  Tests        : [tests à écrire]

✅ CRITÈRES D'ACCEPTATION
  - [ ] Étant donné [...], quand [...], alors [...]
  - [ ] [cas limite ou état d'erreur]

🚫 HORS SCOPE
  [ce que la feature ne fait pas]

  Estimation :
    Temps        : X heures / X jours
    Complexité   : Faible / Moyenne / Élevée
    Livrable seul : Oui / Non

⚠️ POINTS D'ATTENTION
  [risques, dépendances, questions ouvertes — vide si aucun]

🏷️ TAGS
  [feature] [domaine] [taille-S/M/L]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Règles pour le titre

- Court (moins de 60 caractères), factuel.
- Format : `[Écran/Domaine] — [Ce que l'utilisateur pourra faire]`

Bien :
- `Factures — Filtrer par statut de paiement`
- `Relecture — Masquer les lignes déjà confirmées`

À éviter :
- `Nouvelle feature` — trop vague
- `Améliorer l'écran` — pas actionnable
- Un paragraphe entier en titre — mettre le détail dans le besoin

---

## Classer dans Notion

Ne suppose aucune base ni aucun schéma : chaque projet est différent.

1. **Trouver la base cible** avec `notion-search` (« backlog », « roadmap », « features »).
   Plusieurs résultats → les présenter et demander. Aucun → demander l'URL.
2. **Lire son schéma réel** avec `notion-fetch` avant de créer quoi que ce soit. Copier les
   valeurs de sélection caractère pour caractère. Une propriété du gabarit qui n'existe pas
   → mettre l'information dans le corps de la page.

   | Champ du ticket | Propriété Notion typique | Type |
   |---|---|---|
   | Titre | `Name` (titre de la page) | title |
   | Type | `Type` = `User Story` | select |
   | Epic parent | `Epic` | select ou relation |
   | Statut | `Status` (valeur la plus amont) | status |
   | Taille | `Estimate` / `Taille` si elle existe | select |
   | Tout le reste | Corps de la page | blocs |

3. **Story existante pour cette feature** → ajouter le cadrage à sa page
   (`notion-update-page`) sans écraser le contenu. Sinon, créer la page
   (`notion-create-pages`) rattachée à l'Epic existant ; si aucun ne correspond, proposer un
   nom et demander confirmation avant de créer un Epic.
4. **Ne pas changer** le statut, la priorité ou le sprint sans confirmation.
5. **Confirmer** avec le lien de la page.

## Classer en issue GitHub

Utilise l'outil disponible (`gh issue create` ou l'outil d'issues d'un MCP GitHub). Le titre
et le corps reprennent le gabarit tel quel. Applique un label `feature` / `enhancement`
seulement s'il existe déjà dans le dépôt.
