from django import forms
from .models import Tarefa

class FormularioTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ["nome", "detalhes", "projeto", "responsavel", "status", "prazo"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "detalhes": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "projeto": forms.Select(attrs={"class": "form-control"}),
            "responsavel": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "prazo": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
