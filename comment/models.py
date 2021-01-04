import os

from django.db import models

from post.models import PostModel
from user.models import UserModel


# Create your models here.
def images_directory_path(instance, filename):
    return os.path.join(f'{instance.user.username}', 'comments', filename)


class CommentModel(models.Model):
    class Meta:
        db_table = 'comment'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comment')
    body = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to=images_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
