$codeMCD = @'
```mermaid
erDiagram
    UTILISATEUR {
        int id PK
        string nom
        string email
        string mot_de_passe_hash
        string role "Admin, Juriste, Accueil, Avocat, Direction"
    }
    BENEFICIAIRE {
        int id PK
        string nom
        string prenom
        date date_naissance
        string telephone
        string adresse
        string zone
    }
    CAS {
        int id PK
        string reference UK "ex: CAS-2026-001"
        string type "Droits, Etat civil, Foncier, Violences"
        string statut "Nouveau, En cours, Orienté, etc."
        string priorite "Normale, Urgente"
        text description
        datetime date_ouverture
        datetime date_cloture
        int beneficiaire_id FK
        int utilisateur_id FK "Le juriste qui suit le cas"
    }
    DOCUMENT {
        int id PK
        string nom_fichier
        string chemin_stockage
        string categorie
        int version
        datetime date_upload
        int cas_id FK
    }
    RENDEZ_VOUS {
        int id PK
        datetime date_heure
        string lieu
        string objet
        boolean rappel_envoye
        int cas_id FK
    }
    PARTENAIRE {
        int id PK
        string nom
        string type "Avocat, Association"
        string telephone
        string email
    }
    ORIENTATION {
        int id PK
        date date_orientation
        string statut "Proposé, Accepté, Terminé, Refusé"
        text commentaire_retour
        int cas_id FK
        int partenaire_id FK
    }
    JOURNAL_ACTIVITE {
        int id PK
        string action
        string entite_concernee
        datetime date_action
        string adresse_ip
        int utilisateur_id FK
    }
    BENEFICIAIRE ||--o{ CAS : "possède (1,N)"
    UTILISATEUR ||--o{ CAS : "crée / suit (1,N)"
    UTILISATEUR ||--o{ JOURNAL_ACTIVITE : "génère (1,N)"
    CAS ||--o{ DOCUMENT : "contient (1,N)"
    CAS ||--o{ RENDEZ_VOUS : "planifie (1,N)"
    CAS ||--o{ ORIENTATION : "fait l'objet (1,N)"
    PARTENAIRE ||--o{ ORIENTATION : "reçoit (1,N)"