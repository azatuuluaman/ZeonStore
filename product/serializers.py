from rest_framework import serializers
from .models import Product, Collection, ProductColor, ProductGallery


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        exclude = ('id',)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    color = ColorSerializer(many=True)
    collection = serializers.SlugRelatedField(slug_field='title', read_only=True)
    cover_photo = ImageSerializer(many=True)

    class Meta:
        model = Product
        exclude = ('photo',)


class SimilarProductSerializer(serializers.ModelSerializer):
    color = ColorSerializer(many=True)
    collection = serializers.SlugRelatedField(slug_field='title', read_only=True)
    cover_photo = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'cover_photo', 'title', 'price', 'old_price', 'discount', 'size', 'color')


class CollectionProductSerializer(serializers.ModelSerializer):
    color = ColorSerializer(many=True)
    collection = serializers.SlugRelatedField(slug_field='title', read_only=True)
    cover_photo = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('collection', 'id', 'cover_photo', 'title', 'price', 'old_price', 'discount', 'size', 'color',)


class ProductTypeSerializer(serializers.ModelSerializer):
    """
    Избранные, хит продаж, новинки.
    """
    color = ColorSerializer(many=True)
    cover_photo = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'cover_photo', 'title', 'price', 'old_price', 'discount', 'size', 'color', 'favorites', 'bestseller', 'new_clothes')


class Cart2Serializer(serializers.ModelSerializer):
    color = ColorSerializer(many=True)
    cover_photo = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'cover_photo', 'title', 'size', 'color', 'price', 'old_price',)

