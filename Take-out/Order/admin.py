from django.contrib import admin
from .models import *
from Order_dinner.models import *
# Register your models here.
admin.site.register(Order_detail)
admin.site.register(Order)
admin.site.register(History)
admin.site.register(Cart)