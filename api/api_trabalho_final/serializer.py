from rest_framework import serializers
from api_trabalho_final.models import Images, PacotesPromocionais, ServicosPacotesPromocionais, Servicos


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ('id_imagem', 'descricao', 'imagem')


class PacotesPromocionaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacotesPromocionais
        fields = '__all__'


class ServicosPacotesPromocionaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicosPacotesPromocionais
        fields = '__all__'


class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = '__all__'


