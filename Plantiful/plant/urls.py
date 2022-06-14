from telnetlib import LOGOUT
from django.urls import URLPattern, path
from .views import crear_cliente, crear_producto, modificar_cliente, modificar_producto, eliminar_cliente, eliminar_producto, index, galeria, lista, somos, contacto, ingresar, listaP

urlpatterns = [
    path('', index, name="index"),
    path('galeria/', galeria, name="galeria"),
    path('somos/', somos, name="somos"),
    path('contacto/', contacto, name="contacto"),
    path('ingresar/', ingresar, name="ingresar"),
    
    path('lista/', lista, name="lista"),
    path('crearCliente/', crear_cliente, name="crear_cliente"), 
    path('modificarCliente/<id>/', modificar_cliente, name="modificar_cliente"),
    path('eliminarCliente/<id>/', eliminar_cliente, name="eliminar_cliente"),
    
    path('listaP/', listaP, name="listaP"),
    path('crearProducto/', crear_producto, name="crear_producto"),  
    path('modificarProducto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminarProducto/<id>/', eliminar_producto, name="eliminar_producto"),
]