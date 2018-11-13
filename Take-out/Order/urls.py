
from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    url('dingdan/',views.dingdan),
    url('dingdan2/',views.dingdan),
    url('zhifu/',views.zhifu),
]

