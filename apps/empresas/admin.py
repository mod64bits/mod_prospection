from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    #resource_class = BookResource
    fieldsets = (
        ("Cadastro", {"fields": ("nome", "atuacao", "cidade", "whatsapp", "email")}),

    )

    jazzmin_section_order = ("nome", "atuacao", "cidade", "whatsapp", "email")
