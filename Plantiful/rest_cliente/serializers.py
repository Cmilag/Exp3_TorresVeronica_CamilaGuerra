from rest_framework import serializers
from plant.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id','nombre','apellido','correo', 'telefono', 'direccion')