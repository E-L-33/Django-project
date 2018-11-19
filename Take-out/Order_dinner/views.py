from django.shortcuts import render, redirect
from .models import *
from django.db.models import *


# Create your views here.
def xc_xindian(request):
    bos = Seller.objects.all()
    context = {'seller': bos}
    cos = Food.objects.all()
    conten = {'food': cos}
    return render(request, 'Order_dinner/新店.html')


def xc_store(request):
    Sname = request.POST.get('Sname')
    address = request.POST.get('address')
    starting_price = request.POST.get('starting_price')
    dist_price = request.POST.get('dist_price')
    pictur = request.POST.get('pictur')
    Monthle_sale = request.POST.get('Monthle_sale')
    reduce = request.POST.get('reduce')
    new_price = request.POST.get('new_price')
    price_reduction = request.POST.get('price_reduction')
    Business_hours = request.POST.get('Business_hours')
    Sphone = request.POST.get('Sphone')
    Sphone = int(Sphone)
    # print(type(new_price), new_price, reduce)
    seller = Seller()
    seller.Sname = Sname
    seller.address = address
    seller.starting_price = starting_price
    seller.dist_price = dist_price

    seller.Sphone = Sphone
    seller.Monthle_sale = Monthle_sale
    seller.new_price = new_price
    seller.pictur = pictur
    seller.reduce = reduce
    seller.Business_hours = Business_hours
    seller.price_reduction = price_reduction
    seller.save()
    return redirect('/order_dinner/xc_index')


# 首页
def xc_index(request):
    pass


#     bos = Seller.objects.all()
#
#     context = {}
#     context = {'seller': bos}
#     return render(request, 'Order_dinner/index.html', context)


# 发现
def xc_My(request):
    return render(request, 'Order_dinner/mine.html')


# 订单
def xc_order(request):
    return render(request, 'Order_dinner/dingdan4.html')


# 我的
def xc_discovery(request):
    return render(request, 'Order_dinner/mine.html')


# 商品表/小媳妇
def xc_cate(request, ids):
    context = {}
    sid=ids
    context['sid']=sid
    a = Cart.objects.all().aggregate(s=Sum('puantity'))['s']
    if a == None:
        a = 0
    context['sum'] = a
    ss = Food.objects.filter(id=F('cart__Food_id')).annotate(s=F('cart__puantity') * F('price')).values('s')
    ss = ss.aggregate(a=Sum('s'))['a']
    # print(ss)
    if ss == None:
        ss = 0
    context['sumprice'] = ss
    bos1 = Seller.objects.filter(id=ids)
    context['seller'] = bos1
    # context = {'seller': bos}
    bos = Food.objects.filter(Seller_id=ids)
    # context = {'food': bos}
    context['food'] = bos
    # print(context)
    return render(request, 'Order_dinner/小媳妇儿凉皮.html', context)


def xc_food(request):
    Fname = request.POST.get('Fname')
    msq = request.POST.get('msq')
    price = request.POST.get('price')
    discount = request.POST.get('discont')
    describe = request.POST.get('describe')
    photo = request.POST.get("photo")
    food_type = request.POST.get('food_type')
    Seller = request.POST.get('Seller')
    Commodity_type = request.POST.get('Commodity_type')
    Seller = int(Seller)
    # print(price, type(msq))
    food = Food()
    food.Fname = Fname
    food.msq = msq
    food.discount = discount
    food.price = price
    food.describe = describe
    food.photo = photo
    food.food_type = food_type
    food.Seller_id = Seller
    food.Commodity_type = Commodity_type
    food.save()
    return redirect('/order_dinner/xc_cate')


# 购物车
def xc_add(request, ids):
    d = Seller.objects.get(food__id=ids).id
    try:
        a = Cart.objects.get(Food_id=ids).Food_id
        puantity = Cart.objects.get(Food_id=ids).puantity
        puantity = puantity + 1
        # print(type(puantity))
        cart = Cart.objects.get(Food_id=a)
        cart.puantity = puantity
        cart.save()
    except:

        puantity = 1

        Customer = 1
        food_id = ids
        seller = 1
        state = 0
        cart = Cart()
        cart.puantity = puantity
        cart.Food_id = food_id
        cart.state = state
        cart.Seller_id = seller
        cart.Customer_id = Customer
        cart.save()
    return redirect('cate', d)


