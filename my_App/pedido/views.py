from django.shortcuts import render, redirect


from .forms import PedidoForm, PedidoProductoFormSet

from . import forms, models
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView,)
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, "pedido/index.html")


class PedidoDetail(LoginRequiredMixin, DetailView):
    model = models.Pedido

class PedidoList(LoginRequiredMixin, ListView):
    model = models.Pedido

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Pedido.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Pedido.objects.all()
        return object_list
    
# class PedidoCreate(LoginRequiredMixin, CreateView):
#     model = models.Pedido
#     form_class = forms.PedidoForm
#     success_url = reverse_lazy("pedidos:home")
    
class PedidoUpdate(LoginRequiredMixin, UpdateView):
    model = models.Pedido
    form_class = forms.PedidoForm
    success_url = reverse_lazy("pedidos:home")
    
class PedidoDelete(LoginRequiredMixin, DeleteView):
    model = models.Pedido
    success_url = reverse_lazy("pedidos:home")







def PedidoCreate(request):
    if request.method == "POST":
        pedido_form = PedidoForm(request.POST)
        formset = PedidoProductoFormSet(request.POST)
        if pedido_form.is_valid() and formset.is_valid():
            pedido = pedido_form.save()
            pedido_productos = formset.save(commit=False)
            for pedido_producto in pedido_productos:
                pedido_producto.pedido = pedido
                pedido_producto.save()
            pedido.save()
            return redirect('pedidos:pedido_list')  # Redirigir a una página de éxito
    else:
        pedido_form = PedidoForm()
        formset = PedidoProductoFormSet()

    return render(request, 'pedido/pedido_create.html', {
        'pedido_form': pedido_form,
        'formset': formset,
    })
