from random import randint

from faker import Faker

from agenda.models import Contato

fake = Faker('pt_BR')


def make_contatos(qtd: int, request):
    usuario = request.user
    for i in range(qtd):
        nome = fake.first_name()
        sobrenome = fake.last_name()
        email = f'{nome.lower()}{sobrenome.lower()}@email.com'
        telefone = randint(11111111111, 99999999999)
        Contato.objects.create(
            user=usuario,
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            telefone=telefone
        )
