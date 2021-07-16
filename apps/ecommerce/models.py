from core.utils.utils import preview
from django.db import models
from django.shortcuts import reverse
from apps.users.models import Attachments, User
from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(verbose_name='Заголовок события', max_length=100)
    slug = models.SlugField("Slug", unique=True)
    preview = models.ImageField(
        verbose_name='Картинка в блоке', upload_to=preview)
    price = models.FloatField(verbose_name='Цена')
    discount_price = models.FloatField(
        verbose_name='Цена со скидкой', null=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    attachments = models.ManyToManyField(
        Attachments, related_name='attachments_shop', verbose_name='Вложеия товара')
    created_at = models.DateField('Дата создания', auto_now_add=True)
    full_text = RichTextField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cart:product-detail", kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse("staff:product-update", kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse("staff:product-delete", kwargs={'pk': self.pk})

    def get_price(self):
        return "{:.2f}".format(self.price / 100)


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


class Order(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.sessionOrder)

    def get_total(self):
        total = 0
        for order_item in self.items_order.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= total*(self.coupon.discount_percent / 100)
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(
        "Order", related_name='items_order', verbose_name='Заказ', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name='Товар', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order} x {self.product.title}"

    def get_raw_total_item_price(self):
        return self.product.discount_price if self.product.discount_price else self.product.price


class Payment(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='payments')
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
