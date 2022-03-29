from rest_framework.viewsets import ModelViewSet
from . import serializers, models

class AboutUsViewSet (ModelViewSet):
    serializer_class = serializers.AboutUsSerializer
    queryset = models.AboutUs.objects.all()





