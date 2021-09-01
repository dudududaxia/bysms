from django.db import models


class Customer(models.Model):
    """
    定义一张数据库的表 就是定义一个继承自 django.db.models.Model 的类
    定义该表中的字段（列）， 就是定义该类里面的一些属性
    """
    # 客户名称
    name = models.CharField(max_length=200)

    # 联系电话
    phone_number = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)
