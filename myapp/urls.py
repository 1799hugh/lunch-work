from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.login_view, name='login'),  # 登入頁面
    path('', views.home_view, name='home'),         # 首頁
    path('order/', views.order_view, name='order'), # 點餐頁面
]