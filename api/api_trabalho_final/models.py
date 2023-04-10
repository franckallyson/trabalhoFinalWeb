from django.db import models

# Create your models here.


class Images(models.Model):
    descricao = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='images/')


class PacotesPromocionais(models.Model):
    nomepacotepromocional = models.CharField(max_length=100)


class Servicos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()
    marcada = models.BooleanField()


class ServicosPacotesPromocionais(models.Model):
    fk_id_servico = models.ForeignKey(Servicos, models.DO_NOTHING, db_column='fk_id_servico', blank=True, null=True)
    fk_id_pacotes_promocionais = models.ForeignKey(PacotesPromocionais, models.DO_NOTHING, db_column='fk_id_pacotes_promocionais', blank=True, null=True)
