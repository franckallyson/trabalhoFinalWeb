from django.db import models

# Create your models here.


class Comentario(models.Model):
    nome_usuario = models.CharField(max_length=100)
    comentario = models.TextField()


class Image(models.Model):
    descricao = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='images/')


class PacotePromocional(models.Model):
    nomepacotepromocional = models.CharField(max_length=100)


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()
    marcada = models.BooleanField()


class ServicoPacotePromocional(models.Model):
    fk_id_servico = models.ForeignKey(Servico, models.DO_NOTHING, db_column='fk_id_servico', blank=True, null=True)
    fk_id_pacotes_promocionais = models.ForeignKey(PacotePromocional, models.DO_NOTHING, db_column='fk_id_pacotes_promocionais', blank=True, null=True)
