# tarefas/forms.py
from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'projeto', 'responsavel', 'prazo', 'status']
        widgets = {
            'prazo': forms.DateInput(attrs={'type': 'date'}),
        }
