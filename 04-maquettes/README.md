# 🎨 Maquettes et Wireframes — Le Conseil Juridique

Ce dossier contient les **maquettes fonctionnelles** (wireframes) de l'application, réalisées sur **Figma**. 
Elles servent de référence visuelle pour le développement front-end (Sprint 3, semaines S6 à S9).

## 🎯 Objectifs des maquettes

1. **Valider l'ergonomie** : S'assurer que l'interface est simple, car le personnel de l'ONG n'est pas forcément à l'aise avec l'informatique (cf. Besoins non-fonctionnels du cahier des charges).
2. **Respecter la charte graphique** du Centre l'Espoir.
3. **Préparer le Sprint 3** : Ces écrans seront codés en HTML/CSS et intégrés au back-end lors du Sprint 4.

## 🎨 Charte graphique (Centre l'Espoir)

Pour rester cohérent avec l'identité visuelle de l'ONG, les couleurs suivantes ont été appliquées :
- 🟤 **Bordeaux** : Barre de navigation, boutons d'action principaux (couleur institutionnelle).
- 🌸 **Rose clair** : Badges de statut (ex: "En cours"), alertes secondaires.
- ⚪ **Beige / Blanc cassé** : Fond des pages (pour un confort visuel et une lecture facile).
- 🕊️ **Logo** : L'arc-en-ciel et la colombe du Centre l'Espoir sont intégrés sur l'écran de connexion et le menu.

## 📱 Les 5 écrans réalisés

| Fichier | Description | Acteur ciblé |
| :--- | :--- | :--- |
| `01-connexion.png` | Écran d'authentification sécurisé (email + mot de passe). | Tous |
| `02-dashboard.png` | Tableau de bord avec les indicateurs clés (dossiers en cours, échéances, urgences) et les derniers bénéficiaires. | Juriste / Accueil |
| `03-fiche-beneficiaire.png` | Fiche centralisée d'une personne avec ses coordonnées et l'historique de tous ses cas. | Juriste / Accueil |
| `04-detail-cas.png` | Cœur de l'application : suivi du dossier, barre de progression du statut, ajout de notes, documents et bouton d'orientation. | Juriste |
| `05-statistiques.png` | Vue macroscopique (graphiques par type et par zone) avec bouton d'exportation PDF pour les bailleurs. | Direction / Bailleur |

## 🚀 Comment visualiser les maquettes ?

Il suffit d'ouvrir les fichiers `.png` présents dans ce dossier. 
*(Optionnel : ajouter le lien vers le projet Figma si vous le rendez public).*

## 🔄 Prochaines étapes

- [ ] **Validation client** : Faire une démonstration de ces maquettes au responsable du Centre l'Espoir pour valider les écrans (Phase 2 - S5).
- [ ] **MCD / MLD** : Finaliser le modèle de base de données.
- [ ] **Développement** : Utiliser ces écrans comme base pour le Sprint 3.