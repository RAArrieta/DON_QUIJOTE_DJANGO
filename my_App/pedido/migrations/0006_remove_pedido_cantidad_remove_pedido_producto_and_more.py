# Generated by Django 5.0.6 on 2024-05-19 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0005_alter_pedido_estado'),
        ('producto', '0002_rename_categoria_productocategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='producto',
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='producto.producto')),
            ],
        ),
    ]
