from django.urls import path
from . import views

app_name = "producto"

urlpatterns =[
    path('', views.home, name = "home"),
    path("producto/list/", views.ProductoList.as_view(), name="producto_list"),
    path("producto/detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),
    path("producto/create/", views.ProductoCreate.as_view(), name="producto_create"),
    path("producto/update/<int:pk>", views.ProductoUpdate.as_view(), name="producto_update"),
    path("producto/delete/<int:pk>", views.ProductoDelete.as_view(), name="producto_delete"), 
]

urlpatterns += [
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/detail/<int:pk>", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    path("productocategoria/create/", views.ProductoCategoriaCreate.as_view(), name="productocategoria_create"),
    path("productocategoria/update/<int:pk>", views.ProductoCategoriaUpdate.as_view(), name="productocategoria_update"),
    path("productocategoria/delete/<int:pk>", views.ProductoCategoriaDelete.as_view(), name="productocategoria_delete"),
]