from django.urls import path
from .views import *
from App2.views import *
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import conversaciones, mensajes, enviar_mensaje


urlpatterns = [
    
    path('', inicioApp1, name="inicioApp1"),
    path('usuario/', usuario, name="usuario"),
    path('bandas/', bandas, name="bandas"),
    path('vocalista/', vocalista, name="vocalista"),
    path('guitarrista/', guitarrista, name="guitarrista"),

    path('busquedaUsuario/', busquedaUsuario, name="busquedaUsuario"),
    path('buscar/', buscar, name="buscar"),
    path('eliminarUsuario/<id>',eliminarUsuario, name="eliminarUsuario" ),
    path('editarUsuario/<id>', editarUsuario, name="editarUsuario" ),

    path('eliminarBandas/<id>',eliminarBandas, name="eliminarBandas" ),
    path('editarBandas<id>', editarBandas, name="editarBandas" ),
    path('busquedaBandas/', busquedaBandas, name="busquedaBandas"),
    path('buscarBandas/', buscarBandas, name="buscarBandas"),


    path('eliminarGuitarrista/<id>',eliminarGuitarrista, name="eliminarGuitarrista" ),
    path('editarGuitarrista<id>', editarGuitarrista, name="editarGuitarrista" ),
    path('busquedaGuitarrista/', busquedaGuitarrista, name="busquedaGuitarrista"),
    path('buscarGuitarrista/', buscarGuitarrista, name="buscarGuitarrista"),

    path('eliminarVocalista/<id>',eliminarVocalista, name="eliminarVocalista" ),
    path('editarVocalista<id>', editarVocalista, name="editarVocalista" ),
    path('busquedaVocalista/', busquedaVocalista, name="busquedaVocalista"),
    path('buscarVocalista/', buscarVocalista, name="buscarVocalista"),

    path('login/', login_request, name="login"),
    path('register/', register, name="register"),
    path('logout/', LogoutView.as_view(template_name='App1/logout.html'), name= "logout"),

    path('editarPerfil/', editarPerfil, name='editarPerfil'),

    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),


    path('', conversaciones, name='conversaciones'),
    path('<int:conversacion_id>/', mensajes, name='mensajes'),
    path('<int:conversacion_id>/enviar/', enviar_mensaje, name='enviar_mensaje'),



]
