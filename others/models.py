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


class Helping(models.Model):
    """
    Помощь ( вопрос - ответ )
    """
    question = models.CharField('Вопрос', max_length=300)
    answer = models.CharField('Ответ', max_length=300, blank=True)
    image = models.ForeignKey('ImageHelping', on_delete=models.DO_NOTHING, related_name='ImageHelping')


class ImageHelping(models.Model):
    """
    Картинка для помощи
    """
    image = models.ImageField(Helping, upload_to='images/')

    def __str__(self):
        return self.image.name


class Image(models.Model):
    """
    Изображения для помощи
    """
    image = models.ImageField('Изображения', upload_to='images_help')


class OurAdvantages(models.Model):
    """
    Наши преимущества
    """
    icon = models.ImageField('Изображение', upload_to='images_ouradvantages', validators=[validate_file_extension])
    header = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание', max_length=1500)
    valid_extensions = ['.png', '.svg']


class MainPage(models.Model):
    """
    Слайдер.Главная страница
    """
    image = models.ImageField('Изображение', upload_to='images_mainpage')
    link = models.URLField('Ссылка', blank=True)


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
    ('Gmail', 'Gmail'),
    ('Instagram', 'Instagram'),
    ('Telegram', 'Telegram'),
    ('WhatsApp', 'Whatsapp')
)


class Footer(models.Model):
    logo = models.ImageField('Логотип', upload_to='images_footer')
    description = models.TextField('Текстовая информация', max_length=1500)
    num = models.CharField('Номер в хедере', max_length=100)


class Header(models.Model):
    type = models.CharField('Тип', max_length=100, choices=social_media)
    link = models.URLField('Ссылка')

    def save(self, *args, **kwargs):
        if self.type == 'Number':
            self.link = f'{self.link}'
        elif self.type == 'Whatsapp':
            self.link = f'https://wa.me/{self.link}'
        elif self.type == 'Gmail':
            self.link == f'{self.link}'
        elif self.type == 'Instagram':
            self.link = f'https://www.instagram.com/{self.link}/'
        elif self.type == 'Telegram':
            self.link = f'https://t.me/{self.link}/'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.type


#

class FloatingButton(models.Model):
    """
    Плавающая кнопка
    """
    whatsapp = models.CharField('Whatsapp номер', max_length=100)
    link = models.URLField('Whatsapp ссылка', max_length=100)
    telegram = models.URLField('Telegram ссылка', max_length=100)

    def __str__(self):
        return self.whatsapp


choice = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)


class BackCall(models.Model):
    name = models.CharField('Поле для имени', max_length=200)
    number = models.CharField('Поле для номера', max_length=200)
    backcall = models.CharField('Тип обратный звонок', choices=choice, max_length=10)
    data = models.DateTimeField(auto_now=True)
    called = models.CharField('Статус позвонили', choices=choice, max_length=10)
