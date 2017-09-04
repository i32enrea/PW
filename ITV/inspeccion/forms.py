from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from inspeccion.models import *
from django.contrib.auth.forms import UserCreationForm

class autenticacionForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={'password': forms.PasswordInput(),}

class CochesForm(forms.ModelForm):
    class Meta:
        model=Coche
        fields= ['modelo', 'matricula', 'bastidor', 'tipo', 'author']

class CentrosForm(forms.ModelForm):
    class Meta:
        model=Centros
        fields= ['nombre', 'direccion', 'telefono']
