from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home principal
    path('admin/home/', views.home_administrador, name='home_administrador'),
    path('home_admin/', views.home_administrador, name='home_administrador'),  # tu vista personalizada
    path('home_usuario/', views.home_usuario, name='home_usuario'),

    path('login/', views.login, name='login'),
    path('registro_usuario/', views.registro_usuario, name='registro_usuario'),

    path('gestionar-usuarios/', views.gestionar_usuarios, name='gestionar_usuarios'),
    path('registrar-funcionario/', views.registrar_funcionario, name='registrar_funcionario'),
    path('gestionar-funcionarios/', views.gestionar_funcionarios, name='gestionar_funcionarios'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('manual/', views.manual, name='manual'),
    path("olvido_contrasena/", views.olvido_contrasena, name="olvido_contrasena"),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('cambiar_contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),
    path('terminos_condiciones/', views.terminos_condiciones, name='terminos_condiciones'),
]
