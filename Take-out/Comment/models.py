from django.db import models
from Person.models import Customer
from Order.models import Order
from Order_dinner.models import Seller


# Create your models here.
class Elaluate(models.Model):
<<<<<<< HEAD
    shopid = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    orderid = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    userid = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
=======
    shopid = models.ForeignKey(Seller, blank=True, null=True, on_delete=models.SET_NULL)
    orderid = models.ForeignKey(Order, blank=True, null=True, on_delete=models.SET_NULL)
    userid = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
>>>>>>> 705b8135a6f15b88600ab83f3d133443094af22e
    goodsScore = models.IntegerField()
    serviceScore = models.IntegerField()
    content = models.CharField(max_length=120)
    image = models.ImageField()
    isshow = models.BooleanField()
