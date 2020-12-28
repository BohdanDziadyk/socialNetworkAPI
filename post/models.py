import os

from django.db import models

from user.models import UserModel


def images_directory_path(instance, filename):
    return os.path.join(f'{instance.user.username}', 'posts', filename)


# Create your models here.
class PostModel(models.Model):
    class Meta:
        db_table = 'post'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=255, blank=True)
    body = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to=images_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
