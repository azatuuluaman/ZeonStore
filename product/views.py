from rest_framework.viewsets import ModelViewSet
from . import models
from .models import Collection
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = models.Product.objects.all()
    pagination_class = Collection.PaginationCollection




