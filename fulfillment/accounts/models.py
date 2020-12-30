from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass

    class Meta:
        db_table = 'memobot_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
