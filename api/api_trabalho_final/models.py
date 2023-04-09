from django.db import models

# Create your models here.


class Images(models.Model):
    id_imagem = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)
    imagem = models.ImageField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'


class PacotesPromocionais(models.Model):
    id_pacotes_promocionais = models.IntegerField(primary_key=True)
    nomepacotepromocional = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pacotes_promocionais'


class Servicos(models.Model):
    id_servico = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()
    marcada = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'servicos'


class ServicosPacotesPromocionais(models.Model):
    fk_id_servico = models.ForeignKey(Servicos, models.DO_NOTHING, db_column='fk_id_servico', blank=True, null=True)
    fk_id_pacotes_promocionais = models.ForeignKey(PacotesPromocionais, models.DO_NOTHING, db_column='fk_id_pacotes_promocionais', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicos_pacotes_promocionais'
