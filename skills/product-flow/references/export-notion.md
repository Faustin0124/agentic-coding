# Export vers Notion

À la fin (ou à la demande, à n'importe quelle étape), propose l'export et **demande confirmation avant d'écrire**. Comme `product-notes`, lis d'abord le schéma réel de la base (`notion-fetch`), copie les valeurs de sélection caractère pour caractère, ne devine ni identifiant ni vocabulaire.

1. **Mettre à jour l'item d'origine** (`notion-update-page`) : ajouter à sa page une section de synthèse (problème, preuves, décision, scope, métriques, risques principaux). Ne pas écraser le contenu existant.
2. **Créer les stories** (`notion-create-pages`) dans la même base, avec le même Epic parent que l'item (ou la relation que la base utilise), `Type` = `User Story`, une page par story avec contexte, énoncé et critères d'acceptation. Si une story est passée par `feature-scoping`, ajoute son cadrage technique à la page.
3. **Statut et priorité** : ne pas les modifier d'office. Propose le changement (ex. passer l'item à « prêt pour le dev », priorités P0 / P1 / P2 des stories) et applique-le seulement si l'utilisateur confirme.
4. **Sujet de taille Epic** :
   - l'item d'origine **est déjà** un Epic (`Type` = `Epic`) : le mettre à jour avec la synthèse (point 1), puis créer les stories rattachées à lui ;
   - l'item d'origine était une **story trop grosse** : proposer de la convertir en Epic (changer son `Type`, sur confirmation) ou d'en créer un nouveau et de laisser l'ancienne en lien ; ne rien supprimer ;
   - **aucun Epic** ne correspond : proposer un nom, demander confirmation, créer l'Epic **d'abord**, puis les stories qui pointent vers lui ;
   - copier le nom de l'Epic caractère pour caractère si c'est une propriété de sélection, pour ne pas créer une option en double.
5. **Doublons** : si une story existante recoupe une nouvelle, la signaler sans fusionner ni supprimer.
6. **Après l'export** : passer le brouillon `docs/<sujet>.md` au statut « exporté vers Notion » (Notion fait foi), puis finir par une courte liste des pages mises à jour ou créées, avec leur lien.
