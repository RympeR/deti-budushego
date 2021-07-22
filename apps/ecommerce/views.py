from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from apps.lessons.models import Event
from apps.users.models import MenuCategory

from .models import OrderItem, Product, Order, Coupon


def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        if coupon.amount > 0:
            coupon.amount -= 1
            coupon.save()
            return coupon
        else:
            return 0
    except ObjectDoesNotExist:
        return redirect("core:checkout")

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


def cart_view(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            qs = Order.objects.get(Q(finished=False) & Q(user=user))
        except Exception:
            return redirect('shop_section:shop')
        context = {}
        context['order'] = qs
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by(
            '-date_start')[:2]
        items = qs.items_order.all()
        products = [ item.product for item in items ]
        context['products'] = products
        return render(request, 'cart.html', context=context)
    return redirect('shop_section:shop')

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
        if self.request.user.is_authenticated:
            user = self.request.user
            for product in context['products']:
                context['products']
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
        try:
            qs = Order.objects.get(Q(finished=False) & Q(user=user))
        except Exception:
            qs = None
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
        try:
            qs = Order.objects.get(Q(finished=False) & Q(user=user))
        except Exception:
            qs = None
        if not qs:
            return redirect("shop_section:shop")
        order_item = OrderItem.objects.get(
            Q(order=qs) &
            Q(product=product)
        )
        order_item.delete()
        return redirect("shop_section:shop")

class AddCouponView(View):
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            user = self.request.user
        self.coupon_code = self.request.POST['coupon']
        print(self.coupon_code)
        try:
            order = Order.objects.get(Q(finished=False) & Q(user=user))
            try:
                order.coupon = get_coupon(self.request, self.coupon_code)
            except ValueError:
                return redirect("shop_section:cart")
            order.save()
            return redirect("shop_section:cart")
        except ObjectDoesNotExist:
            return redirect("shop_section:cart")
