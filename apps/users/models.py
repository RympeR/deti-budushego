from core.utils.utils import attachment, user_avatar
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from django.template.defaultfilters import truncatechars

class MenuCategory(MPTTModel):
    parent = TreeForeignKey(
        'self', verbose_name='Родительская категория', blank=True, null=True, related_name='parent_category', on_delete=models.CASCADE)
    name_ukr = models.CharField('Название ukr', null=True, help_text='Украинская версия', max_length=100)
    link = models.URLField('Ссылка')
    icon_class = models.CharField(
        'Класс иконки', max_length=20, null=True, blank=True)
    display = models.BooleanField('Отобразить', default=True)
    
    def __str__(self):
        return f"{self.name_ukr}"

    class MPTTMeta:
        level_attr = 'mеnu_cat'

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'


class DropDownPoint(MPTTModel):
    parent = TreeForeignKey(
        'self', verbose_name='Родительская категория', blank=True, null=True, related_name='parent_category', on_delete=models.CASCADE)
    title_ukr = models.TextField('Заголовок ukr', null=True, help_text='Украинская версия',)
    description_ukr = models.TextField('Описание ukr', null=True, help_text='Украинская версия',)
    main_page = models.BooleanField('Отобразить на главной?', default=True)
    opened = models.BooleanField('Развернут', default=False)
    class MPTTMeta:
        level_attr = 'mеnu_cat'

    def short_description(self):
        return truncatechars(self.description_ukr, 20)

    def __str__(self):
        return self.title_ukr

    class Meta:
        verbose_name = 'Раскрывающийся пункт'
        verbose_name_plural = 'Раскрывающиеся пункты'


class Attachments(models.Model):

    class AttachmentType(models.TextChoices):
        IMAGE = 'IMAGE', 'Изображение'
        VIDEO = 'VIDEO', 'Видео'
        AUDIO = 'AUDIO', 'Аудио'
        DOCUMENT = 'DOCUMENT', 'Документ'

    attachment_type = models.CharField(
        verbose_name='Тип вложения', max_length=8, choices=AttachmentType.choices)
    attachment = models.FileField(
        verbose_name='Вложение', upload_to=attachment)

    def __str__(self):
        return str(self.attachment)

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'

class Vacancy(models.Model):
    name_ukr = models.TextField(verbose_name='Название вакансии ukr', null=True, help_text='Украинская версия',)
    icon = models.ImageField(verbose_name='Заставка вакансии')
    short_description_ukr = models.TextField(verbose_name='Краткое описание', null=True, help_text='Украинская версия', blank=True)
    slug = models.SlugField(("Url part"), unique=True)
    full_text_ukr = RichTextField(verbose_name='Полное описание украинский')

    def __str__(self):
        return str(self.name_ukr)

    def vacancy_photo(self):
        if self.icon and hasattr(self.icon, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.icon.url))
        return None

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

class User(AbstractUser):
    username = models.CharField(
        'Логин',
        unique=True,
        max_length=20
    )
    fio_ukr = models.CharField('ФИО  ukr', max_length=255, null=True, blank=True)
    preview_avatar = ProcessedImageField(
        verbose_name='Картинка в маленьком блоке',
        processors=[ResizeToFill(312, 312)],
        options={'quality': 100},
        upload_to=user_avatar,
        null=True,
        blank=True
    )
    image = ProcessedImageField(
        verbose_name='Аватар',
        processors=[ResizeToFill(600, 600)],
        options={'quality': 100},
        upload_to=user_avatar,
        null=True,
        blank=True
    )
    slug = models.SlugField("Url part")
    specialization_ukr = models.TextField(
        verbose_name='Специализация ukr', null=True, blank=True)
    personal_statement_ukr = models.TextField(
        verbose_name='Название программ ukr', null=True, blank=True)
    characteristic_ukr = models.TextField(
        verbose_name='О преподавателе ukr', null=True, blank=True)
    teacher = models.BooleanField(verbose_name='Учитель', default=False)
    sertificates = models.ManyToManyField(
        Attachments, related_name='user_sertificates', verbose_name='Сертификаты', blank=True)
    most_popular = models.BooleanField('Отобразить на главной', default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'fio'
    ]

    def user_photo(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.image.url))
        return None

    @staticmethod
    def _create_user(password, **extra_fields):
        user = User.objects.create(
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(password,  **extra_fields)

    def create_superuser(self, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(password,  **extra_fields)

    def __str__(self):
        return str(self.fio)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Program(models.Model):
    class ClassNames(models.TextChoices):
        painting = 'painting', 'Зеленый'
        fitness = 'fitness', 'Оранжевый'
        english = 'english', 'Фиолетовый'

    name_ukr = models.TextField("Название программы ukr", null=True, help_text='Украинская версия',)
    hours_ukr = models.TextField("Часы проведения программы ukr")
    class_name = models.CharField(
        'Цвет строки', choices=ClassNames.choices, max_length=10, default='')

    class Meta:
        verbose_name = 'Программма'
        verbose_name_plural = 'Программмы'


class Schedule(models.Model):
    programs = models.ManyToManyField(
        Program, related_name='schedule_program', verbose_name='Прогрмамы')
    background = models.ImageField('Картинка на заднем плане')

    def schedule_photo(self):
        if self.background and hasattr(self.background, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.background.url))
        return None

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'


class ParentComment(models.Model):
    parent_name = models.CharField(max_length=100, verbose_name='ФИО родителя')
    profession = models.CharField('Профессия', max_length=50, blank=True, null=True)
    comment = models.TextField(verbose_name='Отзыв')
    parent_image = ProcessedImageField(
        verbose_name='Аватарка родителя',
        processors=[ResizeToFill(60, 60)],
        options={'quality': 100},
        upload_to=user_avatar,
        null=True,
        blank=True
    )

    def short_comment(self):
        return truncatechars(self.comment, 20)

    def __str__(self):
        return self.parent_name

    class Meta:
        verbose_name = 'Комментарий родителя'
        verbose_name_plural = 'Комментарии родителей'


class MainCounters(models.Model):
    amount = models.IntegerField('Значение счетчика')
    symbol = models.CharField(verbose_name='Символ после числа', max_length=1, blank=True, null=True)
    description_ukr = models.CharField(verbose_name='Описание счетчика ukr', null=True, help_text='Украинская версия',max_length=50)
    image = ProcessedImageField(
        verbose_name='Заставка описания',
        processors=[ResizeToFill(91, 86)],
        options={'quality': 100},
        upload_to=user_avatar,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.description_ukr} -> {self.amount}'

    class Meta:
        verbose_name = 'Счетчик на главной'
        verbose_name_plural = 'Счетчики на главной'

class AboutCounters(models.Model):
    amount = models.IntegerField('Значение счетчика')
    symbol = models.CharField(verbose_name='Символ после числа', max_length=1, blank=True, null=True)
    description_ukr = models.CharField(verbose_name='Описание счетчика ukr', null=True, help_text='Украинская версия', max_length=50)
    image = ProcessedImageField(
        verbose_name='Заставка описания',
        processors=[ResizeToFill(91, 86)],
        options={'quality': 100},
        upload_to=user_avatar,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.description_ukr} -> {self.amount}'

    class Meta:
        verbose_name = 'Счетчик на странице о нас'
        verbose_name_plural = 'Счетчики на странице о нас'
