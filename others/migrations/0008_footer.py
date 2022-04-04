# Generated by Django 4.0.3 on 2022-04-04 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0007_publicoffer_mainpage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='images_footer', verbose_name='Логотип')),
                ('description', models.TextField(max_length=1500, verbose_name='Текстовая информация')),
                ('num', models.PositiveIntegerField(verbose_name='Номер в хедере')),
                ('type', models.CharField(choices=[('Number', 'Number'), ('Gmail', 'Gmail'), ('Instagram', 'Instagram'), ('Telegram', 'Telegram'), ('WhatsApp', 'Whatsapp')], max_length=100, verbose_name='Тип')),
                ('link', models.URLField(verbose_name='Ссылка')),
                ('phone', models.IntegerField(max_length=20, verbose_name='Номера телефона')),
                ('gmail', models.CharField(max_length=100, verbose_name='Почта')),
            ],
        ),
    ]