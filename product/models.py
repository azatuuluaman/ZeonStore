from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.db import models


class Product(models.Model):
    """
    Продукт
    """
    title = models.CharField('Название товара', max_length=50)
    price = models.IntegerField('Цена товара')
    old_price = models.IntegerField('Старая цена', null=True, blank=True)
    discount = models.DecimalField('Размер скидки', max_digits=100, blank= True, decimal_places=2)
    fabric_structure = models.CharField('Состав ткани', max_length=50)
    bestseller = models.BooleanField('Хит продаж', default=False)
    new_clothes = models.BooleanField('Новинки', default=True)
    article = models.CharField('Артикул товара', max_length=50)
    description = models.TextField('Описание', max_length=1500)


    cover_photo = models.ManyToManyField('ProductGallery', verbose_name='product_gallery')
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE, related_name='product')
    color = models.ManyToManyField('ProductColor')
    count_item = models.IntegerField('Количество вещей')

    size = models.CharField('Размерный ряд', max_length=100)
    material = models.CharField('Материал товара', max_length=50)

    def __str__(self):
        return self.title


#
# PRODUCT_COLOR_CHOICES = (
#     ('BLA', 'Black'),
#     ('WH', 'White'),
#     ('RE', 'Red'),
#     ('GR', 'Green'),
#     ('YE', 'Yellow'),
#     ('BLU', 'Blue'),
#     ('OR', 'Orange'),
#     ('GR', 'Grey'),
# )


class ProductGallery(models.Model):
    """
    Изображения
    """
    image = models.ImageField('Изображение', upload_to='images/')

    def __str__(self):
        return self.image.name


class Collection(models.Model):
    title = models.CharField('Название', max_length=50)
    img = models.ImageField('Изображение', upload_to='images')

    def __str__(self):
        return self.title

    class PaginationCollection(PageNumberPagination):
        page_size = 1
        max_page_size = 10

        def get_paginated_response(self, data):
            return Response({
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'results': data
            })


class ProductColor(models.Model):
    """

    """
    title = models.CharField("Название цвета", max_length=50)
    color_code = models.CharField('Код цвета', max_length=50)

    # def clean(self):
    #     if len(ProductColor.objects.all()) >= 8:
    #         raise ValidationError('Не больше 8 изображений')
    #
    def __str__(self):
        return self.title

# все маленькие задачи
# class offer(models.Model):
#     """
#     Публичная оферта.
#     """
#     header = models.CharField('Заголовок', max_length=100)
#     description = models.TextField('Описание', max_length=1300)
#
#     def __str__(self):
#         return self.header

#
# class slider_main_page (models.Model):
#     """
#     Слайдер. Главная страница.
#     """
#     image = models.ImageField(upload_to='images/', null=True)
#     "нужно сделать ссылку, хотя она не обязательная"
