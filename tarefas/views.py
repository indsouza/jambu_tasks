# tarefas/views.py
from django.urls import reverse_lazy
from django.views import generic
from .models import Tarefa
from .forms import TarefaForm
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Tarefa
    template_name = 'tarefas/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        qs = Tarefa.objects.all().order_by('-criado_em')
        project = self.request.GET.get('project')
        if project:
            qs = qs.filter(projeto_id=project)
        return qs
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        from projetos.models import Projeto
        ctx['projects'] = Projeto.objects.all()
        return ctx


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tarefa
    template_name = 'tarefas/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'tarefas/task_form.html'
    success_url = reverse_lazy('tarefas:task-list')

    def get_initial(self):
        initial = super().get_initial()
        project = self.request.GET.get('project')
        if project:
            initial['projeto'] = project
        return initial

class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'tarefas/task_form.html'
    success_url = reverse_lazy('tarefas:task-list')

class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tarefa
    template_name = 'tarefas/task_confirm_delete.html'
    success_url = reverse_lazy('tarefas:task-list')
