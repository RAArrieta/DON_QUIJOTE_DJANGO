from django.db import models
from django.utils import timezone

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('Entregado', 'Entregado'),
        ('Pendiente', 'Pendiente'),
        ('Cancelado', 'Cancelado')
    ]

    PAGO_CHOICES = [
        ('Efectivo', 'P. EFECT'),
        ('Transferencia', 'P. TRANSF'),
        ('Debito', 'P. DEBITO'),
        ('Cobrar', 'COBRAR')
    ]

    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Pendiente')
    hora = models.TimeField(editable=False)
    direccion = models.CharField(max_length=100)
    cliente = models.TextField(max_length=100, blank=True, null=True)
    observacion = models.TextField(max_length=100, blank=True, null=True)
    producto = models.ForeignKey("producto.Producto", on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(default=1)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pago = models.CharField(max_length=13, choices=PAGO_CHOICES, default='Cobrar')

    def save(self, *args, **kwargs):
        if not self.id:
            now = timezone.localtime(timezone.now())
            self.hora = now.replace(second=0, microsecond=0).time()
        self.precio_total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido {self.id} - {self.producto.nombre} - {self.estado} - Hora: {self.hora.strftime('%H:%M')}"
