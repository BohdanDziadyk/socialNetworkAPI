# Generated by Django 3.1.3 on 2021-01-04 14:47

import comment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20201116_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to=comment.models.images_directory_path),
        ),
    ]
