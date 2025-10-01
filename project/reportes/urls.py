from django.urls import path
from . import views

urlpatterns = [
    # Registrar
    path('registrar/infraccion/', views.registrar_infraccion, name='registrar_infraccion'),
    path('registrar/infraestructura/', views.registrar_infraestructura, name='registrar_infraestructura'),
    path('registrar/reciclaje-especial/', views.registrar_reciclaje_especial, name='registrar_reciclaje_especial'),

    # Listados
    path('listado/infracciones/', views.listado_infracciones, name='listado_infracciones'),
    path('listado/infraestructura/', views.listado_infraestructura, name='listado_infraestructura'),
    path('listado/residuos-especiales/', views.listado_residuos_especiales, name='listado_residuos_especiales'),
]
