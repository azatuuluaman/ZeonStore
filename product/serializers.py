from rest_framework import serializers
from .models import Product, Collection


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('title', 'id')


class SimilarProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'cover_photo', 'title', 'price', 'old_price', 'discount', 'size', 'color')


class CollectionProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('collection', 'id', 'cover_photo', 'title', 'price', 'old_price', 'discount', 'size', 'color',)


class ProductTypeSerializer(serializers.ModelSerializer):
    """
    Избранные, хит продаж, новинки.
    """
    class Meta:
        model = Product
        fields = ('id', 'cover_photo', 'title', 'price', 'old_price', 'discount', 'size', 'color', 'favorites', 'bestseller', 'new_clothes')


class Cart2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'cover_photo', 'title', 'size', 'color', 'price', 'old_price',)
