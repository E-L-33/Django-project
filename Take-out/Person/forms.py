from django import forms
from django.contrib import auth
from django.contrib.auth.models import User


class Register_Forms(forms.Form):
    username = forms.CharField(min_length=6, max_length=12, label='帐号',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '输账号啊，这里'}))
    email = forms.EmailField(label='邮箱',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '输入邮箱啊，这里'}))
    password = forms.CharField(min_length=6, max_length=20, label='密码',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '输密码，快点'}))
    password_again = forms.CharField(min_length=6, max_length=20, label='Again',
                                     widget=forms.PasswordInput(
                                         attrs={'class': 'form-control', 'placeholder': '密码,Again'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('帐号已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('此邮箱已被使用')
        return email

    def clean_passwoard(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password_again != password:
            raise forms.ValidationError('两次密码不一致')
        return password_again


class Login_Forms(forms.Form):
    username = forms.CharField(label='用户名',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输用户名'}))
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data
