from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homeUrl'),
    path('eliminarProducto/<id>', views.eliminar_producto, name='eliminarUrl'),
    path('modificarProducto/<id>', views.modificar_producto, name='modificarUrl'),
]