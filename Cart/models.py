from django.contrib.auth.models import User
from django.db import models
from product.models import Product


class Cart(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='my_cart')

    def price(self):
        """
        Старая цена
        """
        if self.cart_items:
            return sum([i.product.old_price for i in self.cart_items.all()])
        else:
            return 0

    def qty_line(self):
        """
        Количество линеек
        """
        if self.cart_items:
            return sum([i.qty for i in self.cart_items.all()])
        else:
            return 0

    def qty_count_item(self):
        """
        Количество вещей для подсчета количества товаров
        """
        if self.cart_items:
            return sum([i.product.count_item for i in self.cart_items.all()])
        else:
            return 0

    def qty_product(self):
        """
        Количество товаров
        """
        if self.cart_items:
            return self.qty_line() * self.qty_count_item()
        else:
            return 0

    def qty_count_discount(self):
        """
        Чтобы вытащить скидку
        """
        if self.cart_items:
            return sum([i.product.discount for i in self.cart_items.all()])
        else:
            return 0

    def discount(self):
        """
        Скидка
        """
        if self.cart_items:
            return self.price() - self.qty_count_discount()
        else:
            return 0

    def total_price(self):
        """
        Итоговая цена
        """
        if self.cart_items:
            return self.price() - self.discount()
        else:
            return 0


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items',
                             on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, related_name='product_in_cart',
                                on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1,
                                      verbose_name='count_of_line')
    qty_products = models.PositiveIntegerField(default=1,
                                               verbose_name='count_of_products')
    image = models.ImageField('Изображение', null=True, blank=True)
    color = models.CharField('Цвет',
                             max_length=15, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    old_price = models.IntegerField(null=True, blank=True)
    final_price = models.IntegerField(null=True, blank=True, verbose_name='Цена без скидки')
    final_price_discount = models.IntegerField(null=True, blank=True, verbose_name='Цена с учетом скидки')
    discount = models.IntegerField(null=True, blank=True, verbose_name='Сумма скидки')
    size = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return f"{self.product.title} = cart items"

    def save(self, *args, **kwargs):
        self.size = self.product.size
        self.price = self.product.price
        self.old_price = self.product.old_price
        self.qty_products = self.qty * self.product.count_item
        self.color = str([i.color_code for i in self.product.color.all()][:1])
        self.final_price = self.qty * self.price
        self.discount = (self.price - self.old_price) * self.qty
        self.final_price_discount = self.final_price - self.discount
        self.image = self.product.photo
        super().save(*args, **kwargs)

