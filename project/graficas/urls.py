from django.urls import path
from . import views

urlpatterns = [
    # Gráficas mensuales
    path('mensual/infracciones/', views.grafica_mensual_infracciones, name='grafica_mensual_infracciones'),
    path('mensual/infraestructura/', views.grafica_mensual_infraestructura, name='grafica_mensual_infraestructura'),
    path('mensual/residuos/', views.grafica_mensual_residuos, name='grafica_mensual_residuos'),
    path('mensual/general/', views.grafica_mensual_general, name='grafica_mensual_general'),

    # Gráficas anuales
    path('anual/infracciones/', views.grafica_anual_infracciones, name='grafica_anual_infracciones'),
    path('anual/infraestructura/', views.grafica_anual_infraestructura, name='grafica_anual_infraestructura'),
    path('anual/residuos/', views.grafica_anual_residuos, name='grafica_anual_residuos'),
    path('anual/general/', views.grafica_anual_general, name='grafica_anual_general'),
]
