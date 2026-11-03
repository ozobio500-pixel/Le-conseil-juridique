# Analyse d'écarts — Cahier des charges vs Périmètre V1

> Ce document liste les différences observées entre le `cahier-des-charges.docx`
> existant et le périmètre défini pour la version 1 du projet.  
> **Aucune modification n'a été apportée au cahier des charges.**  
> Chaque écart doit être tranché avant le début du Sprint 3 (développement).

---

## Écart 1 — Module « Documents » : inclus dans le cahier, exclu du périmètre V1

| | Cahier des charges (§ 3 et § 5.4) | Périmètre V1 décidé |
|-|-----------------------------------|---------------------|
| **Position** | Module « Documents » listé comme inclus : upload, classement, versions | **Exclu** de la V1 |
| **Impact** | La table `DOCUMENT` est déjà modélisée dans le MCD (`mcd.md`) et une séquence PlantUML lui est dédiée (`sequence-05-documents.puml`) | Ces éléments resteront dans les fichiers sources mais aucune page ni route ne sera développée en V1 |
| **Décision requise** | ⚠️ **À CONFIRMER** : confirmer que le module Documents est bien exclu de la V1 et prévu en V2. |

---

## Écart 2 — Module « Export de rapports PDF/Excel » : inclus dans le cahier, non mentionné dans le périmètre V1

| | Cahier des charges (§ 5.8) | Périmètre V1 décidé |
|-|---------------------------|---------------------|
| **Position** | « Générer un rapport sur une période choisie, téléchargeable en PDF ou en Excel » | Non mentionné dans la liste des inclus V1 |
| **Impact** | Si exclu, les écrans statistiques n'auront pas de bouton d'export. Le README de `04-maquettes` mentionne un « bouton d'exportation PDF » sur l'écran statistiques. |
| **Décision requise** | ⚠️ **À CONFIRMER** : l'export PDF/Excel est-il inclus ou exclu de la V1 ? |

---

## Écart 3 — Nom de l'ONG : trois variantes dans le dépôt

| Fichier | Nom utilisé |
|---------|-------------|
| `cahier-des-charges.docx` | INTERNATION CENTRE L'ESPOIR ADJOUFFOU-BASSAM |
| `presentation-entreprise.docx` | Centre l'Espoir |
| `04-maquettes/README.md` | Centre l'Espoir |
| `README.md` (nouveau) | Centre l'Espoir |
| `affectation-projet.md` (nouveau) | Centre l'Espoir |

**Nom retenu dans ce projet :** **Centre l'Espoir**  
(forme courte, cohérente avec la présentation officielle de l'entreprise)

> Note : « INTERNATION » dans le cahier des charges semble être une faute de frappe
> pour « INTERNATIONAL ». Le nom complet officiel est :
> **À CONFIRMER** avec l'ONG.

---

## Écart 4 — Module « Statistiques et rapports » : présent dans le cahier, absent de la liste des inclus V1

| | Cahier des charges (§ 5.7) | Périmètre V1 décidé |
|-|---------------------------|---------------------|
| **Position** | « Afficher les chiffres clés : nombre de cas par type, par zone, par statut, taux de résolution » | Le tableau de bord (inclus) couvre les compteurs de base. Les graphiques avancés et les rapports détaillés ne sont pas explicitement mentionnés. |
| **Décision requise** | ⚠️ **À CONFIRMER** : les graphiques statistiques (par type, zone, statut) font-ils partie du tableau de bord V1, ou constituent-ils un module séparé ? |

---

## Écart 5 — Matrice des droits d'accès : incohérence « Administrateur »

| Fonction | Cahier des charges | Périmètre V1 |
|----------|--------------------|--------------|
| Voir les statistiques et les rapports | Admin : **Oui** | Non mentionné pour l'Admin |
| Créer ou modifier un bénéficiaire | Admin : **Non** | Non mentionné |

La matrice du cahier des charges (§ 4) donne à l'Administrateur l'accès aux
statistiques mais pas à la création de bénéficiaires. Le périmètre V1 ne précise
pas les droits de l'Administrateur sur les modules autres que « utilisateurs/rôles ».

> **À CONFIRMER** : l'Administrateur a-t-il accès à l'ensemble de l'application
> ou seulement à la gestion des utilisateurs et au journal d'activité ?

---

## Écart 6 — Rappels d'échéances : mentionnés dans le cahier, non spécifiés en V1

| | Cahier des charges (§ 5.5) | Périmètre V1 décidé |
|-|---------------------------|---------------------|
| **Position** | « L'application envoie un rappel avant chaque date pour éviter les oublis [délai de rappel à définir] » | Le tableau de bord affiche les « échéances dans les 7 prochains jours » mais aucun envoi d'e-mail/SMS n'est mentionné. |
| **Décision requise** | ⚠️ **À CONFIRMER** : les rappels automatiques (e-mail ou notification) sont-ils inclus en V1 ou seulement l'affichage des échéances dans le tableau de bord ? |

---

## Récapitulatif des points à confirmer

| # | Point à confirmer | Impact si non tranché |
|---|-------------------|-----------------------|
| E1 | Module Documents : exclu V1 → confirmé V2 ? | MCD à alléger, séquence à laisser inactive |
| E2 | Export PDF/Excel : inclus ou exclu V1 ? | Écrans statistiques avec ou sans bouton export |
| E3 | Nom complet officiel de l'ONG | Homogénéisation de tous les documents |
| E4 | Graphiques statistiques dans le tableau de bord V1 ? | Portée de l'écran « statistiques » |
| E5 | Droits d'accès complets de l'Administrateur | Filtrage des menus et des vues |
| E6 | Rappels automatiques (e-mail/SMS) en V1 ? | Nécessite une configuration e-mail Django |

---

*Analyse réalisée en novembre 2026 — à valider avant le Sprint 3*
