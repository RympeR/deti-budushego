# Generated by Django 3.1.3 on 2022-07-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20220717_1142'),
    ]

    operations = [
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
    ]