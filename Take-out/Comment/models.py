from django.db import models
from Person.models import Customer
from Order.models import Order
from Order_dinner.models import Seller


# Create your models here.
class Elaluate(models.Model):
    shopid = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    orderid = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    userid = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    goodsScore = models.IntegerField()
    serviceScore = models.IntegerField()
    content = models.CharField(max_length=120)
    image = models.ImageField()
    isshow = models.BooleanField()
