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
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pago = models.CharField(max_length=13, choices=PAGO_CHOICES, default='Cobrar')

    def save(self, *args, **kwargs):
        if not self.id:
            now = timezone.localtime(timezone.now())
            self.hora = now.replace(second=0, microsecond=0).time()
        super().save(*args, **kwargs)
        
        total_precio = 0
        empanada_cantidad = 0
        empanada_precio_doc = 0
        empanada_precio_unit = 0
        
        for item in self.pedidoproducto_set.all():
            producto = item.producto
            if producto.categoria_id.nombre == 'Empanadas':
                empanada_cantidad += item.cantidad
                empanada_precio_doc = producto.precio_doc
                empanada_precio_unit = producto.precio_unit
            else:
                total_precio += producto.precio_unit * item.cantidad
        
        if empanada_cantidad > 0:
            docenas = empanada_cantidad // 12
            sobrantes = empanada_cantidad % 12
            total_precio += docenas * empanada_precio_doc + sobrantes * empanada_precio_unit
        
        self.precio_total = total_precio
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Pedido {self.id} - {self.estado} - Hora: {self.hora.strftime('%H:%M')}"

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey("producto.Producto", on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"



