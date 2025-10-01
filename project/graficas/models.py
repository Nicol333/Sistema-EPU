from django.db import models
from django.conf import settings

class GraficaReporte(models.Model):
    TIPO_REPORTE_CHOICES = [
        ('infraccion', 'Infracción'),
        ('infraestructura', 'Infraestructura'),
        ('residuo', 'Residuo especial'),
        ('general', 'General'), 
    ]

    PERIODO_CHOICES = [
        ('mensual', 'Mensual'),
        ('anual', 'Anual'),
    ]

    tipo_reporte = models.CharField(max_length=20, choices=TIPO_REPORTE_CHOICES)
    periodo = models.CharField(max_length=10, choices=PERIODO_CHOICES)
    datos = models.JSONField()
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='graficas_reporte',
        null=True,
        blank=True
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'graficas_reporte'
        indexes = [
            models.Index(fields=['tipo_reporte']),
            models.Index(fields=['periodo']),
        ]

    def __str__(self):
        return f"{self.get_tipo_reporte_display()} - {self.get_periodo_display()}"
