# Analyse d'écarts — Cahier des charges vs Périmètre V1

> Ce document liste les différences observées entre le `cahier-des-charges.docx`
> et le périmètre initial décrit dans le brief. Les réponses sont extraites du CDC.  
> **Aucune modification n'a été apportée au cahier des charges.**

---

## Tableau récapitulatif

| # | Écart | Statut | Décision |
|---|-------|--------|----------|
| E1 | Module Documents | ⚠️ **À CONFIRMER** | CDC § 5.4 : inclus — Brief : exclu |
| E2 | Export PDF/Excel | ✅ Tranché | Inclus en V1 (CDC § 5.8) |
| E3 | Nom officiel de l'ONG | ✅ Tranché | ONG INTERNATIONAL CENTRE L'ESPOIR ADJOUFFOU-BASSAM |
| E4 | Graphiques statistiques | ✅ Tranché | Inclus en V1 (CDC § 5.7) |
| E5 | Droits Administrateur | ✅ Tranché | Selon matrice CDC § 4 |
| E6 | Rappels automatiques | ✅ Tranché | Inclus en V1 (CDC § 5.5), délai à définir |

---

## Écart 1 — Module « Documents » ⚠️ SEUL POINT EN SUSPENS

| | CDC (§ 3 et § 5.4) | Brief initial |
|-|--------------------|---------------|
| **Position** | **Inclus** : upload, classement, versions | **Exclu** : « Pas de module de gestion de documents (non prévu en V1) » |

La table `DOCUMENT` est modélisée dans le MCD et la séquence `sequence-05-documents.puml` lui est dédiée.

> **⚠️ À CONFIRMER** : le module Documents est-il inclus ou exclu de la V1 ?  
> - **Si inclus** : développer les pages upload/classement et activer la séquence 05.  
> - **Si exclu** : désactiver la séquence 05, garder la table dans le MCD (pour V2) mais ne pas créer de pages.

---

## Écart 2 — Export de rapports PDF/Excel ✅ Résolu

**Décision :** inclus en V1.  
CDC § 5.8 : « Générer un rapport sur une période choisie, téléchargeable en PDF ou en Excel, pour la direction et les bailleurs. »  
Un bouton d'export sera présent sur l'écran statistiques.

---

## Écart 3 — Nom officiel de l'ONG ✅ Résolu

**Nom officiel retenu dans tous les documents :**

> **ONG INTERNATIONAL CENTRE L'ESPOIR ADJOUFFOU-BASSAM**

Forme courte tolérée dans les textes courants : « Centre l'Espoir ».  
Corrigé dans : `README.md`, `affectation-projet.md`.  
Reste à corriger si souhaité : `01-cadrages/presentation-entreprise.docx`, `04-maquettes/README.md`.

---

## Écart 4 — Graphiques statistiques dans le tableau de bord ✅ Résolu

**Décision :** inclus en V1.  
CDC § 5.7 : « Afficher les chiffres clés : nombre de cas par type, par zone géographique, par statut, et taux de résolution. »  
Ces indicateurs feront partie du tableau de bord / écran statistiques.

---

## Écart 5 — Droits d'accès de l'Administrateur ✅ Résolu

Matrice extraite du CDC § 4 :

| Fonction | Admin | Juriste | Accueil | Avocat | Direction |
|----------|-------|---------|---------|--------|-----------|
| Gérer les utilisateurs et les rôles | ✅ | ❌ | ❌ | ❌ | ❌ |
| Créer ou modifier un bénéficiaire | ❌ | ✅ | ✅ | ❌ | ❌ |
| Créer ou modifier un cas | ❌ | ✅ | ❌ | ❌ | ❌ |
| Consulter un cas | ❌ | ✅ | ❌ | Cas référés seulement | ❌ |
| Gérer les rendez-vous | ❌ | ✅ | ✅ | ❌ | ❌ |
| Ajouter des documents | ❌ | ✅ | ✅ | ❌ | ❌ |
| Orienter un cas vers un partenaire | ❌ | ✅ | ❌ | ❌ | ❌ |
| Voir les statistiques et les rapports | ✅ | ✅ | ❌ | ❌ | ✅ |
| Consulter le journal d'activité | ✅ | ❌ | ❌ | ❌ | ❌ |

**Conclusion :** l'Administrateur accède uniquement à la gestion des utilisateurs, aux statistiques et au journal d'activité. Il n'a pas accès aux fiches bénéficiaires ni aux cas.

---

## Écart 6 — Rappels automatiques d'échéances ✅ Résolu

**Décision :** inclus en V1 (affichage dans le tableau de bord).  
CDC § 5.5 : « L'application envoie un rappel avant chaque date pour éviter les oublis [délai de rappel à définir]. »  

**Périmètre précis pour la V1 :**
- Le tableau de bord affiche les échéances dans les 7 prochains jours.
- Les rappels par e-mail/SMS nécessitent une configuration serveur mail : à confirmer si ce niveau est attendu en V1 ou si l'affichage visuel suffit.

> **À PRÉCISER (facultatif) :** les rappels sont-ils uniquement visuels (tableau de bord) ou faut-il aussi envoyer des e-mails ?

---

*Analyse mise à jour : novembre 2026*
