from django.shortcuts import render
from reportes.models import Reporte
from django.http import JsonResponse, HttpResponseBadRequest
from django.db import models as dj_models
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from reportes.models import Reporte, Calificacion
from django.shortcuts import get_object_or_404


def historial_usuario(request):
    return render(request, 'evaluaciones/historial_usuario.html')

def calificaciones_administrador(request):
    reportes = Reporte.objects.all().prefetch_related('calificaciones')
    # attach avg and count
    for r in reportes:
        qs = r.calificaciones.all()
        r.count_cal = qs.count()
        avg = qs.aggregate(dj_models.Avg('valor'))['valor__avg'] or 0
        r.avg_cal = round(avg, 2)
    return render(request, 'evaluaciones/calificaciones_administrador.html', {'reportes': reportes})


@require_POST
def rate_reporte(request):
    try:
        reporte_id = int(request.POST.get('reporte_id'))
        valor = int(request.POST.get('valor'))
    except (TypeError, ValueError):
        return HttpResponseBadRequest('Invalid data')

    if valor < 1 or valor > 5:
        return HttpResponseBadRequest('Valor fuera de rango')

    reporte = get_object_or_404(Reporte, pk=reporte_id)
    # Optional: associate with user if authenticated
    creador = request.user if request.user.is_authenticated else None

    cal = Calificacion.objects.create(reporte=reporte, valor=valor, creador=creador)

    # compute new average and count
    qs = reporte.calificaciones.all()
    total = qs.count()
    avg = qs.aggregate(dj_models.Avg('valor'))['valor__avg'] or 0

    return JsonResponse({'success': True, 'avg': round(avg, 2), 'count': total})