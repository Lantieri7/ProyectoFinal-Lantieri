from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)        
    email=forms.EmailField()

class BandasForm(forms.Form):
    nombre=forms.CharField(max_length=50, label="Nombre de la Banda: ")

class VocalistaForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)

class GuitarristaForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)

class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

class Meta:
    model=User
    fields=["username", "email", "password1", "password2"]
    help_texts = {k:"" for k in fields}
