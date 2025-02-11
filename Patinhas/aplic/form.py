from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Querocachorro, Querogato


class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    cpf = forms.CharField(label='CPF')
    data_nascimento = forms.DateField()
    telefone = forms.CharField(label='Telefone')

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'cpf', 'data_nascimento', 'email', 'username', 'password1', 'password2']


class QueroadotarForm(forms.ModelForm):
    class Meta:
        model = Querocachorro or Querogato
        fields = ['mensagem']
