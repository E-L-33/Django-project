from django.shortcuts import render,redirect
from django.db.models import Q
from Order_dinner.models import Seller
from Order.models import *
from django.core.paginator import Paginator
def xp_index(request):
    #xp_se=Seller.objects.values()
    xp_se='这里可以删除'
    concent={'xp_se':xp_se}
    return render(request,'index.html',concent)
def xp_find(request):
    return render(request,'faxian.html')
def xp_order(request):
    return render(request,'订单/订单.html')
def xp_mine(request):
    return render(request,'mine.html')
def xp_deli(request):
    return render(request,'美食/美食.html')
def xp_search(request):
    se=request.POST.get('search')
    obj=Seller.objects.filter(Q(sname__contain=se)|Q(Food__fname__contain=se))
    content={'obj':obj}
    return redirect(request,'index',content)
def xp_drink(request):
    return render(request,'饮品/饮品.html')
def xp_supermarket(request):
    return render(request,'超市/超市.html')
def xp_near_deli(request):
    return render(request,'附近美食/附近美食.html')
def xp_hot_sale(request):
    return render(request,'热卖/热卖.html')
def xp_order_show(request):
    #order=Order()
    orde=Order_detail.objects.all()
    cont={'orde':orde}
    return render(request,'订单/订单2.html',cont)
