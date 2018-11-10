from django.db import models

# Create your models here.
class Elaluate(models.Model):
	shopid=models.ForeignKey('shopid',on_delete='')
	orderid=models.ForeignKey('orderid',on_delete='')
	userid=models.Foreignkey('userid',on_delete='')
	goodsScore=models.IntegerField(max_length=20)
	serviceScore=models.IntegerField(max_length=20)
	content=models.CharField(max_length=120)
	image=models.ImageField()
	isshow=models.BooleanField()
	####

