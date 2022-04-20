from django.db import models
from ruamel import yaml
from Cart.models import Cart

order = (
    ('New', 'Новый'),
    ('Registration', 'Оформлен'),
    ('Cancel', 'Отменен'),
)


class Order(models.Model):
    """
    Информация юзера. Заказ.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.CharField('Электронная почта', max_length=50)
    phone = models.CharField('Номер телефона', max_length=50)
    country = models.CharField('Страна', max_length=50)
    city = models.CharField('Город', max_length=50)
    date_registration = models.DateTimeField(auto_now=True)
    status_order = models.CharField('Статус заказа', choices=order, max_length=50, default='New')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def order_details(self):
        result = {
            'Last name': self.ordering.last_name,
            'Email address': self.ordering.email,
            'Phone number': str(self.ordering.phone),
            'Country': self.ordering.country,
            'City': self.ordering.city,
            'Date registration': self.date_registration,
        }
        return yaml.dump(result, default_flow_style=False)

    def __str__(self):
        return 'Order {}'.format(self.id)
