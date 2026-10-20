# Documentation du projet

Cette section accueillera les documents complémentaires :

- **Guide technique** : installation, organisation du code et déploiement.
- **Manuel utilisateur** : mode d'emploi par rôle (administrateur, juriste,
  agent d'accueil, avocat partenaire et direction).

Ces documents sont prévus pendant les phases de développement et de déploiement.

## Exporter les diagrammes en PNG

### Diagrammes draw.io

Pour chacun des fichiers `use-case.drawio`, `class.drawio` et `activite.drawio` :

1. Ouvrir le fichier dans l'application de bureau diagrams.net ou sur
   [app.diagrams.net](https://app.diagrams.net).
2. Choisir **Fichier > Exporter en > PNG**.
3. Régler la résolution à 300 DPI, le fond en blanc et la bordure à 10 px.
4. Enregistrer le PNG correspondant dans `02-modelisation/exports/` sous les
   noms `use-case.png`, `class.png` et `activite.png`.

### Diagrammes PlantUML

Les fichiers `.puml` se trouvent dans `02-modelisation/plantuml/`.

**Avec VS Code :**

1. Installer l'extension PlantUML (`jebbs.plantuml`).
2. Ouvrir un fichier `.puml`.
3. Lancer **PlantUML: Export Current Diagram** depuis la palette de commandes
   (`Ctrl+Shift+P`), choisir PNG et enregistrer dans `../exports/`.

**Avec la ligne de commande**, depuis le dossier PlantUML :

```sh
plantuml -tpng -o ../exports/ *.puml
```

Nommer les exports `sequence-01.png` à `sequence-08.png`.

Les PNG doivent être générés à partir des diagrammes sources ; des fichiers
PNG vides ne constituent pas des exports valides.

## Checklist des livrables

| # | Élément | Fichier(s) | État |
| --- | --- | --- | --- |
| 1 | README du projet | `README.md` | Créé |
| 2 | Cahier des charges | `01-cadrages/cahier-des-charges.docx` | Créé, à valider |
| 3 | Présentation de l'entreprise | `01-cadrages/presentation-entreprise.docx` | Créée, à valider |
| 4 | Présentation du projet | `01-cadrages/presentation-projet.pptx` | Créée (13 diapositives), à valider |
| 5 | Diagramme de cas d'utilisation | `02-modelisation/drawio/use-case.drawio` | Créé |
| 6 | Diagramme de classes | `02-modelisation/drawio/class.drawio` | Créé |
| 7 | Diagramme d'activité | `02-modelisation/drawio/activite.drawio` | Créé |
| 8–15 | Huit diagrammes de séquence | `02-modelisation/plantuml/*.puml` | Créés |
| 16 | Dépôt Git initialisé et publié | Dépôt distant à choisir | À faire |
| — | Exports des diagrammes | `02-modelisation/exports/*.png` | À générer localement |
