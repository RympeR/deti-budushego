# Generated by Django 3.1.3 on 2021-06-28 03:29

import core.utils.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок события')),
                ('preview', models.ImageField(upload_to=core.utils.utils.preview, verbose_name='Preview')),
                ('background_image', models.ImageField(upload_to=models.ImageField(upload_to=core.utils.utils.preview, verbose_name='Preview'), verbose_name='Фон')),
                ('location', models.TextField(verbose_name='Место проведения')),
                ('years_old', models.TextField(verbose_name='Возраст')),
                ('fee', models.TextField(verbose_name='Цена мероприятия')),
                ('date_start', models.DateField(verbose_name='Дата начала мероприятия')),
                ('date_end', models.DateField(verbose_name='Дата конца мероприятия')),
                ('time', models.TextField(verbose_name='Время проведения')),
                ('timer_time', models.DateTimeField(verbose_name='Время начала мероприятия')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок категории')),
                ('slug', models.SlugField(verbose_name='Ярлык категории')),
            ],
            options={
                'verbose_name': 'Категория события',
                'verbose_name_plural': 'Категории событий',
            },
        ),
        migrations.CreateModel(
            name='LessonCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок категории')),
                ('slug', models.SlugField(verbose_name='Ярлык категории')),
            ],
            options={
                'verbose_name': 'Категория занятия',
                'verbose_name_plural': 'Категории занятий',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок события')),
                ('preview', models.ImageField(upload_to=core.utils.utils.preview, verbose_name='Preview')),
                ('background_image', models.ImageField(upload_to=models.ImageField(upload_to=core.utils.utils.preview, verbose_name='Preview'), verbose_name='Фон')),
                ('years_old', models.TextField(verbose_name='Возраст')),
                ('class_size', models.TextField(verbose_name='Размер группы')),
                ('date_start', models.DateField(verbose_name='Дата начала занятий группы')),
                ('fee', models.TextField(verbose_name='Цена абонемента')),
                ('class_duration', models.DateField(verbose_name='Длительность абонемента')),
                ('class_time', models.TextField(verbose_name='Длительность занятия')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_category', to='lessons.lessoncategory', verbose_name='Категория зантия')),
                ('gallery', models.ManyToManyField(related_name='lesson_related_gallery', to='blog.Gallery', verbose_name='Схожие посты галереи')),
                ('related_lessons', models.ManyToManyField(blank=True, related_name='_lesson_related_lessons_+', to='lessons.Lesson', verbose_name='Связанные занятия')),
                ('related_posts', models.ManyToManyField(blank=True, related_name='related_lessons_posts', to='blog.Post', verbose_name='Связанные публикации')),
                ('tags', models.ManyToManyField(related_name='lesson_related_tags', to='blog.Tag', verbose_name='Тэги мероприятия')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
    ]
