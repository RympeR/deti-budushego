from ckeditor.fields import RichTextField
from core.utils.utils import preview
from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from apps.users.models import User


class Tag(models.Model):
    title_ukr = models.CharField(
        verbose_name='Заголовок тэга ukr', null=True, help_text='Украинская версия', max_length=100)
    slug = models.SlugField(verbose_name='Класс фильтра тэга')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.title_ukr or ''


class GalleryCategory(models.Model):
    title_ukr = models.CharField(
        verbose_name='Заголовок категории галереи укр', null=True, help_text='Украинская версия', max_length=100)
    slug = models.SlugField(verbose_name='Класс фильтра категории')

    class Meta:
        verbose_name = 'Категория галереи'
        verbose_name_plural = 'Категории галереи'

    def __str__(self):
        return self.title_ukr or ''


class PostCategory(models.Model):
    title_ukr = models.CharField(
        verbose_name='Заголовок категории укр', null=True, help_text='Украинская версия', max_length=100)
    slug = models.SlugField(verbose_name='Класс фильтра категории')

    class Meta:
        verbose_name = 'Категория публикации'
        verbose_name_plural = 'Категории публикаций'

    def __str__(self):
        return self.title_ukr or ''


class Gallery(models.Model):
    image = ProcessedImageField(
        verbose_name='Вложение галереи',
        processors=[ResizeToFill(570, 380)],
        options={'quality': 100},
        upload_to=preview,
        null=True,
        blank=True
    )
    category = models.ManyToManyField(
        GalleryCategory, verbose_name='Категория',  related_name='gallery_category')
    most_popular = models.BooleanField('Отобразить на главной', default=False)

    def __str__(self):
        return self.image.name or ''

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def preview(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.image.url))
        return None


class Post(models.Model):
    title_ukr = models.CharField(verbose_name='Заголовок публикации украинский',
                                 null=True, help_text='Украинская версия', max_length=100)
    slug = models.SlugField("Url part")
    preview = models.ImageField(
        verbose_name='Картинка в блоке', upload_to=preview)
    background_image = models.ImageField(
        verbose_name='Картинка на странице', upload_to=preview)
    author = models.ForeignKey(
        User, related_name='author', verbose_name='Автор', on_delete=models.CASCADE)
    related_gallery = models.ManyToManyField(
        Gallery, related_name='post_related_gallery', verbose_name='Выбрать фото из галереи', blank=True)
    related_posts = models.ManyToManyField(
        'self', related_name='post_related_posts', verbose_name='Связанные публикации', blank=True)
    related_tags = models.ManyToManyField(
        Tag, related_name='post_related_tags', verbose_name='Связанные тэги', blank=True)
    related_categories = models.ManyToManyField(
        PostCategory, related_name='post_related_categories', verbose_name='Связанные категории', blank=True)
    created_at = models.DateField('Дата создания', auto_now_add=True)
    preview_text_ukr = models.TextField(
        null=True, help_text='Украинская версия', verbose_name='Текст заставки укр')
    display = models.BooleanField(verbose_name='Отображать', default=True)
    most_popular = models.BooleanField(
        verbose_name='Отображать на главной?', default=False)
    full_text_ukr = RichTextField(verbose_name='Полный текст укр',)

    def small_image(self):
        if self.preview and hasattr(self.preview, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.preview.url))
        return None

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at']

    def __str__(self):
        return self.title_ukr or ''


class News(models.Model):
    title_ukr = models.CharField(verbose_name='Заголовок публикации украинский',
                                 null=True, help_text='Украинская версия', max_length=100)
    slug = models.SlugField("Url part")
    preview = models.ImageField(
        verbose_name='Картинка в блоке', upload_to=preview)
    background_image = models.ImageField(
        verbose_name='Картинка на странице', upload_to=preview)
    created_at = models.DateField('Дата создания', auto_now_add=True)
    preview_text_ukr = models.TextField(
        null=True, help_text='Украинская версия', verbose_name='Текст заставки укр')
    display = models.BooleanField(verbose_name='Отображать', default=True)
    full_text_ukr = RichTextField(verbose_name='Полный текст укр',)
    related_tags = models.ManyToManyField(
        Tag, related_name='news_related_tags', verbose_name='Связанные тэги', blank=True)

    def small_image(self):
        if self.preview and hasattr(self.preview, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.preview.url))
        return None

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title_ukr or ''
