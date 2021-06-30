# Generated by Django 3.1.3 on 2021-06-28 03:29

import core.utils.utils
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=core.utils.utils.preview, verbose_name='Вложение галереи')),
            ],
            options={
                'verbose_name': 'Галлерея',
                'verbose_name_plural': 'Галлереи',
            },
        ),
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок категории галереи')),
                ('slug', models.SlugField(verbose_name='Ярлык категории')),
            ],
            options={
                'verbose_name': 'Категория галереи',
                'verbose_name_plural': 'Категории галереи',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок публикации')),
                ('preview', models.ImageField(upload_to=core.utils.utils.preview, verbose_name='Preview')),
                ('background_image', models.ImageField(upload_to=models.ImageField(upload_to=core.utils.utils.preview, verbose_name='Preview'), verbose_name='Фон')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('preview_text', models.TextField(verbose_name='Текст заставки')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок категории')),
                ('slug', models.SlugField(verbose_name='Ярлык категории')),
            ],
            options={
                'verbose_name': 'Категория публикации',
                'verbose_name_plural': 'Категории публикаций',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок тэга')),
                ('slug', models.SlugField(verbose_name='Ярлык тэга')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
    ]
