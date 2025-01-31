from django.contrib import admin # type: ignore
from .models import Etudiant, CV, Formation, Experience, Competence, Langue, Loisir, Projet

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'contact', 'age', 'nationalite', 'situation_matrimoniale')
    search_fields = ( 'prenom', 'nom', 'email')
    list_filter = ('situation_matrimoniale', 'nationalite')
    ordering = ('nom', 'prenom')
    fieldsets = (
    (None, {
        'fields': ('prenom', 'nom', 'email', 'contact', 'age', 'nationalite', 'situation_matrimoniale', 'mobile', 'mot_de_passe')  # Garder mot_de_passe ici
    }),
    ('Social Media', {
        'fields': ('facebook', 'linkedin', 'instagram')
    }),
    ('Photo', {
        'fields': ('photo',)
    }),
    ('Security', {
        'fields': (),  # Ne pas inclure mot_de_passe ici
        'classes': ('collapse',),  # Cette section sera réductible
    }),
)
    readonly_fields = ('mot_de_passe',)  # Make the password field read-only

def save_model(self, request, obj, form, change):
    if not change:  # Si l'objet est en cours de création
        mot_de_passe = form.cleaned_data.get('mot_de_passe')
        if mot_de_passe:  # Vérifiez si mot_de_passe est fourni
            obj.set_mot_de_passe(mot_de_passe)
    super().save_model(request, obj, form, change)

# Enregistrement du modèle CV
class CVAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'titre', 'date_creation')
    search_fields = ('titre', 'etudiant__prenom', 'etudiant__nom')
    list_filter = ('date_creation',)
    ordering = ('date_creation',)

# Enregistrement du modèle Formation
class FormationAdmin(admin.ModelAdmin):
    list_display = ('cv', 'diplomes', 'etablissement', 'localite')
    search_fields = ('diplomes', 'etablissement')
    list_filter = ('diplomes',)
    ordering = ('diplomes',)

# Enregistrement du modèle Experience
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('cv', 'titre', 'entreprise', 'date_debut', 'date_fin')
    search_fields = ('titre', 'entreprise', 'cv__etudiant__prenom', 'cv__etudiant__nom')
    list_filter = ('date_debut', 'date_fin')
    ordering = ('date_debut',)

# Enregistrement du modèle Competence
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('cv', 'titre', 'niveau')
    search_fields = ('titre', 'cv__etudiant__prenom', 'cv__etudiant__nom')
    list_filter = ('niveau',)
    ordering = ('niveau',)

# Enregistrement du modèle Langue
class LangueAdmin(admin.ModelAdmin):
    list_display = ('cv', 'nom', 'niveau')
    search_fields = ('nom', 'cv__etudiant__prenom', 'cv__etudiant__nom')
    list_filter = ('niveau',)
    ordering = ('niveau',)

# Enregistrement du modèle Loisir
class LoisirAdmin(admin.ModelAdmin):
    list_display = ('cv', 'libelle')
    search_fields = ('libelle',)
    ordering = ('libelle',)

# Enregistrement du modèle Projet
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('cv', 'titre', 'date_debut', 'date_fin')
    search_fields = ('titre', 'cv__etudiant__prenom', 'cv__etudiant__nom')
    list_filter = ('date_debut', 'date_fin')
    ordering = ('date_debut',)

# Enregistrement des modèles dans l'admin
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(CV, CVAdmin)
admin.site.register(Formation, FormationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(Langue, LangueAdmin)
admin.site.register(Loisir, LoisirAdmin)
admin.site.register(Projet, ProjetAdmin)

# Register your models here.
