from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import FormularioCadastroUsuario

class CadastrarUsuario(generic.CreateView):
    form_class = FormularioCadastroUsuario
    template_name = 'usuarios/cadastrar.html'
    success_url = reverse_lazy('usuarios:entrar')

    def form_valid(self, form):
        usuario = form.save()
        login(self.request, usuario)
        return super().form_valid(form)

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')
