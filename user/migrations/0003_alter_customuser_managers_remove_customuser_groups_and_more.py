# Generated by Django 4.2 on 2023-04-29 21:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_make_custom_user_first_name_and_last_name_required"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="user_permissions",
        ),
    ]