"""Take_out URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Order/', include('Order.urls')),
    path('Order_dinner/', include('Order_dinner.urls')),
    path('Person/', include('Person.urls')),
    path('Payment/', include('Payment.urls')),
    path('Comment/', include('Comment.urls')),
    path('Delicious/', include('Delicious.urls')),
    url(r'^index/',views.xp_index,),
    url(r'^find/$',views.xp_find,),
    url('order/',views.xp_order,),
    url('mine/',views.xp_mine,),
    url('meisi/',views.xp_deli),
    url('search/',views.xp_search),
    url('drink/',views.xp_drink),
    url('supermarkete/',views.xp_supermarket),
    url('nearmeisi/',views.xp_near_deli),
    url('hotsa/',views.xp_hot_sale),
    url('order_show/',views.xp_order_show),

]

