from . import forms, models

from django.shortcuts import render, redirect


def home(request):
    return render(request, "producto/index.html")

# def productocategoria_create(request):
#     return render(request, "producto/productocategoria_create.html")


# class ProductoCategoriaCreate(CreateView):
#     model = models.ProductoCategoria
#     form_class = forms.ProductoCategoriaForm
#     success_url = reverse_lazy("producto:home")

def productocategoria_list(request):
    consulta_producto = models.Producto.objects.all()
    context = {"productos": consulta_producto}
    return render(request, "producto/productocategoria_list.html", context)

def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("producto:home")
    else: 
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/productocategoria_create.html", context={"form": form})