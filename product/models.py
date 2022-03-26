from django.db import models
from django.core.exceptions import ValidationError
from collection.models import Collection
from django.core.exceptions import ValidationError
from django.db import models
from product.models import Product_item


class Product(models.Model):
    """
    Продукт
    """
    name = models.CharField('Название товара', max_length=50)
    price = models.IntegerField('Цена товара')
    old_price = models.IntegerField('Старая цена', null=True, blank=True)
    fabric_structure = models.CharField('Состав ткани', max_length=50)
    material = models.CharField('Материал товара', max_length=50)
    novelties = models.BooleanField('Новинки', default=True)
    item_number = models.CharField('Артикул товара', max_length=50)
    description = models.TextField('Описание', max_length=1500)
    bestseller = models.BooleanField('Хит продаж', default=False)

    # cover_photo
    # collection_id
    title = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='Название коллекции')
    gender = models.CharField('Пол', max_length=50)

    def __str__(self):
        return self.name


PRODUCT_COLOR_CHOICES = (
    ('BLA', 'Black'),
    ('WH', 'White'),
    ('RE', 'Red'),
    ('GR', 'Green'),
    ('YE', 'Yellow'),
    ('BLU', 'Blue'),
    ('OR', 'Orange'),
    ('GR', 'Grey'),
)


class Product_gallery(models.Model):
    """
    Изображения
    """
    img = models.ImageField('Изображение', upload_to='images/')
    product_item = models.ForeignKey(Product_item, on_delete=models.CASCADE, verbose_name='Продукт')

    def clean(self):
        if len(Image.objects.all()) >= 8:
            raise ValidationError('Не больше 8 изображений')

    def __str__(self):
        return self.img.name


class Product_number(models.Model):
    """
    Количество конкретного вида продукта
    """
    size_range = models.CharField("Размерный ряд", max_length=50)
    number_in_ruler = models.PositiveSmallIntegerField('Количество в линейке')
    product_item = models.ForeignKey(Product_item, on_delete=models.CASCADE, related_name='product_number')

    def __str__(self):
        return str(self.number_in_ruler)


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
#
# class about_us(models.Model):
#     """
#     О нас.
#     """
#     image = models.ImageField(upload_to='images/', null=True)
#     header = models.CharField('Заголовок', max_length=100)
#     description = models.TextField('Описание', max_length=1300)
#
#     def __str__(self):
#         return self.header
#
#
# class slider_main_page (models.Model):
#     """
#     Слайдер. Главная страница.
#     """
#     image = models.ImageField(upload_to='images/', null=True)
#     "нужно сделать ссылку, хотя она не обязательная"
