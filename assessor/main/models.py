from django.db import models

class Main(models.Model):
    name = models.CharField('ФИО', max_length=100)
    date_birth = models.DateField('Дата рождения')
    phone_number = models.CharField('Номер телефона', max_length=12)
    email = models.EmailField('Email')
    city = models.CharField('Город', max_length=25)
    site_1 = models.URLField('Сайт 1', max_length=250, blank=True)
    site_2 = models.URLField('Сайт 2', max_length=250, blank=True)
    site_3 = models.URLField('Сайт 3', max_length=250, blank=True)
    site_4 = models.URLField('Сайт 4', max_length=250, blank=True)
    site_5 = models.URLField('Сайт 5', max_length=250, blank=True)
    site_6 = models.URLField('Сайт 6', max_length=250, blank=True)
    site_7 = models.URLField('Сайт 7', max_length=250, blank=True)
    site_8 = models.URLField('Сайт 8', max_length=250, blank=True)
    site_9 = models.URLField('Сайт 9', max_length=250, blank=True)
    site_10 = models.URLField('Сайт 10', max_length=250, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'
