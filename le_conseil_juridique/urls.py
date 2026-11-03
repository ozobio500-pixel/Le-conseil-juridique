from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Page d'accueil et connexion
    path('', views.login_view, name='login'),
    path('connexion/', views.login_view, name='login_page'),
    path('inscription/', views.inscription_view, name='inscription'),
    
    # Tableau de bord
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Bénéficiaires
    path('beneficiaires/', views.beneficiaires_view, name='beneficiaires'),
    path('beneficiaires/ajouter/', views.ajouter_beneficiaire_view, name='ajouter_beneficiaire'),
    path('beneficiaires/supprimer/<int:id>/', views.supprimer_beneficiaire_view, name='supprimer_beneficiaire'),
    path('beneficiaires/corbeille/', views.corbeille_beneficiaires_view, name='corbeille_beneficiaires'),
    path('beneficiaires/restaurer/<int:id>/', views.restaurer_beneficiaire_view, name='restaurer_beneficiaire'),
        path('beneficiaires/modifier/<int:id>/', views.modifier_beneficiaire_view, name='modifier_beneficiaire'),

    # Cas Juridiques
    path('cas-juridiques/', views.cas_juridiques_view, name='cas_juridiques'),
    path('cas-juridiques/ajouter/', views.ajouter_cas_view, name='ajouter_cas'),
    path('cas-juridiques/supprimer/<int:id>/', views.supprimer_cas_view, name='supprimer_cas'),
    path('cas-juridiques/corbeille/', views.corbeille_cas_view, name='corbeille_cas'),
    path('cas-juridiques/restaurer/<int:id>/', views.restaurer_cas_view, name='restaurer_cas'),
    path('cas-juridiques/ajouter/', views.ajouter_cas_view, name='ajouter_cas'),
        path('cas-juridiques/<int:id>/', views.detail_cas_view, name='detail_cas'),

    # Agenda
    path('agenda/', views.agenda_view, name='agenda'),
    path('agenda/ajouter/', views.ajouter_rdv_view, name='ajouter_rdv'),
    path('agenda/supprimer/<int:id>/', views.supprimer_rdv_view, name='supprimer_rdv'),
    path('agenda/corbeille/', views.corbeille_rdv_view, name='corbeille_rdv'),
    path('agenda/restaurer/<int:id>/', views.restaurer_rdv_view, name='restaurer_rdv'),
    path('agenda/ajouter/', views.ajouter_rdv_view, name='ajouter_rdv'),

    # Partenaires
    path('partenaires/', views.partenaires_view, name='partenaires'),
    path('partenaires/ajouter/', views.ajouter_partenaire_view, name='ajouter_partenaire'),
    path('partenaires/supprimer/<int:id>/', views.supprimer_partenaire_view, name='supprimer_partenaire'),
    path('partenaires/corbeille/', views.corbeille_partenaire_view, name='corbeille_partenaire'),
    path('partenaires/restaurer/<int:id>/', views.restaurer_partenaire_view, name='restaurer_partenaire'),
        path('cas-juridiques/modifier/<int:id>/', views.modifier_cas_view, name='modifier_cas'),
    path('agenda/modifier/<int:id>/', views.modifier_rdv_view, name='modifier_rdv'),
    path('partenaires/modifier/<int:id>/', views.modifier_partenaire_view, name='modifier_partenaire'),
        # Suppression définitive
    path('beneficiaires/supprimer-definitif/<int:id>/', views.supprimer_definitivement_beneficiaire, name='supprimer_definitivement_beneficiaire'),
    path('cas-juridiques/supprimer-definitif/<int:id>/', views.supprimer_definitivement_cas, name='supprimer_definitivement_cas'),
    path('agenda/supprimer-definitif/<int:id>/', views.supprimer_definitivement_rdv, name='supprimer_definitivement_rdv'),
    path('partenaires/supprimer-definitif/<int:id>/', views.supprimer_definitivement_partenaire, name='supprimer_definitivement_partenaire'),
]