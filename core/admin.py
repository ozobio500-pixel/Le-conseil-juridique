from django.contrib import admin
from .models import Beneficiaire, Cas, Document, RendezVous, Partenaire

# ... (garde ce que tu avais) ...

@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_partenaire', 'telephone', 'email')
    list_filter = ('type_partenaire',)