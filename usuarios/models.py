from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField("Biografia", blank=True)

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username
