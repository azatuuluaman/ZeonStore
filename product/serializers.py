from rest_framework import serializers
from .models import Product, Collection

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class SimilarProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id' ,'cover_photo' , 'title', 'price', 'old_price', 'discount', 'size', 'color', 'collection')








