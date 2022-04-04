# Generated by Django 4.0.3 on 2022-04-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0006_alter_ouradvantages_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=1500, verbose_name='Описание')),
            ],
        ),
        migrations.AddField(
            model_name='mainpage',
            name='image',
            field=models.ImageField(default=1, upload_to='images_mainpage', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]