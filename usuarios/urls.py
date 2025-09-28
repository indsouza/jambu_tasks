from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CadastrarUsuario, perfil
from .forms import FormularioLogin  # <-- importa o formulário de login customizado

urlpatterns = [
    path('cadastrar/', CadastrarUsuario.as_view(), name='cadastrar'),
    path(
        'entrar/',
        auth_views.LoginView.as_view(
            template_name='usuarios/entrar.html',
            authentication_form=FormularioLogin   # <-- usa o form customizado
        ),
        name='entrar'
    ),
    path('sair/', auth_views.LogoutView.as_view(), name='sair'),
    path('perfil/', perfil, name='perfil'),
]
