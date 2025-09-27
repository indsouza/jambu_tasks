from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'responsavel', 'status', 'prazo')
    list_filter = ('status', 'projeto')
    search_fields = ('titulo', 'descricao')
