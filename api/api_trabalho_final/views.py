from rest_framework import viewsets
from api_trabalho_final.models import Comentario, Image, Servico, ServicoPacotePromocional, PacotePromocional
from api_trabalho_final.serializer import ComentariosSerializer, ImagesSerializer, ServicosSerializer, ServicosPacotesPromocionaisSerializer, PacotesPromocionaisSerializer


class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializer


class ServicosViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicosSerializer


class ServicosPacotesPromocionaisViewSet(viewsets.ModelViewSet):
    queryset = ServicoPacotePromocional.objects.all()
    serializer_class = ServicosPacotesPromocionaisSerializer


class PacotesPromocionaisViewSet(viewsets.ModelViewSet):
    queryset = PacotePromocional.objects.all()
    serializer_class = PacotesPromocionaisSerializer
