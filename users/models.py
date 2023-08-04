import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    id = models.UUIDField(
        verbose_name=_('ID'),
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    email = models.EmailField(
        verbose_name=_('Email'),
        unique=True,
        blank=False,
        null=True
    )
    telefone = models.CharField(
        max_length=20,
        verbose_name=_('Phone Number'),
        blank=True,
        null=True
    )
    data_nascimento = models.DateField(
        verbose_name=_('Data de Nascimento'),
        blank=False,
        null=True
    )

    def __str__(self) -> str:
        return self.get_full_name()

    def save(self, *args, **kwargs):
        # Verifique se o username está vazio (None) e se o email está definido
        if not self.username and self.email:
            self.username = self.email
        super().save(*args, **kwargs)

    # Defina o campo email como o campo de nome de usuário
    USERNAME_FIELD = 'email'
    # Defina quais campos serão obrigatórios ao criar um usuário
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['first_name', ]
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['telefone']),
            models.Index(fields=['data_nascimento']),
        ]
