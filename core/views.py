from .mock_data import BENEFICIAIRES, CAS, RENDEZ_VOUS, PARTENAIRES, JOURNAL, UTILISATEURS
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from .models import Beneficiaire, Cas, RendezVous, Partenaire

def login_view(request):
    from .mock_data import UTILISATEURS
    
    if request.method == 'POST':
        email = request.POST.get('email')
        role = request.POST.get('role', 'Juriste') # Rôle par défaut
        
        # Simulation de connexion : on cherche l'utilisateur par email
        user_found = None
        for u in UTILISATEURS:
            if u['email'] == email:
                user_found = u
                break
                
        if user_found:
            # On stocke le rôle dans la session pour simuler l'authentification
            request.session['user_id'] = user_found['id']
            request.session['user_email'] = user_found['email']
            request.session['user_role'] = user_found['role']
            request.session['user_nom'] = user_found['nom'] + " " + user_found['prenom']
            
            return redirect('dashboard')
        else:
            messages.error(request, "Aucun compte trouvé avec cet email.")
            
    return render(request, 'core/login.html')
    if request.method == 'POST':
        identifiant = request.POST.get('email')
        password = request.POST.get('password')
        
        username = None
        try:
            user_obj = User.objects.get(username=identifiant)
            username = user_obj.username
        except User.DoesNotExist:
            try:
                user_obj = User.objects.get(email=identifiant)
                username = user_obj.username
            except User.DoesNotExist:
                username = None

        if username:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Mot de passe incorrect.")
        else:
            messages.error(request, "Aucun compte trouvé avec cet identifiant.")
            
    return render(request, 'core/login.html')

