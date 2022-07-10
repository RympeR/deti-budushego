# Generated by Django 3.1.3 on 2021-07-06 08:19

import core.utils.utils
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210706_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCounters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Значение счетчика')),
                ('symbol', models.CharField(blank=True, max_length=1, null=True, verbose_name='Символ после числа')),
                ('description', models.CharField(max_length=50, verbose_name='Описание счетчика')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=core.utils.utils.user_avatar, verbose_name='Заставка описания')),
            ],
            options={
                'verbose_name': 'Счетчик на странице о нас',
                'verbose_name_plural': 'Счетчики на странице о нас',
            },
        ),
    ]