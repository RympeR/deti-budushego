# Generated by Django 3.1.3 on 2021-07-01 12:51

import core.utils.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_most_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerycategory',
            name='slug',
            field=models.SlugField(verbose_name='Класс фильтра категории'),
        ),
        migrations.AlterField(
            model_name='post',
            name='background_image',
            field=models.ImageField(upload_to=models.ImageField(upload_to=core.utils.utils.preview, verbose_name='Картинка в блоке'), verbose_name='Картинка на странице'),
        ),
        migrations.AlterField(
            model_name='post',
            name='preview',
            field=models.ImageField(upload_to=core.utils.utils.preview, verbose_name='Картинка в блоке'),
        ),
        migrations.AlterField(
            model_name='post',
            name='related_gallery',
            field=models.ManyToManyField(blank=True, related_name='post_related_gallery', to='blog.Gallery', verbose_name='Выбрать фото из галереи'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(verbose_name='Url part'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='slug',
            field=models.SlugField(verbose_name='Класс фильтра категории'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(verbose_name='Класс фильтра тэга'),
        ),
    ]
