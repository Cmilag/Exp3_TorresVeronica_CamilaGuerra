
from django.shortcuts import redirect, render
from pytest import console_main

from plant.forms import ClienteForm, ProductoForm
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
<<<<<<< HEAD


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
        'form_cliente' : formulario
        }
    else:
        formulario = ClienteForm(request.POST, instance = cliente)
        context = {
        'form_cliente' : formulario
        }
        if formulario.is_valid():
            formulario.save()
            return redirect('lista')
    return render(request,'crear_cliente.html',context)


def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id = id)
    cliente.delete()
    return redirect('lista')


def crear_producto(request):
    if request.method=='POST': 
        producto_form = ProductoForm(request.POST)
        if producto_form .is_valid:
            producto_form .save()
            return redirect ('lista')
    else:
        producto_form  =ProductoForm()
    return render(request, 'crear_producto.html', {'producto_form': producto_form})

def modificar_producto(request,id):
    producto = Producto.objects.get(id = id)
    if request.method == 'GET':
        formulario = ProductoForm(instance = producto)
        context = {
        'form_producto' : formulario
        }
    else:
        formulario = ProductoForm(request.POST, instance = producto)
        context = {
        'form_producto' : formulario
        }
        if formulario.is_valid():
            formulario.save()
            return redirect('lista')
    return render(request,'crear_producto.html',context)


def eliminar_producto(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
=======

def crear_cliente(request):
    if request.method == 'GET':
        form_cliente = ClienteForm()
        context = {
        'form_cliente' : form_cliente
        }
    else:
        form_cliente = ClienteForm(request.POST)
        context = {
        'form_cliente' : form_cliente
        }
        if form_cliente.is_valid():
            form_cliente.save()
            return redirect('lista')
    return render(request,'crear_cliente.html', context)

def modificar_cliente(request,id):
    cliente = Cliente.objects.get(id = id)
    if request.method == 'GET':
        form_cliente = ClienteForm(instance = cliente)
        context = {
        'form_cliente' : form_cliente
        }
    else:
        form_cliente = ClienteForm(request.POST, instance = cliente)
        context = {
        'form_cliente' : form_cliente
        }
        if form_cliente.is_valid():
            form_cliente.save()
            return redirect('lista')
    return render(request,'crear_cliente.html',context)


def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id = id)
    cliente.delete()
<<<<<<< HEAD
    return redirect('lista')


def crear_producto(request):
    if request.method == 'GET':
        form_producto = ProductoForm()
        context = {
        'form_producto' : form_producto
        }

    elif request.method == 'FILES':
     
        form_producto = ProductoForm()
        context = {
        'form_producto' : form_producto
         }
        if form_producto.is_valid():
            form_producto.save()
            return redirect('listaP')
    else:
        form_producto = ProductoForm(request.POST)
        context = {
        'form_producto' : form_producto
        }
        if form_producto.is_valid():
            form_producto.save()
            return redirect('listaP')
    return render(request,'crear_producto.html', context)


def modificar_producto(request,id):
    producto = Producto.objects.get(id = id)
    if request.method == 'GET':
        form_producto = ProductoForm(instance = producto)
        context = {
        'form_producto' : form_producto
        }
    else:
        form_producto = ProductoForm(request.POST, instance = producto)
        context = {
        'form_producto' : form_producto
        }
        if form_producto.is_valid():
            form_producto.save()
            return redirect('listaP')
    return render(request,'crear_producto.html',context)


def eliminar_producto(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('listaP')
=======
>>>>>>> 697968bfd0926f9c702e26acbcc4da1eae17c0eb
    return redirect('lista')
>>>>>>> origin/main
