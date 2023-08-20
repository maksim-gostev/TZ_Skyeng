from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(blank=True, max_length=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
