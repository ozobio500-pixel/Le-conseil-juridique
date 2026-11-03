# Backlog produit — Le Conseil Juridique
## ONG INTERNATIONAL CENTRE L'ESPOIR ADJOUFFOU-BASSAM

> Format : « En tant que [rôle], je veux [action] afin de [bénéfice] »  
> Priorité MoSCoW : **M** = Must Have · **S** = Should Have · **C** = Could Have · **W** = Won't Have (V1)  
> Estimation en points de complexité (1 = trivial, 2 = simple, 3 = moyen, 5 = complexe, 8 = très complexe)  
> Sprints : 1 = Cadrage · 2 = Modélisation · 3 = Front-end · 4 = Back-end · 5 = Intégration

---

## Module 0 — Authentification et sécurité

| ID | User Story | Critères d'acceptation | MoSCoW | Points | Sprint |
|----|-----------|------------------------|--------|--------|--------|
| US-01 | En tant qu'**utilisateur**, je veux me connecter avec mon adresse e-mail et mon mot de passe afin d'accéder à l'application selon mon rôle. | - Formulaire avec champ e-mail + mot de passe<br>- Redirection vers le tableau de bord après connexion<br>- Message d'erreur si identifiants incorrects<br>- Protection CSRF active | M | 2 | 3 |
| US-02 | En tant qu'**administrateur**, je veux créer un compte utilisateur et lui attribuer un rôle afin de contrôler les accès. | - Formulaire : nom, prénom, e-mail, rôle, mot de passe temporaire<br>- Rôles disponibles : Admin, Juriste, Accueil, Avocat, Direction<br>- Le nouveau compte est immédiatement actif | M | 3 | 3 |
| US-03 | En tant qu'**administrateur**, je veux modifier ou désactiver un compte utilisateur afin de maintenir l'annuaire à jour. | - Pouvoir changer le rôle ou désactiver le compte<br>- Un compte désactivé ne peut plus se connecter<br>- Confirmation avant désactivation | M | 2 | 3 |
| US-04 | En tant qu'**utilisateur**, je veux me déconnecter afin de protéger les données si je quitte mon poste. | - Bouton de déconnexion accessible depuis toutes les pages<br>- Redirection vers l'écran de connexion<br>- Session invalidée côté serveur | M | 1 | 3 |
| US-05 | En tant qu'**administrateur**, je veux consulter le journal d'activité afin de savoir qui a fait quoi et quand. | - Liste chronologique : utilisateur, action, entité concernée, date/heure, adresse IP<br>- Filtrable par utilisateur et par période<br>- Non modifiable | M | 3 | 3 |

---

## Module 1 — Bénéficiaires

| ID | User Story | Critères d'acceptation | MoSCoW | Points | Sprint |
|----|-----------|------------------------|--------|--------|--------|
| US-06 | En tant qu'**agent d'accueil**, je veux enregistrer un nouveau bénéficiaire afin d'ouvrir son dossier dans le système. | - Formulaire : nom, prénom, date de naissance, téléphone, adresse, zone géographique<br>- Champs obligatoires signalés<br>- Message de confirmation à la création | M | 2 | 3 |
| US-07 | En tant qu'**agent d'accueil** ou **juriste**, je veux rechercher un bénéficiaire par nom ou téléphone afin de retrouver rapidement son dossier. | - Barre de recherche sur la liste des bénéficiaires<br>- Résultats en temps réel ou après validation<br>- Affiche nom, prénom, téléphone, nombre de cas | M | 2 | 3 |
| US-08 | En tant que **juriste**, je veux consulter la fiche complète d'un bénéficiaire afin de voir son identité et l'historique de ses cas. | - Fiche : identité complète + liste de tous ses cas (statut, type, date)<br>- Lien vers chaque cas depuis la fiche | M | 2 | 3 |
| US-09 | En tant qu'**agent d'accueil** ou **juriste**, je veux modifier la fiche d'un bénéficiaire afin de corriger ou compléter ses informations. | - Formulaire pré-rempli avec les données actuelles<br>- Seuls les champs modifiés sont mis à jour<br>- Journalisation de la modification | M | 2 | 3 |
| US-10 | En tant que **juriste**, je veux envoyer un bénéficiaire à la corbeille afin de le retirer de la liste active sans le supprimer définitivement. | - Bouton « Mettre à la corbeille »<br>- Le bénéficiaire n'apparaît plus dans la liste principale<br>- Confirmation avant mise à la corbeille | M | 2 | 3 |
| US-11 | En tant qu'**administrateur**, je veux restaurer ou supprimer définitivement un bénéficiaire en corbeille afin de gérer les archives. | - Liste de la corbeille séparée<br>- Boutons « Restaurer » et « Supprimer définitivement »<br>- Confirmation avec avertissement avant suppression définitive | M | 2 | 3 |

---

## Module 2 — Cas juridiques

