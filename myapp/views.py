from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.urls import path
from . import views
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from myapp.models import Account

def index(request):
    return render(request, 'myapp/index.html')  # 渲染模板

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

def home_view(request):
    return render(request, 'myapp/home.html')



urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),  # 首頁
]