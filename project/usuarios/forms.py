from django import forms
from .models import User, Role
from django.contrib.auth.forms import UserCreationForm

#---------------Registro de usuario---------------------- 

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        # Campos que realmente existen en tu modelo
        fields = ['cedula', 'first_name', 'last_name', 'telefono', 'email', 'password1']

    def save(self, commit=True):
        user = super().save(commit=False)
        # Asignar rol por defecto a usuarios normales
        user.role = Role.objects.get(nombre='usuario')  # Asegúrate que exista el rol 'usuario'
        if commit:
            user.save()
        return user


#-------------Login----------------

class LoginUsuarioForm(forms.Form):
    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo electrónico',
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña',
            'class': 'form-control'
        })
    )