| ID | User Story | Critères d'acceptation | MoSCoW | Points | Sprint |
|----|-----------|------------------------|--------|--------|--------|
| US-12 | En tant que **juriste**, je veux créer un cas juridique pour un bénéficiaire afin de démarrer le suivi de son problème. | - Formulaire : bénéficiaire (sélection), type, priorité, description, statut initial = Nouveau<br>- Référence générée automatiquement (ex : CAS-2026-001)<br>- Journalisation de la création | M | 3 | 3 |
| US-13 | En tant que **juriste**, je veux consulter le détail d'un cas afin de voir toutes les informations et l'historique des étapes. | - Fiche : référence, type, statut, priorité, description, bénéficiaire lié, juriste responsable, date d'ouverture, étapes, notes, rendez-vous liés, orientation | M | 3 | 3 |
| US-14 | En tant que **juriste**, je veux modifier le statut et les informations d'un cas afin de refléter son avancement réel. | - Statuts disponibles : Nouveau → En cours → Orienté → En attente → Résolu → Clôturé<br>- Chaque changement de statut est journalisé avec la date | M | 2 | 3 |
| US-15 | En tant que **juriste**, je veux ajouter une note à un cas afin de consigner mes observations ou les échanges avec le bénéficiaire. | - Zone de texte libre<br>- Chaque note affiche l'auteur et la date/heure<br>- Notes non modifiables après enregistrement | M | 2 | 3 |
| US-16 | En tant que **juriste**, je veux filtrer la liste des cas par type, statut et priorité afin de me concentrer sur les dossiers pertinents. | - Filtres : type (Droits / État civil / Foncier / Violences / Autre), statut, priorité<br>- Les filtres sont combinables<br>- Réinitialisation possible | M | 2 | 3 |
| US-17 | En tant que **juriste**, je veux marquer un cas comme urgent afin d'alerter l'équipe sur les dossiers prioritaires. | - Priorité « Urgente » visible en badge coloré dans la liste<br>- Compteur « Cas urgents » sur le tableau de bord | M | 1 | 3 |
| US-18 | En tant que **juriste**, je veux envoyer un cas à la corbeille afin de le retirer de la liste active. | - Bouton « Mettre à la corbeille »<br>- Confirmation avant action<br>- Le cas n'apparaît plus dans la liste principale | M | 2 | 3 |
| US-19 | En tant qu'**administrateur**, je veux restaurer ou supprimer définitivement un cas en corbeille. | - Liste corbeille des cas<br>- Restauration ou suppression définitive avec confirmation | M | 2 | 3 |

---

## Module 3 — Rendez-vous et agenda

| ID | User Story | Critères d'acceptation | MoSCoW | Points | Sprint |
|----|-----------|------------------------|--------|--------|--------|
| US-20 | En tant que **juriste** ou **agent d'accueil**, je veux planifier un rendez-vous lié à un cas afin d'organiser les consultations et audiences. | - Formulaire : cas lié, date, heure, lieu, objet (consultation / audience / autre)<br>- Le rendez-vous apparaît dans l'agenda et sur la fiche du cas | M | 3 | 3 |
| US-21 | En tant que **juriste**, je veux voir l'agenda des prochains rendez-vous afin d'organiser ma semaine. | - Vue liste ou calendrier des rendez-vous à venir<br>- Tri par date croissante<br>- Filtrable par cas ou par type | M | 3 | 3 |
| US-22 | En tant que **juriste** ou **agent d'accueil**, je veux modifier un rendez-vous afin de corriger l'heure, le lieu ou l'objet. | - Formulaire pré-rempli<br>- Journalisation de la modification | M | 2 | 3 |
| US-23 | En tant que **juriste**, je veux envoyer un rendez-vous à la corbeille afin de l'annuler sans le supprimer définitivement. | - Bouton « Mettre à la corbeille » avec confirmation<br>- Restauration ou suppression définitive disponible | M | 2 | 3 |
| US-24 | En tant qu'**utilisateur**, je veux voir les rendez-vous des 7 prochains jours sur le tableau de bord afin d'anticiper les échéances. | - Compteur et liste des prochains rendez-vous sur la page d'accueil<br>- Lien direct vers le cas concerné | M | 2 | 3 |

---

## Module 4 — Partenaires

| ID | User Story | Critères d'acceptation | MoSCoW | Points | Sprint |
|----|-----------|------------------------|--------|--------|--------|
| US-25 | En tant que **juriste**, je veux consulter l'annuaire des partenaires (avocats et associations) afin d'identifier vers qui orienter un cas. | - Liste : nom, type (Avocat / Association), téléphone, e-mail, spécialité<br>- Recherche par nom ou type | M | 2 | 3 |
| US-26 | En tant qu'**administrateur** ou **juriste**, je veux ajouter un partenaire à l'annuaire afin de mettre à jour la liste des ressources disponibles. | - Formulaire : nom, type, téléphone, e-mail, spécialité, commentaire<br>- Message de confirmation | M | 2 | 3 |
| US-27 | En tant qu'**administrateur** ou **juriste**, je veux modifier la fiche d'un partenaire afin de maintenir ses coordonnées à jour. | - Formulaire pré-rempli<br>- Journalisation de la modification | M | 1 | 3 |
| US-28 | En tant que **juriste**, je veux orienter un cas vers un partenaire afin de lui confier le dossier et suivre la réponse. | - Formulaire d'orientation : cas, partenaire, date, commentaire<br>- Statut de l'orientation : Proposé / Accepté / En cours / Terminé / Refusé<br>- Visible sur la fiche du cas | M | 3 | 3 |
| US-29 | En tant qu'**administrateur**, je veux mettre à la corbeille et supprimer un partenaire afin de retirer les contacts obsolètes. | - Corbeille partenaires avec restauration / suppression définitive | M | 2 | 3 |

