from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [

    # url(r'^xc_xindian/$',views.xc_xindian),
    path('xc_xaindian/', views.xc_xindian, name='xc_xindian'),
    url(r'^xc_store/*$', views.xc_store, name='store'),
    url(r'^xc_index/$', views.xc_index, name='index'),
    url(r'^xc_My/$', views.xc_My),
    url(r'^xc_discovery/$', views.xc_discovery),
    url(r'^xc_order/$', views.xc_order),
    # url(r'^xc_cate/$',views.xc_cate,name='xc_cate'),
    path(r'xc_cate/<int:ids>', views.xc_cate, name='cate'),#商品表
    path('xc_reduction/<int:ids>', views.xc_reduction, name='xc_reduction'),#商品减
    path('xc_add/<int:ids>', views.xc_add, name='xc_add'),#商品增加
    url(r'^xc_food/$', views.xc_food, name='xc_food'),
    path('xc_Delicious_food/',views.xc_Delicious_food,name='xc_Delicious_food'),#美食
    path('xc_drink/',views.xc_drink,name='xc_drink'),#饮品
    path('xc_supermarket',views.xc_supermarket,name='xc_supermarket'),#超市
    path('xc_breakfast/',views.xc_breakfast,name='xc_breakfast'),#早餐
    path('xc_vegetable/', views.xc_vegetable, name='xc_vegetable'),  # 蔬果
    path('xc_new_store/', views.xc_new_store, name='xc_new_store'),  # 新店
    path('xc_buy_out/', views.xc_buy_out, name='xc_buy_out'),  # 外卖
    path('xc_lunch/', views.xc_lunch, name='xc_lunch'),  # 午饭
    path('xc_nearby_gourmet/', views.xc_nearby_gourmet, name='xc_nearby_gourmet'),  # 附近美食
    path('xc_dine/', views.xc_dine, name='xc_dine'),  # 霸王餐
    path('xc_snacks/', views.xc_snacks, name='xc_snacks'),  # 零食

    path('xc_boutique/', views.xc_boutique, name='xc_boutique'),  # 精品
    # path('xc_drink/', views.xc_drink, name='xc_drink'),  # 饮品


]
