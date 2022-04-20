from rest_framework import serializers
from Cart.models import CartItem, Cart
from product.serializers import Cart2Serializer
from Order.models import Order


class CartItemSerializer(serializers.ModelSerializer):
    product = Cart2Serializer()

    class Meta:
        model = CartItem
        fields = ('product',)


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'qty_line', 'qty_product', 'price', 'discount',
                  'total_price', 'cart_items',)
