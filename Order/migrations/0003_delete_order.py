# Generated by Django 4.0.3 on 2022-04-14 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_order_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
