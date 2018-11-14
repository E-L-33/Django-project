from django.shortcuts import render, redirect
from django.db.models import *
# from Order_dinner.models import *
from django.db.models import *
from Order.models import *
from Order_dinner.models import *
from django.core.paginator import Paginator


def xp_index(request):

    #zjc修改11-13
    bos = Seller.objects.all()

    context = {'seller': bos}
    print(context['seller'])
    return render(request, 'pzb/index.html',context)


def xp_find(request):
    return render(request, 'pzb/faxian.html')


def xp_order(request):
    return render(request, 'pzb/订单/订单.html')


def xp_mine(request):
    return render(request, 'mine.html')

#美食
def xp_deli(request):
    #zjc修改11-14
    bos = Seller.objects.all()

    context = {'seller': bos}
    print(context['seller'])

    return render(request, 'pzb/美食/美食.html',context)


def xp_search(request):
    se = request.POST.get('search')
    obj = Seller.objects.filter(Q(sname__contains=se) | Q(Food__fname__contains=se))
    content = {'obj': obj}
    return redirect(request, 'index', content)


def xp_drink(request):
    return render(request, 'pzb/饮品/饮品.html')


def xp_supermarket(request):
    return render(request, 'pzb/超市/超市.html')


def xp_near_deli(request):
    return render(request, 'pzb/附近美食/附近美食.html')


def xp_hot_sale(request):
    return render(request, 'pzb/热卖/热卖.html')


def xp_order_show(request):
    # order=Order()
    orde = Order_detail.objects.all()
    cont = {'orde': orde}
    return render(request, 'pzb/订单/订单2.html', cont)
