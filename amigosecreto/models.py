from django.db import models

class Participante(models.Model):
    nome = models.CharField()
    cod = models.IntegerField()
    presentes = models.ForeignKey()
    amigo = models.IntegerField()


class Presente(models.Model):
    descricao = models.CharField()
    tamanho = models.CharField()
    link = models.CharField()
    observacoes = models.CharField()