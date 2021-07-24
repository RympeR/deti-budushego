from django.urls import path
from .views import (
    ShopDetail,
    ShopList,
    ShopListFiltered,
    add_to_cart,
    remove_from_cart,
    cart_view,
    AddCouponView,
    CheckoutView,
)

app_name = 'shop_section'
urlpatterns = [
    path('shop-single/<slug:slug>', ShopDetail.as_view(), name='single_shop'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('shop/', ShopList.as_view(), name='shop'),
    path('add-to-cart/<slug:slug>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug:slug>', remove_from_cart, name='remove-from-cart'),
    path('shop/', ShopList.as_view(), name='shop'),
    path('shop/<slug:slug>', ShopListFiltered.as_view(), name='filtered_shop'),
    path('add-coupon/', AddCouponView.as_view(), name='add_coupon'),
]
