from django.shortcuts import render, redirect
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm



def home(request):
    productos = Producto.objects.all()  # Trae todos los productos
    return render(request, 'mi_primer_app/home.html', {'productos': productos})

def categoria(request):
    return render(request, 'mi_primer_app/cargar_categoria.html')

def producto(request):
    return render(request, 'mi_primer_app/cargar_producto.html')

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'mi_primer_app/listar_productos.html', {'productos': productos})

def cargar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'mi_primer_app/cargar_producto.html', {'form': form})

def cargar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'mi_primer_app/cargar_categoria.html', {'form': form})
