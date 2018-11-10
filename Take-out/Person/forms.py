from django import forms
from django import contrib
from django.contrib.auth.models import User

class Register_Forms(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    password_again = forms.CharField()

class Login_Forms(forms.Form):
    pass