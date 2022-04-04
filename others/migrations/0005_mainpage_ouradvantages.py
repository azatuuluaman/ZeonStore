# Generated by Django 4.0.3 on 2022-04-01 09:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0004_rename_help_helping'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OurAdvantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='images_ouradvantages', validators=[django.core.validators.validate_image_file_extension], verbose_name='Изображение')),
                ('header', models.CharField(max_length=100, verbose_name='Заголовок')),
            ],
        ),
    ]