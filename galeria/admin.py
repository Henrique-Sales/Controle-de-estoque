from django.contrib import admin
from galeria.models import Fotografia
# Register your models here.

class listando_fotos(admin.ModelAdmin):
    list_display = ["id", "nome", "legenda", "publicada", "data_publicada"]
    list_display_links = ["id", "nome"]
    search_fields= ["nome"]
    list_filter = ["categoria"]
    list_per_page = 10
    list_editable = ["publicada"]

admin.site.register(Fotografia, listando_fotos)