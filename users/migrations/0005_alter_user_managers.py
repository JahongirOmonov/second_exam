# Generated by Django 4.2.7 on 2024-03-18 15:07

import django.contrib.auth.models
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_user_is_deleted"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("user_manager", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
