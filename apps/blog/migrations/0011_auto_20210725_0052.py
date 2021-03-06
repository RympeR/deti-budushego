# Generated by Django 3.1.3 on 2021-07-25 00:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210701_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='description_ukr',
            field=models.CharField(help_text='Украинская версия', max_length=100, null=True, verbose_name='Описание укр'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_ukr',
            field=models.CharField(help_text='Украинская версия', max_length=100, null=True, verbose_name='Заголовок укр'),
        ),
        migrations.AddField(
            model_name='gallerycategory',
            name='title_ukr',
            field=models.CharField(help_text='Украинская версия', max_length=100, null=True, verbose_name='Заголовок категории галереи укр'),
        ),
        migrations.AddField(
            model_name='post',
            name='full_text_ukr',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='preview_text_ukr',
            field=models.TextField(help_text='Украинская версия', null=True, verbose_name='Текст заставки укр'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ukr',
            field=models.CharField(help_text='Украинская версия', max_length=100, null=True, verbose_name='Заголовок публикации украинский'),
        ),
        migrations.AddField(
            model_name='postcategory',
            name='title_ukr',
            field=models.CharField(help_text='Украинская версия', max_length=100, null=True, verbose_name='Заголовок категории укр'),
        ),
        migrations.AddField(
            model_name='tag',
            name='title_ukr',
            field=models.CharField(help_text='Украинская версия', max_length=100, null=True, verbose_name='Заголовок тэга ukr'),
        ),
    ]
