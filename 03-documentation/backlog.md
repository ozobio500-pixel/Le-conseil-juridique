# Backlog produit — Le Conseil Juridique

**Projet :** Application de gestion de l'assistance juridique de l'ONG Centre l'Espoir
**Référence :** périmètre V1 fourni; les points à valider restent **À CONFIRMER**.

## Conventions

- Une story décrit une valeur attendue par un rôle ou une tâche de livraison explicitement demandée.
- **Must** : indispensable à la V1; **Should** : important et compris dans le périmètre; **Could** : amélioration facultative sans nouvelle fonction hors périmètre.
- Les estimations sont des points d'effort relatifs (1, 2, 3, 5 ou 8).
- Le sprint cible est le sprint de livraison du résultat décrit. Toutes les interfaces listées sont réalisées en HTML/CSS avec données simulées au sprint 3; leur branchement aux données persistantes et les contrôles réels relèvent du sprint 4.
- Les données de démonstration sont fictives. Les rôles simulés servent à la démonstration; ils ne constituent pas une authentification réelle.
- La validation client, l'équipe, l'encadrant et la fréquence des sauvegardes restent **À CONFIRMER** lorsque non renseignés.

## Plan des sprints

| Sprint | Phase IIT | Résultat visé |
|---|---|---|
| 1 | Cadrage — S1–S2 | Référence de périmètre et affectation préparées pour validation. |
| 2 | Maquette et modélisation — S3–S5 | Backlog, wireframes, MCD/MLD et décision de validation client consignés. |
| 3 | Développement front-end — S6–S9 | Toutes les pages et interactions V1 démontrables avec données simulées. |
| 4 | Back-end — S10–S13 | Données persistantes, authentification, autorisations, corbeilles et journal opérationnels. |
| 5 | Intégration et soutenance — S14–S15 | Vérifications, démonstration et documentation de livraison. |

Les sprints 3 et 4 sont complémentaires : le sprint 3 livre l'interface et ses états avec des données simulées; le sprint 4 remplace ces données par les données persistantes. Le sprint cible d'une story ne signifie pas que son intégration aux deux couches doit attendre le sprint 4.

## Stories

