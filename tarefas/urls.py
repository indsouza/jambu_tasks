from django.urls import path
from .views import (
    ListaTarefas, DetalheTarefa, CriarTarefa,
    EditarTarefa, ExcluirTarefa
)

urlpatterns = [
    path('', ListaTarefas.as_view(), name='lista_tarefas'),
    path('nova/', CriarTarefa.as_view(), name='criar'),
    path('<int:pk>/', DetalheTarefa.as_view(), name='detalhe'),
    path('<int:pk>/editar/', EditarTarefa.as_view(), name='editar'),
    path('<int:pk>/excluir/', ExcluirTarefa.as_view(), name='excluir'),
]
