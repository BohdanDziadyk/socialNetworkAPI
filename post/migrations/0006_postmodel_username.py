# Generated by Django 3.1.3 on 2021-02-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20210212_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='username',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]