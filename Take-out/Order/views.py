from django.shortcuts import render
from .models import *
# Create your views here.
def dingdan(request):
    return render(request,'Order/订单/订单.html')
def dingdan2(request):
    return render(request,'Order/订单/订单2.html')
def zhifu(request):
    return render(request,'Order/订单/支付详情.html')