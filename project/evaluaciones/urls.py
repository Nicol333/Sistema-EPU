from django.urls import path
from . import views  # Asegúrate de que 'views.py' exista o créalo

urlpatterns = [
    # Tus rutas existentes...
    path('historial-usuario/', views.historial_usuario, name='historial_usuario'),
    path('calificaciones-admin/', views.calificaciones_administrador, name='calificaciones_admin'),
]