# Generated by Django 4.0.3 on 2022-04-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0010_floatingbutton'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floatingbutton',
            name='telegram',
            field=models.CharField(max_length=100, verbose_name='Telegram ссылка'),
        ),
        migrations.AlterField(
            model_name='floatingbutton',
            name='whatsapp',
            field=models.CharField(default='whatsapp.com/', max_length=100, verbose_name='Whatsapp номер'),
        ),
    ]
