from mgr import customer
from mgr import medicine
from mgr import sign_in_out
from django.urls import path


urlpatterns = [
    # 添加路由记录
    path('customers',   customer.dispatcher),
    path('medicines',   medicine.dispatcher),
    path('signin',      sign_in_out.sign_in),
    path('signout',     sign_in_out.sign_out),
]