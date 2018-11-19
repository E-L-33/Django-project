from django.db import models
from Person.models import Customer, Address
from Order_dinner.models import Seller, Food



class Order(models.Model):
    custome = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL) #用户外建
    selle= models.ForeignKey(Seller, blank=True, null=True, on_delete=models.SET_NULL) #店家外建
    histor = models.ForeignKey('History', blank=True, null=True, on_delete=models.SET_NULL) #历史外建
    foo = models.ForeignKey(Food, blank=True, null=True, on_delete=models.SET_NULL)  #商品外建
    order_number = models.IntegerField()  #商品数量
    order_money = models.IntegerField()   #金额
    odate = models.DateTimeField(auto_now_add=True) #时间
    order_status = models.IntegerField(choices=[(0, '未发送'), (1, '已发送'), (2, '确认收货')]) #状态


class Order_detail(models.Model):
    custome= models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    selle = models.ForeignKey(Seller, blank=True, null=True, on_delete=models.SET_NULL)
    histor= models.ForeignKey('History', blank=True, null=True, on_delete=models.SET_NULL)
    foo= models.ForeignKey(Food, blank=True, null=True, on_delete=models.SET_NULL)
    orde = models.ForeignKey("Order", blank=True, null=True, on_delete=models.SET_NULL)  #订单外建
    addres = models.ForeignKey(Address, blank=True, null=True, on_delete=models.SET_NULL)  #地址外建
    order_detail_number = models.IntegerField() #商品数量
    order_detail_money = models.IntegerField() #金额
    order_num = models.IntegerField()
    odate = models.DateTimeField(auto_now_add=True)
    order_detail_remarks = models.CharField(max_length=40)  # 备注


class History(models.Model):
    custome= models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    selle = models.ForeignKey(Seller, blank=True, null=True, on_delete=models.SET_NULL)
    foo = models.ForeignKey(Food, blank=True, null=True, on_delete=models.SET_NULL)
    orde = models.ForeignKey('Order', blank=True, null=True, on_delete=models.SET_NULL)  # 订单外建
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.SET_NULL)  # 地址外建
    order_detai = models.ForeignKey('order_detail', blank=True, null=True, on_delete=models.SET_NULL)
    order_detail_number = models.IntegerField()
    order_detail_money = models.IntegerField()
    odate = models.DateTimeField(auto_now_add=True)
    order_status = models.IntegerField(choices=[(0, '未发送'), (1, '已发送'), (2, '确认收货')])
