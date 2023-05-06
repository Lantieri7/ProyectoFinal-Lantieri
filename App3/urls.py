from django.urls import path 
from App1.views import conversaciones, mensajes, enviar_mensaje


urlpatterns = [

    path('', conversaciones, name='conversaciones'),
    path('<int:conversacion_id>/', mensajes, name='mensajes'),
    path('<int:conversacion_id>/enviar/', enviar_mensaje, name='enviar_mensaje'),


]
