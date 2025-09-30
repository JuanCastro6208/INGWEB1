from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # Página principal
    path('fyq/', views.fyq, name='fyq'),          # Preguntas frecuentes
    path('open/', views.open_view, name='open'),  # Entidad (videojuegos)  
]
