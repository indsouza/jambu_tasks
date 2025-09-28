from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tarefa
from .forms import FormularioTarefa
from projetos.models import Projeto


class ListaTarefas(LoginRequiredMixin, generic.ListView):
    model = Tarefa
    template_name = 'tarefas/lista_tarefas.html'
    context_object_name = 'tarefas'
    ordering = ['-criado_em']

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['projetos'] = Projeto.objects.all()
        return contexto


class DetalheTarefa(LoginRequiredMixin, generic.DetailView):
    model = Tarefa
    template_name = 'tarefas/detalhe_tarefa.html'
    context_object_name = 'tarefa'


class CriarTarefa(LoginRequiredMixin, generic.CreateView):
    model = Tarefa
    form_class = FormularioTarefa
    template_name = 'tarefas/formulario_tarefa.html'
    success_url = reverse_lazy('tarefas:lista_tarefas')  # <-- mantive 'lista' como nome-padrão

    def get_initial(self):
        inicial = super().get_initial()
        projeto_id = self.request.GET.get('projeto')  # pega ?projeto=ID da URL
        if projeto_id:
            inicial['projeto'] = projeto_id
        return inicial


class EditarTarefa(LoginRequiredMixin, generic.UpdateView):
    model = Tarefa
    form_class = FormularioTarefa
    template_name = 'tarefas/formulario_tarefa.html'
    success_url = reverse_lazy('tarefas:lista_tarefas')  # <-- padronizado


class ExcluirTarefa(LoginRequiredMixin, generic.DeleteView):
    model = Tarefa
    template_name = 'tarefas/confirma_exclusao_tarefa.html'
    success_url = reverse_lazy('tarefas:lista_tarefas')  # <-- padronizado

