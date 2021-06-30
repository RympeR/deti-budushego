from django.db import models
from core.utils.utils import preview
from apps.users.models import User
from core.utils.utils import preview
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill


class Tag(models.Model):
    title = models.CharField(
        verbose_name='Заголовок тэга', max_length=100)
    slug = models.SlugField(verbose_name='Ярлык тэга')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.title


class GalleryCategory(models.Model):
    title = models.CharField(
        verbose_name='Заголовок категории галереи', max_length=100)
    slug = models.SlugField(verbose_name='Ярлык категории')

    class Meta:
        verbose_name = 'Категория галереи'
        verbose_name_plural = 'Категории галереи'

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    title = models.CharField(
        verbose_name='Заголовок категории', max_length=100)
    slug = models.SlugField(verbose_name='Ярлык категории')

    class Meta:
        verbose_name = 'Категория публикации'
        verbose_name_plural = 'Категории публикаций'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=100)
    image = ProcessedImageField(
        verbose_name='Вложение галереи',
        processors=[ResizeToFill(600, 600)],
        options={'quality': 100},
        upload_to=preview,
        null=True,
        blank=True
    )
    category = models.ManyToManyField(GalleryCategory, verbose_name='Категория',  related_name='gallery_category')
    most_popular = models.BooleanField('Отобразить на главной', default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def preview(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.image.url))
        return None


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок публикации', max_length=100)
    slug = models.SlugField("Slug")
    preview = models.ImageField(verbose_name='Preview', upload_to=preview)
    background_image = models.ImageField(verbose_name='Фон', upload_to=preview)
    author = models.ForeignKey(
        User, related_name='author', verbose_name='Автор', on_delete=models.CASCADE)
    related_gallery = models.ManyToManyField(
        Gallery, related_name='post_related_gallery', verbose_name='Связанные галереи', blank=True)
    related_posts = models.ManyToManyField(
        'self', related_name='post_related_posts', verbose_name='Связанные публикации', blank=True)
    related_tags = models.ManyToManyField(
        Tag, related_name='post_related_tags', verbose_name='Связанные тэги', blank=True)
    related_categories = models.ManyToManyField(
        PostCategory, related_name='post_related_categories', verbose_name='Связанные категории', blank=True)
    created_at = models.DateField('Дата создания', auto_now_add=True)
    preview_text = models.TextField(verbose_name='Текст заставки')
    display = models.BooleanField(verbose_name='Отображать', default=True)
    
    def small_image(self):
        if self.preview and hasattr(self.preview, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.preview.url))
        return None


    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
