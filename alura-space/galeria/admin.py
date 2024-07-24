from django.contrib import admin
from galeria.models import Fotografia

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'categoria', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome', 'legenda')
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 20

admin.site.register(Fotografia, FotografiaAdmin)