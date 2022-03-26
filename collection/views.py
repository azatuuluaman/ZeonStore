from django.http import Http404
from django.shortcuts import render
from rest_framework import status, generics, pagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from .models import Collection, PaginationCollection
from collection.serializers import CollectionSerializer
from .models import PaginationCollection

#
# @api_view(['GET'])
# def collection(request):
#     collection = Collection.objects.all()
#     serializer = CollectionSerializer(collection, many=True)
#     return Response(serializer.data)


class CollectionList(APIView, LimitOffsetPagination):
    """
    Перечислите все фрагменты или создайте новый фрагмент.
    """
    def get(self, request, format=None):
        collections = Collection.objects.all()
        results = self.paginate_queryset(collections, request, view=self)

        serializer =CollectionSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CollectionDetail(APIView):
    """
    Получить, обновить или удалить экземпляр фрагмента.
    """
    def get_object(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise Http404

    def get (self, request, pk , format=None):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        collection = self.get_object(pk)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # class Pagination(pagination.PageNumberPagination):
    #     """
    #     Пагинация для результата коллекций
    #     """
    #     page_size = 8
    #     page_size_query_param = 'page_size'
    #     pagination_class = Pagination
    #



    # class CollectionsView(generics.ListAPIView):
    #     queryset = Collection.objects.all()
    #     serializer_class = CollectionSerializer
    #     pagination_class = PaginationCollection

    # def post (self, request, format = None):
    #     serializer = CollectionSerializer (data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status = status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




