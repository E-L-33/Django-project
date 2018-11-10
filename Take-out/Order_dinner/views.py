from django.shortcuts import render
from .models import *
# Create your views here.
def xc_xindian(request):
    return render(request,'新店.html')