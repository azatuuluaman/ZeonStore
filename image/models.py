from django.core.exceptions import ValidationError
from django.db import models
from product.models import Product_item


class Image(models.Model):
    img = models.ImageField('Изображение', upload_to='images/')
    product_item = models.ForeignKey(Product_item, on_delete=models.CASCADE, verbose_name='Продукт')

    def clean(self):
        if len(Image.objects.all()) >= 8:
            raise ValidationError('Не больше 8 изображений')

    def __str__(self):
        return self.img.name


