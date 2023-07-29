from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255, default=None, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    email_is_verified = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['username', 'password']
    USERNAME_FIELD = 'email'
