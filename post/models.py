from django.db import models

from user.models import UserModel


# Create your models here.
class PostModel(models.Model):
    class Meta:
        db_table = 'post'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=255, blank=True)
    body = models.CharField(max_length=255)
