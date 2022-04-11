from rest_framework import serializers
from .models import Product, Collection

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('title' , 'id')

class SimilarProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id' ,'cover_photo' , 'title', 'price', 'old_price', 'discount', 'size', 'color')

class CollectionProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'collection','id', 'cover_photo', 'title',  'price', 'old_price', 'discount','size',  'color',)

class  BestsellerSerializer(serializers.ModelSerializer):
    """
    Хит продаж
    """
    class Meta:
        model = Product
        fields = ('id' ,'cover_photo' , 'title', 'price', 'old_price', 'discount', 'size', 'color','favorites')


class NewClothesSerializer(serializers.ModelSerializer):
    """
    Новинки
    """
    class Meta:
        model = Product
        fields = ('id' ,'cover_photo' , 'title', 'price', 'old_price', 'discount', 'size', 'color', 'favorites')


class FavoritesSerializer(serializers.ModelSerializer):
    """
    Избранные
    """
    class Meta:
        model = Product
        fields = ('id', 'cover_photo', 'title', 'price', 'old_price', 'discount', 'size', 'color', 'favorites')



