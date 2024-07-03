from django.contrib import admin
from galeria.models import Fotografia

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'categoria', 'publicado')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome', 'legenda')
    list_filter = ('categoria',)
    list_editable = ('publicado',)
    list_per_page = 20

admin.site.register(Fotografia, FotografiaAdmin)