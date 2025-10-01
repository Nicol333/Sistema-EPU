from django.urls import path
from . import views 

urlpatterns = [
    path('usuarios/', views.notificaciones_usuarios, name='notificaciones_usuarios'),
    path('funcionarios/', views.notificaciones_funcionarios, name='notificaciones_funcionarios'),
]
