from django import forms
from . import models

class PedidoForm(forms.ModelForm):
    class Meta:
        model = models.Pedido
        fields = "__all__"
        # widgets = {
        #     "nombre": forms.TextInput(attrs={"class": "form-control"}),
        #     "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        #     "precio": forms.TextInput(attrs={"class": "form-control"}),
        #     "categoria_id": forms.Select(attrs={"class": "form-control"}),
        # }