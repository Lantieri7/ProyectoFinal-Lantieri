from django.shortcuts import render, redirect
from App1.models import *
from App1.forms import *
from django.http import HttpResponse
# Create your views here.
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
            return redirect ("usuario")
        pass
    else:
        formulario=UsuarioForm(initial={"nombre": usuario.nombre, "apellido":usuario.apellido, "email": usuario.email})
        return render (request, 'App1/editarUsuario.html', {"form": formulario, "usuario": usuario})