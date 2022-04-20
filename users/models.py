from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUserModel(AbstractUser):
    age = models.PositiveIntegerField(verbose_name = 'возраст', default=18, blank=True)
    phone = models.CharField(verbose_name='телефон', blank=True, max_length=20)
    city = models.CharField(verbose_name='город', blank=True, max_length=20)
    email = models.EmailField(verbose_name='email', unique=True)