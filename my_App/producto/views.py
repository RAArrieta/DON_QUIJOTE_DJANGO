from . import forms, models
from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView,)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

def home(request):
    return render(request, "producto/index.html")


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria

class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.ProductoCategoria.objects.all()
        return object_list
    
class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:home")
    
class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    
class ProductoCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = models.    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")


class ProductoDetail(DetailView):
    model = models.Producto

class ProductoList(ListView):
    model = models.Producto

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Producto.objects.all()
        return object_list

class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:home")
    
class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")
    
class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")