# Generated by Django 4.0.3 on 2022-04-13 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0002_cartitem_final_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total_products',
            new_name='total_price',
        ),
    ]
