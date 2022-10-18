from celery import shared_task
from django.contrib import admin
from django.contrib import messages

from mod_prospection.celery import app
from .tasks import send_mail
from .models import Campanha
from .models import EmailTemplate




@admin.register(Campanha)
class CampanhaAdmin(admin.ModelAdmin):
    # resource_class = BookResource
    fieldsets = (
        ("Campanha", {"fields": ("tipo", "nome", "envios")}),

    )
    filter_horizontal = (
        "envios",

    )

    jazzmin_section_order = ("tipo", "nome", "envios")

    actions = ['enviar_campanha']

   # @admin.action(description='Enviar Campanha')
    def enviar_campanha(self, request, queryset):
        contador = 0
        for item in queryset:

            for email in item.envios.all():
                contador += 1
                send_mail.delay(item.tipo.template_key, item.tipo.plain_text, email.email, contador)
        self.message_user(request, "Campanha Processada com Sucesso!", messages.SUCCESS)

    enviar_campanha.short_description = "Enviar Campanha"