# Generated by Django 3.1.3 on 2021-02-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210209_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='messengermodel',
            name='sender_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
