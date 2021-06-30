# Generated by Django 3.1.3 on 2021-06-28 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_auto_20210628_0329'),
        ('lessons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_set', to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель'),
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_category', to='lessons.eventcategory', verbose_name='Категория мероприятия'),
        ),
        migrations.AddField(
            model_name='event',
            name='gallery',
            field=models.ManyToManyField(related_name='event_related_gallery', to='blog.Gallery', verbose_name='Схожие посты галереи'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizer', to=settings.AUTH_USER_MODEL, verbose_name='Организатор'),
        ),
        migrations.AddField(
            model_name='event',
            name='related_posts',
            field=models.ManyToManyField(related_name='event_related_posts', to='blog.Post', verbose_name='Схожие посты'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(related_name='event_related_tags', to='blog.Tag', verbose_name='Тэги мероприятия'),
        ),
    ]
