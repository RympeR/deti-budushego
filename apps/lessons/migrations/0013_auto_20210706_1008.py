# Generated by Django 3.1.3 on 2021-07-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0012_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_end',
            field=models.DateField(blank=True, null=True, verbose_name='Дата конца мероприятия'),
        ),
    ]