| ID | User story | Critères d'acceptation | MoSCoW | Points | Sprint |
|---|---|---|---|---:|---:|
| US-01 | En tant qu'équipe projet, je veux disposer d'un cadrage et d'une fiche d'affectation lisibles afin de partager la référence du projet. | Les informations connues sont consignées; les noms de l'équipe, de l'encadrant et les autres éléments inconnus sont indiqués **À CONFIRMER**; le périmètre V1 et ses exclusions sont repris sans ajout. | Must | 2 | 1 |
| US-02 | En tant qu'équipe projet, je veux définir et faire relire les écrans et le modèle de données afin de préparer leur validation avant le développement. | Les 20 écrans demandés ont une fiche et un wireframe; le MCD/MLD couvre les neuf entités requises; les points de validation client et les différences UML sont consignés. | Must | 8 | 2 |
| US-03 | En tant qu'utilisateur, je veux me connecter ou accéder à l'écran d'inscription afin d'entrer dans l'application selon le parcours prévu. | Les deux écrans sont disponibles en français; erreurs de saisie et confirmation sont illustrées; aucun mot de passe réel n'est utilisé par la démonstration du sprint 3. | Must | 3 | 3 |
| US-04 | En tant que membre du personnel, je veux voir une navigation adaptée au rôle de démonstration afin de présenter les accès attendus pour chaque acteur. | Sélecteur de rôle disponible uniquement en développement; menus et accès présentés pour les cinq rôles; la simulation est explicitement distinguée d'une autorisation réelle. | Must | 3 | 3 |
| US-05 | En tant qu'agent d'accueil, je veux créer, rechercher, consulter et modifier une fiche bénéficiaire afin de tenir ses informations à jour. | Liste avec recherche, fiche et formulaire prérempli; validations de champs et retours visibles; données de démonstration cohérentes et fictives. | Must | 5 | 3 |
| US-06 | En tant qu'agent d'accueil, je veux placer un bénéficiaire dans la corbeille, le restaurer ou le supprimer définitivement afin de gérer les suppressions demandées. | Vue corbeille, actions de restauration et de suppression définitive avec confirmation; états vide, erreur et succès visibles. | Must | 3 | 3 |
| US-07 | En tant que juriste, je veux consulter, rechercher et filtrer les cas afin de retrouver rapidement les dossiers à suivre. | Liste filtrable par type, statut et priorité; valeurs conformes à la V1; résultat vide et filtres actifs présentés. | Must | 3 | 3 |
| US-08 | En tant que juriste, je veux créer, consulter et modifier un cas afin d'en suivre la situation juridique. | Formulaire et détail; types Droits, État civil, Foncier, Violences et Autre; statuts Nouveau, En cours, Orienté, En attente, Résolu et Clôturé; priorités Normale et Urgente. | Must | 5 | 3 |
| US-09 | En tant que juriste, je veux voir les étapes et notes d'un cas afin de conserver le fil de son suivi. | Le détail distingue étapes et notes datées; leurs listes ont un état vide; aucune gestion de documents n'est proposée. | Must | 3 | 3 |
| US-10 | En tant que juriste, je veux déplacer un cas vers la corbeille, le restaurer ou le supprimer définitivement afin de limiter les suppressions accidentelles. | Corbeille des cas avec confirmation des actions et retours de succès/erreur. | Must | 2 | 3 |
| US-11 | En tant qu'agent d'accueil ou juriste, je veux consulter l'agenda et créer ou modifier un rendez-vous lié à un cas afin d'organiser le suivi. | Vue agenda distinguant passé et à venir; formulaire avec cas, date/heure, lieu et objet; erreurs et confirmations présentées. | Must | 5 | 3 |
| US-12 | En tant qu'agent d'accueil ou juriste, je veux placer un rendez-vous dans la corbeille, le restaurer ou le supprimer définitivement afin de gérer l'agenda. | Corbeille et confirmations présentées; rendez-vous rattachés à un cas. | Must | 2 | 3 |
| US-13 | En tant que juriste, je veux rechercher, consulter, créer et modifier un partenaire afin de maintenir l'annuaire des avocats et associations. | Annuaire avec recherche et type de partenaire; fiche/formulaire et retours de validation; aucun autre type de partenaire n'est ajouté. | Must | 3 | 3 |
| US-14 | En tant que juriste, je veux placer un partenaire dans la corbeille, le restaurer ou le supprimer définitivement afin de tenir l'annuaire à jour. | Corbeille, confirmations et retours visibles. | Must | 2 | 3 |
| US-15 | En tant que membre autorisé du personnel, je veux voir les indicateurs du tableau de bord afin de suivre l'activité et les prochaines échéances. | Compteurs « Dossiers en cours », « Cas urgents », « Échéances dans les 7 prochains jours », derniers cas et prochains rendez-vous; valeurs calculées sur les données simulées. | Must | 3 | 3 |
| US-16 | En tant qu'administrateur, je veux consulter le journal d'activité afin de savoir qui a fait quoi et quand. | Journal en français affichant auteur, action et date/heure; états vide, erreur et succès prévus; accès présenté selon le rôle autorisé. | Must | 2 | 3 |
| US-17 | En tant qu'administrateur, je veux consulter et gérer les utilisateurs et leurs rôles afin d'organiser les accès à l'application. | Écrans de liste et formulaire; rôles Administrateur, Juriste/conseiller, Agent d'accueil, Avocat partenaire et Direction/bailleur; aucun rôle bénéficiaire. | Must | 3 | 3 |
| US-18 | En tant qu'avocat partenaire, je veux consulter en lecture seule les cas qui me sont référés afin de préparer mon intervention. | Vue avocat en lecture seule; seuls les cas référés à son compte sont présentés; cas non référé inaccessible. | Must | 3 | 3 |
| US-19 | En tant qu'utilisateur, je veux utiliser des pages adaptatives et des formulaires accessibles afin de naviguer sur téléphone, tablette ou ordinateur. | Gabarit commun, libellés de champs, erreurs associées, ordre de lecture cohérent, styles responsive et jeton CSRF prévu dans chaque formulaire Django. | Must | 5 | 3 |
| US-20 | En tant qu'équipe projet, je veux remplacer les données simulées par un schéma persistant afin de préparer l'intégration back-end. | Schéma et migrations conformes au MLD validé; PostgreSQL introduit au sprint 4 et non requis pour le sprint 3. | Must | 5 | 4 |
| US-21 | En tant qu'utilisateur du personnel, je veux une authentification réelle et des permissions côté serveur afin que les rôles protègent effectivement les données. | Mots de passe hachés; protections CSRF actives; accès contrôlé côté serveur; inscription et attribution des rôles conformes à la décision **À CONFIRMER**. | Must | 8 | 4 |
| US-22 | En tant qu'agent d'accueil, je veux que les opérations sur les bénéficiaires soient persistées afin de retrouver leurs fiches après rechargement. | Création, modification, recherche, corbeille, restauration et suppression définitive sur les données persistantes; actions autorisées selon les droits validés. | Must | 5 | 4 |
| US-23 | En tant que juriste, je veux que les cas, étapes, notes et orientations soient persistés afin de suivre les dossiers dans le temps. | CRUD des cas conforme aux droits; étapes et notes liées au cas; orientations vers un partenaire; aucun stockage de document. | Must | 8 | 4 |
| US-24 | En tant qu'agent d'accueil ou juriste, je veux que les rendez-vous et partenaires soient persistés afin de gérer l'agenda et l'annuaire. | Enregistrements liés au bon cas/partenaire; modification, corbeille, restauration et suppression définitive disponibles selon les droits. | Must | 5 | 4 |
| US-25 | En tant que membre autorisé du personnel, je veux que les compteurs et listes du tableau de bord soient calculés sur les données persistantes afin d'obtenir une vue à jour. | Compteurs définis par le périmètre; échéances limitées aux sept prochains jours; accès sans divulgation de fiches aux rôles de consultation statistique. | Must | 5 | 4 |
| US-26 | En tant qu'administrateur, je veux que les actions requises soient inscrites au journal afin de disposer d'une traçabilité. | Auteur, action et date/heure persistés pour les opérations suivies; journal visible uniquement aux rôles autorisés. | Must | 5 | 4 |
| US-27 | En tant qu'administrateur, je veux appliquer les droits d'accès aux données et aux pages afin que les agents ne consultent que les informations permises. | Contrôles serveur pour chaque rôle; avocat limité aux cas référés; direction limitée aux statistiques; accès refusé sans fuite de contenu. | Must | 8 | 4 |
| US-28 | En tant qu'équipe projet, je veux vérifier les écrans et les droits par des tests afin de livrer une démonstration cohérente. | Tests ciblés des pages principales, états et accès par rôle; anomalies bloquantes corrigées; parcours de démonstration décrit. | Must | 5 | 5 |
| US-29 | En tant qu'administrateur, je veux sauvegarder et restaurer les données afin de limiter les pertes d'information. | Fréquence **À CONFIRMER** avec l'ONG; procédure de sauvegarde et restauration testée selon la fréquence validée. | Should | 3 | 4 |
| US-30 | En tant qu'équipe projet, je veux mesurer les pages principales afin de vérifier l'exigence de performance. | Mesure des pages principales sur une connexion moyenne; objectif inférieur à 3 secondes documenté. | Should | 2 | 5 |
| US-31 | En tant qu'équipe projet, je veux préparer les consignes d'installation et de démonstration afin que l'application puisse être présentée et reprise. | Commandes de lancement vérifiées; rôles et données fictives décrits; limites de la simulation expliquées. | Must | 3 | 5 |

## Points restant à confirmer

- Dénomination juridique exacte, noms de l'équipe et de l'encadrant.
- Informations réellement nécessaires dans une fiche bénéficiaire et politique de conservation/suppression définitive.
- Matrice exacte des droits, en particulier inscription, attribution de rôle, journal et modification des bénéficiaires.
- Vocabulaire client, détails d'une orientation et champs d'agenda.
- Fréquence des sauvegardes et contraintes de validation client.
