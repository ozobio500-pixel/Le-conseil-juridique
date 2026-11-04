# Le Conseil Juridique

Application web de gestion de l'assistance juridique de l'ONG Centre l'Espoir, située à Adjouffou-Bassam, Grand-Bassam.

> Projet de Génie Logiciel, Institut Ivoirien de Technologie (IIT) Grand-Bassam
> Équipe : **À CONFIRMER** · Encadrant : **À CONFIRMER**

## Objectif et périmètre V1

L'application vise à centraliser les bénéficiaires et leurs cas juridiques, suivre les rendez-vous et les orientations, gérer l'annuaire des partenaires et afficher des indicateurs de suivi.

La V1 comprend les bénéficiaires, les cas, les rendez-vous, les partenaires, le tableau de bord et la sécurité (connexion, inscription, rôles, protection CSRF et journal d'activité). Elle exclut le paiement en ligne, le chatbot IA, l'application mobile native et la gestion de documents. Le bénéficiaire ne se connecte pas : le personnel saisit ses informations.

## Avancement observé dans le dépôt

| Phase du programme | Éléments présents | État observé |
|---|---|---|
| Cadrage — S1 à S2 | Cahier des charges, présentations et documents d'affectation/analyse | Documents présents; validation par l'ONG et certains champs restent **À CONFIRMER**. Les trois fichiers portant une extension `.docx` ou `.pptx` sont actuellement du texte brut, pas des fichiers Office valides. |
| Maquette et modélisation — S3 à S5 | Backlog Markdown/CSV, 20 fiches et wireframes HTML/CSS, MCD/MLD et sources/export PNG, checklist de validation | Livrables de travail présents; validation par l'ONG et certains choix métier restent **À CONFIRMER**. Les autres diagrammes UML existants ont encore des éléments hors périmètre à examiner. |
| Développement front-end — S6 à S9 | Code Django présent à la racine (`core/`, `le_conseil_juridique/`, `static/`, `manage.py`) et base locale `db.sqlite3` | Le code existe déjà hors du cheminement annoncé. Sa conformité au front-end avec données simulées n'est pas établie ici; le dépôt contient une base SQLite, et non une configuration PostgreSQL de phase back-end. |
| Back-end — S10 à S13 | Application Django existante | À poursuivre selon le programme après validation du front-end; PostgreSQL est prévu ultérieurement. |
| Intégration et soutenance — S14 à S15 | Aucun livrable final indiqué dans l'inventaire actuel | À réaliser. |

Ce tableau décrit la présence des fichiers, pas une validation fonctionnelle ni une validation client.

## Structure réelle

```text
Le-conseil-juridique/
├── 01-cadrages/
│   ├── affectation-projet.md
│   ├── analyse-ecarts-cdc.md
│   ├── cahier-des-charges.docx          # texte brut, extension à corriger
│   ├── presentation-entreprise.docx     # texte brut, extension à corriger
│   └── presentation-projet.pptx         # texte brut, extension à corriger
├── 02-modelisation/
│   ├── exports/                         # exports PNG, dont mcd.png et mld.png
│   ├── plantuml/                        # sources UML .puml et .mmd
│   ├── wireframes/                      # 20 fiches et wireframes HTML/CSS
│   └── mcd.md                           # MCD, MLD et différences de modélisation
├── 03-documentation/
│   ├── README.md
│   ├── backlog.md
│   ├── backlog.csv
│   └── validation-client.md
├── 04-maquettes/                        # cinq maquettes PNG et leur README
├── 05-gestion-projet/
│   └── Backlog.xlsx
├── .gitignore
├── core/                                # application Django
├── le_conseil_juridique/                # configuration Django
├── static/
├── db.sqlite3
├── manage.py
└── README.md
```

## Comment lire le dépôt

1. Lire ce README pour l'état du dépôt et le périmètre retenu.
2. Consulter `01-cadrages/cahier-des-charges.docx` pour le besoin existant; malgré son extension, ce fichier est du texte brut.
3. Lire `01-cadrages/analyse-ecarts-cdc.md` pour les différences constatées avec le périmètre V1. Le cahier des charges n'est pas modifié sans validation.
4. Consulter `01-cadrages/affectation-projet.md`; les informations inconnues y restent marquées **À CONFIRMER**.
5. Lire `02-modelisation/mcd.md`, parcourir ses sources `.puml`/`.mmd` et leurs exports, puis consulter `02-modelisation/wireframes/fiches.md` et `index.html`.
6. Consulter `03-documentation/backlog.md`, `backlog.csv` et `validation-client.md`, puis les cinq maquettes PNG dans `04-maquettes/`.
7. Le code Django est à la racine pour le moment; son existence ne signifie pas que les livrables des séances S6 à S9 sont terminés.

## Conventions de nommage et points ouverts

- Le nom d'usage utilisé dans le dépôt est **ONG Centre l'Espoir**. La dénomination juridique exacte est **À CONFIRMER**.
- Les fichiers `cahier-des-charges.docx`, `presentation-entreprise.docx` et `presentation-projet.pptx` ne sont pas des documents Office valides. Leur contenu ne doit pas être confondu avec leur format.
- Les choix techniques, les écarts du cahier et les éléments qui nécessitent une validation sont détaillés dans `01-cadrages/analyse-ecarts-cdc.md`.
- Les informations d'équipe, d'encadrement, de calendrier et de sauvegarde encore inconnues sont marquées **À CONFIRMER** dans les documents concernés.

## Conventions Git

Messages de commit en français au format `type: description` (`feat`, `docs`, `fix` ou `chore`).
