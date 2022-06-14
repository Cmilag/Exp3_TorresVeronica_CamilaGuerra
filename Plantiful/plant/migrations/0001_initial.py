# Generated by Django 4.2.dev20220603193729 on 2022-06-10 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=100, verbose_name="Nombre")),
                ("apellido", models.CharField(max_length=100, verbose_name="Apellido")),
                ("correo", models.EmailField(max_length=100, verbose_name="E-mail")),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "nombre",
                    models.CharField(max_length=50, verbose_name="Nombre Producto"),
                ),
                ("valor", models.CharField(max_length=10, verbose_name="Valor")),
                (
                    "categoria",
                    models.CharField(max_length=50, verbose_name="Categoría"),
                ),
            ],
        ),
    ]
