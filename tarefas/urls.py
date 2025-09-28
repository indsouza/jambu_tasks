from django.urls import path
from .views import (
    ListaTarefas, DetalheTarefa, CriarTarefa,
    EditarTarefa, ExcluirTarefa
)

app_name='tarefas'

urlpatterns = [
    path('', ListaTarefas.as_view(), name='lista_tarefas'),
    path('nova/', CriarTarefa.as_view(), name='criar_tarefa'),
    path('<int:pk>/', DetalheTarefa.as_view(), name='detalhe_tarefa'),
    path('<int:pk>/editar/', EditarTarefa.as_view(), name='editar_tarefa'),
    path('<int:pk>/excluir/', ExcluirTarefa.as_view(), name='excluir_tarefa'),
]
