from django.urls import path
from . import views

urlpatterns = [
    # Otras rutas de tu aplicación
    path('messages/', views.lista_mensajes, name='lista_mensajes'),
    path('messages/enviar/', views.enviar_mensaje, name='enviar_mensaje'),
]