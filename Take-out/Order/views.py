from django.shortcuts import render,redirect,HttpResponse
from .models import *
from Order_dinner.models import *
from Person.models import *

from django.contrib.auth.models import User
from Person import *
# Create your views here.
def dingdan(request):
    # seller1=request.GET.getlist("id")
    #  id=request.POST.get('')
    obj = Order.objects.all()
    sp = Seller.objects.all()
    sp2 = Food.objects.all()
    con = {'user': obj, 'user2': sp, 'user3': sp2}
    return render(request, 'Order/订单/订单2.html', con)


def xp_pay(request):
    sid = request.POST.get('seller')

    ca = Cart()
    #print(sid)
    li = []
    qu = []
    per = []
    # uid = request.POST.get('uid')
    id=request.session.get('userid')
    uid=id
    print('----------------------')
    print(uid,type(uid))
    cost = request.POST.get('cost')
    #print(cost)
    for i in request.POST.getlist('qu'):
        if i != '':
            qu.append(i)
    for s in request.POST.getlist('food'):
        if s != '':
            li.append(s)
    for e in request.POST.getlist('price'):
        if e!='':
            per.append(e)
    # print(li,qu,per)
    #print(ids)
    for g in range(len(li)):
            Cart.objects.create(Seller_id=sid,Food_id=li[g],puantity=qu[g],Customer_id=uid)
            ca.save()

    sname=Seller.objects.filter(id=sid)
    cont={'uid':uid,'sname':sname,'cost':cost}
    return render(request, 'Order/订单/微信支付.html', cont)


def xp_pays(request):
    userid = request.session.get('userid', '')  # 从session获取设置的userid值
    # print(name,'***************')
    if userid=='':
        return HttpResponse('<h1>您还没登录，请！<a href="/Person/login/">登录</a></h1>')
    name=User.objects.filter(id=userid).values('username')[0]['username']

    paypwd=request.POST.get('pwd')
    cost = request.POST.get('cost')
    Sname=request.POST.get('Sname')
    # sellerid=Seller.objects.filter(Sname=Sname).values('id')[0]['id']
    cost=int(cost)
    print('====================')
    pay = ''
    for i in paypwd:

        if i!=',':

            pay+=i
    pay=int(pay)
    cart = Cart.objects.filter(puantity=0).all()

    cart.delete()
    cart=Cart.objects.filter(Customer_id=userid).values()
    ord = Order()
    for j in cart:


        print(j)
        price=Food.objects.filter(id=j['Food_id']).values('price')[0]['price']
        money=price*j['puantity']
        print(j['puantity'])
        Order.objects.create(selle_id=j['Seller_id'],foo_id=j['Food_id'],order_number=j['puantity'],order_status=0,
                            custome_id=j['Customer_id'],order_money=money)
        ord.save()

    cart = Cart.objects.filter(Customer_id=userid).all()
    cart.delete()

    password=Customer.objects.filter(uname=name).values('pay_password')[0]['pay_password']
    wallet = Customer.objects.filter(uname=name).values('wallet')[0]['wallet']

    # print('---------------------------------------')
    # print(type(wallet),type(cost))
    # print(paypwd,pay,password,type(pay),type(password))

    if pay==password:
        if wallet<cost:
            return HttpResponse('<h1>余额不足，请冲值！<a href="/index/">返回到首页</a></h1>')
        else:
            wallet = wallet-cost
            cus=Customer.objects.get(uname=name)
            cus.wallet=wallet
            cus.save()

            contest={'cost':cost,'sname':Sname,'sel':wallet}
            return render(request, 'Order/订单/支付成功.html',contest)
    else:
        return HttpResponse('<h1>密码输入错误！<a href="#" onclick="javascript:history.back(-1);">返回到上一页</a></h1>')
    # else:
    #     return render(request,'Order/订单/微信支付.html')


# def xp_dingdanxq(request):
#     return render(request,'Order/订单/订单详情.html')
def xp_dingdan4(request):
    return render(request, 'pzb/dingdan4.html')
