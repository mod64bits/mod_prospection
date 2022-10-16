from django.contrib import admin
from django.contrib import messages
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
        for item in queryset:
            for email in item.envios.all():
                EmailTemplate.send(
                    item.tipo.template_key, {
                        "mensagem": item.tipo.plain_text,
                    }
                    , emails=[email.email],
                )
        self.message_user(request, "Campanha Processada com Sucesso!", messages.SUCCESS)

    enviar_campanha.short_description = "Enviar Campanha"