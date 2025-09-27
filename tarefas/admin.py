from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class AdministradorTarefa(admin.ModelAdmin):
    list_display = ('nome', 'projeto', 'responsavel', 'status', 'prazo', 'criado_em')
    list_filter = ('status', 'projeto', 'responsavel')
    search_fields = ('nome', 'detalhes')
