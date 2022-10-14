from django.db import models


class Empresa(models.Model):
    nome = models.CharField("Nome", max_length=150)
    atuacao = models.CharField("Atuação", max_length=150, null=True, blank=True)
    cidade = models.CharField("Cidade", max_length=150)
    whatsapp = models.CharField("Whatsapp", max_length=30, null=True, blank=True)
    email = models.EmailField("E-mail")
    enviar_email = models.BooleanField("Enviar Email", default=True)
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    def __str__(self):
        return self.nome
