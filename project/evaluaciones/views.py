from django.shortcuts import render


def historial_usuario(request):
    return render(request, 'evaluaciones/historial_usuario.html')

def calificaciones_administrador(request):
    return render(request, 'evaluaciones/calificaciones_administrador.html')