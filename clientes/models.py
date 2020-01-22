from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=14)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    data_de_nascimento = models.CharField(max_length=10)
    idade = models.IntegerField()
