# Generated by Django 3.1.3 on 2021-02-12 14:06

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20201228_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=post.models.images_directory_path),
        ),
    ]
