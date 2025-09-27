from django.contrib import admin
from .models import Projeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado_por', 'criado_em')
    search_fields = ('nome', 'descricao')
    filter_horizontal = ('participantes',)
