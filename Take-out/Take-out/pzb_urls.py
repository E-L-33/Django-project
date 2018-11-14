from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.xp_index, ),
    path('find/', views.xp_find, ),
    path('order/', views.xp_order, ),
    path('meisi/', views.xp_deli),
    path('search/', views.xp_search),
    path('drink/', views.xp_drink),
    path('supermarkete/', views.xp_supermarket),
    path('nearmeisi/', views.xp_near_deli),
    path('hotsa/', views.xp_hot_sale),
    path('order_show/', views.xp_order_show),
]
