from django.contrib import admin
from .models import Campanha

@admin.register(Campanha)
class CampanhaAdmin(admin.ModelAdmin):
    #resource_class = BookResource
    fieldsets = (
        ("Campanha", {"fields": ("tipo", "nome", "envios")}),

    )
    filter_horizontal = (
        "envios",

    )

    jazzmin_section_order = ("tipo", "nome", "envios")