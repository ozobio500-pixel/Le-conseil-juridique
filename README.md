# Le Conseil Juridique

Application web de gestion de l'assistance juridique du **Centre l'Espoir**  
ONG d'utilité publique internationale — Adjouffou-Bassam, Grand-Bassam, Côte d'Ivoire

> Projet de Génie Logiciel — Institut Ivoirien de Technologie (IIT) Grand-Bassam  
> Promotion : **À CONFIRMER** · Encadrant : **À CONFIRMER**

---

## Présentation

Le Centre l'Espoir reçoit des bénéficiaires ayant des problèmes juridiques (droits,
état civil, foncier, violences, etc.). Le suivi se fait aujourd'hui sur papier, Excel
et WhatsApp, ce qui entraîne des pertes d'informations, des retards et des difficultés
de reporting.

**Problématique :** comment un système numérique peut-il améliorer l'accès au conseil
juridique et le suivi des cas des bénéficiaires ?

**Solution :** une application web qui permet d'enregistrer les bénéficiaires, de suivre
leurs cas juridiques de l'accueil à la résolution, d'être alerté des échéances et de
produire des statistiques.

---

## État d'avancement

| Phase | Séances | Contenu | État |
|-------|---------|---------|------|
| 1 — Cadrage | S1–S2 | Cahier des charges, affectation, présentation | ✅ Terminé |
| 2 — Maquette et modélisation | S3–S5 | Diagrammes UML, MCD/MLD, backlog, wireframes | 🔄 En cours |
| 3 — Développement front-end | S6–S9 | Templates Django, données simulées, toutes les pages | 🔄 En cours |
| 4 — Back-end | S10–S13 | PostgreSQL, API, sécurité complète | ⏳ À venir |
| 5 — Intégration et soutenance | S14–S15 | Tests, déploiement, soutenance | ⏳ À venir |

---

## Structure du dépôt

```
Le-conseil-juridique/
├── 01-cadrages/                    # Documents de cadrage (S1–S2)
│   ├── cahier-des-charges.docx     # Cahier des charges complet
│   ├── presentation-entreprise.docx# Fiche de présentation du Centre l'Espoir
│   ├── presentation-projet.pptx   # Présentation du projet (13 diapositives)
│   ├── affectation-projet.md       # Fiche d'affectation formelle de l'équipe
│   └── pieces-jointes/             # Pièces justificatives
│
├── 02-modelisation/                # Diagrammes et modèles de données (S3–S5)
│   ├── plantuml/                   # Sources PlantUML (.puml)
│   │   ├── use-case.puml           # Diagramme de cas d'utilisation
│   │   ├── class.puml              # Diagramme de classes
│   │   ├── activite.puml           # Diagramme d'activité
│   │   └── sequence-01 à 08.puml  # Huit diagrammes de séquence
│   ├── exports/                    # PNG générés depuis les .puml
│   │   └── *.png                   # use-case, class, activite, sequence-01..08
│   ├── wireframes/                 # Fiches texte et HTML basse fidélité (À CRÉER)
│   └── mcd.md                      # MCD/MLD en Mermaid
│
├── 03-documentation/               # Documentation complémentaire
│   ├── README.md                   # Guide d'exportation des diagrammes
│   ├── backlog.md                  # User stories et backlog produit (À CRÉER)
│   ├── backlog.csv                 # Version CSV du backlog (À CRÉER)
│   └── validation-client.md        # Checklist de validation ONG (À CRÉER)
│
├── 04-maquettes/                   # Maquettes Figma exportées en PNG
│   ├── 01-connexion.png            # Écran de connexion (fichier vide — à générer)
│   ├── 02-tableau-de-bord.png      # Tableau de bord (fichier vide — à générer)
│   ├── 03-fiche-beneficiaire.png   # Fiche bénéficiaire (fichier vide — à générer)
│   ├── 04-detail-cas.png           # Détail d'un cas (fichier vide — à générer)
│   ├── 05-statistiques.png         # Statistiques (fichier vide — à générer)
│   └── README.md                   # Charte graphique et guide des maquettes
│
├── 05-gestion-projet/              # Artefacts de gestion de projet
│   └── Backlog.xlsx                # Backlog au format tableur Excel
│
├── core/                           # Application Django principale
│   ├── migrations/                 # Migrations de base de données
│   ├── templates/                  # Gabarits HTML
│   ├── models.py                   # Modèles de données
│   ├── views.py                    # Vues (logique applicative)
│   ├── admin.py                    # Interface d'administration Django
│   └── tests.py                    # Tests automatisés
│
├── le_conseil_juridique/           # Configuration Django du projet
│   ├── settings.py                 # Paramètres Django
│   ├── urls.py                     # Routage URL
│   ├── wsgi.py                     # Point d'entrée WSGI
│   └── asgi.py                     # Point d'entrée ASGI
│
├── static/                         # Fichiers statiques (CSS, images)
├── .venv/                          # Environnement virtuel Python (non versionné)
├── manage.py                       # Commande de gestion Django
├── .gitignore                      # Fichiers exclus du versionnement
└── README.md                       # Ce fichier
```

