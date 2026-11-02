from django.db import models
from django.contrib.auth.models import User

class Beneficiaire(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(blank=True, null=True)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField(blank=True, null=True)
    zone = models.CharField(max_length=100)
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    est_supprime = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Cas(models.Model):
    TYPE_CHOICES = [
        ('DROITS', 'Droits'),
        ('ETAT_CIVIL', 'État civil'),
        ('FONCIER', 'Foncier'),
        ('VIOLENCES', 'Violences'),
        ('AUTRE', 'Autre'),
    ]
    STATUT_CHOICES = [
        ('NOUVEAU', 'Nouveau'),
        ('EN_COURS', 'En cours'),
        ('ORIENTE', 'Orienté'),
        ('EN_ATTENTE', 'En attente'),
        ('RESOLU', 'Résolu'),
        ('CLOTURE', 'Clôturé'),
    ]
    PRIORITE_CHOICES = [
        ('NORMALE', 'Normale'),
        ('URGENTE', 'Urgente'),
    ]

    beneficiaire = models.ForeignKey(Beneficiaire, on_delete=models.CASCADE, related_name='cas')
    reference = models.CharField(max_length=50, unique=True, blank=True)
    type_cas = models.CharField(max_length=20, choices=TYPE_CHOICES, default='AUTRE')
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='NOUVEAU')
    priorite = models.CharField(max_length=20, choices=PRIORITE_CHOICES, default='NORMALE')
    date_ouverture = models.DateTimeField(auto_now_add=True)
    date_cloture = models.DateTimeField(blank=True, null=True)
    juriste = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    est_supprime = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.reference} - {self.beneficiaire.nom}"

    def save(self, *args, **kwargs):
        if not self.reference:
            import uuid
            self.reference = f"CAS-{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)

class Document(models.Model):
    cas = models.ForeignKey(Cas, on_delete=models.CASCADE, related_name='documents')
    nom_fichier = models.CharField(max_length=255)
    fichier = models.FileField(upload_to='documents/')
    categorie = models.CharField(max_length=100)
    version = models.IntegerField(default=1)
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_fichier

class RendezVous(models.Model):
    TYPE_CHOICES = [
        ('CONSULTATION', 'Consultation'),
        ('AUDIENCE', 'Audience'),
        ('ECHEANCE', 'Échéance'),
    ]

    cas = models.ForeignKey(Cas, on_delete=models.CASCADE, related_name='rendez_vous')
    date_heure = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    objet = models.CharField(max_length=255)
    type_rdv = models.CharField(max_length=20, choices=TYPE_CHOICES, default='CONSULTATION')
    est_supprime = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.objet} - {self.date_heure.strftime('%d/%m/%Y')}"

class Partenaire(models.Model):
    TYPE_CHOICES = [
        ('AVOCAT', 'Avocat'),
        ('ASSOCIATION', 'Association'),
        ('INSTITUTION', 'Institution'),
    ]

    nom = models.CharField(max_length=255)
    type_partenaire = models.CharField(max_length=20, choices=TYPE_CHOICES, default='AVOCAT')
    telephone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    est_supprime = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} ({self.get_type_partenaire_display()})"
