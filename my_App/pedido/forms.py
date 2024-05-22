from django import forms
from django.forms.models import inlineformset_factory
from .models import Pedido, PedidoProducto

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = "__all__"
        widgets = {
            "estado": forms.Select(attrs={"class": "form-control"}),
            "hora": forms.TimeInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "cliente": forms.TextInput(attrs={"class": "form-control"}),
            "observacion": forms.TextInput(attrs={"class": "form-control"}),
            "precio_total": forms.NumberInput(attrs={"class": "form-control"}),
            "pago": forms.Select(attrs={"class": "form-control"}),
        }

class PedidoProductoForm(forms.ModelForm):
    class Meta:
        model = PedidoProducto
        fields = ['producto', 'cantidad']
        widgets = {
            "producto": forms.Select(attrs={"class": "form-control"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control"}),
        }

PedidoProductoFormSet = inlineformset_factory(Pedido, PedidoProducto, form=PedidoProductoForm, extra=1, can_delete=True)
