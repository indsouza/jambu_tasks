from django.contrib import admin
from .models import Projeto

@admin.register(Projeto)
class AdministradorProjeto(admin.ModelAdmin):
    list_display = ('titulo', 'criador', 'criado_em')
    search_fields = ('titulo', 'descricao')
    filter_horizontal = ('participantes',)
