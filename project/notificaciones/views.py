from django.shortcuts import render

# Notificaciones para usuarios ciudadanos
def notificaciones_usuarios(request):
    return render(request, 'notificaciones/notificsciones_usuarios.html')

# Notificaciones para funcionarios
def notificaciones_funcionarios(request):
    return render(request, 'notificaciones/notificaciones_funcionarios.html')


