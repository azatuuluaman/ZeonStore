from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import About_Us
from .serializers import About_UsSerializer

class About_UsList(APIView):
    """
    Перечислите все фрагменты или создайте новый фрагмент.
    """
    def get(self, request, format=None):
        aboutus = About_Us.objects.all()
        serializer =About_UsSerializer(aboutus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = About_UsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class About_UsDetail(APIView):
    """
    Получить, обновить или удалить экземпляр фрагмента.
    """
    def get_object(self, pk):
        try:
            return About_Us.objects.get(pk=pk)
        except About_Us.DoesNotExist:
            raise Http404

    def get (self, request, pk , format=None):
        aboutus = self.get_object(pk)
        serializer = About_UsSerializer(aboutus)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        aboutus = self.get_object(pk)
        serializer = About_UsSerializer(aboutus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        aboutus = self.get_object(pk)
        aboutus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





