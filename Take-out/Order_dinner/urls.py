from django.conf.urls import url,include
from django.urls import path
from . import views

urlpatterns = [

    url(r'^xc_xindian/$',views.xc_xindian),
    url(r'^xc_store/*$',views.xc_store),
    url(r'^xc_index/$',views.xc_index,name='index'),
    url(r'^xc_My/$',views.xc_My),
    url(r'^xc_discovery/$',views.xc_discovery),
    url(r'^xc_order/$',views.xc_order),
    # url(r'^xc_cate/$',views.xc_cate,name='xc_cate'),
    path(r'xc_cate/<int:ids>',views.xc_cate,name='cate'),
    path('xc_reduction/<int:ids>',views.xc_reduction,name='xc_reduction'),
    path('xc_add/<int:ids>',views.xc_add,name='xc_add'),
    url(r'^xc_food/$',views.xc_food),
]
