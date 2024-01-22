from ckeditor.fields import RichTextField
from core.utils.utils import preview
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe

from apps.blog.models import Gallery, Post, Tag
from apps.users.models import User


class LessonCategory(models.Model):
    title_ukr = models.CharField(
        verbose_name='Заголовок категории ukr', null=True, help_text='Украинская версия', max_length=100)
    slug = models.SlugField(verbose_name='Класс фильтра категории')

    class Meta:
        verbose_name = 'Возрастная группа занятия'
        verbose_name_plural = 'Возрастные группы занятий'

    def __str__(self):
        return self.title_ukr or ''


class EventCategory(models.Model):
    title_ukr = models.CharField(
        verbose_name='Заголовок категории ukr', null=True, help_text='Украинская версия', max_length=100)
    slug = models.SlugField(verbose_name='Класс фильтра категории')

    class Meta:
        verbose_name = 'Возрастная группа мероприятия'
        verbose_name_plural = 'Возрастные группы мероприятий'

    def __str__(self):
        return self.title_ukr or ''


class Event(models.Model):
    title_ukr = models.CharField(verbose_name='Заголовок события ukr',
                                 null=True, help_text='Украинская версия', max_length=100)
    slug = models.SlugField("Slug")
    preview = models.ImageField(
        verbose_name='Картинка в блоке', upload_to=preview)
    background_image = models.ImageField(
        verbose_name='Картинка на странице', upload_to=preview)
    location_ukr = models.TextField(verbose_name='Место проведения ukr')
    years_old_ukr = models.TextField(verbose_name='Возраст ukr')
    fee_ukr = models.TextField(verbose_name='Цена мероприятия ukr')
    date_start = models.DateField(verbose_name="Дата начала мероприятия")
    date_end = models.DateField(
        verbose_name="Дата конца мероприятия", blank=True, null=True)
    time_ukr = models.TextField(verbose_name='Окончание ukr')
    timer_time = models.DateTimeField(verbose_name='Время начала мероприятия')
    related_posts = models.ManyToManyField(
        Post, related_name='event_related_posts', blank=True, verbose_name='Схожие посты')
    gallery = models.ManyToManyField(
        Gallery, related_name='event_related_gallery', blank=True, verbose_name='Выбрать фото из галереи')
    tags = models.ManyToManyField(
        Tag, related_name='event_related_tags', blank=True, verbose_name='Тэги мероприятия')
    organizer = models.ForeignKey(
        User, related_name='organizer', verbose_name='Организатор', null=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField(
        EventCategory, related_name='event_category', verbose_name='Категория мероприятия')
    online = models.BooleanField('Онлайн формат', default=False)
    full_text_ukr = RichTextField(verbose_name='Полное описание украинский')
    most_popular = models.BooleanField('Отобразить на главной', default=False)

    def small_image(self):
        if self.preview and hasattr(self.preview, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.preview.url))
        return None

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title_ukr or ''


class Lesson(models.Model):
    title_ukr = models.CharField(verbose_name='Заголовок группы ukr',
                                 null=True, help_text='Украинская версия', max_length=100)
    slug = models.SlugField("Url part")
    preview = models.ImageField(
        verbose_name='Картинка в блоке', upload_to=preview)
    background_image = models.ImageField(
        verbose_name='Картинка на странице', upload_to=preview)
    years_old_ukr = models.TextField(verbose_name='Возраст')
    class_size_ukr = models.TextField(verbose_name='Размер группы')
    date_start_ukr = models.TextField(
        verbose_name="Дата начала занятий группы", null=True, blank=True)
    fee_ukr = models.TextField(verbose_name='Цена абонемента')
    discount_fee_ukr = models.TextField(
        verbose_name='Цена абонемента со скидкой', null=True, blank=True)
    class_duration_ukr = models.TextField(
        verbose_name="Длительность абонемента")
    class_time_ukr = models.TextField(
        verbose_name='Расписание ukr', null=True, help_text='Украинская версия',)
    tags = models.ManyToManyField(
        Tag, related_name='lesson_related_tags', blank=True, verbose_name='Тэги группы')
    related_lessons = models.ManyToManyField(
        'self', related_name='related_lessons', verbose_name='Связанные занятия', blank=True)
    teacher = models.ForeignKey(
        User, related_name='teacher_set', verbose_name='Преподаватель', null=True, on_delete=models.SET_NULL)
    try_lesson = models.IntegerField(
        verbose_name='Пробное занятие', null=True, blank=True)
    related_posts = models.ManyToManyField(
        Post, related_name='related_lessons_posts', verbose_name='Связанные публикации', blank=True)
    gallery = models.ManyToManyField(
        Gallery, related_name='lesson_related_gallery', blank=True, verbose_name='Выбрать фото из галереи')
    category = models.ManyToManyField(
        LessonCategory, related_name='lesson_category', verbose_name='Возрастная категория')
    most_popular = models.BooleanField('Отобразить на главной', default=False)
    online = models.BooleanField('Онлайн формат', default=False)
    display = models.BooleanField('Отображать', default=True)
    full_text_ukr = RichTextField(verbose_name='Полное описание украинский')

    def small_image(self):
        if self.preview and hasattr(self.preview, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.preview.url))
        return None

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f'{self.title_ukr} -- {self.years_old_ukr} -- {self.class_time_ukr}'


class Faq(models.Model):
    question_ukr = models.CharField(
        max_length=150, verbose_name='Заголовок вопроса', null=True, help_text='Украинская версия',)
    answer_ukr = models.TextField(
        'Ответ ukr', null=True, help_text='Украинская версия',)
    right = models.BooleanField(
        verbose_name='Отобразить в правой колонке?', default=False)

    @property
    def short_description(self):
        return truncatechars(self.answer_ukr, 20)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question_ukr or ''
