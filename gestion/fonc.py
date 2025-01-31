from django.shortcuts import render, redirect# type: ignore
from .models import Etudiant, Formation, Experience, Competence, Langue, Loisir, Projet

def formulaire_etudiant(request, etudiant_id):
    # Récupérer l'étudiant existant
    etudiant = Etudiant.objects.get(id=etudiant_id)

    if request.method == 'POST':
        # Récupérer les données pour chaque section du formulaire
        formations_data = request.POST.getlist('annee')
        diplomes_data = request.POST.getlist('diplomes')
        etablissements_data = request.POST.getlist('etablissement')
        localites_data = request.POST.getlist('localite')
        
        experiences_data = request.POST.getlist('date_debut')
        date_fin_data = request.POST.getlist('date_fin')
        titres_data = request.POST.getlist('titre_experience')
        entreprises_data = request.POST.getlist('entreprise')
        localite_entreprise_data = request.POST.getlist('localite_entreprise')
        taches_data = request.POST.getlist('taches')
        
        competences_data = request.POST.getlist('titre_competence')
        outils_data = request.POST.getlist('outils')

        langues_data = request.POST.getlist('langues')
        loisirs_data = request.POST.getlist('libelle_loisir')
        projets_data = request.POST.getlist('titre_projet')
        descriptions_projets_data = request.POST.getlist('description_projet')

        # Enregistrer les formations
        for i in range(len(formations_data)):
            Formation.objects.create(
                etudiant=etudiant,
                annee=formations_data[i],
                diplomes=diplomes_data[i],
                etablissement=etablissements_data[i],
                localite=localites_data[i]
            )

        # Enregistrer les expériences
        for i in range(len(experiences_data)):
            Experience.objects.create(
                etudiant=etudiant,
                date_debut=experiences_data[i],
                date_fin=date_fin_data[i],
                titre=titres_data[i],
                entreprise=entreprises_data[i],
                localite_entreprise=localite_entreprise_data[i],
                taches=taches_data[i]
            )

        # Enregistrer les compétences
        for i in range(len(competences_data)):
            Competence.objects.create(
                etudiant=etudiant,
                titre=competences_data[i],
                outils=outils_data[i]
            )

        # Enregistrer les langues
        for langue in langues_data:
            Langue.objects.create(
                etudiant=etudiant,
                libelle=langue
            )

        # Enregistrer les loisirs
        for loisir in loisirs_data:
            Loisir.objects.create(
                etudiant=etudiant,
                libelle=loisir
            )

        # Enregistrer les projets
        for i in range(len(projets_data)):
            Projet.objects.create(
                etudiant=etudiant,
                titre=projets_data[i],
                description=descriptions_projets_data[i]
            )

        # Retourner à une page de confirmation ou rediriger vers un autre formulaire
        return redirect('confirmation_page')  # Remplacez par une page de confirmation

    # Afficher le formulaire
    return render(request, 'formulaire_etudiant.html', {'etudiant': etudiant})
