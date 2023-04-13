from django.urls import path
from .views import *


urlpatterns = [
    
    path('', inicioApp1, name="inicioApp1"),
    path('Curso1/', Curso1),
    path('usuario/', usuario, name="usuario"),
    path('bandas/', bandas, name="bandas"),
    path('vocalista/', vocalista, name="vocalista"),
    path('guitarrista/', guitarrista, name="guitarrista"),
    
]
