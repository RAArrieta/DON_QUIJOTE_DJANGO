# Generated by Django 5.0.6 on 2024-05-11 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='ProductoCategoria',
        ),
    ]
