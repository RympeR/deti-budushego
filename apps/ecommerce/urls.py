from django.urls import path
from .views import (
    ShopDetail,
    ShopList,
    ShopListFiltered,
)

app_name = 'shop_section'
urlpatterns = [
    path('shop-single/<slug:slug>', ShopDetail.as_view(), name='single_shop'),
    path('shop/', ShopList.as_view(), name='shop'),
    path('shop/<slug:slug>', ShopListFiltered.as_view(), name='filtered_shop'),
]
