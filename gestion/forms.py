# gestion/forms.py
from django import forms # type: ignore
from .models import Etudiant
class LoginForm(forms.Form):
    identifiant = forms.CharField(max_length=100)
    mot_de_passe = forms.CharField(widget=forms.PasswordInput)



class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = [
             'prenom', 'nom', 'email', 'contact', 'age',
            'photo', 'nationalite', 'situation_matrimoniale', 'mobile', 'mot_de_passe'
        ]
        widgets = {
            'mot_de_passe': forms.PasswordInput(),  # Masquer le mot de passe
        }