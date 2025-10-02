from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Reporte(models.Model):
    TIPO_REPORTE_CHOICES = [
        ('infraccion', 'Infracción'),
        ('danos', 'Daño a la infraestructura'),
        ('residuo', 'Residuo especial'),
    ]

    TIPO_ESTRUCTURA_CHOICES = [
        ('Alcantarillado', 'Alcantarillado'),
        ('Acueducto', 'Acueducto'),
    ]

    ESTADO_CHOICES = [
        ('Enviado', 'Enviado'),
        ('En proceso', 'En proceso'),
        ('Finalizado', 'Finalizado'),
        ('Rechazado', 'Rechazado'),
    ]

    ciudadano = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='reportes'
    )
    tipo_reporte = models.CharField(
        max_length=50,
        choices=TIPO_REPORTE_CHOICES
    )
    tipo_estructura = models.CharField(
        max_length=20,
        choices=TIPO_ESTRUCTURA_CHOICES,
        null=True,
        blank=True
    )
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    estado = models.CharField(
        max_length=50,
        choices=ESTADO_CHOICES,
        default='Enviado',
        db_index=True
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    anonimo = models.BooleanField(default=False)
    imagen = models.ImageField(
        upload_to='reportes/%Y/%m/%d/',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'reportes'
        indexes = [
            models.Index(fields=['estado']),
            models.Index(fields=['tipo_reporte']),
        ]

    def __str__(self):
        return f"{self.get_tipo_reporte_display()} - {self.ubicacion[:30]} ({self.estado})"

    def clean(self):
        # Validación de anonimato y ciudadano
        if self.tipo_reporte == 'infraccion':
            if not self.anonimo and self.ciudadano is None:
                raise ValidationError("Un reporte de infracción no anónimo requiere un ciudadano asociado.")
        else:
            if self.anonimo:
                raise ValidationError("Solo los reportes de infracción pueden ser anónimos.")
            if self.ciudadano is None:
                raise ValidationError("Este tipo de reporte requiere un ciudadano asociado.")

        # Validación de tipo_estructura solo si aplica
        if self.tipo_reporte in ['danos', 'residuo'] and not self.tipo_estructura:
            raise ValidationError("El tipo de estructura es obligatorio para este tipo de reporte.")

    def save(self, *args, **kwargs):
        # Siempre validar antes de guardar
        self.full_clean()
        super().save(*args, **kwargs)


class Calificacion(models.Model):
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE, related_name='calificaciones')
    valor = models.PositiveSmallIntegerField()  # 1..5
    creador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='calificaciones'
    )
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'calificaciones'

    def __str__(self):
        return f"{self.reporte_id} - {self.valor}"

    def clean(self):
        if not (1 <= self.valor <= 5):
            raise ValidationError('El valor de la calificación debe estar entre 1 y 5')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

@property
def reporte_avg(self):
    # helper at module level if needed
    return None
