
from django.shortcuts import render


# ---------------- Gráficas Mensuales ----------------
def grafica_mensual_infracciones(request):
    return render(request, 'graficas/grafica_mensual_infracciones.html')

def grafica_mensual_infraestructura(request):
    return render(request, 'graficas/grafica_mensual_infraestructura.html')

def grafica_mensual_residuos(request):
    return render(request, 'graficas/grafica_mensual_residuos.html')

def grafica_mensual_general(request):
    return render(request, 'graficas/grafica_mensual_general.html')


# ---------------- Gráficas Anuales ----------------
def grafica_anual_infracciones(request):
    return render(request, 'graficas/grafica_anual_infracciones.html')

def grafica_anual_infraestructura(request):
    return render(request, 'graficas/grafica_anual_infraestructura.html')

def grafica_anual_residuos(request):
    return render(request, 'graficas/grafica_anual_residuos.html')

def grafica_anual_general(request):
    return render(request, 'graficas/ general_grafica_anual.html')
