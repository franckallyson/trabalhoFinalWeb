from rest_framework import viewsets
from api_trabalho_final.models import Images, Servicos, ServicosPacotesPromocionais, PacotesPromocionais
from api_trabalho_final.serializer import ImagesSerializer, ServicosSerializer, ServicosPacotesPromocionaisSerializer, PacotesPromocionaisSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class ServicosViewSet(viewsets.ModelViewSet):
    queryset = Servicos.objects.all()
    serializer_class = ServicosSerializer


class ServicosPacotesPromocionaisViewSet(viewsets.ModelViewSet):
    queryset = ServicosPacotesPromocionais.objects.all()
    serializer_class = ServicosPacotesPromocionaisSerializer


class PacotesPromocionaisViewSet(viewsets.ModelViewSet):
    queryset = PacotesPromocionais.objects.all()
    serializer_class = PacotesPromocionaisSerializer
