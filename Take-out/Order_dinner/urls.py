from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^xc_xindian/$',views.xc_xindian),
    url(r'^xc_store/*$',views.xc_store,name='store'),
    url(r'^xc_index/$',views.xc_index,name='xc_index'),
    url(r'^xc_My/$',views.xc_My,name='xc_My'),
    url(r'^xc_discovery/$',views.xc_discovery,name='xc_discovery'),
    url(r'^xc_order/$',views.xc_order,name='xc_order'),
    url(r'^xc_cate/$',views.xc_cate,name='xc_cate'),
    url(r'^xc_food/$',views.xc_food,name='xc_food'),
]

