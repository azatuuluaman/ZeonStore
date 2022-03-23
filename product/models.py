from django.db import models

class Product(models.Model):
    """
    Продукт.
    """
    name = models.CharField('Название товара' , max_length=50)
    description = models.TextField('Описание', max_length= 1300)
    fabric_structure = models.CharField('Состав ткани' , max_length=50 )
    material = models.CharField('Материал товара', max_length=50 )
    bestseller = models.BooleanField('Хит продаж', default=False)
    novelties = models.BooleanField('Новинки', default=True)

    # color = models.ManyToManyField('Color',verbose_name='Цвет' ,related_name='product' )
    # collection = models.ForeignKey('category',
    #                                on_delete=models.DO_NOTHING,
    #                                null=True, blank=True)

class Category(models.Model):
    """
    Деление по коллекции и полу (м\ж)
    """
    title = models.CharField('Название коллекции' , max_length=50)
    gender = models.CharField('Пол', max_length=50)

    def __str__(self):
        return self.title


class Product_item(models.Model):
    """
    То, что может изменяться
    """
    price = models.IntegerField('Цена товара')
    old_price = models.IntegerField('Старая цена', null=True, blank=True)
    size_range = models.CharField("Размерный ряд", max_length=50)
    color = models.CharField('Цвет', max_length=50)
    number_in_ruler = models.PositiveSmallIntegerField('Количество в линейке', default=0)
    item_number = models.CharField('Артикул товара', max_length=50)



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


