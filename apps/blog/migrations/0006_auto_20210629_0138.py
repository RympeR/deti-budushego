# Generated by Django 3.1.3 on 2021-06-29 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_gallery_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='category',
        ),
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.ManyToManyField(related_name='gallery_category', to='blog.GalleryCategory', verbose_name='Категория'),
        ),
    ]
