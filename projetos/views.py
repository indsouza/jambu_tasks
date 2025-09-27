# projetos/views.py
from django.urls import reverse_lazy
from django.views import generic
from .models import Projeto
from .forms import ProjetoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Projeto
    template_name = 'projetos/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        # usuário pode ver projetos onde é participante ou todos (ajuste conforme: aqui mostramos todos)
        return Projeto.objects.all().order_by('-criado_em')

class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Projeto
    template_name = 'projetos/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'projetos/project_form.html'
    success_url = reverse_lazy('projetos:project-list')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'projetos/project_form.html'
    success_url = reverse_lazy('projetos:project-list')

class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Projeto
    template_name = 'projetos/project_confirm_delete.html'
    success_url = reverse_lazy('projetos:project-list')
