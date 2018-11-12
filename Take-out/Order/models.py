from django.db import models
<<<<<<< HEAD
from Order_dinner.models import Seller,Food
from Person.models import Customer,Address
=======
from Person.models import Customer, Address
from Order_dinner.models import Seller, Food



>>>>>>> 705b8135a6f15b88600ab83f3d133443094af22e
# Create your models here.
class Order(models.Model):
    customer_id = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    seller_id = models.ForeignKey(Seller, blank=True, null=True, on_delete=models.SET_NULL)
    history_id = models.ForeignKey('History', blank=True, null=True, on_delete=models.SET_NULL)
    food_id = models.ForeignKey(Food, blank=True, null=True, on_delete=models.SET_NULL)
    order_number = models.IntegerField()
    order_money = models.IntegerField()
    odate = models.DateTimeField(auto_now_add=True)
    order_status = models.IntegerField(choices=[(0, '未发送'), (1, '已发送'), (2, '确认收货')])


class Order_detail(models.Model):
    customer_id = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    seller_id = models.ForeignKey(Seller, blank=True, null=True, on_delete=models.SET_NULL)
    history_id = models.ForeignKey('History', blank=True, null=True, on_delete=models.SET_NULL)
    food_id = models.ForeignKey(Food, blank=True, null=True, on_delete=models.SET_NULL)
<<<<<<< HEAD
    order_id = models.ForeignKey("Order", blank=True, null=True, on_delete=models.SET_NULL)  #订单外建
    address_id = models.ForeignKey(Address, blank=True, null=True, on_delete=models.SET_NULL)  #地址外建
    order_detail_number = models.IntegerField() #商品数量
    order_detail_money = models.IntegerField() #金额
=======
    order_id = models.ForeignKey(Order, blank=True, null=True, on_delete=models.SET_NULL)  # 订单外建
    address_id = models.ForeignKey(Address, blank=True, null=True, on_delete=models.SET_NULL) # 地址外建
    order_detail_number = models.IntegerField()  # 商品数量
    order_detail_money = models.IntegerField()  # 金额
>>>>>>> 705b8135a6f15b88600ab83f3d133443094af22e
    order_num = models.IntegerField()
    odate = models.DateTimeField(auto_now_add=True)
    order_detail_remarks = models.CharField(max_length=40)  # 备注


class History(models.Model):
    customer_id = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    seller_id = models.ForeignKey(Seller, blank=True, null=True, on_delete=models.SET_NULL)
    food_id = models.ForeignKey(Food, blank=True, null=True, on_delete=models.SET_NULL)
<<<<<<< HEAD
    order_id = models.ForeignKey("Order", blank=True, null=True, on_delete=models.SET_NULL)  # 订单外建
=======
    order_id = models.ForeignKey(Order, blank=True, null=True, on_delete=models.SET_NULL)  # 订单外建
>>>>>>> 705b8135a6f15b88600ab83f3d133443094af22e
    address_id = models.ForeignKey(Address, blank=True, null=True, on_delete=models.SET_NULL)  # 地址外建
    order_detail_id = models.ForeignKey('order_detail', blank=True, null=True, on_delete=models.SET_NULL)
    order_detail_number = models.IntegerField()
    order_detail_money = models.IntegerField()
    odate = models.DateTimeField(auto_now_add=True)
    order_status = models.IntegerField(choices=[(0, '未发送'), (1, '已发送'), (2, '确认收货')])
