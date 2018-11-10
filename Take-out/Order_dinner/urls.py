<<<<<<< HEAD
from django.urls import path


urlpatterns = []
=======
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('xc_xindian/',views.xc_xindian)
]
>>>>>>> 945be238c71e9e76dd43db4d8302bd9bdf15cf2a
