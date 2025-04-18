from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 定義首頁路由
    path('login/', views.login_view, name='login'),  # 登入頁面
]