
from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    url('dingdan/',views.dingdan),
    # url('dingdanxq/',views.xp_dingdanxq),
    url('pay/',views.xp_pay),
    url('paysu/',views.xp_pays),
    url('pay/',views.xp_dingdan4)

]

