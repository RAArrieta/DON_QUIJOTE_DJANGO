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





# from django import forms
# from . import models

# class PedidoForm(forms.ModelForm):
#     class Meta:
#         model = models.Pedido
#         fields = "__all__"
#         # widgets = {
#         #     "nombre": forms.TextInput(attrs={"class": "form-control"}),
#         #     "descripcion": forms.TextInput(attrs={"class": "form-control"}),
#         #     "precio": forms.TextInput(attrs={"class": "form-control"}),
#         #     "categoria_id": forms.Select(attrs={"class": "form-control"}),
#         # }