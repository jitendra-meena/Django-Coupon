from django.urls import path
from .views import Coupon_List,Coupon_Apply,Add_Coupon

urlpatterns = [
    path('coupon_list/',Coupon_List.as_view(),name='coupon_list'),
    path('coupon_apply/',Coupon_Apply.as_view(),name='coupon_apply'),
    path('add_coupon/',Add_Coupon.as_view(),name='add_coupon'),

    
]