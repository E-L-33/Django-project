from django.shortcuts import render,HttpResponse,redirect
from .models import *
from Order_dinner.models import *
from Person import *

# Create your views here.
def dingdan(request):
    seller1=request.GET.getlist("id")
    id=request.POST.get('')
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
    uid = request.POST.get('uid')
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
    print(li,qu,per)
    #print(ids)
    for g in range(len(li)):
            Cart.objects.create(Seller_id=sid,Food_id=li[g],puantity=qu[g],Customer_id=uid)
            ca.save()

    sname=Seller.objects.filter(id=sid)
    cont={'uid':uid,'sname':sname,'cost':cost,'li':li,'qu':qu,'per':per,'si':sid}
    return render(request, 'Order/订单/微信支付.html', cont)


def xp_pays(request):
    try:
        ca=Cart
        hi=History()
        od = Order_detail()
        ordd=Order()
        cu=Customer()
        paypwd=request.POST.get('pwd')
        qu=request.POST.get('qu')
        prices=request.POST.get('price')
        foodid=request.POST.get('food')
        paypwd=paypwd.replace(',','')
        sid=request.POST.get('sid')
        si=request.POST.get('si')
        si=str(si)
    #print(paypwd)
        cost=request.POST.get('cost')
        print(cost,qu,prices,paypwd,foodid,'_____')
        cost=int(cost)

        print(si)
        uid=request.POST.get('uid')
        print(uid)
       # pw=Customer.objects.filter(pay_password=paypwd)
        mo=Customer.objects.get(id=uid)
        foodid=list(foodid)
        qu=list(qu)
        yu=mo.wallet-cost
        print(type(qu),type(foodid))

        # if len(pw)!= 0:
        if '1' in paypwd:
            #支付成功
                if  yu>0:
                    mo.wallet=yu
                    mo.save()
                    # Cart.objects.filter(id=)
                    for o in range (len(foodid)):
                        print('-----',qu[o],foodid[o])
                    if qu[o].isdecimal() and foodid[o].isdecimal():

                            Order.objects.create(custome_id=uid, selle_id=si,foo_id=foodid[o], order_number=qu[o],order_money=cost,order_status=1)
                            ordd.save()
                    cons={'sid':sid,'cost':cost}
                    return render(request, 'Order/订单/支付成功.html',cons)
                else:
                    #余额不足

                    con={'提示':"您的余额已不足，请及时充值","cost":cost,'sid':sid,'pa':1,'uid': uid, 'cost': cost, 'li': foodid, 'qu': qu, 'per': prices}

                    return render(request,'Order/订单/微信支付.html',con)
        else:
            #支付失败
                de={'提示':'您输入的密码有误请重新输入','cost':cost,'sid':sid,'pa':1,'uid': uid, 'cost': cost, 'li': foodid, 'qu': qu, 'per': prices}
                return render(request,'Order/订单/微信支付.html',de)
    except:
                         #支付异常，调试时请关闭
                             return HttpResponse('系统正在维护中...')


def xp_dingdanxq(request):
    return render(request,'Order/订单/订单详情.html')
def xp_dingdan4(request):
    return render(request, 'pzb/dingdan4.html')

