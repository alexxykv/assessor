# Generated by Django 3.2.5 on 2021-07-10 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210513_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='main',
            old_name='lastName',
            new_name='last_name',
        ),
    ]