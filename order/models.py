from django.db import models
from common.models import Currency
from customer.models import Customer

from digi_tp.utils.models import DigiTpBaseModelWithUserAndCompany


# initial start-date, initial-stop date
# updated start-date, updated end date (defaults equals to initials)
class OrderStatus(models.TextChoices):
    QUOTATION = "Quotation"
    PROFORMA_INVOICE = "Proforma Invoice"
    PURCHASE_ORDER = "Purchase Order"
    APPROVED = "Approved"
    CONFIRMED_BY_CUSTOMER = "Confirmed By Customer"


class OrderUnitOfMesurement(models.TextChoices):
    DAYS = "Days"
    TRIPS = "Trips"


class Order(DigiTpBaseModelWithUserAndCompany):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    number_of_vehicles = models.IntegerField()
    number_of_days = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    status = models.CharField(
        max_length=50,
        choices=OrderStatus.choices,
        blank=False, null=False,
        default=OrderStatus.QUOTATION
    )
    from_location = models.CharField(max_length=255, null=False, blank=False)
    to_location = models.CharField(max_length=255, null=False, blank=False)
    unit_of_masurement = models.CharField(
        max_length=50,
        choices=OrderUnitOfMesurement.choices,
        blank=False, null=False,
        default=OrderUnitOfMesurement.DAYS
    )
    initial_start_date = models.DateField(null=False, blank=False)
    initial_end_date = models.DateField(null=False, blank=False)
    updated_start_date = models.DateField(null=True, blank=True)
    updated_end_date = models.DateField(null=True, blank=True)
    budget_amount_or_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=False,
        blank=False
    )
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title
