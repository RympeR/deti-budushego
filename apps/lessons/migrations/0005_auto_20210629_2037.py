# Generated by Django 3.1.3 on 2021-06-29 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_auto_20210629_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='class_duration',
            field=models.TextField(verbose_name='Длительность абонемента'),
        ),
    ]
