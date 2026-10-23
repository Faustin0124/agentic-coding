# Grille de diagnostic d'un écran existant

À passer après l'inventaire (étape 1). On ne cherche pas à tout cocher : on relève ce qui explique les problèmes exprimés, et les incohérences qui sautent aux yeux.

## 1. Incohérences internes (à chercher en premier)

- **Compteurs** : le même nombre est-il affiché à plusieurs endroits ? Dit-il la même chose partout (en-tête, groupes, pied de page) ?
- **Messages et états** : un texte affirme-t-il une chose que l'interface contredit ? (« ne bloque pas la validation » alors que le bouton paraît désactivé)
- **Signaux visuels** : une couleur, une pastille, un style garde-t-il le même sens partout ? Deux couleurs différentes pour le même statut ?
- **Actions** : pourquoi certains éléments ont-ils deux boutons et d'autres un lien ? La différence est-elle expliquée ?
- **Vocabulaire** : le même concept porte-t-il plusieurs noms (« à relire », « incertaine », « avec hésitation ») ?

## 2. Compréhension (« je ne comprends pas… »)

- L'utilisateur sait-il **ce qu'on attend de lui** sur cet écran, en une phrase ?
- Chaque action dit-elle **sur quoi elle porte** ? Un « Confirmer » sans objet visible est un signal fort.
- Le **pourquoi** est-il donné quand le système demande une intervention (doute, alerte, erreur) ?
- L'**impact** d'un choix est-il visible (montant, délai, conséquence) ?
- Le jargon interne (catégories techniques, statuts back) est-il traduit en langage utilisateur ?

## 3. Efficacité (« je perds du temps… »)

- Quelle part des éléments affichés demande réellement une action ? Si c'est moins de 30 %, l'écran montre surtout du bruit.
- Les éléments **déjà traités** restent-ils dans le chemin ?
- Existe-t-il un **filtre, un tri ou un regroupement** qui place d'abord ce qui reste à faire ?
- Combien de scrolls ou de clics pour traiter un élément ? Pour tout traiter ?
- Peut-on **traiter en lot** quand plusieurs éléments partagent la même décision ?
- Raccourcis clavier pour les tâches répétitives ?

## 4. Orientation et progression

- L'utilisateur sait-il **où il en est** (x / n, barre de progression) ?
- Sait-il **ce qui bloque** la suite et ce qui est facultatif ?
- La navigation « suivant » garde-t-elle ses repères ou le fait-elle sauter dans une longue liste ?
- Que se passe-t-il **quand tout est traité** (résumé, appel à l'action clair) ?

## 5. États et cas limites (à vérifier dans le code si possible)

- État vide, chargement, erreur.
- Zéro élément à traiter / tous traités / très gros volume.
- Retour en arrière : peut-on annuler une décision ?

## 6. Accessibilité (contrôle rapide)

- Contraste des textes secondaires et des boutons désactivés.
- Information portée uniquement par la couleur (pastille sans libellé).
- Cibles cliquables assez grandes, focus clavier visible.

Pour un audit complet, utilise un skill d'accessibilité dédié.
