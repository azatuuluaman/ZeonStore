from django.db import models
from .validators import validate_file_extension
class AboutUs(models.Model):
    """
    О нас
    """
    image1 = models.ImageField('Изображение', upload_to='images')
    image2 = models.ImageField('Изображение', upload_to='images')
    image3 = models.ImageField('Изображение', upload_to='images')
    title = models.CharField('Заголовок', max_length=50)
    description = models.TextField('Описание', max_length=1500)

    def __str__(self):
        return self.title

class News(models.Model):
    """
    Новости
    """
    image = models.ImageField('Изображение', upload_to='images_news')
    title = models.CharField('Заголовок', max_length=50)
    description = models.TextField('Описание', max_length=1500)

    def __str__(self):
        return self.title

class Helping (models.Model):
    """
    Помощь ( вопрос - ответ )
    """
    question = models.CharField('Вопрос', max_length=300)
    answer = models.CharField('Ответ', max_length=300, blank=True)
    image = models.ForeignKey('Image', on_delete=models.DO_NOTHING ,related_name='help')


class Image(models.Model):
    """
    Изображения для помощи
    """
    image=models.ImageField('Изображения', upload_to='images_help')


class OurAdvantages(models.Model):
    """
    Наши преимущества
    """
    icon = models.ImageField('Изображение', upload_to='images_ouradvantages', validators=[validate_file_extension])
    header = models.CharField('Заголовок', max_length=100)
    valid_extensions = ['.png', '.svg']

class MainPage(models.Model):
    """
    Слайдер.Главная страница
    """
    image = models.ImageField('Изображение', upload_to='images_mainpage')

class PublicOffer(models.Model):
    """
    Публичная оферта.
    """
    header = models.CharField('Заголовок', max_length=50)
    description = models.TextField('Описание', max_length=1500)

    def __str__(self):
        return self.header


social_media = (
    ('Number', 'Number'),
    ('Gmail' , 'Gmail'),
    ('Instagram','Instagram'),
    ('Telegram', 'Telegram'),
    ('WhatsApp', 'Whatsapp')
)

class Footer(models.Model):
    """
    Первая вкладка футер
    """
    logo = models.ImageField('Логотип', upload_to='images_footer')
    description = models.TextField('Текстовая информация', max_length=1500)
    num = models.PositiveIntegerField('Номер в хедере')
    type = models.CharField('Тип', max_length=100, choices=social_media)
    link = models.URLField('Ссылка')
    phone1 = models.CharField('Номера телефона 1' , max_length=20)
    phone2 = models.CharField('Номера телефона 2', max_length=20, blank=True)
    phone3 = models.CharField('Номера телефона 3', max_length=20, blank = True)
    gmail = models.CharField('Почта', max_length=100)

