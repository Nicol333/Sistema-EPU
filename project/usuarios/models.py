from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Role(models.Model):
    nombre = models.CharField(max_length=50, unique=True)  # El nombre del rol debe ser único

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.nombre


class User(AbstractUser):
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    role = models.ForeignKey(
        Role,
        null=True,  # se permite que quede NULL en la base de datos
        blank=True,  # se permite que quede vacío en formularios
        on_delete=models.SET_NULL,
        related_name='users'
    )

    # Evitar conflictos con auth.User agregando related_name en grupos y permisos
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # nombre único
        blank=True,
        help_text='Grupos a los que pertenece el usuario.',
        verbose_name='grupos'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # nombre único
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='permisos de usuario'
    )

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
