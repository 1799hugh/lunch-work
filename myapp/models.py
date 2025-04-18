from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=150, unique=True)  # 帳號名稱
    email = models.EmailField(unique=True)  # 電子郵件
    password = models.CharField(max_length=128)  # 密碼（應加密存儲）
    created_at = models.DateTimeField(auto_now_add=True)  # 建立時間

    def __str__(self):
        return self.username
