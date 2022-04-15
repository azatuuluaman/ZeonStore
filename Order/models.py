from django.db import models
from Cart.models import Cart

order = (
    ('New', 'New'),
    ('Registration', 'Registration'),
    ('Cancel', 'Cancel'),
)


# class Order(models.Model):
#     """
#     Информация юзера. Заказ.
#     """
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
#     first_name = models.CharField('Имя', max_length=50)
#     last_name = models.CharField('Фамилия', max_length=50)
#     email = models.CharField('Электронная почта', max_length=50)
#     phone = models.CharField('Номер телефона', max_length=50)
#     country = models.CharField('Страна', max_length=50)
#     city = models.CharField('Город', max_length=50)
#     date_registration = models.DateTimeField(auto_now=True) # дата заказа
#     status_order = models.CharField('Статус заказа', choices=order, max_length=50, default='New')
#
#     class Meta:
#         ordering = ('-date_registration')
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'
#
#     def __str__(self):
#         return 'Order {}'.format(self.id)
#
#     def get_total_cost(self):
#         return sum(item.get_cost() for item in self.products.all())