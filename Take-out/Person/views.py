from django.shortcuts import render


# Create your views here.
def uregister(request):
    return render(request, 'Person/register.html')


def ulogin(request):
    return render(request, 'Person/login.html')
