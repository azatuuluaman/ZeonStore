from rest_framework.filters import SearchFilter

from . import serializers
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import models
from others.serializers import MainPageSerializer, OurAdvantagesSerializer
from others.models import MainPage, OurAdvantages
from .models import Collection, Product
from .serializers import ProductSerializer, CollectionSerializer, \
    SimilarProductSerializer, CollectionProductSerializer, ProductTypeSerializer


class BasicPagination(PageNumberPagination):
    page_size = 8
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


class TenPagination(PageNumberPagination):
    page_size = 10
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


class TwelvePagination(PageNumberPagination):
    page_size = 12
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
    filter_backends = [SearchFilter]
    search_fields = ['title']
    serializer_class = ProductSerializer



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
    pagination_class = BasicPagination


class CollectionProductViewSet(ModelViewSet):
    """
    Коллекция (Товары)
    """
    queryset = models.Product.objects.all()
    serializer_class = CollectionProductSerializer
    pagination_class = TwelvePagination


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
    serializer_class = ProductTypeSerializer


@api_view(['GET'])
def new_products(request):
    """
    Фильтр для вывода 5ти товаров со статусом новинки
    """
    queryset = Product.objects.all().filter(new_clothes=True)[0:5]
    serializer = SimilarProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_search(request):
    """
    Поисковик
    """
    obj = []
    number = models.Collection.objects.all().count()  #
    if number >= 5:
        for i in models.Collection.objects.all().values_list('id')[0:5]:  #
            if models.Product.objects.all().filter(collection=i).first() is None:
                pass
            else:
                obj.append(models.Product.objects.all().filter(collection=i).first())
    else:
        for i in models.Collection.objects.all().values_list('id')[0:number]:
            if models.Product.objects.all().filter(collection=i).first() is None:
                pass
            else:
                obj.append(models.Product.objects.all().filter(collection=i).first())
    serializer = serializers.ProductSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def mainpage(request):
    """
    Главная страница API
    """
    main_page = MainPage.objects.all()
    main_page_ser = MainPageSerializer(main_page, many=True).data

    bestseller = Product.objects.all().filter(bestseller=True)[0:8]
    bestseller_ser = ProductTypeSerializer(bestseller, many=True).data

    new = Product.objects.all().filter(new_clothes=True)[0:4]
    new_ser = ProductTypeSerializer(new, many=True).data

    collection = Collection.objects.all()
    collection_ser = CollectionSerializer(collection, many=True).data

    ouradvantages = OurAdvantages.objects.all()
    ouradvantages_ser = OurAdvantagesSerializer(ouradvantages, many=True).data

    response_data = {}
    response_data['main_page'] = main_page_ser
    response_data['products'] = bestseller_ser
    response_data['products'] = new_ser
    response_data['products'] = collection_ser
    response_data['products'] = ouradvantages_ser

    return Response({"Слайдер, список": main_page_ser,
                     "Хит продаж": bestseller_ser,
                     "Новинки": new_ser,
                     "Коллекция список ": collection_ser,
                     "Наши преимущества": ouradvantages_ser},
                    status=status.HTTP_200_OK)


class FavoritesViewSet(ModelViewSet):
    """
     Фильтр для вывода 12ти товаров со статусом избранное
    """
    queryset = models.Product.objects.all().filter(favorites=True)[0:12]
    serializer_class = ProductTypeSerializer
