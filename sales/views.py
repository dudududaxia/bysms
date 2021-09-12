from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from common.models import Customer


def list_orders(request):
    # request 是Django中的 HttpRequest 对象, 包含了HTTP请求中的信息
    return HttpResponse("Hello, world. You're at the polls index.")


def list_customers(request):
    # 返回一个 QuerySet 对象(类似于列表), 这个对象是Django 定义的, 包含所有的 表记录(表里的每一条数据)
    # 每条表记录都是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values()

    # 定义返回字符串
    retStr = ''

    for customer in qs:
        # Looping through all key-value pairs
        for key, value in customer.items():
            retStr += f'{key} : {value} | '
        # 输出整条数据后 需要换行 -- <br> 表示换行
        retStr += '<br>'
    return HttpResponse(retStr)
