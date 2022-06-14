from sre_parse import Verbose
from tabnanny import verbose
from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, verbose_name='Nombre')
    apellido = models.CharField(max_length = 100, verbose_name='Apellido')
    correo = models.EmailField(max_length = 100, verbose_name='E-mail')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.IntegerField(primary_key= True)
    nombre = models.CharField(max_length = 50, verbose_name='Nombre Producto')
    valor = models.CharField(max_length = 10, verbose_name= 'Valor')
    categoria = models.CharField(max_length=50, verbose_name='Categoría')
    #foto
    def __str__(self):
        return self.nombre
