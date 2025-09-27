# usuarios/apps.py

from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    # O atributo 'name' DEVE corresponder ao nome da pasta/pacote do seu app.
    name = 'usuarios'
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'Contas de Usuários' # Opcional: nome amigável para o Admin