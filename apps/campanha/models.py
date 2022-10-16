from django.db import models
from apps.empresas.models import Empresa
from apps.emailtemplate.models import EmailTemplate


class Campanha(models.Model):
    tipo = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE, verbose_name="Email Template",
                             null=True, blank=True, related_name="camp_template")
    nome = models.CharField("Nome", max_length=50, unique=True)
    envios = models.ManyToManyField(Empresa, verbose_name="Empresas")
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    def __str__(self):
        return self.nome

