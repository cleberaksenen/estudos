from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('', views.home, name='home'), #Página inicial 
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
