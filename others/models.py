from django.db import models

class AboutUs(models.Model):
    image1 = models.ImageField('Изображение', upload_to='images')
    image2 = models.ImageField('Изображение', upload_to='images')
    image3 = models.ImageField('Изображение', upload_to='images')
    title = models.CharField('Заголовок', max_length=50)
    description = models.TextField('Описание', max_length=1500)

    def __str__(self):
        return self.title

class News(models.Model):
    image = models.ImageField('Изображение', upload_to='images_news')
    title = models.CharField('Заголовок', max_length=50)
    description = models.TextField('Описание', max_length=1500)

    def __str__(self):
        return self.title

class Helping (models.Model):
    question = models.CharField('Вопрос', max_length=300)
    answer = models.CharField('Ответ', max_length=300, blank=True)
    image = models.ForeignKey('Image', on_delete=models.DO_NOTHING ,related_name='help')


class Image(models.Model):
        image=models.ImageField('Изображения', upload_to='images_help')




