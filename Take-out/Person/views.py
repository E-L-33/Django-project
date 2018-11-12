from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import Register_Forms, Login_Forms


# Create your views here.
def uregister(request):
    if request.method == 'POST':
        register = Register_Forms(request.POST)
        if register.is_valid():  # 如果数据是有效数据
            username = register.cleaned_data['username']
            email = register.cleaned_data['email']
            password = register.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.save()
            # 用户登录
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('test')))
    else:
        register = Register_Forms()

    context = {}
    context['register'] = register
    return render(request, 'Person/register.html', context)


def tests(request):
    return HttpResponse('<h1>sucessful!!!!</h1>')


def ulogin(request):
    if request.method == 'POST':
        forms = Login_Forms(request.POST)
        if forms.is_valid():
            user = forms.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('form', reverse('test')))
    else:
        forms = Login_Forms()

    context = {}
    context['forms'] = forms
    return render(request, 'Person/login.html', context)


def umine(request):
    return render(request, 'Person/mine.html')


def uaddress(request):
    return render(request, 'Person/address.html')


def uchange(request):
    return render(request, 'Person/change.html')


def ucollection(request):
    return render(request, 'Person/collection.html')


def uinstall(request):
    return render(request, 'Person/install.html')


def uintegral(request):
    return render(request, 'Person/integral.html')


def umember(request):
    return render(request, 'Person/member.html')


def unotice(request):
    return render(request, 'Person/notice.html')


def uservice(request):
    return render(request, 'Person/service.html')


def uuser(request):
    return render(request, 'Person/user.html')


def uwallet(request):
    return render(request, 'Person/wallet.html')


def uchoice(request):
    return render(request, 'Person/choice.html')
