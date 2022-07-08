# Generated by Django 3.1.3 on 2021-07-03 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210703_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='Url part'),
            preserve_default=False,
        ),
    ]
