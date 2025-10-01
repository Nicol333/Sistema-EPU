from django.db import models
from django.conf import settings

class Notificacion(models.Model):
    destinatario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notificaciones'
    )
    reporte = models.ForeignKey(
        'reportes.Reporte',  # <--- referencia en string
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notificaciones'
    )
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=[('no_leida','No leída'),('leida','Leída')],
        default='no_leida'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.estado}"
