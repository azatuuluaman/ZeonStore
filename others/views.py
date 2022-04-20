from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import serializers, models
from .serializers import NewsSerializer, HelpingSerializer, PublicOfferSerializer, FooterSerializer, FloatingButtonSerializer, BackCallSerializer, \
    HeaderSerializer


class AboutUsViewSet (ModelViewSet):
    serializer_class = serializers.AboutUsSerializer
    queryset = models.AboutUs.objects.all()

class Pagination(PageNumberPagination):
    page_size = 1
    max_page_size = 8

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


class NewsViewSet(ModelViewSet):
    """
    Новости
    """
    queryset = models.News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = Pagination

class HelpingViewSet(ModelViewSet):
    """
    Помощь
    """
    queryset = models.Helping.objects.all()
    serializer_class = HelpingSerializer

class PublicOfferViewSet(ModelViewSet):
    """
    Публичная оферта
    """
    queryset = models.PublicOffer.objects.all()
    serializer_class = PublicOfferSerializer

class FooterViewSet(ModelViewSet):
    """
    Футер
    """
    queryset = models.Footer.objects.all()
    serializer_class = FooterSerializer

class HeaderViewSet(ModelViewSet):
    """
    Header
    """
    queryset = models.Header.objects.all()
    serializer_class = HeaderSerializer


class FloatingButtonViewSet(ModelViewSet):
    """
    Плавающая кнопка. 1
    """
    queryset = models.FloatingButton.objects.all()
    serializer_class = FloatingButtonSerializer


class BackCallViewSet(ModelViewSet):
    """
    Плавающая кнопка. 2
    """
    queryset = models.BackCall.objects.all()
    serializer_class = BackCallSerializer