---

## Module 5 — Tableau de bord et statistiques

| ID | User Story | Critères d'acceptation | MoSCoW | Points | Sprint |
|----|-----------|------------------------|--------|--------|--------|
| US-30 | En tant que **juriste** ou **agent d'accueil**, je veux voir un tableau de bord avec les indicateurs clés afin d'avoir une vue d'ensemble immédiate. | - Compteurs : dossiers en cours, cas urgents, échéances dans les 7 jours<br>- Liste des 5 derniers cas<br>- Liste des 5 prochains rendez-vous | M | 3 | 3 |
| US-31 | En tant que **direction** ou **bailleur**, je veux voir les statistiques des cas par type, zone et statut afin de produire des rapports d'activité. | - Graphiques : répartition par type, par statut, par zone<br>- Taux de résolution (cas Résolus / total)<br>- Filtrable par période | M | 5 | 3 |
| US-32 | En tant que **direction** ou **bailleur**, je veux exporter un rapport en PDF ou Excel afin de le partager avec les bailleurs de fonds. | - Bouton « Exporter PDF » et « Exporter Excel » sur l'écran statistiques<br>- Le rapport couvre la période sélectionnée<br>- Généré en moins de 10 secondes | S | 5 | 4 |

---

## Module 6 — Vue Avocat partenaire (lecture seule)

| ID | User Story | Critères d'acceptation | MoSCoW | Points | Sprint |
|----|-----------|------------------------|--------|--------|--------|
| US-33 | En tant qu'**avocat partenaire**, je veux consulter uniquement les cas qui me sont référés afin de préparer mon intervention. | - Liste filtrée : seuls les cas orientés vers cet avocat sont visibles<br>- Lecture seule : aucun bouton de modification<br>- Accès aux informations du cas et aux notes | M | 3 | 3 |
| US-34 | En tant qu'**avocat partenaire**, je veux voir le détail d'un cas qui m'est référé afin d'en comprendre le contexte. | - Fiche du cas (sans les boutons d'action)<br>- Statut de l'orientation visible | M | 2 | 3 |

---

## Module 7 — Gestion des utilisateurs (Admin)

| ID | User Story | Critères d'acceptation | MoSCoW | Points | Sprint |
|----|-----------|------------------------|--------|--------|--------|
| US-35 | En tant qu'**administrateur**, je veux voir la liste de tous les utilisateurs afin de gérer les accès. | - Tableau : nom, prénom, e-mail, rôle, statut (actif / inactif)<br>- Recherche par nom ou rôle | M | 2 | 3 |
| US-36 | En tant qu'**administrateur**, je veux changer le rôle d'un utilisateur afin d'adapter ses droits à son poste. | - Sélecteur de rôle modifiable depuis la liste ou la fiche<br>- Journalisation du changement | M | 2 | 3 |

---

## Hors périmètre V1 (Won't Have)

| ID | User Story | Raison |
|----|-----------|--------|
| US-W1 | En tant que bénéficiaire, je veux suivre mon dossier en ligne. | Le bénéficiaire n'est pas un acteur du système |
| US-W2 | En tant que juriste, je veux uploader des documents sur un cas. | Module Documents exclu de la V1 |
| US-W3 | En tant qu'utilisateur, je veux payer des honoraires en ligne. | Exclu du périmètre |
| US-W4 | En tant qu'utilisateur, je veux interroger un chatbot juridique. | Exclu du périmètre |
| US-W5 | En tant que juriste, je veux recevoir un e-mail de rappel automatique. | Rappels e-mail repoussés en V2 |

---

## Récapitulatif par sprint

| Sprint | Stories | Points totaux | Livrable |
|--------|---------|---------------|---------|
| Sprint 1 — Cadrage | — | — | Cahier des charges, fiche d'affectation |
| Sprint 2 — Modélisation | — | — | Diagrammes, MCD/MLD, backlog, wireframes |
| Sprint 3 — Front-end | US-01 à US-31, US-33 à US-36 | **60** | Application Django avec données simulées |
| Sprint 4 — Back-end | US-32 (export) + intégration BD | **5+** | Base PostgreSQL, authentification réelle |
| Sprint 5 — Intégration | Tests, déploiement | — | Application finale, guide utilisateur |
