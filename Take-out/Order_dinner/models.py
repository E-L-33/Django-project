from django.db import models

# Create your models here.
class Seller(models.Model):
    Sname=models.CharField(max_length=20)# 店铺名称
    address=models.CharField(max_length=100)#店铺地址
    starting_price=models.IntegerField()#起送价
    dist_price=models.IntegerField()#配送价
    seller_photo=models.ImageField (upload_to='img',height_field=500,width_field=500,max_length=100)#品牌图片
    Sphone=models.IntegerField()
    class Meta:
        db_table='Seller'
class Food(models.Model):
    Fname=models.CharField(max_length=20)
    msq=models.IntegerField()
    price=models.IntegerField()
    discount=models.IntegerField(null=True)
    describe=models.CharField(max_length=200)
    food_photo=models.ImageField(upload_to='img',height_field=500,width_field=500,max_length=100)

    Seller=models.ForeignKey("Seller",on_delete=models.DO_NOTHING)
