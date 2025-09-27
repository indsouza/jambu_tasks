# projetos/models.py
from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    participantes = models.ManyToManyField(User, related_name='projetos', blank=True)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='projetos_criados')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
