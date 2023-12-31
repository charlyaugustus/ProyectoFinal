# Generated by Django 4.2.5 on 2023-09-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=60)),
                ("apellido", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=254)),
                ("tipo_servicio", models.CharField(max_length=40)),
            ],
        ),
    ]
