from django.shortcuts import render, redirect
from App1.models import *
from App1.forms import *
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def busquedaUsuario(request):
    return render(request, "App1/busquedaUsuario.html")

@login_required
def buscar(request):
      if request.GET["apellido"]:
        apellido= request.GET["apellido"]
        usuario=Usuario.objects.filter(apellido__icontains=apellido)
        return render(request, "App1/resultadosBusqueda.html", {"usuario": usuario})
      else:
        return render(request, "App1/busquedaUsuario.html", {"mensaje": "Ingrese un Apellido"})

@login_required
def eliminarUsuario(request, id):
    usuario=Usuario.objects.get(id=id)
    usuario.delete()
    return redirect("usuario")

@login_required
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
            return redirect ("usuario")
        pass
    else:
        formulario=UsuarioForm(initial={"nombre": usuario.nombre, "apellido":usuario.apellido, "email": usuario.email})
        return render (request, 'App1/editarUsuario.html', {"form": formulario, "usuario": usuario})
    
#########################################################################################################################
@login_required
def eliminarBandas(request, id):
    bandas=Bandas.objects.get(id=id)
    bandas.delete()
    return redirect("bandas")

@login_required
def editarBandas(request, id):
    bandas=Bandas.objects.get(id=id)
    if request.method=="POST":
        form= BandasForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            bandas.nombre=info["nombre"]
            bandas.save()
            bandas=Bandas.objects.all()
            form=BandasForm()
            return redirect ("bandas")
        pass
    else:
        formulario=BandasForm(initial={"nombre": bandas.nombre})
        return render (request, 'App1/editarUsuario.html', {"form": formulario, "bandas": bandas})

@login_required   
def busquedaBandas(request):
     return render(request, "App1/busquedaBandas.html")

@login_required
def buscarBandas(request):
      if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        bandas=Bandas.objects.filter(nombre__icontains=nombre)
        return render(request, "App1/resultadosBusquedaBandas.html", {"bandas": bandas})
      else:
        return render(request, "App1/busquedaBandas.html", {"mensaje": "Ingrese un Nombre"})

#################################################################################################

def login_request(request):
    if request.method=="POST":
      form=AuthenticationForm(request, data=request.POST)
      if form.is_valid():
          info=form.cleaned_data
          usu=info["username"]
          clave=info["password"]
          usuario=authenticate(username=usu, password=clave)
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
    
def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, 'App1/inicio.html', {"mensaje": f"Cuenta {username} creada  correctamente"})
        else:
            return render(request, 'App1/register.html', {"form": form, "mensaje": "Error en el proceso"})
    else:
        form= RegistroUsuarioForm()
        return render(request, 'App1/register.html', {"form": form})
######################################################################################################################
@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "App1/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "App1/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "App1/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
#######################################################################################################################

@login_required
def eliminarGuitarrista(request, id):
    bandas=Guitarrista.objects.get(id=id)
    bandas.delete()
    return redirect("guitarrista")

@login_required
def editarGuitarrista(request, id):
    guitarrista=Guitarrista.objects.get(id=id)
    if request.method=="POST":
        form= GuitarristaForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            guitarrista.nombre=info["nombre"]
            guitarrista.save()
            guitarristas=Guitarrista.objects.all()
            form=GuitarristaForm()
            return redirect ("bandas")
        pass
    else:
        formulario=GuitarristaForm(initial={"nombre": guitarrista.nombre})
        return render (request, 'App1/editarGuitarrista.html', {"form": formulario, "guitarrista": guitarrista})

@login_required   
def busquedaGuitarrista(request):
     return render(request, "App1/busquedaBandas.html")

@login_required
def buscarGuitarrista(request):
      if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        guitarrista=Guitarrista.objects.filter(nombre__icontains=nombre)
        return render(request, "App1/resultadosBusquedaGuitarrista.html", {"guitarrista": guitarrista})
      else:
        return render(request, "App1/busquedaGuitarrista.html", {"mensaje": "Ingrese un Nombre"})