from django.contrib import admin

from .models import Contato


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'nome', 'sobrenome',
        'telefone', 'email'
    ]
    list_display_links = 'user', 'nome', 'sobrenome'
