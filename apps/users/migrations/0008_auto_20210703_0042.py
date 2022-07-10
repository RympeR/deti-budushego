# Generated by Django 3.1.3 on 2021-07-03 00:42

import core.utils.utils
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210703_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=core.utils.utils.user_avatar, verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(verbose_name='Url part'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
    ]