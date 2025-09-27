from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CadastrarUsuario, perfil

urlpatterns = [
    path('cadastrar/', CadastrarUsuario.as_view(), name='cadastrar'),
    path('entrar/', auth_views.LoginView.as_view(template_name='usuarios/entrar.html'), name='entrar'),
    path('sair/', auth_views.LogoutView.as_view(), name='sair'),
    path('perfil/', perfil, name='perfil'),
]
