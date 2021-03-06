# Generated by Django 3.1.3 on 2021-07-25 00:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210707_1942'),

    ]

    operations = [
        migrations.AddField(
            model_name='aboutcounters',
            name='description_ukr',
            field=models.CharField(help_text='Украинская версия', max_length=50, null=True, verbose_name='Описание счетчика ukr'),
        ),
        migrations.AddField(
            model_name='dropdownpoint',
            name='description_ukr',
            field=models.TextField(help_text='Украинская версия', null=True, verbose_name='Описание ukr'),
        ),
        migrations.AddField(
            model_name='dropdownpoint',
            name='title_ukr',
            field=models.TextField(help_text='Украинская версия', null=True, verbose_name='Заголовок ukr'),
        ),
        migrations.AddField(
            model_name='maincounters',
            name='description_ukr',
            field=models.CharField(help_text='Украинская версия', max_length=50, null=True, verbose_name='Описание счетчика ukr'),
        ),
        migrations.AddField(
            model_name='menucategory',
            name='name_ukr',
            field=models.CharField(help_text='Украинская версия', max_length=100, null=True, verbose_name='Название ukr'),
        ),
        migrations.AddField(
            model_name='program',
            name='name_ukr',
            field=models.TextField(help_text='Украинская версия', null=True, verbose_name='Название программы ukr'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='full_text_ukr',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='name_ukr',
            field=models.TextField(help_text='Украинская версия', null=True, verbose_name='Название вакансии ukr'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='short_description_ukr',
            field=models.TextField(blank=True, help_text='Украинская версия', null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='program',
            name='hours',
            field=models.TextField(verbose_name='Часы проведения программы'),
        ),
    ]
