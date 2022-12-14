# Generated by Django 4.1.2 on 2022-10-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Empresa",
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
                ("nome", models.CharField(max_length=150, verbose_name="Nome")),
                (
                    "atuacao",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Atuação"
                    ),
                ),
                ("cidade", models.CharField(max_length=150, verbose_name="Cidade")),
                (
                    "whatsapp",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Whatsapp"
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="E-mail")),
                (
                    "enviar_email",
                    models.BooleanField(default=True, verbose_name="Enviar Email"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Cadastrado em"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Modificado em"
                    ),
                ),
            ],
        ),
    ]
