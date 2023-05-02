from django.shortcuts import render
from .models import Usuario, Bandas, Vocalista, Guitarrista
from .forms import *
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate 

# Create your views here.
def Curso1(request):
    
    nombre_curso="Python"
    usuario=Usuario(nombre=nombre_curso)
    usuario.save()
    respuesta=(f"Curso creado----> {nombre_curso}")
    return HttpResponse(respuesta)

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


def busquedaUsuario(request):
    return render(request, "App1/busquedaUsuario.html")

def buscar(request):
      if request.GET["apellido"]:
        apellido= request.GET["apellido"]
        usuario=Usuario.objects.filter(apellido__icontains=apellido)
        return render(request, "App1/resultadosBusqueda.html", {"usuario": usuario})
      else:
        return render(request, "App1/busquedaUsuario.html", {"mensaje": "Ingrese un Apellido"})

def eliminarUsuario(request, id):
    usuario=Usuario.objects.get(id=id)
    usuario.delete()
    usuario=Usuario.objects.all()
    form=UsuarioForm()
    return render(request,'App1/usuario.html',{"usuario": usuario, "mensaje": "Usuario eliminado correctamente"})

def editarUsuario(request, id):
    usuario=Usuario.objects.get(id=id)
    if request.method=="POST":
        form= UsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.nombre=info["nombre"]
            usuario.apellido=info["apellido"]
            usuario.email=info["email"]
            usuario.save()
            usuario=Usuario.objects.all()
            form=UsuarioForm()
            return render(request, 'App1/usuario.html',{"usuario": usuario, "mensaje": "Usuario editado correctamente"})
        pass
    else:
        formulario=UsuarioForm(initial={"nombre": usuario.nombre, "apellido":usuario.apellido, "email": usuario.email})
        return render (request, 'App1/usuario.html', {"form": formulario, "usuario": usuario})
##################################################################################################
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
###################################################################   

def login_request(request):
    if request.method=="POST":
      form=AuthenticationForm(request, data=request.POST)
      if form.is_valid():
          info=form.cleaned_data
          usu=info["username"]
          clave=info["password"]

          if usuario is not None: 
              login(request, usuario)
              return render(request, 'App1/inicio.html', {"mensaje": f"Usuario {usu} logueado correctamente"})
          else:
              return render (request, 'App1/login.html', {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
          
      else:
          return render(request, 'App1/login.html', {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
      
    else:
        form=AuthenticationForm()
        return render(request, 'App1/login.html', {"form":form})
