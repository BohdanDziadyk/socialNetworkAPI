import os

from django.contrib.auth.models import AbstractUser
from django.db import models


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
    friends = models.ManyToManyField("UserModel", blank=True)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(UserModel, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserModel, related_name='to_user', on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=20, blank=True)


def images_directory_path(instance, filename):
    return os.path.join(f'{instance.user.username}', 'messages', filename)


class MessengerModel(models.Model):
    class Meta:
        db_table = "messenger"

    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="messages_send")
    receiver = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="messages_received")
    sender_name = models.CharField(max_length=20, blank=True)
    body = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to=images_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
