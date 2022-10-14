from django.db import models
from apps.empresas.models import Empresa


class Campanha(models.Model):
    TIPO_CHOICE = (
        ("condominios", "CONDOMÍNIOS"),
        ("empresas", "EMPRESAS"),
        ("redes", "REDES"),
        ("prestacao", "PRESTAÇÃO DE SERVIÇOS"),
    )
    tipo = models.CharField("Tipo de Campanha", max_length=30, choices=TIPO_CHOICE, default="condominios")
    nome = models.CharField("Nome", max_length=50)
    envios = models.ManyToManyField(Empresa, verbose_name="Empresas")
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    def __str__(self):
        return self.nome

