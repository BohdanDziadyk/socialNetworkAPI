from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    photo = models.ImageField(blank=True)
    phone = models.CharField(max_length=13, unique=True)
