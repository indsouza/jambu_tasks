from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    titulo = models.CharField("Título", max_length=200, default="Sem título")
    descricao = models.TextField("Descrição", blank=True)
    participantes = models.ManyToManyField(
        User,
        related_name='participacao_projetos',
        blank=True,
        verbose_name="Participantes"
    )
    criador = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projetos_criados',
        verbose_name="Criador"
    )
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return self.titulo

