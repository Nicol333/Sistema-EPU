from django.http import HttpResponse
from django.shortcuts import render 

# ---------------- Registrar ----------------
def registrar_infraccion(request):
    return render(request, 'reportes/registrar_infraccion.html')

def registrar_infraestructura(request):
    return render(request, 'reportes/registrar_infraestructura.html')

def registrar_reciclaje_especial(request):
    return render(request, 'reportes/registrar_reciclaje_especial.html')


# ---------------- Listados ----------------
def listado_infracciones(request):
    return render(request, 'reportes/listado_infracciones.html')

def listado_infraestructura(request):
    return render(request, 'reportes/listado_infraestructura.html')

def listado_residuos_especiales(request):
    return render(request, 'reportes/listado_residuos_especiales.html')
