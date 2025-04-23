from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.urls import path
from . import views
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from myapp.models import Account
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order

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
    if not request.user.is_authenticated:  # 如果用戶未登入
        return render(request, 'myapp/index.html')  # 顯示登入選項
    return render(request, 'myapp/home.html')  # 已登入顯示歡迎頁面

@login_required
def order_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # 儲存點餐資料
            Order.objects.create(
                user=request.user,
                item=form.cleaned_data['item'],
                quantity=form.cleaned_data['quantity']
            )
            return redirect('home')  # 點餐完成後返回首頁
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),  # 首頁
]