from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models  # necessário para usar Q
from .models import Projeto
from .forms import FormularioProjeto
from tarefas.models import Tarefa


class ListaProjetos(LoginRequiredMixin, generic.ListView):
    model = Projeto
    template_name = 'projetos/lista_projetos.html'
    context_object_name = 'projetos'
    ordering = ['-criado_em']

    def get_queryset(self):
        user = self.request.user
        return Projeto.objects.filter(
            models.Q(criador=user) | models.Q(participantes=user)
        ).distinct()


class DetalheProjeto(LoginRequiredMixin, generic.DetailView):
    model = Projeto
    template_name = 'projetos/detalhe_projeto.html'
    context_object_name = 'projeto'

    def get_queryset(self):
        user = self.request.user
        return Projeto.objects.filter(
            models.Q(criador=user) | models.Q(participantes=user)
        ).distinct()

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        # adiciona as tarefas ligadas a este projeto
        contexto['tarefas'] = Tarefa.objects.filter(projeto=self.object)
        return contexto


class CriarProjeto(LoginRequiredMixin, generic.CreateView):
    model = Projeto
    form_class = FormularioProjeto
    template_name = 'projetos/formulario_projeto.html'
    success_url = reverse_lazy('projetos:lista_projetos')

    def form_valid(self, form):
        form.instance.criador = self.request.user
        return super().form_valid(form)


class EditarProjeto(LoginRequiredMixin, generic.UpdateView):
    model = Projeto
    form_class = FormularioProjeto
    template_name = 'projetos/formulario_projeto.html'
    success_url = reverse_lazy('projetos:lista_projetos')

    def get_queryset(self):
        user = self.request.user
        return Projeto.objects.filter(
            models.Q(criador=user) | models.Q(participantes=user)
        ).distinct()


class ExcluirProjeto(LoginRequiredMixin, generic.DeleteView):
    model = Projeto
    template_name = 'projetos/confirma_exclusao_projeto.html'
    success_url = reverse_lazy('projetos:lista_projetos')

    def get_queryset(self):
        user = self.request.user
        return Projeto.objects.filter(
            models.Q(criador=user) | models.Q(participantes=user)
        ).distinct()


