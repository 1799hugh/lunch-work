from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    username = models.CharField(max_length=150, unique=True)  # 帳號名稱
    email = models.EmailField(unique=True)  # 電子郵件
    password = models.CharField(max_length=128)  # 密碼（應加密存儲）
    created_at = models.DateTimeField(auto_now_add=True)  # 建立時間

    def __str__(self):
        return self.username

class Order(models.Model):
    MENU_CHOICES = [
        ('burger', '麵類'),
        ('pizza', '飯類'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 使用者
    item = models.CharField(max_length=50, choices=MENU_CHOICES)  # 選單選項
    quantity = models.PositiveIntegerField()                 # 數量
    created_at = models.DateTimeField(auto_now_add=True)     # 點餐時間

    def __str__(self):
        return f"{self.user.username} ordered {self.quantity} x {self.get_item_display()}"