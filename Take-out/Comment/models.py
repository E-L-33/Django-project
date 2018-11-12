from django.db import models
from Person.models import Customer
from Order.models import Order
from Order_dinner.models import Seller


# Create your models here.
class Elaluate(models.Model):

    shopid = models.ForeignKey(Seller, blank=True, null=True, on_delete=models.SET_NULL)
    orderid = models.ForeignKey(Order, blank=True, null=True, on_delete=models.SET_NULL)
    userid = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    goodsScore = models.IntegerField()
    serviceScore = models.IntegerField()
    content = models.CharField(max_length=120)
    image = models.ImageField()
    isshow = models.BooleanField()
