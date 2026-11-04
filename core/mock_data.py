# core/mock_data.py

UTILISATEURS = [
    {"id": 1, "nom": "Aka", "prenom": "Salomé", "role": "Agent d'accueil", "email": "salome@ong.ci"},
    {"id": 2, "nom": "Diallo", "prenom": "Aminata", "role": "Juriste", "email": "aminata@ong.ci"},
    {"id": 3, "nom": "Kouassi", "prenom": "Jean", "role": "Avocat", "email": "jean@cabinet.ci"},
    {"id": 4, "nom": "Admin", "prenom": "System", "role": "Administrateur", "email": "admin@ong.ci"},
    {"id": 5, "nom": "Bailleur", "prenom": "Fonds", "role": "Direction", "email": "direction@bailleur.org"},
]

BENEFICIAIRES = [
    {"id": 1, "nom": "Koné", "prenom": "Awa", "telephone": "+225 07 00 00 14 82", "zone": "Bassam", "date": "17/06/2026", "supprime": False},
    {"id": 2, "nom": "N'Guessan", "prenom": "Kouamé", "telephone": "+225 05 00 00 21 63", "zone": "Abobo", "date": "17/06/2026", "supprime": False},
    {"id": 3, "nom": "Bamba", "prenom": "Fatou", "telephone": "+225 07 00 00 32 11", "zone": "Yopougon", "date": "16/06/2026", "supprime": False},
    {"id": 4, "nom": "Koffi", "prenom": "Yao", "telephone": "+225 01 00 00 45 08", "zone": "Bassam", "date": "16/06/2026", "supprime": False},
    {"id": 5, "nom": "Assi", "prenom": "Adjoua", "telephone": "+225 05 00 00 67 24", "zone": "Port-Bouët", "date": "15/06/2026", "supprime": False},
    {"id": 6, "nom": "Coulibaly", "prenom": "Mariam", "telephone": "+225 07 00 00 19 36", "zone": "Adjouffou", "date": "15/06/2026", "supprime": True},
]

CAS = [
    {"id": 1, "reference": "CAS-2026-001", "beneficiaire_id": 1, "type": "Foncier", "priorite": "Urgente", "statut": "En cours", "description": "Problème de médiation foncière.", "supprime": False},
    {"id": 2, "reference": "CAS-2026-083", "beneficiaire_id": 2, "type": "État civil", "priorite": "Normale", "statut": "Nouveau", "description": "Demande de certificat de nationalité.", "supprime": False},
    {"id": 3, "reference": "CAS-2026-076", "beneficiaire_id": 3, "type": "Droits", "priorite": "Normale", "statut": "En cours", "description": "Conflit de voisinage.", "supprime": False},
    {"id": 4, "reference": "CAS-2026-071", "beneficiaire_id": 4, "type": "Foncier", "priorite": "Normale", "statut": "Orienté", "description": "Litige de terrain.", "supprime": False},
    {"id": 5, "reference": "CAS-2026-068", "beneficiaire_id": 5, "type": "Violences", "priorite": "Urgente", "statut": "En attente", "description": "Violences conjugales.", "supprime": False},
    {"id": 6, "reference": "CAS-2026-059", "beneficiaire_id": 6, "type": "Autre", "priorite": "Normale", "statut": "Résolu", "description": "Problème administratif.", "supprime": True},
]

RENDEZ_VOUS = [
    {"id": 1, "cas_id": 1, "date": "18/06/2026 10:30", "objet": "Médiation foncière", "lieu": "Bureau 2", "type": "Consultation", "supprime": False},
    {"id": 2, "cas_id": 2, "date": "19/06/2026 09:00", "objet": "Entretien de suivi", "lieu": "Centre", "type": "Consultation", "supprime": False},
    {"id": 3, "cas_id": 4, "date": "19/06/2026 14:00", "objet": "Point avec avocat", "lieu": "Cabinet", "type": "Audience", "supprime": False},
    {"id": 4, "cas_id": 1, "date": "22/06/2026 09:00", "objet": "Médiation foncière", "lieu": "Centre", "type": "Échéance", "supprime": False},
    {"id": 5, "cas_id": 3, "date": "10/06/2026 11:00", "objet": "Entretien", "lieu": "Centre", "type": "Consultation", "supprime": True},
]

PARTENAIRES = [
    {"id": 1, "nom": "Me Jean Kouassi", "type": "Avocat", "telephone": "+225 07 00 00 82 15", "email": "j.kouassi@cabinet.ci", "supprime": False},
    {"id": 2, "nom": "Association Femmes & Droits", "type": "Association", "telephone": "+225 05 00 00 48 12", "email": "contact@femmes-droits.ci", "supprime": False},
    {"id": 3, "nom": "Me Awa Soro", "type": "Avocat", "telephone": "+225 01 00 00 67 41", "email": "awa.soro@cabinet.ci", "supprime": False},
    {"id": 4, "nom": "Institution X", "type": "Institution", "telephone": "+225 27 00 00 00 00", "email": "info@institution.ci", "supprime": True},
]

JOURNAL = [
    {"id": 1, "utilisateur": "Salomé", "action": "Connexion réussie", "date": "04/11/2026 18:53"},
    {"id": 2, "utilisateur": "Aminata", "action": "Création d'un cas", "date": "04/11/2026 18:54"},
    {"id": 3, "utilisateur": "Aminata", "action": "Modification d'un bénéficiaire", "date": "04/11/2026 18:55"},
]