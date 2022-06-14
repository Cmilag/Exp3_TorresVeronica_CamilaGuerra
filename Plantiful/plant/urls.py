from django.urls import URLPattern, path
from .views import crear_cliente, index, galeria, lista, modificar_cliente, somos, contacto, ingresar, listaP, eliminar_cliente

urlpatterns = [
    path('', index, name="index"),
    path('galeria/', galeria, name="galeria"),
    path('somos/', somos, name="somos"),
    path('contacto/', contacto, name="contacto"),
    path('ingresar/', ingresar, name="ingresar"),
    path('lista/', lista, name="lista"),
    path('listaP/', listaP, name="listaP"),
    path('crearCliente/', crear_cliente, name="crear_cliente"), 
    path('modificarCliente/<id>/', modificar_cliente, name="modificar_cliente"),
    path('eliminarCliente/<id>/', eliminar_cliente, name="eliminar_cliente"),
     

]