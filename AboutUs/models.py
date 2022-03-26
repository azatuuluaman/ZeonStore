from django.db import models

class About_Us(models.Model):
    image1 = models.ImageField('Изображение', upload_to='images')
    image2 = models.ImageField('Изображение', upload_to='images')
    image3 = models.ImageField('Изображение', upload_to='images')
    header = models.CharField('Заголовок', max_length=50)
    description = models.TextField('Описание', max_length=1500)

    def __str__(self):
        return self.header


