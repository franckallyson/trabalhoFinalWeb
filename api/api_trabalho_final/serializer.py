from rest_framework import serializers
from api_trabalho_final.models import Comentario, Image, PacotePromocional, ServicoPacotePromocional, Servico


class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    imagem = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Image
        fields = ('id', 'descricao', 'imagem')


class PacotesPromocionaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacotePromocional
        fields = '__all__'


class ServicosPacotesPromocionaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoPacotePromocional
        fields = '__all__'


class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'

