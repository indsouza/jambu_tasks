# gerenciador/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('projetos/', include(('projetos.urls', 'projetos'), namespace='projetos')),
    path('tarefas/', include(('tarefas.urls', 'tarefas'), namespace='tarefas')),
    path('', include(('projetos.urls', 'projetos'), namespace='root')),  # página inicial -> projetos
]
