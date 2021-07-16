from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from apps.lessons.models import Event
from apps.users.models import MenuCategory

from .models import OrderItem, Product, Order


class ShopList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by(
            '-date_start')[:2]
        return context


class ShopListFiltered(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop.html'
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by(
            '-date_start')[:2]
        return context


class ShopDetail(DetailView):
    model = Product
    template_name = 'shop-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by(
            '-date_start')[:2]
        return context


def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.user.is_authenticated:
        user = request.user
        qs = Order.objects.get(Q(finished=False) & Q(user=user))
        if not qs:
            qs = Order.objects.create(user=request.user)
        order_item, created = OrderItem.objects.get_or_create(
            order=qs,
            product=product
        )
        return redirect("shop_section:shop")

def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.user.is_authenticated:
        user = request.user
        qs = Order.objects.get(Q(finished=False) & Q(user=user))
        if not qs:
            return redirect("shop_section:shop")
        order_item = OrderItem.objects.get(
            Q(order=qs) &
            Q(product=product)
        )
        order_item.delete()
        return redirect("shop_section:shop")
