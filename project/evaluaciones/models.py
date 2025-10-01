from django.db import models
from django.conf import settings

class Evaluacion(models.Model):
    TIPO_REPORTE_CHOICES = [
        ('infraccion', 'Infracción'),
        ('danos', 'Infraestructura'),
        ('residuo', 'Residuo especial'),
    ]

    PUNTAJE_CHOICES = [(i, str(i)) for i in range(0, 11)]  # Calificación del 0 al 10

    reporte = models.ForeignKey(
        'reportes.Reporte',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='evaluaciones'
    )
    tipo_reporte = models.CharField(max_length=20, choices=TIPO_REPORTE_CHOICES)
    evaluador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='evaluaciones_realizadas'
    )
    evaluado = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='evaluaciones_recibidas'
    )
    puntaje = models.IntegerField(choices=PUNTAJE_CHOICES)
    comentarios = models.TextField(blank=True, null=True)
    fecha_evaluacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'evaluaciones'
        indexes = [
            models.Index(fields=['tipo_reporte']),
            models.Index(fields=['puntaje']),
            models.Index(fields=['fecha_evaluacion']),
        ]

    def __str__(self):
        return f"{self.get_tipo_reporte_display()} - {self.puntaje} puntos"
