from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from apps.lessons.models import Event
from apps.users.models import MenuCategory

from .models import Coupon, Order, OrderItem, Product
from .wayforpaymodule import WayForPayAPI
from core.utils.mixins import (
    FooterContentMixin,
)

def get_coupon(request, code):
    try:
        coupon = Coupon.objects.filter(code=code, datetime_end__lte=timezone.now()).first()
        if coupon:
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

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товары'
        footer_context = {
            'menu' : MenuCategory.objects.filter(display=True),
            'footer_events' : Event.objects.all().order_by(
                '-date_start')[:2]
        }
        context = {**context,**footer_context}
        return context

def cart_view(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            order = Order.objects.get(Q(finished=False) & Q(user=user))
        except Exception:
            return redirect('shop_section:shop')
        order_items = order.items_order.all()
        wpay = WayForPayAPI(
            'detibudushego_club',
            '93500448ed437cb41a1639ed67e374457b65e935',
            'detibudushego.club',
        )
        names = []
        cost = []
        amount = []
        for item in order_items:
            names.append(item.product.title)
        for item in order_items:
            cost.append(item.product.final_price())
        for item in order_items:
            amount.append(1)
        import calendar
        import time
        ts = calendar.timegm(time.gmtime())
        data = {
            'orderReference': ts,
            'orderDate': ts,
            'amount': order.get_total(),
            'currency': 'UAH',
            'productName': list(names),
            'productPrice': list(cost),
            'serviceUrl': 'https://detibudushego.club/finish-order/',
            'returnUrl': 'https://detibudushego.club/finish-order/',
            'productCount': list(amount),
        }
        widget = wpay.generate_widget(data)
        context = {
            'widget': widget
        }
        context['order'] = order
        context['menu'] = MenuCategory.objects.filter(display=True)
        context['footer_events'] = Event.objects.all().order_by(
            '-date_start')[:2]
        items = order.items_order.all()
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

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товары'
        footer_context = {
            'menu' : MenuCategory.objects.filter(display=True),
            'footer_events' : Event.objects.all().order_by(
                '-date_start')[:2]
        }
        context = {**context,**footer_context}
        return context

class ShopDetail(DetailView):
    model = Product
    template_name = 'shop-single.html'

    def get_context_data(self, **kwargs: any) -> dict:
        context = super().get_context_data(**kwargs)
        footer_context = {
            'menu' : MenuCategory.objects.filter(display=True),
            'footer_events' : Event.objects.all().order_by(
                '-date_start')[:2]
        }
        context = {**context,**footer_context}
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
    return redirect("lessons_section:login")
    


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
    return redirect("lessons_section:login")

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
class FinishOrder(View):
    def get(self, *args, **kwargs):
        
        user = self.request.user
        print(user)
        try:
            order = Order.objects.get(Q(finished=False) & Q(user=user))
            order.finished = True
            order.save()
            return redirect("users_section:profile_detail")
        except ObjectDoesNotExist:
            return redirect("shop_section:shop")
        

class CheckoutView(View):
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            user = self.request.user
        try:
            order = Order.objects.get(Q(finished=False) & Q(user=user))
            order_items = order.items_order.all()
            wpay = WayForPayAPI(
                'detibudushego_club',
                '93500448ed437cb41a1639ed67e374457b65e935',
                'detibudushego.club',
            )
            names = []
            cost = []
            amount = []
            for item in order_items:
                names.append(item.product.title)
            for item in order_items:
                cost.append(item.product.final_price())
            for item in order_items:
                amount.append(1)
            import calendar
            import time
            ts = calendar.timegm(time.gmtime())
            data = {
                'orderReference': ts,
                'orderDate': ts,
                'amount': order.get_total(),
                'currency': 'UAH',
                'productName': names,
                'productPrice': cost,
                'productCount': list(map(int, amount)),
            }
            print(data)
            widget = wpay.generate_widget(data)
            context = {
                'widget': widget
            }
            context['order'] = order
            context['menu'] = MenuCategory.objects.filter(display=True)
            context['footer_events'] = Event.objects.all().order_by(
                '-date_start')[:2]
            items = order.items_order.all()
            products = [ item.product for item in items ]
            context['products'] = products
            print(widget)
            return render(self.request, "cart.html", context)
        except ObjectDoesNotExist:
            return redirect("shop_section:shop")
