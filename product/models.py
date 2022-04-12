from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.db import models
from colorfield.fields import ColorField


class Product(models.Model):
    """
    Товар
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
    count_item = models.IntegerField('Количество вещей', default=1)
    size = models.CharField('Размерный ряд', max_length=100)
    material = models.CharField('Материал товара', max_length=50)
    favorites = models.BooleanField('Избранные', default=False)

    def __str__(self):
        return self.title

class ProductGallery(models.Model):
    """
    Изображения
    """
    image = models.ImageField('Изображение', upload_to='images/')

    def __str__(self):
        return self.image.name


class Collection(models.Model):
    """
    Коллекции, категории
    """
    title = models.CharField('Название', max_length=50)
    img = models.ImageField('Изображение', upload_to='images')

    def __str__(self):
        return self.title


class ProductColor(models.Model):
    """
    Цвета для товаров
    """
    title = models.CharField("Название цвета", max_length=50)
    color_code = ColorField('Код цвета', default='#FF0000' , max_length=50)

    def __str__(self):
        return self.title

order = (
    ('New', 'New'),
    ('Registration', 'Registration'),
    ('Cancel', 'Cancel'),
)


class UserOrder(models.Model):
    """
    Информация юзера. Заказ.
    """
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.CharField('Электронная почта', max_length=50)
    phone = models.CharField('Номер телефона', max_length=50)
    country = models.CharField('Страна', max_length=50)
    city = models.CharField('Город', max_length=50)
    date_registration = models.DateTimeField(auto_now=True)
    status_order = models.CharField('Статус заказа', choices=order, max_length=50, default='New')


class Basket(models.Model):
    """
    Корзина
    """
    

# class ProductOrder(models.Model):
#     """
#
#     """
#     img = models.ManyToManyField('ProductGallery', verbose_name='product_gallery')
#     title = models.CharField('Название товара', max_length=50)
#     count_item = models.IntegerField('Количество вещей', default=1)
#     size = models.CharField('Размерный ряд', max_length=100)
#     color = models.ManyToManyField('ProductColor')
#     price = models.IntegerField('Цена товара')
#     old_price = models.IntegerField('Старая цена', null=True, blank=True)
#     discount = models.DecimalField('Размер скидки', max_digits=100, blank=True, decimal_places=2)


# class Order(models.Model):
#     numbers_line =



