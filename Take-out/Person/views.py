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
