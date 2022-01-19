from django.urls import path
from .views import Coupon_List, Coupon_Use

urlpatterns = [
    path('coupon_list/',Coupon_List.as_view(),name='coupon_list'),
    path('coupon_use/',Coupon_Use.as_view(),name='coupon_use'),

    
]