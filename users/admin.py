from atexit import register
from django.contrib import admin
from .models import MyUserModel
# Register your models here.

admin.site.register(MyUserModel)