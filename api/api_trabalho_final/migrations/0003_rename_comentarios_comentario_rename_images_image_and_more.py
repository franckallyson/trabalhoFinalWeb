# Generated by Django 4.2 on 2023-04-10 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_trabalho_final', '0002_comentarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comentarios',
            new_name='Comentario',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RenameModel(
            old_name='PacotesPromocionais',
            new_name='PacotePromocional',
        ),
        migrations.RenameModel(
            old_name='Servicos',
            new_name='Servico',
        ),
        migrations.RenameModel(
            old_name='ServicosPacotesPromocionais',
            new_name='ServicoPacotePromocional',
        ),
    ]
