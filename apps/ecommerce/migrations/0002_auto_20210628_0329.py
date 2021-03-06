# Generated by Django 3.1.3 on 2021-06-28 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('ecommerce', '0001_initial'),
        ('blog', '0002_auto_20210628_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='attachments',
            field=models.ManyToManyField(related_name='attachments_shop', to='users.Attachments', verbose_name='Вложеия товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='related_gallery',
            field=models.ManyToManyField(blank=True, related_name='product_related_gallery', to='blog.Gallery', verbose_name='Связанные галереи'),
        ),
    ]
