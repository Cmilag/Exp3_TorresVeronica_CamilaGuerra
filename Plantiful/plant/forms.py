from dataclasses import fields
from django import forms
from .models import Cliente, Producto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('id','nombre','apellido','correo', 'telefono', 'direccion')


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('id','nombre','valor','categoria')