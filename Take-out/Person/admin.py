from django.contrib import admin
from .models import Customer, Address


# Register your models here.
@admin.register(Customer)
class Customer_Admin(admin.ModelAdmin):
    list_display = (
        'id', 'uname', 'pay_password', 'loyalty', 'ex_password', 'wallet', 'phone', 'add_time')


@admin.register(Address)
class Adress_Admin(admin.ModelAdmin):
    list_display = ('id', 'uid', 'adress', 'Aphone')