def xc_reduction(request, ids):
    d = Seller.objects.get(food__id=ids).id
    try:
        a = Cart.objects.get(Food_id=ids).Food_id  # 判断食物id在Cart表中是否存在
        puantity = Cart.objects.get(Food_id=ids).puantity

        # print(puantity)
        if puantity > 1:

            puantity = puantity - 1

            cart = Cart.objects.get(Food_id=a)
            cart.puantity = puantity
            cart.save()
        elif puantity > 0:

            reduct = Cart.objects.filter(Food_id=ids)
            reduct.delete()
    except:
        print(1)
    return redirect('cate', d)


# 11_13增加
# 食品
def xc_Delicious_food(request):
    bos = Seller.objects.all()

    context = {'seller': bos}
    print(context['seller'])
    return render(request, 'Order_dinner/美食.html', context)


# 饮品
def xc_drink(request):
    bos = Seller.objects.filter(id__gt=11).values()

    context = {'seller': bos}
    # print(context['seller'])
    return render(request, 'Order_dinner/饮品.html', context)


# 超市
def xc_supermarket(request):
    bos = Seller.objects.all()

    context = {'seller': bos}
    # print(context['seller'])
    return render(request, 'Order_dinner/超市.html', context)


#早餐
def xc_breakfast(request):
    bos = Seller.objects.all()

    context = {'seller': bos}

    return render(request, 'Order_dinner/饮品.html', context)
# 蔬果
def xc_vegetable(request):

    bos = Seller.objects.all()

    context = {'seller': bos}

    return render(request,'Order_dinner/饮品.html',context)
#新店
def xc_new_store(request):

    bos = Seller.objects.all()

    context = {'seller': bos}

    return render(request,'Order_dinner/饮品.html',context)
# 外卖
def xc_buy_out(request):

    bos = Seller.objects.all()

    context = {'seller': bos}

    return render(request,'Order_dinner/饮品.html',context)
# 午饭
def xc_lunch(request):

    bos = Seller.objects.all()

    context = {'seller': bos}

    return render(request,'Order_dinner/饮品.html',context)
# 附近美食
def xc_nearby_gourmet(request):

    bos = Seller.objects.all()

    context = {'seller': bos}

    return render(request,'Order_dinner/饮品.html',context)
# 霸王餐
def xc_dine(request):

    bos = Seller.objects.all()

    context = {'seller': bos}

    return render(request,'Order_dinner/饮品.html',context)
# 零食
def xc_snacks(request):

    bos = Seller.objects.all()

    context = {'seller': bos}

    return render(request,'Order_dinner/饮品.html',context)
#精品
def xc_boutique(request):

    bos = Seller.objects.all()

    context = {'seller': bos}
    return render(request,'Order_dinner/饮品.html',context)
def xc_find(request):

    bos = Seller.objects.all()

    context = {'seller': bos}
    # bos = Food.objects.filter(id3)
    #
    # context = {'foods': bos}
    # bos = Food.objects.filter(id<3)
    #
    # context = {'food': bos}

    return render(request,'Order_dinner/faxian.html',context)
# def xc_payment(request,ids):
#     id=request.POST.get('seller')
#     Sname=Seller.objects.get(id=id).Sname
#     bos = Food.objects.values()
#     # cont={}
#     # cont['bos']=bos
#     # for fod in bos:
#
#         # print(fod)
#     food = request.POST.get('food1')
#     qu = request.POST.get('qu1')
#     price = request.POST.get('price1')
#     cost = request.POST.get('cost')
#     # print(id,type(id),ids,price,qu,food,Sname)
#
#     context={}
#     context['Sname']=Sname
#     context['cost'] = cost
#
#     return render(request,'Order_dinner/微信支付.html',context)