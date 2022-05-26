
from django.urls import path
from . import customer
from mgr import sign_in_out


urlpatterns = [

    # 添加路由记录
    path('customers',   customer.dispatcher),
    path('signin',      sign_in_out.sign_in),
    path('signout',     sign_in_out.sign_out),
]