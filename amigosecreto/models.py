from django.db import models

class AmigoSecreto(models.Model):
    descricao = models.CharField(max_length=50)
    cod_amigosecreto = models.IntegerField()


class Participante(models.Model):
    cod_participante = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    id_amigo_sorteado = models.IntegerField()


class Presente(models.Model):
    id_participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=20)
    tamanho = models.CharField(max_length=2, blank=True)
    observacao = models.TextField(blank=True)
