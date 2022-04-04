from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import models
from .models import Collection, Product
from .serializers import ProductSerializer, CollectionSerializer, SimilarProductSerializer, CollectionProductSerializer


class Pagination(PageNumberPagination):
    page_size = 1
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


class CollectionProductPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 12

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


class ProductViewSet(viewsets.ModelViewSet):
    """
    Товар
    """
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer
    # serializer_class = SimilarProductSerializer


@api_view(['GET'])
def filter(request, pk):
    """
    Фильтр для вывода 5ти похожих товаров.
    """
    collection = Collection.objects.get(id=pk)
    queryset = Product.objects.filter(collection=collection)[0:5]
    serializer = SimilarProductSerializer(queryset, many=True)
    return Response(serializer.data)


class CollectionViewSet(ModelViewSet):
    """
    Коллекции
    """
    queryset = models.Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = Pagination


class CollectionProductViewSet(ModelViewSet):
    """
    Коллекция (Товары)
    """
    queryset = models.Product.objects.all()
    serializer_class = CollectionProductSerializer
    pagination_class = CollectionProductPagination


@api_view(['GET'])
def collection_products(request, pk):
    """
    Фильтр для вывода 12ти товаров из одной коллекции
    """
    collection = Collection.objects.get(id=pk)
    queryset = Product.objects.filter(collection=collection)[0:12]
    serializer = SimilarProductSerializer(queryset, many=True)
    return Response(serializer.data)

class NewProductViewSet(ModelViewSet):
    """
    Список новинки
    """
    queryset = models.Product.objects.all()
    serializer_class = CollectionProductSerializer


@api_view(['GET'])
def new_products(request):
    """
    Фильтр для вывода 5ти товаров со статусом новинки
    """
    # collection = Collection.objects.get(id=pk)
    queryset = Product.objects.all().filter(new_clothes=True)[0:5]
    serializer = SimilarProductSerializer(queryset, many=True)
    return Response(serializer.data)
# Model View Set
# Generix - когда пишешь апишку , выбираешь
