from rest_framework.viewsets import ModelViewSet

from Cart import models
from Cart.serializers import CartSerializer


class CartViewSet(ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = CartSerializer


