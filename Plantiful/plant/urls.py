from django.urls import URLPattern, path 
from .views import index , galeria, somos,contacto,ingresar 

urlpatterns = [
    path( '', index, name="index"),
    path('galeria/', galeria, name="galeria"),
    path('somos/', somos, name="somos"),
    path('contacto/', contacto, name="contacto"),
    path('ingresar/', ingresar ,name="ingresar"),
]