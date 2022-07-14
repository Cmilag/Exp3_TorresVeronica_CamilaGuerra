from dataclasses import fields
from django import forms
from .models import Cliente, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('id','nombre','apellido','correo', 'telefono', 'direccion')


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('id','nombre','valor','categoria', 'imagen')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
