
from django.urls import path
from . import customer


urlpatterns = [

    # 添加路由记录
    path('customers', customer.dispatcher),
]