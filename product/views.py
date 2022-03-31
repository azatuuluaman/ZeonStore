from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import models
from .models import Collection, Product
from .serializers import ProductSerializer, CollectionSerializer, SimilarProductSerializer


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


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer
    serializer_class = SimilarProductSerializer

@api_view(['GET'])
def filter (request, pk):
    """
    Фильтр для вывода 5ти похожих товаров.
    """
    collection = Collection.objects.get(id=pk)
    queryset = Product.objects.filter(collection=collection)[0:5]
    serializer = SimilarProductSerializer(queryset, many = True)
    return Response (serializer.data)

class CollectionViewSet(ModelViewSet):
    """
    Коллекции
    """
    serializer_class = CollectionSerializer
    queryset = models.Collection.objects.all()
    pagination_class = Pagination

# class SimilarProductViewSet(ModelViewSet):
#     serializer_class = SimilarProductSerializer
#     queryset = models.Product.objects.all()
#     pagination_class =



    # Entry.objects.all().filter(pub_date__year=2006)


