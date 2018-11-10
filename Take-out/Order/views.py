from django.shortcuts import render

# Create your views here.
def O_index(request):
    return render(request,'订单.html')