# Generated by Django 3.1.3 on 2021-07-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название программы')),
                ('hours', models.TextField(verbose_name='Чамы проведения программы')),
                ('class_name', models.CharField(choices=[('painting', 'Зеленый'), ('fitness', 'Оранжевый'), ('english', 'Фиолетовый')], default='', max_length=10, verbose_name='Цвет строки')),
            ],
            options={
                'verbose_name': 'Программма',
                'verbose_name_plural': 'Программмы',
            },
        ),
        migrations.AddField(
            model_name='menucategory',
            name='icon_class',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Класс иконки'),
        ),
        migrations.AddField(
            model_name='menucategory',
            name='link',
            field=models.URLField(default='', verbose_name='Ссылка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='most_popular',
            field=models.BooleanField(default=False, verbose_name='Отобразить на главной'),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(upload_to='', verbose_name='Картинка на заднем плане')),
                ('programs', models.ManyToManyField(related_name='schedule_program', to='users.Program', verbose_name='Прогрмамы')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
    ]
