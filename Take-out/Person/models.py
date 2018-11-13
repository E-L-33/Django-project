from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Address(models.Model):
    uid = models.ForeignKey('Customer', on_delete=models.DO_NOTHING)  # 用户的id
    adress = models.CharField(max_length=100)  # 地址
    Aphone = models.IntegerField()  # 配送地址的关联电话


class Customer(models.Model):
    uname = models.CharField(max_length=20)  # 用户名
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # Foreign Key	关联到User
    pay_password = models.IntegerField()  # 用户的支付密码
    loyalty = models.IntegerField()  # 积分
    vips = models.IntegerField()  # vip等级，默认为0,普通会员
    address_id = models.ForeignKey(Address, on_delete=models.DO_NOTHING)  # Foreign Key	关联到用户的地址表
    head = models.ImageField()  # Varchar	用户的头像
    ex_password = models.IntegerField()  # 免密支付，0为免，1为不免，默认为1
    wallet = models.IntegerField()  # 钱包余额
    phone = models.IntegerField()  # 用户绑定的手机
    wechat = models.CharField(max_length=20)  # 用户绑定的微信号
    qq = models.IntegerField()  # 用户绑定的QQ
    add_time = models.DateTimeField()  # 加入时间
