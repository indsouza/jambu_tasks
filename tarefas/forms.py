from django import forms
from .models import Tarefa

class FormularioTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'detalhes', 'projeto', 'responsavel', 'prazo', 'status']
        widgets = {
            'prazo': forms.DateInput(attrs={'type': 'date'}),
        }

