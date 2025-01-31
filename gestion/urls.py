from django.urls import path # type: ignore
from .views import create_cv, deconnexion,edit_cv, cv_success, envoyer_fichier_par_mail, list_cv, list_cv_by_etudiant, search_cv,view_cv,login_etudiant,etudiant_create,modifier_etudiant,generate_pdf
from gestion import views
from django.contrib.auth import views as auth_views # type: ignore

urlpatterns = [
    path('', list_cv, name='list_cv'),  # URL pour la liste de tous les CV
    path('create_cv/', create_cv, name='create_cv'),
    path('cv_success/', cv_success, name='cv_success'),
    path('list_cv/', list_cv, name='list_cv'),  # URL pour la liste de tous les CV
    path('list_cv_by_etudiant/', list_cv_by_etudiant, name='list_cv_by_etudiant'),  # URL pour la liste de CV par étudiant
    path('view_cv/<int:cv_id>/', view_cv, name='view_cv'),  # URL pour afficher un CV
    path('edit_cv/<int:cv_id>/', edit_cv, name='edit_cv'),
    path('login/', login_etudiant, name='login_etudiant'),
    path('etudiant_creer/', etudiant_create, name='etudiant_create'),
    path('modifier_etudiant/', modifier_etudiant, name='modifier_etudiant'),
    path('search/', search_cv, name='search_cv'),
    path('list_cv_by_etudiant/', list_cv_by_etudiant, name='list_cv_by_etudiant'),  #
    path('deconnexion/', deconnexion, name='deconnexion'),  #
    path('generate_pdf/', generate_pdf, name='generate_pdf'),
    path('cvmodele-moderne/<int:cv_id>/', views.cv_modele_moderne, name='cv_modele_moderne'),
    path('cvmodele-classique/<int:cv_id>/', views.cv_modele_classique, name='cv_modele_classique'),
    path('cvmodele-creatif/<int:cv_id>/', views.cv_modele_creatif, name='cv_modele_creatif'),
    path('cvmodele-minimaliste/<int:cv_id>/', views.cv_modele_minimaliste, name='cv_modele_minimaliste'),
    path('cvmodele-professionnel/<int:cv_id>/', views.cv_modele_professionnel, name='cv_modele_professionnel'),
    path('cvmodele-accademique/<int:cv_id>/', views.cv_modele_accademique, name='cv_modele_accademique'),
    path('cvmodele-infographique/<int:cv_id>/', views.cv_modele_infographique, name='cv_modele_infographique'),
    path('cvmodele-thematique/<int:cv_id>/', views.cv_modele_thematique, name='cv_modele_thematique'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]