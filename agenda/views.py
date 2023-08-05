from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import ContatoForm, GeradorContatoForm
from .models import Contato
from .utils.scripts.make_db import make_contatos


class GeradorDeContatoView(View):
    def get(self, request):
        form = GeradorContatoForm()
        ctx = {
            'form': form
        }
        return render(request, 'agenda/pages/gerador.html', ctx)

    def post(self, request):
        POST = request.POST
        qtd = int(POST['qtd'])
        make_contatos(qtd, request)
        messages.success(request, f'{qtd} Contatos Criados!')
        return redirect('agenda:gerador')


class ContatoListView(View):
    def get(self, request):
        contatos = Contato.objects.all().select_related('user')
        ctx = {
            'contatos': contatos
        }
        return render(request, 'agenda/pages/contatos_list.html', ctx)


class ContatoCreateView(View):
    def get(self, request):
        form = ContatoForm()
        ctx = {
            'form': form
        }
        return render(request, 'agenda/pages/contatos_create.html', ctx)

    def post(self, request):
        form = ContatoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato Salvo com Sucesso!')
            return redirect('agenda:create')


class ContatoUpdateView(View):
    def get(self, request, id):
        contato = Contato.objects.get(id=id)
        form = ContatoForm(instance=contato)
        ctx = {
            'contato': contato,
            'form': form
        }
        return render(request, 'agenda/pages/contatos_update.html', ctx)

    def post(self, request, id):
        contato = Contato.objects.get(id=id)
        form = ContatoForm(request.POST or None, instance=contato)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato atualizado com sucesso!')
            return redirect('agenda:list')
        else:
            ctx = {
                'contato': contato,
                'form': form
            }
            messages.error(request, 'Houve um erro ao editar o contato')
            return render(request, 'agenda/pages/contatos_update.html', ctx)


class ContatoDeleteView(View):
    def get(self, request, id):
        contato = get_object_or_404(Contato, id=id)
        ctx = {
            'contato': contato,
        }
        return render(request, 'agenda/pages/contatos_delete.html', ctx)

    def post(self, request, id):
        contato = get_object_or_404(Contato, id=id)
        contato.delete()
        messages.success(request, 'Contato apagado com sucesso!')
        return redirect('agenda:list')
