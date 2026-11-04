# Fiche d'affectation du projet — Le Conseil Juridique

> Document de cadrage formel établi dans le cadre du cours de Génie Logiciel  
> Institut Ivoirien de Technologie (IIT) Grand-Bassam

---

## 1. Identification du projet

| Champ | Valeur |
|-------|--------|
| **Nom du projet** | Le Conseil Juridique |
| **Type** | Application web de gestion de l'assistance juridique |
| **Structure d'accueil** | ONG Centre l'Espoir |
| **Adresse** | Adjouffou-Bassam, Grand-Bassam, Côte d'Ivoire |
| **Dénomination juridique exacte** | **À CONFIRMER** |
| **Statut de la structure** | ONG d'utilité publique internationale **À CONFIRMER** |
| **Responsable de la structure** | **À CONFIRMER** |
| **Date d'affectation du projet** | **À CONFIRMER** |
| **Date de début** | **À CONFIRMER** |
| **Date de fin prévue** | **À CONFIRMER** |

---

## 2. Équipe projet

| Rôle | Nom complet | Contact |
|------|-------------|---------|
| Chef de projet / Développeur principal | **À CONFIRMER** | **À CONFIRMER** |
| Développeur | **À CONFIRMER** | **À CONFIRMER** |
| Développeur | **À CONFIRMER** | **À CONFIRMER** |

> Si l'équipe comporte d'autres membres, ajouter une ligne par personne.

---

## 3. Encadrement pédagogique

| Champ | Valeur |
|-------|--------|
| **Encadrant IIT** | **À CONFIRMER** |
| **Établissement** | Institut Ivoirien de Technologie (IIT) Grand-Bassam |
| **Cours** | Génie Logiciel |
| **Promotion / Année** | **À CONFIRMER** |
| **Niveau** | **À CONFIRMER** |

---

## 4. Contexte et problématique

L'ONG Centre l'Espoir assure le suivi de
bénéficiaires ayant des problèmes juridiques (droits, état civil, foncier,
violences, etc.). Ce suivi est actuellement réalisé sur papier, dans des
fichiers Excel et par messages WhatsApp, ce qui entraîne :

- des **pertes d'informations** (dossiers dispersés, incomplets) ;
- des **retards** (aucune alerte automatique sur les échéances) ;
- des **difficultés de reporting** (comptage manuel pour les rapports bailleurs).

**Problématique :** comment un système numérique peut-il améliorer l'accès au conseil
juridique et le suivi des cas des bénéficiaires ?

---

## 5. Objectif général

Concevoir et développer une application web qui permet à l'ONG Centre l'Espoir de :

1. centraliser les fiches des bénéficiaires et leurs cas juridiques ;
2. suivre l'avancement de chaque cas (statut, étapes, échéances) ;
3. orienter les cas vers des avocats ou partenaires et en suivre le retour ;
4. produire automatiquement des statistiques pour la direction et les bailleurs ;
5. garantir la confidentialité des données par une gestion des accès par rôle.

---

## 6. Périmètre version 1

### 6.1 Modules inclus

| Module | Description |
|--------|-------------|
| **Bénéficiaires** | Créer, modifier, rechercher, corbeille (restaurer / supprimer définitivement) |
| **Cas** | Type (droits, état civil, foncier, violences, autre), statut (Nouveau, En cours, Orienté, En attente, Résolu, Clôturé), priorité (Normale, Urgente), description, corbeille |
| **Rendez-vous** | Agenda, rendez-vous et audiences liés à un cas, modification, corbeille |
| **Partenaires** | Annuaire des avocats et associations, modification, corbeille |
| **Tableau de bord** | Compteurs clés (dossiers en cours, cas urgents, échéances à 7 jours), derniers cas, prochains rendez-vous |
| **Sécurité** | Connexion, inscription, accès par rôle, protection CSRF, journal d'activité |

### 6.2 Éléments exclus de la V1

| Élément exclu | Raison |
|---------------|--------|
| Paiement en ligne | Hors périmètre — aucun règlement d'honoraires |
| Chatbot IA | Hors périmètre |
| Application mobile native | Le site responsive reste utilisable sur mobile |
| Module de gestion de documents | Prévu pour une version ultérieure |

---

## 7. Acteurs du système

| Rôle | Responsabilités |
|------|-----------------|
| **Administrateur** | Gestion des utilisateurs et des rôles |
| **Juriste / Conseiller** | Créer et suivre les cas, ajouter des notes |
| **Agent d'accueil** | Enregistrer les bénéficiaires, planifier les rendez-vous |
| **Avocat partenaire** | Consulter les cas qui lui sont référés (lecture seule) |
| **Direction / Bailleur** | Consulter les statistiques |

> Le **bénéficiaire** n'est pas un acteur : il ne se connecte pas à l'application.
> Ses informations sont saisies par le personnel.

---

## 8. Planning des sprints

| Sprint | Phase | Séances | Livrable principal |
|--------|-------|---------|-------------------|
| Sprint 1 | Cadrage | S1–S2 | Cahier des charges, fiche d'affectation, présentation du projet |
| Sprint 2 | Maquette et modélisation | S3–S5 | Backlog, wireframes, diagrammes UML, MCD/MLD, validation client |
| Sprint 3 | Développement front-end | S6–S9 | Application Django avec données simulées, toutes les pages |
| Sprint 4 | Back-end | S10–S13 | Base PostgreSQL, authentification réelle, sécurité |
| Sprint 5 | Intégration et soutenance | S14–S15 | Tests, déploiement, guide utilisateur, soutenance |

---

## 9. Technologies retenues

| Couche | Technologie |
|--------|-------------|
| Langage | Python 3 |
| Framework web | Django |
| Base de données (dev) | SQLite → PostgreSQL (production) |
| Front-end | HTML5, CSS3, JavaScript minimal |
| Diagrammes | PlantUML |
| Maquettes | Figma |
| Versionning | Git / GitHub |
| Méthode | Scrum allégé (5 sprints) |

---

## 10. Signatures

| Rôle | Nom | Date | Signature |
|------|-----|------|-----------|
| Responsable de la structure d'accueil | **À CONFIRMER** | **À CONFIRMER** | |
| Encadrant pédagogique | **À CONFIRMER** | **À CONFIRMER** | |
| Chef de projet étudiant | **À CONFIRMER** | **À CONFIRMER** | |

---

*Document établi le : 4 novembre 2026*
