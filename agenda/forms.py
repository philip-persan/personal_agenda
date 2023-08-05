from django import forms

from .models import Contato


class GeradorContatoForm(forms.Form):
    qtd = forms.IntegerField(
        widget=forms.NumberInput,
        label='Quantidade de Contatos'
    )


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = [
            'nome', 'sobrenome',
            'telefone', 'email', 'imagem'
        ]
        widgets = {
            'nome': forms.TextInput,
            'sobrenome': forms.TextInput,
            'telefone': forms.TextInput,
            'email': forms.EmailInput
        }
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'telefone': 'Telefone',
            'email': 'Email'
        }
