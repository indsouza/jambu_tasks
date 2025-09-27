# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

# exemplo: perfil simples (opcional)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
