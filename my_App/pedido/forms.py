from django import forms
from django.forms.models import inlineformset_factory
from .models import Pedido, PedidoProducto

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = "__all__"

class PedidoProductoForm(forms.ModelForm):
    class Meta:
        model = PedidoProducto
        fields = ['producto', 'cantidad']

PedidoProductoFormSet = inlineformset_factory(Pedido, PedidoProducto, form=PedidoProductoForm, extra=1, can_delete=True)
