
from django.db import models
from django.contrib.auth.models import User
from projetos.models import Projeto

class Tarefa(models.Model):
    STATUS = [
        ('a_fazer', 'A Fazer'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    ]
    nome = models.CharField("Nome", max_length=200, default="Sem nome")
    detalhes = models.TextField("Detalhes", blank=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, verbose_name="Projeto")
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='minhas_tarefas', verbose_name="Responsável")
    prazo = models.DateField("Prazo", null=True, blank=True)
    status = models.CharField("Status", max_length=20, choices=STATUS, default='a_fazer')
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return self.nome

