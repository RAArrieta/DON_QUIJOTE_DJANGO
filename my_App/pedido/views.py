from django.shortcuts import render, redirect
from django.db import transaction
from .forms import PedidoForm, PedidoProductoFormSet
from .models import Pedido
from . import models
from django.urls import reverse_lazy
from django.views.generic import (DeleteView, DetailView, ListView, UpdateView,)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection


def home(request):
    return render(request, "pedido/index.html")

class PedidoDetail(LoginRequiredMixin, DetailView):
    model = models.Pedido

class PedidoList(LoginRequiredMixin, ListView):
    model = models.Pedido

    def get_queryset(self):
        queryset = models.Pedido.objects.all()
        consulta = self.request.GET.get("consulta")
        estado = self.request.GET.get("estado")
        
        if consulta:
            queryset = queryset.filter(nombre__icontains=consulta)
        
        if estado:
            queryset = queryset.filter(estado=estado)
        
        return queryset
       
class PedidoUpdate(LoginRequiredMixin, UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido/pedido_update.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['pedido_form'] = PedidoForm(self.request.POST, instance=self.object)
            data['formset'] = PedidoProductoFormSet(self.request.POST, instance=self.object)
        else:
            data['pedido_form'] = PedidoForm(instance=self.object)
            data['formset'] = PedidoProductoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        pedido_form = context['pedido_form']
        formset = context['formset']
        with transaction.atomic():
            self.object = pedido_form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(pedido_form)

    def get_success_url(self):
        return reverse_lazy('pedidos:pedido_list')
    
class PedidoDelete(LoginRequiredMixin, DeleteView):
    model = models.Pedido
    success_url = reverse_lazy("pedidos:pedido_list")

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
            return redirect('pedidos:pedido_list')  
    else:
        pedido_form = PedidoForm()
        formset = PedidoProductoFormSet()

    return render(request, 'pedido/pedido_create.html', {
        'pedido_form': pedido_form,
        'formset': formset,
    })
    
@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_all_orders(request):
    if request.method == 'POST':
        Pedido.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='pedido_pedido'")
        messages.success(request, 'Todos los pedidos han sido eliminados y el contador de IDs ha sido reiniciado.')
        return redirect('pedidos:pedido_list') 

    return render(request, 'pedido/pedidotodos_confirm_delete.html')
