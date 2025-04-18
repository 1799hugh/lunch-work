from django.contrib import admin
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

admin.site.register(Account)