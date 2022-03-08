from django.shortcuts import redirect, render
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def home (request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else: 
        form = ProductoForm()

    productos = Producto.objects.all()
    return render(request, "home.html", {"productos":productos, "form":form})

def eliminar_producto (request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/')

def modificar_producto (request, id):
    producto_id = Producto.objects.get(id=id)

    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto_id)
        if form.is_valid():
            form.save()
            return redirect('/')
    else: 
        formulario = ProductoForm(instance=producto_id)

    return render(request, "modificar.html", {"formulario":formulario})