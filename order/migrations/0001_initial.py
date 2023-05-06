# Generated by Django 4.2 on 2023-05-06 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("common", "0001_initial"),
        ("company", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("customer", "0002_customer_company_customer_created_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("number_of_vehicles", models.IntegerField()),
                ("number_of_days", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Quotation", "Quotation"),
                            ("Proforma Invoice", "Proforma Invoice"),
                            ("Purchase Order", "Purchase Order"),
                            ("Approved", "Approved"),
                            ("Confirmed By Customer", "Confirmed By Customer"),
                        ],
                        default="Quotation",
                        max_length=50,
                    ),
                ),
                ("from_location", models.CharField(max_length=255)),
                ("to_location", models.CharField(max_length=255)),
                (
                    "unit_of_masurement",
                    models.CharField(choices=[("Days", "Days"), ("Trips", "Trips")], default="Days", max_length=50),
                ),
                ("initial_start_date", models.DateField()),
                ("initial_end_date", models.DateField()),
                ("updated_start_date", models.DateField(blank=True, null=True)),
                ("updated_end_date", models.DateField(blank=True, null=True)),
                ("budget_amount_or_cost", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_company",
                        to="company.company",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("currency", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="common.currency")),
                (
                    "customer",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="customer.customer"),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
