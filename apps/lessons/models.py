from core.utils.utils import preview
from django.db import models
from django.utils.safestring import mark_safe
from unixtimestampfield.fields import UnixTimeStampField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import truncatechars
from apps.blog.models import Gallery, Post, Tag
from apps.users.models import User

# Create your models here.


class LessonCategory(models.Model):
    title = models.CharField(
        verbose_name='Заголовок категории', max_length=100)
    slug = models.SlugField(verbose_name='Класс фильтра категории')

    class Meta:
        verbose_name = 'Возрастная группа занятия'
        verbose_name_plural = 'Возрастные группы занятий'

    def __str__(self):
        return self.title

class EventCategory(models.Model):
    title = models.CharField(
        verbose_name='Заголовок категории', max_length=100)
    slug = models.SlugField(verbose_name='Класс фильтра категории')

    class Meta:
        verbose_name = 'Возрастная группа мероприятия'
        verbose_name_plural = 'Возрастные группы мероприятий'

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(verbose_name='Заголовок события', max_length=100)
    slug = models.SlugField("Slug")
    preview = models.ImageField(verbose_name='Картинка в блоке', upload_to=preview)
    background_image = models.ImageField(verbose_name='Картинка на странице', upload_to=preview)
    location = models.TextField(verbose_name='Место проведения')
    years_old = models.TextField(verbose_name='Возраст')
    fee = models.TextField(verbose_name='Цена мероприятия')
    date_start = models.DateField(verbose_name="Дата начала мероприятия")
    date_end = models.DateField(verbose_name="Дата конца мероприятия", blank=True, null=True)
    time = models.TextField(verbose_name='Время проведения')
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
    full_text = RichTextField()
    most_popular = models.BooleanField('Отобразить на главной', default=False)
    def small_image(self):
        if self.preview and hasattr(self.preview, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.preview.url))
        return None

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(verbose_name='Заголовок группы', max_length=100)
    slug = models.SlugField("Url part")
    preview = models.ImageField(verbose_name='Картинка в блоке', upload_to=preview)
    background_image = models.ImageField(verbose_name='Картинка на странице', upload_to=preview)
    years_old = models.TextField(verbose_name='Возраст')
    class_size = models.TextField(verbose_name='Размер группы')
    date_start = models.TextField(verbose_name="Дата начала занятий группы", null=True, blank=True)
    fee = models.TextField(verbose_name='Цена абонемента')
    discount_fee = models.TextField(verbose_name='Цена абонемента со скидкой', null=True, blank=True)
    class_duration = models.TextField(verbose_name="Длительность абонемента")
    class_time = models.TextField(verbose_name='Расписание')
    tags = models.ManyToManyField(
        Tag, related_name='lesson_related_tags', blank=True, verbose_name='Тэги группы')
    related_lessons = models.ManyToManyField('self', related_name='related_lessons', verbose_name='Связанные занятия', blank=True)
    teacher = models.ForeignKey(
        User, related_name='teacher_set', verbose_name='Преподаватель', null=True, on_delete=models.SET_NULL)
    related_posts = models.ManyToManyField(Post, related_name='related_lessons_posts', verbose_name='Связанные публикации', blank=True)
    gallery = models.ManyToManyField(
        Gallery, related_name='lesson_related_gallery', blank=True, verbose_name='Выбрать фото из галереи')
    category = models.ManyToManyField(
        LessonCategory, related_name='lesson_category', verbose_name='Возрастная категория')
    most_popular = models.BooleanField('Отобразить на главной', default=False)
    online = models.BooleanField('Онлайн формат', default=False)
    full_text = RichTextField()
    def small_image(self):
        if self.preview and hasattr(self.preview, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.preview.url))
        return None
        
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f'{self.title} -- {self.years_old} -- {self.class_time}'
 

class Faq(models.Model):
    question = models.CharField(max_length=150, verbose_name='Заголовок вопроса')
    answer = models.TextField('Ответ')
    right = models.BooleanField(verbose_name='Отобразить в правой колонке?',default=False)
    
    @property
    def short_description(self):
        return truncatechars(self.answer, 20)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question
