# Generated by Django 4.0.3 on 2022-03-24 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Collection',
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.collection', verbose_name='Название коллекции'),
        ),
    ]
