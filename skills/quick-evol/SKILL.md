---
name: quick-evol
description: Version courte de product-flow pour une petite évolution (une story, pas un Epic). Part d'un item du backlog Notion (créé avec product-notes) ou d'une note brute, vérifie d'abord que le sujet est vraiment petit (sinon renvoie vers product-flow ou ux-evolution), puis produit une fiche évol d'une page (problème, solution, critères Given/When/Then, hors scope, risque, mesure) avec une seule porte de validation, et met à jour la story Notion sur confirmation. Déclencheurs : "petite évol", "quick evol", "petit truc à ajouter", "prépare cette story pour le dev", "c'est rapide à faire", "pas besoin d'un PRD", "prends la prochaine petite évol du backlog".
---

# Quick Evol

**D'une petite évol à une story prête pour le dev, en une page et une validation.**

`product-flow` déroule cinq étapes et cinq portes : c'est trop pour un libellé à changer, un filtre à ajouter ou un champ à rendre facultatif. Ce skill garde sa logique (lire la vraie structure de Notion, séparer le su du supposé, ne rien écrire sans confirmation) dans un format court.

| Skill | Rôle |
|---|---|
| `product-notes` | Capture l'idée dans le backlog |
| `quick-evol` | Prépare une **petite** évol pour le dev |
| `ux-evolution` | Fait évoluer un écran ou un parcours existant à partir de captures et d'irritants |
| `product-flow` | Raffine un **gros** sujet ou un Epic |

## Entrée

`$ARGUMENTS` : un sujet, sous l'une de ces formes :
1. **Un item du backlog Notion** (titre, lien ou « la prochaine petite évol ») → le retrouver (`notion-search` / `notion-fetch`) et lire sa page. Si rien n'est précisé, lister les items en statut le plus amont et demander lequel prendre.
2. **Une note brute** donnée en conversation.

Pour la base Notion, applique la logique de `product-notes` : trouver la base, lire son schéma réel, copier les valeurs de sélection caractère pour caractère.

## Étape 1. Test de taille

Avant tout, vérifie que le sujet relève bien d'ici. Il passe seulement si **tout** est vrai :

- [ ] **Un seul parcours** utilisateur touché.
- [ ] **Quelques jours de travail**, au plus un sprint.
- [ ] **Pas de nouveau modèle de données** ni de nouvelle intégration externe.
- [ ] **Problème connu** : retour client, bug d'usage, demande claire. Rien à valider auprès des utilisateurs.

Annonce le résultat en une phrase. Si un point échoue, dis lequel et propose de passer la main :

| Point qui échoue | Redirection |
|---|---|
| Plusieurs parcours, plus d'un sprint, nouveau modèle de données | `product-flow` (probablement un Epic) |
| Problème non validé, seulement une intuition | `product-flow`, étape 1 (`mom-test` / `jobs-to-be-done`) |
| Sujet surtout lié à un écran existant mal compris ou trop long | `ux-evolution` |

L'utilisateur peut forcer le passage en `quick-evol` ; note alors le point qui échoue dans la fiche, section « Risque principal ».

## Étape 2. Mini-cadrage

**Deux questions au plus**, seulement si l'entrée ne permet pas d'y répondre :
- Qui est gêné, et dans quelle situation ?
- Qu'est-ce qui doit être vrai une fois l'évol livrée ?

Si le code est accessible, regarde rapidement où l'évol se loge (composant, route, règle) : ça évite une solution qui ignore l'existant et ça révèle un sujet plus gros qu'annoncé.

## Étape 3. Fiche évol

Une page, pas plus. Gabarit :

```markdown
# <Titre court, 5–10 mots>

**Problème** : <qui, quoi, preuve, en 1–2 lignes>
**Solution** : <ce qui change, en 3–5 lignes ; ce qui ne change pas si utile>

**Critères d'acceptation**
- [ ] Étant donné <…>, quand <…>, alors <…>
- [ ] … (3 à 5 critères, dont au moins un état d'erreur ou un cas limite)

**Hors scope** : <ce qu'on ne fait pas dans cette évol>
**Risque principal** : <ce qui pourrait mal tourner> → <parade>
**Comment on sait que ça marche** : <une métrique ou un signal simple>

_Su_ : <faits> · _Supposé_ : <hypothèses à confirmer>
```

Les critères suivent le format de `create-user-stories`, en version courte. Le risque est un pre-mortem en une ligne : la chose la plus probable qui ferait échouer l'évol.

> **Porte unique. La fiche te va ?** Propose : *valider* / *ajuster X* / *c'est plus gros que prévu → product-flow*.

## Étape 4. Sortie

Après validation :

1. **Notion** (sur confirmation) :
   - si on partait d'un item : ajouter la fiche à sa page (`notion-update-page`), sans écraser le contenu existant ;
   - si on partait d'une note : créer la story comme le fait `product-notes` (type, Epic parent existant, statut le plus amont), avec la fiche comme contenu ;
   - ne pas changer le statut, la priorité ou le sprint d'office : proposer (ex. « passer à prêt pour le dev ? ») et appliquer seulement si l'utilisateur confirme.
2. **En option**, propose un **prompt Lovable** ou un **brief dev** prêt à coller, construit à partir de la solution et des critères (une modification par point numéroté, libellés exacts, ce qui ne change pas).
3. Termine par le lien de la page Notion mise à jour ou créée.

Pas de dossier `docs/<sujet>/` par défaut : la fiche vit dans Notion. Écris `docs/<sujet>.md` seulement si l'utilisateur le demande ou si Notion n'est pas disponible.

## Si le sujet grossit en route

Si le mini-cadrage ou la lecture du code montre que le sujet est plus gros qu'annoncé, **arrête et dis-le** : « Ce n'est plus une petite évol parce que <raison>. Je passe sur `product-flow` ? » La fiche déjà écrite sert alors de `brief.md` de départ.

## Règles

- **Test de taille d'abord**, toujours annoncé en une phrase.
- **Deux questions au plus**, jamais celles dont la réponse est déjà dans l'item.
- **Une page, une porte** : pas de PRD, pas de pre-mortem complet, pas de découpage.
- **Séparer le su du supposé** dans la fiche.
- **Notion en écriture seulement sur confirmation** ; jamais de suppression, de fusion ou de changement de sprint.
- **Rediriger plutôt que forcer** : une grosse évol déguisée en petite coûte plus cher qu'un `product-flow`.
