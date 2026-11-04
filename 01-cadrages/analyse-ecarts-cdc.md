# Analyse des écarts — cahier des charges et périmètre V1

Cette analyse compare le contenu actuel de `cahier-des-charges.docx` au périmètre V1 donné pour le projet. Le cahier des charges n'a pas été modifié. Les écarts ci-dessous sont à arbitrer avant toute mise à jour de ce document.

## Écarts et points à valider

| ID | Sujet | Constat dans le cahier des charges | Écart ou décision nécessaire |
|---|---|---|---|
| E1 | Bénéficiaires | Le §5.2 prévoit créer, modifier et rechercher; plusieurs champs restent à définir. | La corbeille, la restauration et la suppression définitive ne sont pas décrites. Définir les champs avec l'ONG. |
| E2 | Cas | Le §5.3 décrit type, statut, priorité, étapes et notes; le type et la priorité sont formulés comme des exemples/propositions. | La modification et la corbeille ne sont pas décrites. Fixer la liste des types (dont « autre »), les valeurs de statut et de priorité selon le périmètre V1. |
| E3 | Rendez-vous | Le §5.4 prévoit la planification de rendez-vous, audiences et échéances; le tableau des données relie un rendez-vous à un cas. | La modification et la corbeille (restauration/suppression définitive) ne sont pas décrites. |
| E4 | Partenaires et orientations | Le §5.5 prévoit l'annuaire, l'orientation et l'enregistrement d'un retour. | La modification et la corbeille des partenaires ne sont pas décrites. Les valeurs de statut du retour ne sont pas définies par le périmètre fourni et restent à confirmer. |
| E5 | Tableau de bord | Les indicateurs requis et les listes de derniers cas et prochains rendez-vous figurent au §5.6. | Le cahier ajoute des « statistiques de synthèse utiles » sans les préciser. Confirmer qu'il s'agit uniquement des indicateurs V1. |
| E6 | Authentification et rôles | Le §5.1 décrit la connexion; la matrice du §4 propose des permissions par rôle. | L'inscription et la protection CSRF ne sont pas mentionnées explicitement. Les rôles autorisés à créer des comptes et à modifier une fiche bénéficiaire doivent être confirmés. L'administrateur dispose aussi de « paramètres », absents du périmètre fourni. |
| E7 | Confidentialité et sécurité | Le §6 cite mots de passe hachés et accès par rôle, mais ajoute HTTPS, chiffrement et anonymisation des statistiques. | La protection CSRF et la limitation de l'accès aux agents concernés doivent apparaître explicitement. HTTPS, chiffrement, anonymisation et conformité légale sont des exigences supplémentaires à confirmer. |
| E8 | Recherche et filtres | Le §5.7 cite la recherche par nom, type, statut ou date. | Le filtrage par priorité n'est pas cité explicitement; confirmer que les filtres attendus couvrent type, statut et priorité. |
| E9 | Technologies | Le §7 laisse le choix ouvert et mentionne Angular comme exemple. | Le choix fourni est Django, HTML/CSS et JavaScript minimal; PostgreSQL est prévu plus tard, pendant la phase back-end. |
| E10 | Méthode et calendrier | Le §9 laisse à choisir entre Scrum allégé et cycle itératif et décrit six phases génériques sans dates. | La méthode est Scrum allégé et le programme est organisé en cinq sprints correspondant aux phases S1–S15. Les dates restent à confirmer. |
| E11 | Exclusions | Le §3 exclut paiement, chatbot IA, application mobile native et gestion documentaire; il place aussi l'export PDF/Excel hors V1. | Les quatre exclusions V1 sont cohérentes. L'export PDF/Excel est également hors périmètre fourni, mais n'est pas cité parmi les exclusions explicites; ne pas le développer en V1. |
| E12 | Identité et informations ouvertes | Les §3, §6, §7 et §13 laissent des éléments à valider ou compléter. | Confirmer la dénomination juridique, les champs bénéficiaire, les accès, les sauvegardes, le calendrier et les autres points ouverts. |

## Référence de travail

Le périmètre V1 fourni sert de référence pour identifier ces écarts. Cette analyse ne vaut pas validation client et ne modifie ni ne remplace le cahier des charges. Les points non tranchés doivent rester **À CONFIRMER** jusqu'à validation par l'ONG.
