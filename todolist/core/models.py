from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    REQUIRED_FIELDS = [] #поскольку в Abstract_User есть emal, нам надо сделать его необязательным

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"

# Create your models here.
