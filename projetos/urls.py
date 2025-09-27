# projetos/urls.py
from django.urls import path
from .views import (
    ProjectListView, ProjectDetailView, ProjectCreateView,
    ProjectUpdateView, ProjectDeleteView
)

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('novo/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('<int:pk>/editar/', ProjectUpdateView.as_view(), name='project-update'),
    path('<int:pk>/deletar/', ProjectDeleteView.as_view(), name='project-delete'),
]
