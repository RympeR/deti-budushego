# Generated by Django 3.1.3 on 2021-07-04 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0010_auto_20210703_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='most_popular',
            field=models.BooleanField(default=False, verbose_name='Отобразить на главной'),
        ),
    ]
