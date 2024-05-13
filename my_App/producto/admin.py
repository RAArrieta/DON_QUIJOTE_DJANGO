from django.contrib import admin
from . import models

# admin.site.site_title = "Productos"

# class ProductoCategoriaAdmin(admin.ModelAdmin):
#     list_display = ("nombre",)
#     list_display_links = ("nombre",)
    
admin.site.register(models.ProductoCategoria)
admin.site.register(models.Producto)
