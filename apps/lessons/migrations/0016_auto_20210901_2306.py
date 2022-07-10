# Generated by Django 3.1.3 on 2021-09-01 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0015_auto_20210725_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='try_lesson',
            field=models.BooleanField(default=False, null=True, verbose_name='Пробное занятие'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='discount_fee',
            field=models.TextField(blank=True, null=True, verbose_name='Цен9*+-а абонемента со скидкой'),
        ),
    ]