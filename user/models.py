from django.contrib.auth.models import AbstractUser
from django.db import models
import os


def user_directory_path(instance, filename):
    return os.path.join(f'{instance.user.username}', filename)


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    photo = models.ImageField(blank=True, upload_to=user_directory_path)
    phone = models.CharField(max_length=13, unique=True)
