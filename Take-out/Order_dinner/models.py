from django.db import models


# Create your models here.
class Seller(models.Model):
    Sname = models.CharField(max_length=20)  # 店铺名称
    address = models.CharField(max_length=100)  # 店铺地址
    starting_price = models.IntegerField()  # 起送价
    dist_price = models.IntegerField()  # 配送价
    Monthle_sale = models.IntegerField(default='30')  # 月销量
    reduce = models.IntegerField(default='13')  # 满减价
    price_reduction = models.IntegerField(default='13')  # 减价
    new_price = models.IntegerField(default='18')  # 新用户立减
    pictur= models.CharField(max_length=100,default='wm-1.gif')  # 图片名
    Sphone = models.BigIntegerField()  # 电话
    Business_hours=models.CharField(max_length=100,default='8:00-21:00')#营业时间

    class Meta:
        db_table = 'Seller'


class Food(models.Model):
    Fname = models.CharField(max_length=30)  # 食物名
    msq = models.IntegerField()  #商品月销量
    price = models.IntegerField()#商品价格
    discount = models.IntegerField(null=True)#商品打折
    describe = models.CharField(max_length=300)#商品描述
    photo = models.CharField(max_length=100,default='wm-1.gif')  # 食物图片名
    food_type=models.CharField(max_length=100,default='木桶饭')#食品类型
    Seller = models.ForeignKey("Seller", on_delete=models.DO_NOTHING)#商铺外键
    Commodity_type=models.CharField(max_length=50,default="早餐/汉堡")#商品类型
    class Meta:
        db_table = 'Food'
