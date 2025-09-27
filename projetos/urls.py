from django.urls import path
from .views import (
    ListaProjetos, DetalheProjeto, CriarProjeto,
    EditarProjeto, ExcluirProjeto
)

urlpatterns = [
    path('', ListaProjetos.as_view(), name='lista_projetos'),
    path('novo/', CriarProjeto.as_view(), name='criar'),
    path('<int:pk>/', DetalheProjeto.as_view(), name='detalhe'),
    path('<int:pk>/editar/', EditarProjeto.as_view(), name='editar'),
    path('<int:pk>/excluir/', ExcluirProjeto.as_view(), name='excluir'),
]
