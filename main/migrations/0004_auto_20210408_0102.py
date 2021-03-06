# Generated by Django 3.1.7 on 2021-04-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210326_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='name',
        ),
        migrations.AddField(
            model_name='main',
            name='firstName',
            field=models.CharField(default='No info', max_length=25, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='main',
            name='lastName',
            field=models.CharField(default='No info', max_length=25, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='main',
            name='middleName',
            field=models.CharField(default='No info', max_length=25, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='main',
            name='phone_number',
            field=models.CharField(max_length=11, verbose_name='Телефон'),
        ),
    ]
