# tarefas/models.py
from django.db import models
from django.contrib.auth.models import User
from projetos.models import Projeto

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('to_do', 'A Fazer'),
        ('in_progress', 'Em Progresso'),
        ('done', 'Concluída'),
    ]
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefas')
    prazo = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_do')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.projeto.nome})"