def inscription_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'core/inscription.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà pris.")
            return render(request, 'core/inscription.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Compte créé avec succès ! Vous pouvez maintenant vous connecter.")
        return redirect('login')

    return render(request, 'core/inscription.html')

def dashboard_view(request):
    # Récupération du nom depuis la session (simulation)
    nom_utilisateur = request.session.get('user_nom', 'Invité')
    role_utilisateur = request.session.get('user_role', 'Inconnu')

    # Compteurs (données simulées)
    cas_actifs = [c for c in CAS if not c['supprime']]
    benefs_actifs = [b for b in BENEFICIAIRES if not b['supprime']]
    rdvs_actifs = [r for r in RENDEZ_VOUS if not r['supprime']]
    partenaires_actifs = [p for p in PARTENAIRES if not p['supprime']]

    nombre_cas = len(cas_actifs)
    nombre_urgents = len([c for c in cas_actifs if c['priorite'] == 'Urgente'])
    nombre_echeances = len(rdvs_actifs)

    # Listes pour l'affichage
    derniers_benefs = benefs_actifs[-5:]
    derniers_cas = cas_actifs[-5:]
    prochains_rdv = rdvs_actifs[:5]
    derniers_partenaires = partenaires_actifs[-5:]

    context = {
        'nom_utilisateur': nom_utilisateur,
        'role_utilisateur': role_utilisateur,
        'nombre_cas': nombre_cas,
        'nombre_urgents': nombre_urgents,
        'nombre_echeances': nombre_echeances,
        'derniers_benefs': derniers_benefs,
        'derniers_cas': derniers_cas,
        'prochains_rdv': prochains_rdv,
        'derniers_partenaires': derniers_partenaires,
    }
    return render(request, 'core/dashboard.html', context)
# --- BENEFICIAIRES ---
def beneficiaires_view(request):
    benefs = [b for b in BENEFICIAIRES if not b['supprime']]
    return render(request, 'core/beneficiaires.html', {'beneficiaires': benefs})
def ajouter_beneficiaire_view(request):
    if request.method == 'POST':
        Beneficiaire.objects.create(
            nom=request.POST.get('nom'), prenom=request.POST.get('prenom'),
            telephone=request.POST.get('telephone'), zone=request.POST.get('zone'),
            adresse=request.POST.get('adresse')
        )
        return redirect('beneficiaires')
    return render(request, 'core/ajouter_beneficiaire.html')

def supprimer_beneficiaire_view(request, id):
    benef = Beneficiaire.objects.get(id=id)
    benef.est_supprime = True
    benef.save()
    return redirect('beneficiaires')

def corbeille_beneficiaires_view(request):
    benefs_supprimes = Beneficiaire.objects.filter(est_supprime=True)
    return render(request, 'core/corbeille_beneficiaires.html', {'beneficiaires': benefs_supprimes})

def restaurer_beneficiaire_view(request, id):
    benef = Beneficiaire.objects.get(id=id)
    benef.est_supprime = False
    benef.save()
    return redirect('corbeille_beneficiaires')

def modifier_beneficiaire_view(request, id):
    benef = Beneficiaire.objects.get(id=id)
    if request.method == 'POST':
        benef.nom = request.POST.get('nom')
        benef.prenom = request.POST.get('prenom')
        benef.telephone = request.POST.get('telephone')
        benef.zone = request.POST.get('zone')
        benef.adresse = request.POST.get('adresse')
        benef.save()
        return redirect('beneficiaires')
    return render(request, 'core/modifier_beneficiaire.html', {'benef': benef})

# --- CAS JURIDIQUES ---
def cas_juridiques_view(request):
    cas_actifs = [c for c in CAS if not c['supprime']]
    return render(request, 'core/cas_juridiques.html', {'cas': cas_actifs})

def detail_cas_view(request, id):
    cas_obj = Cas.objects.get(id=id)
    documents = cas_obj.documents.all()
    rendez_vous = cas_obj.rendez_vous.all().order_by('date_heure')
    context = {
        'cas': cas_obj,
        'documents': documents,
        'rendez_vous': rendez_vous
    }
    return render(request, 'core/detail_cas.html', context)

def ajouter_cas_view(request):
    if request.method == 'POST':
        beneficiaire_id = request.POST.get('beneficiaire')
        type_cas = request.POST.get('type_cas')
        priorite = request.POST.get('priorite')
        description = request.POST.get('description')

        if beneficiaire_id:
            beneficiaire = Beneficiaire.objects.get(id=beneficiaire_id)
            Cas.objects.create(
                beneficiaire=beneficiaire, type_cas=type_cas,
                priorite=priorite, description=description,
                juriste=request.user
            )
            return redirect('cas_juridiques')
        else:
            messages.error(request, "Veuillez choisir un bénéficiaire.")
            
    beneficiaires = Beneficiaire.objects.filter(est_supprime=False)
    return render(request, 'core/ajouter_cas.html', {'beneficiaires': beneficiaires})

def supprimer_cas_view(request, id):
    cas_obj = Cas.objects.get(id=id)
    cas_obj.est_supprime = True
    cas_obj.save()
    return redirect('cas_juridiques')

def corbeille_cas_view(request):
    cas_supprimes = Cas.objects.filter(est_supprime=True)
    return render(request, 'core/corbeille_cas.html', {'cas': cas_supprimes})

def restaurer_cas_view(request, id):
    cas_obj = Cas.objects.get(id=id)
    cas_obj.est_supprime = False
    cas_obj.save()
    return redirect('corbeille_cas')

def modifier_cas_view(request, id):
    cas_obj = Cas.objects.get(id=id)
    if request.method == 'POST':
        cas_obj.type_cas = request.POST.get('type_cas')
        cas_obj.priorite = request.POST.get('priorite')
        cas_obj.description = request.POST.get('description')
        cas_obj.statut = request.POST.get('statut')
        cas_obj.save()
        return redirect('cas_juridiques')
    return render(request, 'core/modifier_cas.html', {'cas': cas_obj})

# --- AGENDA ---
def agenda_view(request):
    rdvs = [r for r in RENDEZ_VOUS if not r['supprime']]
    return render(request, 'core/agenda.html', {'rdvs': rdvs})


def ajouter_rdv_view(request):
    if request.method == 'POST':
        cas_id = request.POST.get('cas')
        if cas_id:
            cas_obj = Cas.objects.get(id=cas_id)
            RendezVous.objects.create(
                cas=cas_obj, type_rdv=request.POST.get('type_rdv'),
                date_heure=request.POST.get('date_heure'), objet=request.POST.get('objet'),
                lieu=request.POST.get('lieu')
            )
            return redirect('agenda')
        else:
            messages.error(request, "Veuillez choisir un dossier.")
            
    cas_list = Cas.objects.filter(est_supprime=False)
    return render(request, 'core/ajouter_rdv.html', {'cas': cas_list})

def supprimer_rdv_view(request, id):
    rdv = RendezVous.objects.get(id=id)
    rdv.est_supprime = True
    rdv.save()
    return redirect('agenda')

def corbeille_rdv_view(request):
    rdv_supprimes = RendezVous.objects.filter(est_supprime=True)
    return render(request, 'core/corbeille_rdv.html', {'rdvs': rdv_supprimes})

def restaurer_rdv_view(request, id):
    rdv = RendezVous.objects.get(id=id)
    rdv.est_supprime = False
    rdv.save()
    return redirect('corbeille_rdv')

def modifier_rdv_view(request, id):
    rdv = RendezVous.objects.get(id=id)
    if request.method == 'POST':
        rdv.date_heure = request.POST.get('date_heure')
        rdv.objet = request.POST.get('objet')
        rdv.lieu = request.POST.get('lieu')
        rdv.type_rdv = request.POST.get('type_rdv')
        rdv.save()
        return redirect('agenda')
    return render(request, 'core/modifier_rdv.html', {'rdv': rdv})

# --- PARTENAIRES ---
def partenaires_view(request):
    partenaires = [p for p in PARTENAIRES if not p['supprime']]
    return render(request, 'core/partenaires.html', {'partenaires': partenaires})
def ajouter_partenaire_view(request):
    if request.method == 'POST':
        Partenaire.objects.create(
            nom=request.POST.get('nom'), type_partenaire=request.POST.get('type_partenaire'),
            telephone=request.POST.get('telephone'), email=request.POST.get('email'),
            adresse=request.POST.get('adresse')
        )
        return redirect('partenaires')
    return render(request, 'core/ajouter_partenaire.html')

def supprimer_partenaire_view(request, id):
    part = Partenaire.objects.get(id=id)
    part.est_supprime = True
    part.save()
    return redirect('partenaires')

def corbeille_partenaire_view(request):
    part_supprimes = Partenaire.objects.filter(est_supprime=True)
    return render(request, 'core/corbeille_partenaire.html', {'partenaires': part_supprimes})

def restaurer_partenaire_view(request, id):
    part = Partenaire.objects.get(id=id)
    part.est_supprime = False
    part.save()
    return redirect('corbeille_partenaire')

def modifier_partenaire_view(request, id):
    part = Partenaire.objects.get(id=id)
    if request.method == 'POST':
        part.nom = request.POST.get('nom')
        part.type_partenaire = request.POST.get('type_partenaire')
        part.telephone = request.POST.get('telephone')
        part.email = request.POST.get('email')
        part.adresse = request.POST.get('adresse')
        part.save()
        return redirect('partenaires')
    return render(request, 'core/modifier_partenaire.html', {'part': part})
# --- SUPPRESSION DÉFINITIVE ---
def supprimer_definitivement_beneficiaire(request, id):
    benef = Beneficiaire.objects.get(id=id)
    benef.delete()
    return redirect('corbeille_beneficiaires')

def supprimer_definitivement_cas(request, id):
    cas_obj = Cas.objects.get(id=id)
    cas_obj.delete()
    return redirect('corbeille_cas')

def supprimer_definitivement_rdv(request, id):
    rdv = RendezVous.objects.get(id=id)
    rdv.delete()
    return redirect('corbeille_rdv')

def supprimer_definitivement_partenaire(request, id):
    part = Partenaire.objects.get(id=id)
    part.delete()
    return redirect('corbeille_partenaire')
def logout_view(request):
    # On vide la session
    request.session.flush()
    return redirect('login')