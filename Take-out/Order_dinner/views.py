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
    print(type(new_price), new_price, reduce)
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
    bos = Seller.objects.all()

    context = {}
    context = {'seller': bos}
    return render(request, 'Order_dinner/index.html', context)


# 发现
def xc_My(request):
    return render(request, 'Order_dinner/mine.html')


# 订单
def xc_order(request):
    return render(request, 'Order_dinner/dingdan4.html')


# 我的
def xc_discovery(request):
    return render(request, 'Order_dinner/mine.html')


def xc_cate(request, ids):

    context = {}
    # aa=Cart.objects.filter(Food_id=ids)['puantity']
    # context['cart']=aa
    a=Cart.objects.all().aggregate(s=Sum('puantity'))['s']
    context['sum']=a
    ss = Food.objects.filter(id=F('cart__Food_id')).annotate(s=F('cart__puantity') * F('price')).values('s')
    ss=ss.aggregate(a=Sum('s'))['a']
    context['sumprice']=ss
    bos1 = Seller.objects.filter(id=ids)
    context['seller'] = bos1
    # context = {'seller': bos}
    bos = Food.objects.filter(Seller_id=ids)
    # context = {'food': bos}
    context['food'] = bos
    print(context)
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
    print(price, type(msq))
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
def xc_add(request,ids):
    d = Seller.objects.get(food__id=ids).id
    try:
        a =Cart.objects.get(Food_id=ids).Food_id
        puantity=Cart.objects.get(Food_id=ids).puantity
        puantity=puantity+1
        print(type(puantity))
        cart=Cart.objects.get(Food_id=a)
        cart.puantity=puantity
        cart.save()
    except:

        puantity=1


        food_id=ids

        state=0
        cart=Cart()
        cart.puantity=puantity
        cart.Food_id=food_id
        cart.state=state
        cart.save()
    return redirect('cate',d)
def xc_reduction(request,ids):
    d = Seller.objects.get(food__id=ids).id
    reduct=Cart.objects.filter(Food_id=ids)
    reduct.delete()
    return redirect('cate',d)

