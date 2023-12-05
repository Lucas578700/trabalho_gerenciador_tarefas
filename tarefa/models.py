from django.conf import settings
from django.db import models
from django.utils import timezone


class Tarefas(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(max_length=255, default='teste@teste.com')
    descricao = models.TextField(max_length=255)
    status = models.BooleanField(default=False)
