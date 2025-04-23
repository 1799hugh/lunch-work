from django import forms
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from myapp.models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="帳號")
    password = forms.CharField(widget=forms.PasswordInput, label="密碼")

class OrderForm(forms.Form):
    MENU_CHOICES = [
        ('noodles', '麵類'),
        ('rise', '飯類'),
    ]
    item = forms.ChoiceField(label="餐點選擇", choices=MENU_CHOICES)
    quantity = forms.IntegerField(label="數量", min_value=1)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # 登入成功後重定向到首頁
            else:
                form.add_error(None, "帳號或密碼錯誤")
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})