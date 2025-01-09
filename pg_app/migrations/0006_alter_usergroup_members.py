# Generated by Django 5.1.4 on 2025-01-09 03:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg_app', '0005_remove_customuser_user_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='members',
            field=models.ManyToManyField(related_name='user_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]