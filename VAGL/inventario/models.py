from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.

class Producto (models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    nombre_del_producto = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    cantidad = models.IntegerField()

    def __str__ (self):
        texto="{} {}"
        return texto.format(self.id, self.nombre_del_producto, self.precio,self.cantidad)


    


    



