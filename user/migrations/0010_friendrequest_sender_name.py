# Generated by Django 3.1.3 on 2021-02-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_friendrequest_sender_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='sender_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
