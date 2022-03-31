from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import serializers, models
from .serializers import NewsSerializer


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