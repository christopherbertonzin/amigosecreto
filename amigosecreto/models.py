from django.db import models


class Participante(models.Model):
    cod = models.IntegerField(primary_key=True,)
    nome = models.CharField(max_length=20)
    cod_amigo = models.IntegerField()


class Presente(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    tamanho = models.CharField(max_length=2)
    link = models.CharField(max_length=500)
    observacoes = models.CharField(max_length=500)

class Sorteados(models.Model):
    cod_participante = models.IntegerField()
