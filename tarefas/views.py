from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from .models import Tarefa
from .forms import FormularioTarefa
from projetos.models import Projeto


class ListaTarefas(LoginRequiredMixin, generic.ListView):
    model = Tarefa
    template_name = 'tarefas/lista_tarefas.html'
    context_object_name = 'tarefas'
    ordering = ['-criado_em']

    def get_queryset(self):
        user = self.request.user
        return Tarefa.objects.filter(
            models.Q(responsavel=user) |  # se a tarefa tem responsável
            models.Q(projeto__criador=user) |  # se o user é criador do projeto
            models.Q(projeto__participantes=user)  # se o user é participante do projeto
        ).distinct()

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        # só mostra projetos que o usuário criou ou participa
        contexto['projetos'] = Projeto.objects.filter(
            models.Q(criador=self.request.user) | models.Q(participantes=self.request.user)
        ).distinct()
        return contexto


class DetalheTarefa(LoginRequiredMixin, generic.DetailView):
    model = Tarefa
    template_name = 'tarefas/detalhe_tarefa.html'
    context_object_name = 'tarefa'

    def get_queryset(self):
        user = self.request.user
        return Tarefa.objects.filter(
            models.Q(responsavel=user) |
            models.Q(projeto__criador=user) |
            models.Q(projeto__participantes=user)
        ).distinct()


class CriarTarefa(LoginRequiredMixin, generic.CreateView):
    model = Tarefa
    form_class = FormularioTarefa
    template_name = 'tarefas/formulario_tarefa.html'
    success_url = reverse_lazy('tarefas:lista_tarefas')

    def get_initial(self):
        inicial = super().get_initial()
        projeto_id = self.request.GET.get('projeto')
        if projeto_id:
            inicial['projeto'] = projeto_id
        return inicial

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # filtra os projetos disponíveis no form para só os acessíveis ao user
        form.fields['projeto'].queryset = Projeto.objects.filter(
            models.Q(criador=self.request.user) | models.Q(participantes=self.request.user)
        ).distinct()
        return form


class EditarTarefa(LoginRequiredMixin, generic.UpdateView):
    model = Tarefa
    form_class = FormularioTarefa
    template_name = 'tarefas/formulario_tarefa.html'
    success_url = reverse_lazy('tarefas:lista_tarefas')

    def get_queryset(self):
        user = self.request.user
        return Tarefa.objects.filter(
            models.Q(responsavel=user) |
            models.Q(projeto__criador=user) |
            models.Q(projeto__participantes=user)
        ).distinct()


class ExcluirTarefa(LoginRequiredMixin, generic.DeleteView):
    model = Tarefa
    template_name = 'tarefas/confirma_exclusao_tarefa.html'
    success_url = reverse_lazy('tarefas:lista_tarefas')

    def get_queryset(self):
        user = self.request.user
        return Tarefa.objects.filter(
            models.Q(responsavel=user) |
            models.Q(projeto__criador=user) |
            models.Q(projeto__participantes=user)
        ).distinct()

