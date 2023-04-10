from django.contrib import admin
from api_trabalho_final.models import Comentario, Image, Servico, ServicoPacotePromocional, PacotePromocional

# Register your models here.
admin.site.register([Comentario, Image, Servico, ServicoPacotePromocional, PacotePromocional])
