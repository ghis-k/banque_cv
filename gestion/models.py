from django.db import models # type: ignore
from django.core.validators import MinValueValidator, MaxValueValidator # type: ignore
from django.contrib.auth.hashers import make_password, check_password # type: ignore

# Modèle pour l'Utilisateur (étudiant)


class Etudiant(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    age = models.IntegerField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    nationalite = models.CharField(max_length=50)
    situation_matrimoniale = models.CharField(
        max_length=50,
        choices=[
            ('Celibataire', 'Celibataire'),
            ('Marie', 'Marie'),
            ('Divorcé', 'Divorcé'),
            ('Veuve/Veuf', 'Veuve/Veuf'),
        ],
        default='Celibataire',
        help_text="Niveau de maîtrise de la situation_matrimoniale"
    )
    mobile = models.CharField(max_length=20)
   
    mot_de_passe = models.CharField(max_length=128)  # Champ pour le mot de passe

    def set_mot_de_passe(self, mot_de_passe):
        self.mot_de_passe = make_password(mot_de_passe)  # Hachage du mot de passe

    def verifier_mot_de_passe(self, mot_de_passe):
        return check_password(mot_de_passe, self.mot_de_passe)  # Vérification du mot de passe

    def __str__(self):
        return f"{self.prenom} {self.nom} )"
# Modèle pour le CV
class CV(models.Model):
    etudiant = models.ForeignKey(Etudiant, related_name='cv', on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"CV de {self.etudiant.prenom} {self.etudiant.nom}"

# Modèle pour la Formation
class Formation(models.Model):
    cv = models.ForeignKey(CV, related_name='formations_cv', on_delete=models.CASCADE, blank=True, null=True)
    diplomes = models.CharField(max_length=255)
    etablissement = models.CharField(max_length=255)
    date_debut = models.DateField(
        default="2000-01-01",  # Valeur par défaut pour éviter les erreurs de migration
        help_text="Date de début de la formation."
    )
    date_fin = models.DateField(
        default="2000-12-31",  # Vous pouvez définir une autre valeur pertinente
        help_text="Date de fin de la formation."
    )
    localite = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.diplomes} - {self.etablissement}"

# Modèle pour l'Expérience Professionnelle
class Experience(models.Model):
    cv = models.ForeignKey(CV, related_name='experiences_cv', on_delete=models.CASCADE, blank=True, null=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    titre = models.CharField(max_length=255)
    entreprise = models.CharField(max_length=255)
    localite_entreprise = models.CharField(max_length=100)
    taches = models.TextField()

    def __str__(self):
        return f"{self.titre} chez {self.entreprise}"

# Modèle pour la Compétence
class Competence(models.Model):
    titre = models.CharField(max_length=100)
    cv = models.ForeignKey(CV, related_name='competences_cv', on_delete=models.CASCADE, blank=True, null=True)
    niveau = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Niveau en pourcentage (ex: 80 pour 80%).", default=50
    )

    def __str__(self):
        return f"{self.titre} ({self.niveau}%)"
    
# Modèle pour la Langue
class Langue(models.Model):
    cv = models.ForeignKey(CV, related_name='langues_cv', on_delete=models.CASCADE, blank=True, null=True)
    nom = models.CharField(max_length=100,default="Inconnu",)    
    niveau = models.CharField(
        max_length=50,
        choices=[
            ('Débutant', 'Débutant'),
            ('Intermédiaire', 'Intermédiaire'),
            ('Avancé', 'Avancé'),
            ('Bilingue', 'Bilingue'),
        ],
        default='Débutant',  # Ajout de la valeur par défaut
        help_text="Niveau de maîtrise de la langue"
    )

    def __str__(self):
        return f"{self.nom} ({self.niveau})"

# Modèle pour les Loisirs
class Loisir(models.Model):
    cv = models.ForeignKey(CV, related_name='loisirs_cv', on_delete=models.CASCADE, blank=True, null=True)
    libelle = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle

# Modèle pour le Projet
class Projet(models.Model):
    cv = models.ForeignKey(CV, related_name='projets_cv', on_delete=models.CASCADE, blank=True, null=True)
    titre = models.CharField(max_length=255)
    date_debut = models.DateField(default="2000-01-01",help_text="Date de début du projet.")
    date_fin = models.DateField(blank=True, null=True, help_text="Date de fin du projet.")
    description = models.TextField()

    def __str__(self):
        return self.titre

# Create your models here.
