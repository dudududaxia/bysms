
from django.urls import path
from . import views


urlpatterns = [

    # 添加路由记录
    path('orders/', views.list_orders),
    path('customers/', views.list_customers)
]
