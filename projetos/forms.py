from django import forms
from .models import Projeto

class FormularioProjeto(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'participantes']

