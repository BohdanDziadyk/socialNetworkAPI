# Generated by Django 3.1.3 on 2021-02-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210201_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='sender_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
