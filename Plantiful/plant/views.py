
from django.shortcuts import redirect, render

from plant.forms import ClienteForm
from .models import Cliente, Producto 

# Create your views here.

#index 
def index(request):
    return render(request, 'index.html')


def galeria(request):
    return render(request, 'galeria.html')


def somos(request):
    return render(request, 'somos.html')

def contacto(request):
    return render(request, 'contacto.html')

def ingresar(request):
    return render(request, 'ingresar.html')

def lista(request):
    clientes = Cliente.objects.all()
    contexto = {
        'clientes':clientes
    }
    return render(request, 'lista.html', contexto)

#crud
def listaP(request):
    productos = Producto.objects.all()
    contexto = {
        'productos':productos
    }
    return render(request, 'listaP.html', contexto)

def crear_cliente(request):
    if request.method=='POST': 
        cliente_form = ClienteForm(request.POST)
        if cliente_form .is_valid:
            cliente_form .save()
            return redirect ('lista')
    else:
        cliente_form  =ClienteForm()
    return render(request, 'crear_cliente.html', {'cliente_form': cliente_form})

def modificar_cliente(request,id):
    cliente = Cliente.objects.get(id = id)
    if request.method == 'GET':
        formulario = ClienteForm(instance = cliente)
        context = {
        'formulario' : formulario
        }
    else:
        formulario = ClienteForm(request.POST, instance = cliente)
        context = {
        'formulario' : formulario
        }
        if formulario.is_valid():
            formulario.save()
            return redirect('lista')
    return render(request,'crear_cliente.html',context)


def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id = id)
    cliente.delete()
    return redirect('lista')