# Generated by Django 4.2 on 2023-04-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone", models.CharField(max_length=50)),
                ("phone_option", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("Personal", "Personal"), ("Organiszation", "Organization"), ("Group", "Group")],
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]