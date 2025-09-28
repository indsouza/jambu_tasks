from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class FormularioCadastroUsuario(UserCreationForm):
    primeiro_nome = forms.CharField(max_length=30, required=True, label='Nome:')
    sobrenome = forms.CharField(max_length=30, required=True, label='Último nome:')
    email = forms.EmailField(required=True, label='E-mail:')

    class Meta:
        model = User
        fields = ('username', 'primeiro_nome', 'sobrenome', 'email', 'password1', 'password2')
        labels = {
            "username":"Usuário",
            "password1":"Senha",
            "password2":"Confirmar senha"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['primeiro_nome']
        user.last_name = self.cleaned_data['sobrenome']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class FormularioLogin(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'username',
            'autofocus': True
        }),
        label='Usuário'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'autocomplete': 'current-password'
        }),
        label='Senha'
    )

