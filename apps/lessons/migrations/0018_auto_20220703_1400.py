# Generated by Django 3.1.3 on 2022-07-03 14:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0017_auto_20210905_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='fee_ukr',
            field=models.TextField(default='', verbose_name='Цена мероприятия ukr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='location_ukr',
            field=models.TextField(default='', verbose_name='Место проведения ukr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time_ukr',
            field=models.TextField(default='', verbose_name='Окончание ukr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='years_old_ukr',
            field=models.TextField(default='', verbose_name='Возраст ukr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='class_duration_ukr',
            field=models.TextField(default='', verbose_name='Длительность абонемента'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='class_size_ukr',
            field=models.TextField(default='', verbose_name='Размер группы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='date_start_ukr',
            field=models.TextField(blank=True, null=True, verbose_name='Дата начала занятий группы'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='discount_fee_ukr',
            field=models.TextField(blank=True, null=True, verbose_name='Цена абонемента со скидкой'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='fee_ukr',
            field=models.TextField(default='', verbose_name='Цена абонемента'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='full_text_ukr',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Полное описание украинский'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_ukr',
            field=models.CharField(help_text='Украинская версия', max_length=100, null=True, verbose_name='Заголовок группы ukr'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='years_old_ukr',
            field=models.TextField(default='', verbose_name='Возраст'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='full_text',
            field=ckeditor.fields.RichTextField(verbose_name='Полное описание русский'),
        ),
        migrations.AlterField(
            model_name='event',
            name='full_text_ukr',
            field=ckeditor.fields.RichTextField(verbose_name='Полное описание украинский'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='full_text',
            field=ckeditor.fields.RichTextField(verbose_name='Полное описание русский'),
        ),
    ]