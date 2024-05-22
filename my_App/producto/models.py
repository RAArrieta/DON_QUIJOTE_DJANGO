from django.db import models

class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio_unit = models.DecimalField(max_digits=10, decimal_places=2)
    precio_doc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    categoria_id = models.ForeignKey(ProductoCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} -> {self.precio_unit}"
    


