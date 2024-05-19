from django.urls import path
from . import views

app_name = "pedidos"

urlpatterns =[
    path('', views.home, name = "home"),
    path("pedido/list/", views.PedidoList.as_view(), name="pedido_list"),
    path("pedido/detail/<int:pk>", views.PedidoDetail.as_view(), name="pedido_detail"),
    path("pedido/create/", views.PedidoCreate, name="pedido_create"),
    path("pedido/update/<int:pk>", views.PedidoUpdate.as_view(), name="pedido_update"),
    path("pedido/delete/<int:pk>", views.PedidoDelete.as_view(), name="pedido_delete"), 
]