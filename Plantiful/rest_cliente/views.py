from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from plant.models import Cliente
from .serializers import ClienteSerializer
# Create your views here. parametros globales. afectan a todos los metodos dentro de este archivo
@csrf_exempt
@api_view(['GET', 'POST'])

def lista_clientes(request):
    if request.method=='GET':#consultar. trae los objetos y los almacena
        cliente = Cliente.objects.all()
        serializer= ClienteSerializer(cliente, many=True) #se convierte en serializador
        return Response(serializer.data) #respuesta al navegador
    elif request.method=='POST':# crear nuevo objeto
        data = JSONParser().parse(request) #almacena informacion que el usuario ingresa a la plataforma
        serializer = ClienteSerializer(data=data) 
        if serializer.is_valid(): #si es valido
            serializer.save() #se graba
            return Response(serializer.data, status=status.HTTP_201_CREATED) #guardado exitosamente
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
