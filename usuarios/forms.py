from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioCadastroUsuario(UserCreationForm):
    primeiro_nome = forms.CharField(max_length=30, required=True, label='Nome')
    sobrenome = forms.CharField(max_length=30, required=True, label='Sobrenome')
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        model = User
        fields = ('username', 'primeiro_nome', 'sobrenome', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['primeiro_nome']
        user.last_name = self.cleaned_data['sobrenome']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
