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
<<<<<<< HEAD
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Order/', include('Order.urls')),
    path('Order_dinner/', include('Order_dinner.urls')),
    path('Person/', include('Person.urls')),
    path('Payment/', include('Payment.urls')),
    path('Comment/', include('Comment.urls')),
    path('Delicious/', include('Delicious.urls'))
=======
from django.urls import path
from django.conf.urls import url,include
from Order import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url('Order/', include('Order.urls')),
    url('dingdan/', views.O_index)
    #url('Order_dinner/', include('Order_dinner.urls')),
    #url('Person/', include('Person.urls')),
    #url('Payment/', include('payment.urls')),
    #url('Comment/', include('Comment.urls')),
    #url('Delicious/', include('Delicious.urls')),

>>>>>>> 9a52cebf62d17fe90275716243159a0a719ae9ef
]

