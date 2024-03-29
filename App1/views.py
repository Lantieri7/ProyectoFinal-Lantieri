from django.shortcuts import render, redirect
from .models import Usuario, Bandas, Vocalista, Guitarrista, Avatar
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate 
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Conversacion, Mensaje
from django.shortcuts import render, get_object_or_404
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

@login_required
def obtenerAvatar(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/media/avatars/imagencomun.png"

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "App1/inicio.html", {"mensaje":f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "App1/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "App1/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})
    
#############################################################################################################################################

@login_required
def conversaciones(request):
    conversaciones = request.user.conversaciones.all()
    return render(request, 'App3/conversaciones.html', {'conversaciones': conversaciones})

@login_required
def mensajes(request, conversacion_id):
    conversacion = get_object_or_404(Conversacion, id=conversacion_id, participantes=request.user)
    mensajes = conversacion.mensajes.all()
    return render(request, 'App3/mensajes.html', {'conversacion': conversacion, 'mensajes': mensajes})

@login_required
def enviar_mensaje(request, conversacion_id):
    conversacion = get_object_or_404(Conversacion, id=conversacion_id, participantes=request.user)
    if request.method == 'POST':
        mensaje = Mensaje()
        mensaje.conversacion = conversacion
        mensaje.autor = request.user
        mensaje.texto = request.POST.get('texto')
        mensaje.save()
    return redirect('mensajes', conversacion_id=conversacion_id)