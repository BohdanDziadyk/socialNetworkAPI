from django.db import models

from post.models import PostModel
from user.models import UserModel


# Create your models here.

class CommentModel(models.Model):
    class Meta:
        db_table = 'comment'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comment')
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
