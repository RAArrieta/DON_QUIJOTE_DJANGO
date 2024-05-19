# Generated by Django 5.0.6 on 2024-05-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_rename_medio_pago_pedido_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('Entregado', 'Entregado'), ('Pendiente', 'Pendiente'), ('Cancelado', 'Cancelado')], default='Pendiente', max_length=10),
        ),
    ]
