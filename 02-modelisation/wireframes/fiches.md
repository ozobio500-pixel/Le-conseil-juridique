# Fiches de wireframes — Le Conseil Juridique

Ces fiches décrivent les wireframes basse fidélité de `index.html`. Elles servent de base à une reproduction dans Figma; elles ne constituent pas une maquette Figma validée.

## 1. Connexion

- **Zones/composants :** en-tête avec nom du projet, formulaire centré avec courriel et mot de passe, bouton « Se connecter », lien vers l'inscription.
- **Actions :** saisir les identifiants, envoyer le formulaire, ouvrir l'inscription.
- **États :** vide : formulaire prêt; erreur : champs requis ou identifiants refusés; succès : confirmation et accès au tableau de bord.
- **Rôles :** utilisateurs inscrits (Administrateur, Juriste/conseiller, Agent d'accueil, Avocat partenaire, Direction/bailleur).

## 2. Inscription

- **Zones/composants :** formulaire nom, prénom, courriel, mot de passe et confirmation; bouton « Créer mon compte »; lien connexion; avertissement sur l'attribution du rôle.
- **Actions :** compléter et envoyer la demande d'inscription.
- **États :** vide : champs vierges; erreur : champs manquants/courriel invalide; succès : demande confirmée, rôle **À CONFIRMER**.
- **Rôles :** personne demandant l'inscription; activation et attribution des rôles **À CONFIRMER**.

## 3. Tableau de bord

- **Zones/composants :** navigation latérale selon rôle, trois cartes de compteurs, tableau des derniers cas et liste des prochains rendez-vous.
- **Actions :** ouvrir un cas, un rendez-vous ou un module permis par le rôle.
- **États :** vide : compteurs à zéro et listes vides; erreur : message de chargement; succès : compteurs et listes issus des données de démonstration ou disponibles.
- **Rôles :** Administrateur, Juriste/conseiller et Direction/bailleur selon les droits à valider; agent d'accueil et avocat **À CONFIRMER** pour l'accès au tableau.

## 4. Bénéficiaires — Liste

- **Zones/composants :** titre, recherche, bouton de création selon droit, tableau nom/téléphone/zone, pagination.
- **Actions :** rechercher, ouvrir une fiche, ouvrir le formulaire ou la corbeille si autorisé.
- **États :** vide : aucun bénéficiaire; erreur : recherche indisponible; succès : résultats ou message « Aucun résultat ».
- **Rôles :** Agent d'accueil et Juriste/conseiller; autres droits **À CONFIRMER**.

## 5. Bénéficiaires — Fiche

- **Zones/composants :** identité et coordonnées, actions modifier/corbeille selon rôle, sections cas et rendez-vous liés.
- **Actions :** modifier la fiche, naviguer aux cas et rendez-vous.
- **États :** vide : fiche sans cas ni rendez-vous; erreur : fiche introuvable/non autorisée; succès : fiche et historique affichés.
- **Rôles :** Agent d'accueil et Juriste/conseiller; visibilité précise **À CONFIRMER**.

## 6. Bénéficiaires — Formulaire

- **Zones/composants :** champs nom, prénom, date de naissance, téléphone, adresse, zone; actions enregistrer et annuler.
- **Actions :** créer une fiche ou modifier les champs préremplis.
- **États :** vide : création; erreur : champs invalides avec aide associée; succès : confirmation et lien vers la fiche.
- **Rôles :** Agent d'accueil et Juriste/conseiller selon la matrice **À CONFIRMER**.

## 7. Bénéficiaires — Corbeille

- **Zones/composants :** liste des fiches supprimées, date de mise en corbeille, actions restaurer/supprimer définitivement.
- **Actions :** restaurer ou demander une suppression définitive avec confirmation.
- **États :** vide : corbeille vide; erreur : action refusée; succès : retour visible après chaque action.
- **Rôles :** Agent d'accueil ou Juriste/conseiller selon les droits **À CONFIRMER**.

## 8. Cas — Liste

- **Zones/composants :** recherche, filtres type/statut/priorité, tableau référence/bénéficiaire/type/statut/priorité, bouton nouveau cas.
- **Actions :** rechercher, combiner les filtres, ouvrir un détail, créer un cas, ouvrir la corbeille.
- **États :** vide : aucun cas; erreur : filtres indisponibles; succès : résultats filtrés ou « Aucun résultat ».
- **Rôles :** Juriste/conseiller; l'Administrateur n'a pas d'accès métier explicite dans le périmètre (**À CONFIRMER**).

## 9. Cas — Détail

- **Zones/composants :** référence, bénéficiaire, type, statut, priorité, description; chronologie étapes/notes; rendez-vous et orientations associés.
- **Actions :** modifier, ajouter une note/étape, orienter, ouvrir un rendez-vous ou mettre en corbeille selon rôle.
- **États :** vide : historique absent; erreur : dossier non disponible/non autorisé; succès : détail et historique affichés.
- **Rôles :** Juriste/conseiller; Avocat partenaire en lecture seule uniquement pour les cas référés; autres accès **À CONFIRMER**.

## 10. Cas — Formulaire

- **Zones/composants :** bénéficiaire, type, statut, priorité, description; enregistrer/annuler.
- **Actions :** créer ou modifier les champs autorisés.
- **États :** vide : création avec statut initial « Nouveau »; erreur : champs requis/choix invalides; succès : confirmation et lien vers le détail.
- **Rôles :** Juriste/conseiller.

## 11. Cas — Corbeille

- **Zones/composants :** liste référence/bénéficiaire/type/date de suppression et actions de restauration/suppression définitive.
- **Actions :** restaurer ou confirmer la suppression définitive.
- **États :** vide : aucun cas supprimé; erreur : action refusée; succès : message après action.
- **Rôles :** Juriste/conseiller; accès **À CONFIRMER**.

## 12. Rendez-vous — Agenda

- **Zones/composants :** navigation temporelle, liste/calendrier simplifié, dates passées et à venir distinguées, cas lié.
- **Actions :** parcourir les dates, ouvrir un rendez-vous ou le formulaire.
- **États :** vide : aucun rendez-vous pour la période; erreur : agenda indisponible; succès : rendez-vous visibles.
- **Rôles :** Agent d'accueil et Juriste/conseiller.

## 13. Rendez-vous — Formulaire

- **Zones/composants :** cas lié, nature (rendez-vous/audience), date/heure, lieu, objet; enregistrer/annuler.
- **Actions :** créer ou modifier un événement.
- **États :** vide : formulaire vierge ou prérempli; erreur : cas/date/champs invalides; succès : événement confirmé dans l'agenda.
- **Rôles :** Agent d'accueil et Juriste/conseiller.

## 14. Rendez-vous — Corbeille

- **Zones/composants :** liste date/heure/objet/cas, actions restaurer/supprimer définitivement.
- **Actions :** restaurer ou confirmer la suppression définitive.
- **États :** vide : corbeille vide; erreur : action refusée; succès : confirmation.
- **Rôles :** Agent d'accueil et Juriste/conseiller.

## 15. Partenaires — Annuaire

- **Zones/composants :** recherche, filtre avocat/association, liste nom/type/téléphone/courriel, création.
- **Actions :** rechercher, filtrer, ouvrir/modifier un partenaire, afficher la corbeille.
- **États :** vide : annuaire vide; erreur : recherche indisponible; succès : résultats ou « Aucun résultat ».
- **Rôles :** Juriste/conseiller; autres rôles **À CONFIRMER**.

## 16. Partenaires — Formulaire

- **Zones/composants :** nom, type (avocat/association), téléphone, courriel; enregistrer/annuler.
- **Actions :** ajouter ou modifier les coordonnées.
- **États :** vide : création; erreur : champs invalides; succès : confirmation et retour à l'annuaire.
- **Rôles :** Juriste/conseiller.

## 17. Partenaires — Corbeille

- **Zones/composants :** liste des partenaires supprimés, type/date, actions restaurer/supprimer définitivement.
- **Actions :** restaurer ou confirmer la suppression définitive.
- **États :** vide : corbeille vide; erreur : action refusée; succès : confirmation.
- **Rôles :** Juriste/conseiller; accès **À CONFIRMER**.

## 18. Journal d'activité

- **Zones/composants :** filtres utilisateur/action/période; tableau auteur, action, objet concerné et date/heure.
- **Actions :** filtrer et parcourir les entrées; aucune modification des événements.
- **États :** vide : aucune activité; erreur : journal indisponible; succès : entrées filtrées affichées.
- **Rôles :** Administrateur selon le cahier actuel; autres accès **À CONFIRMER**.

## 19. Gestion des utilisateurs et rôles

- **Zones/composants :** liste nom/courriel/rôle/état, formulaire de création/modification, sélecteur de rôle et état du compte.
- **Actions :** créer, consulter et modifier un compte ou son rôle.
- **États :** vide : aucun compte; erreur : courriel/rôle invalide; succès : compte ou changement confirmé.
- **Rôles :** Administrateur.

## 20. Avocat — Cas référés

- **Zones/composants :** liste des cas référés à son partenaire, référence/type/statut et détail en lecture seule.
- **Actions :** ouvrir le détail et consulter les informations autorisées; aucun bouton de modification.
- **États :** vide : aucun cas référé; erreur : accès non autorisé; succès : cas référés seulement.
- **Rôles :** Avocat partenaire.

## Règles communes des wireframes

- Tous les libellés, messages et actions visibles sont en français.
- Les données montrées sont fictives; les écrans n'enregistrent aucune donnée.
- Les contrôles d'accès réels sont à implémenter côté serveur; le sélecteur de rôle de la future démonstration est réservé au mode développement.
- Les états d'erreur, de succès et d'absence de données sont indiqués pour chaque écran.
- Le périmètre ne comprend ni paiement, ni chatbot, ni application mobile native, ni gestion de documents.
