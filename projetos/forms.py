# projetos/forms.py
from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'participantes']
        widgets = {
            'participantes': forms.SelectMultiple(attrs={'size': 6}),
        }
