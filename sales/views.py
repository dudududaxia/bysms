from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from common.models import Customer

# 先定义好HTML模板
html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话号码</th>
        <th>地址</th>
        </tr>

        %s


        </table>
    </body>
</html>
'''


def list_orders(request):
    # request 是Django中的 HttpRequest 对象, 包含了HTTP请求中的信息
    return HttpResponse("Hello, world. You're at the polls index.")


def list_customers(request):
    # 返回一个 QuerySet 对象(类似于列表), 这个对象是Django 定义的, 包含所有的 表记录(表里的每一条数据)
    # 每条表记录都是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values()

    # 检查url中是否有参数 phone_number
    # 有 -- 返回筛选值; 没有 -- 返回None
    # request.GET 对URL分析, output 是一个 类似字典格式的对象，如下
    # request.GET = {
    #     'phone_number': '13899998888',
    #     'qq': '9116801'
    # }
    ph = request.GET.get('phone_number', None)

    # 对数据执行 筛选操作:
    if ph:
        # Django 会在底层执行数据库查询的SQL语句 加上相应的 where 从句，进行过滤查询
        # select * from  Customer where phone_number = 13899998888
        qs = qs.filter(phone_number=ph)

    # 生成html模板中要插入的html片段内容
    tableContent = ''

    for customer in qs:

        tableContent += '<tr>'

        # Looping through all key-value pairs
        for key, value in customer.items():
            tableContent += f'<td>{value}</td>'

        tableContent += '<tr>'
    return HttpResponse(html_template%tableContent)
