from django import forms
from .models import UserQuote


class UserQuoteForm(forms.ModelForm):
    """Formulaire pour créer un utilisateur et lui attribuer une citation"""
    
    class Meta:
        model = UserQuote
        fields = ['nom', 'prenom', 'ecole', 'email']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Votre nom',
                'required': True
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Votre prénom',
                'required': True
            }),
            'ecole': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Votre école',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Votre email',
                'required': True
            }),
        }
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'ecole': 'École',
            'email': 'Mail',
        }