from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.ulogin, name='login'),
    path('register/', views.uregister, name='register'),
    path('test/', views.tests, name='test'),

    path('mine/', views.umine, name='mine'),
    path('address/', views.uaddress, name='address'),
    path('change/', views.uchange, name='change'),
    path('collection/', views.ucollection, name='collection'),
    path('install/', views.uinstall, name='install'),
    path('integral/', views.uintegral, name='integral'),
    path('member/', views.umember, name='member'),
    path('notice/', views.unotice, name='notice'),
    path('service/', views.uservice, name='service'),
    path('user/', views.uuser, name='user'),
    path('wallet/', views.uwallet, name='wallet'),
    path('choice/', views.uchoice, name='chioce'),
]
