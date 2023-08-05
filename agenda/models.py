from django.db import models

from users.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/photos/{1}".format(instance.user.first_name, filename)


class Contato(models.Model):
    user = models.ForeignKey(
        verbose_name='Usuário',
        to=User,
        on_delete=models.CASCADE,
        blank=True
    )
    nome = models.CharField(
        verbose_name='Nome',
        max_length=150,
        blank=False,
        null=True
    )
    sobrenome = models.CharField(
        verbose_name='Sobrenome',
        max_length=150,
        blank=False,
        null=True
    )
    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=13,
        blank=False,
        null=True
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    imagem = models.ImageField(
        verbose_name='Foto',
        upload_to=user_directory_path,
        default='user.png'
    )

    def nome_completo(self) -> str:
        frase = f'{self.nome} {self.sobrenome}'
        return frase

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['user', 'nome']
