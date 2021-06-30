from core.utils.utils import preview
from django.db import models
from django.shortcuts import reverse
from unixtimestampfield.fields import UnixTimeStampField
from apps.blog.models import Gallery
from apps.users.models import Attachments


class Product(models.Model):
    title = models.CharField(verbose_name='Заголовок события', max_length=100)
    slug = models.SlugField("Slug")
    preview = models.ImageField(verbose_name='Preview', upload_to=preview)
    background_image = models.ImageField(verbose_name='Фон', upload_to=preview)
    price = models.FloatField(verbose_name='Цена')
    discount_price = models.FloatField(
        verbose_name='Цена со скидкой', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    attachments = models.ManyToManyField(
        Attachments, related_name='attachments_shop', verbose_name='Вложеия товара')
    related_gallery = models.ManyToManyField(
        Gallery, related_name='product_related_gallery', verbose_name='Связанные галереи', blank=True)
    created_at = models.DateField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering =['-created_at']
        
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    slug = models.SlugField(verbose_name='Slug')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ecommerce_section:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("ecommerce_section:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("ecommerce_section:remove-from-cart", kwargs={
            'slug': self.slug
        })

    
class SessionOrder(models.Model):
    approved = models.BooleanField('Подтвержден',null=True, default=False)

    class Meta:
        verbose_name = 'Номер заказа в сессии'
        verbose_name_plural = 'Номера заказов в сессии'

    def __str__(self):
        return f"{self.pk}"

class Order(models.Model):
    sessionOrder = models.ForeignKey(
        SessionOrder, null=True, blank=True, on_delete=models.CASCADE)
    ref_code = models.CharField('Пригласительный код', max_length=20, blank=True, null=True)
    items = models.ManyToManyField(Product,related_name='order_products', verbose_name='Товары в заказе')
    name = models.CharField('Имя', max_length=50, blank=False, null=True)
    phone_number = models.CharField('Номер телефона', max_length=40, blank=False, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField('Заказан', default=False)
    address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.sessionOrder)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= total*(self.coupon.discount_percent / 100)
        return total


class Address(models.Model):
    sessionOrder = models.ForeignKey(
        SessionOrder, null=True, blank=True, on_delete=models.CASCADE)
    street_address = models.CharField('Улица',max_length=100)
    apartment_address = models.CharField('Квартира',max_length=100)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return str(self.sessionOrder)


class Payment(models.Model):
    sessionOrder = models.ForeignKey(
        SessionOrder, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.FloatField('Цена')
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        return str(self.sessionOrder)


class Coupon(models.Model):
    code = models.CharField('Код', max_length=15)
    discount_percent = models.IntegerField('Процент скидки')
    amount = models.IntegerField('Количество использований')

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    def __str__(self):
        return self.code
