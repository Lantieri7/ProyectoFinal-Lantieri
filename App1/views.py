from django.shortcuts import render, redirect
from .models import Usuario, Bandas, Vocalista, Guitarrista
from .forms import *
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate 
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def usuario(request):
    
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            usuario = Usuario()
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.email = email
            usuario.save()
            form = UsuarioForm()
        else:
            pass
    else:
        form = UsuarioForm()

    usuario= Usuario.objects.all()
    contex = {"usuario": usuario, "form": form}
    return render(request,'App1/usuario.html', contex)



##################################################################################################
@login_required
def bandas(request):

    if request.method == "POST":
        form = BandasForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            bandas = Bandas()
            bandas.nombre = nombre
            bandas.save()
            form = BandasForm()
        else:
            pass
    else:
        form = BandasForm()

    bandas= Bandas.objects.all()
    contex = {"bandas": bandas, "form": form}
    return render(request,'App1/bandas.html', contex)
######################################################################
@login_required
def vocalista(request):
        if request.method == "POST":
         form = VocalistaForm(request.POST)
         if form.is_valid():
            vocalista = Vocalista()
            vocalista.nombre = form.cleaned_data['nombre']
            vocalista.apellido = form.cleaned_data['apellido']
            vocalista.save()
            form = VocalistaForm()
        else:
          form = VocalistaForm()

        vocalista= Vocalista.objects.all()
        contex = {"vocalista": vocalista,"form": form}
        return render(request,'App1/vocalista.html', contex)
######################################################################
@login_required
def guitarrista(request):
    if request.method == "POST":
         form = GuitarristaForm(request.POST)
         if form.is_valid():
            guitarrista = Guitarrista()
            guitarrista.nombre = form.cleaned_data['nombre']
            guitarrista.apellido = form.cleaned_data['apellido']
            guitarrista.save()
            form = GuitarristaForm()
    else:
          form = GuitarristaForm()

    guitarrista= Guitarrista.objects.all()
    contex = {"guitarrista": guitarrista, "form": form}
    return render(request,'App1/guitarrista.html', contex)
###################################################################
def inicio(request):
    return HttpResponse("Bienvenidos a la página principal")

def inicioApp1(request):
    return render(request,'App1/inicio.html')
##################################################################

