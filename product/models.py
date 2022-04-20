from django.db import models
from colorfield.fields import ColorField


class Product(models.Model):
    """
    Товар
    """
    title = models.CharField('Название товара',
                             max_length=50)
    price = models.IntegerField('Цена товара')
    old_price = models.IntegerField('Старая цена',
                                    null=True,
                                    blank=True)
    discount = models.IntegerField('Размер скидки', null=True, blank=True, default=0)
    fabric_structure = models.CharField('Состав ткани', max_length=50)
    bestseller = models.BooleanField('Хит продаж', default=False)
    new_clothes = models.BooleanField('Новинки', default=True)
    article = models.CharField('Артикул товара', max_length=50)
    description = models.TextField('Описание', max_length=1500)
    cover_photo = models.ManyToManyField('ProductGallery', verbose_name='product_gallery')
    photo = models.ImageField( upload_to='images')
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE, related_name='product')
    color = models.ManyToManyField('ProductColor')
    count_item = models.IntegerField('Количество вещей', default=1)  # линейка
    size = models.CharField('Размерный ряд', max_length=100)
    material = models.CharField('Материал товара', max_length=50)
    favorites = models.BooleanField('Избранные', default=False)

    def __str__(self):
        return self.title


class ProductGallery(models.Model):
    """
    Изображения для товара
    """
    image = models.ImageField('Изображение', upload_to='images/')

    def __str__(self):
        return self.image.url


class Collection(models.Model):
    """
    Коллекции, категории для товара
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
    color_code = ColorField('Код цвета', default='#FF0000', max_length=50, null=True)

    def __str__(self):
        return self.title
