from django import forms

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



