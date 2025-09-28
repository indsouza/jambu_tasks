from django import forms
from .models import Projeto

class FormularioProjeto(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'participantes']
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "participantes": forms.SelectMultiple(attrs={"class": "form-control"}),
        }

