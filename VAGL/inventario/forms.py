from django import forms
from django.forms import ModelForm
from .models import Producto

class ProductoForm (ModelForm):
    class Meta: 
        model = Producto 
        fields = "__all__"

        labels = {
            'id' : '',
            'nombre_del_producto' : '',
            'precio' : '',
            'cantidad' : '',
        }

        widgets = {
            'id' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Id'}),
            'nombre_del_producto' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del producto'}),
            'precio' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'$ Precio'}),
            'cantidad' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cantidad'}),
        }


        