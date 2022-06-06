from django.db import models
import datetime

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


class Medicine(models.Model):
    # 药品名
    name = models.CharField(max_length=200)
    # 药品编号
    sn = models.CharField(max_length=200)
    # 描述
    desc = models.CharField(max_length=200)


class Order(models.Model):
    # 订单名
    name = models.CharField(max_length=200, null=True,blank=True)

    # 创建日期
    create_date = models.DateTimeField(default=datetime.datetime.now)

    # 客户
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    # 订单购买的药品，和Medicine表是多对多 的关系, 有时 through 可以忽略(见下文)
    # 是多对多关系的字段 不会在数据库创建
    medicines = models.ManyToManyField(Medicine, through='OrderMedicine')


# attention: 如果不需要对 medicines 添加其他字段(如 amount), 不需要定义 OrderMedicine 这个表
# Django 会自动创建 多对多的中间表

# Order表和 Medicine 表 的多对多关系 是 通过另外一张表
# 也就是 through 参数 指定的 OrderMedicine 表 来确定的。
class OrderMedicine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)

    # 订单中药品的数量
    amount = models.PositiveIntegerField()
