from django.db import models

class UsuarioCargo(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    telefono = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)   
    cargo_id = models.ForeignKey(UsuarioCargo, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.cargo_id}: {self.apellido}, {self.nombre}"
