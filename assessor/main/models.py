from django.db import models

class Main(models.Model):
    name = models.CharField('ФИО', max_length=100)
    date_birth = models.DateField('Дата рождения')
    phone_number = models.CharField('Номер телефона', max_length=12)
    email = models.EmailField('Email')
    city = models.CharField('Город', max_length=25)
    site_1 = models.CharField('Сайт 1', max_length=250)
    site_2 = models.CharField('Сайт 2', max_length=250)
    site_3 = models.CharField('Сайт 3', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'