---

## Périmètre version 1

**Inclus :**
- **Bénéficiaires** : créer, modifier, rechercher, corbeille (restaurer / supprimer définitivement)
- **Cas** : type (droits, état civil, foncier, violences, autre), statut (Nouveau, En cours, Orienté, En attente, Résolu, Clôturé), priorité (Normale, Urgente), description, corbeille
- **Rendez-vous** : agenda, rendez-vous et audiences liés à un cas, corbeille
- **Partenaires** : annuaire des avocats et associations, corbeille
- **Tableau de bord** : compteurs clés, derniers cas, prochains rendez-vous
- **Sécurité** : connexion, inscription, accès par rôle, protection CSRF, journal d'activité

**Exclus de la V1 :**
- Paiement en ligne
- Chatbot IA
- Application mobile native
- Module de gestion de documents (prévu V2)

---

## Acteurs (rôles)

| Rôle | Responsabilités principales |
|------|-----------------------------|
| **Administrateur** | Gestion des utilisateurs et des rôles |
| **Juriste / Conseiller** | Créer et suivre les cas, ajouter des notes |
| **Agent d'accueil** | Enregistrer les bénéficiaires, planifier les rendez-vous |
| **Avocat partenaire** | Consulter les cas qui lui sont référés (lecture seule) |
| **Direction / Bailleur** | Consulter les statistiques |

> Le **bénéficiaire** n'est pas un acteur : il ne se connecte pas à l'application.

---

## Installation et lancement

> **Pré-requis :** Python 3.10+

```bash
# 1. Cloner le dépôt
git clone https://github.com/ozobio500-pixel/Le-conseil-juridique.git
cd Le-conseil-juridique

# 2. Créer et activer l'environnement virtuel
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt   # À CRÉER — voir Phase 3

# 4. Appliquer les migrations (base SQLite locale)
python manage.py migrate

# 5. Lancer le serveur de développement
python manage.py runserver
```

Ouvrir ensuite [http://127.0.0.1:8000](http://127.0.0.1:8000) dans un navigateur.

---

## Technologies

| Couche | Technologie |
|--------|-------------|
| Langage | Python 3 |
| Framework web | Django |
| Base de données (dev) | SQLite (PostgreSQL en production) |
| Front-end | HTML5, CSS3, JavaScript minimal |
| Diagrammes | PlantUML |
| Maquettes | Figma |
| Versionning | Git / GitHub |

---

## Comment lire ce dépôt

1. **Comprendre le projet** → lire `01-cadrages/cahier-des-charges.docx`
2. **Voir l'équipe et le périmètre** → `01-cadrages/affectation-projet.md`
3. **Explorer les diagrammes** → `02-modelisation/exports/` (PNG) ou `02-modelisation/plantuml/` (sources)
4. **Consulter le backlog** → `03-documentation/backlog.md`
5. **Lancer l'application** → suivre les instructions ci-dessus

---

## Conventions Git

Messages de commit au format `type: description` :
- `feat` — nouvelle fonctionnalité
- `fix` — correction de bug
- `docs` — documentation
- `chore` — tâche de maintenance

---

*Dernière mise à jour : novembre 2026*
