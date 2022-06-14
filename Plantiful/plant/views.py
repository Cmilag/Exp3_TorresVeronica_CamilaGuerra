from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def galeria(request):
    return render( request,'galeria.html')

def ingresar(request):
    return render (request, 'ingresar.html')

def somos (request):
    return render (request, 'somos.html')

def contacto (request):
    return render (request, 'contacto.html')


