from core.utils.utils import attachment, user_avatar
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill
from mptt.models import MPTTModel, TreeForeignKey


class MenuCategory(MPTTModel):
    parent = TreeForeignKey(
        'self', verbose_name='Родительская категория', blank=True, null=True, related_name='parent_category', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=100)
    link = models.URLField('Ссылка')
    icon_class = models.CharField('Класс иконки', max_length=20, null=True, blank=True)
    display = models.BooleanField('Отобразить', default=True)

    def __str__(self):
        return f"{self.name}"

    class MPTTMeta:
        level_attr = 'mеnu_cat'

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'


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
        return str(self.pk)

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'


class User(AbstractUser):
    username = models.CharField(
        'Телефон',
        unique=True,
        max_length=20
    )
    fio = models.CharField('ФИО', max_length=255, null=True, blank=True)
    email = models.EmailField(verbose_name='Почта', blank=True)
    image = ProcessedImageField(
        verbose_name='ImagePNG',
        processors=[ResizeToFill(600, 600)],
        options={'quality': 100},
        upload_to=user_avatar,
        null=True,
        blank=True
    )
    slug = models.SlugField("Slug")
    specialization = models.TextField(
        verbose_name='Специализация', null=True, blank=True)
    personal_statement = models.TextField(
        verbose_name='Описание', null=True, blank=True)
    characteristic = models.TextField(
        verbose_name='Характеристика', null=True, blank=True)
    teacher = models.BooleanField(verbose_name='Учитель', default=False)
    sertificates = models.ManyToManyField(
        Attachments, related_name='user_sertificates', verbose_name='Сертификаты', blank=True)
    most_popular = models.BooleanField('Отобразить на главной', default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
    ]

    def user_photo(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.image.url))
        return None

    def get_contacts(self):
        return ' || '.join(self.contacts.all())

    def get_blocked_users(self):
        return ' || '.join(self.blocked_users.all())

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
        return str(self.username)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
