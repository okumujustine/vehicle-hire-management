from django.db import models

from digi_tp.utils.models import DigiTpBaseModelWithUserAndCompany


class CustomerTypes(models.TextChoices):
    PERSONAL = "Personal"
    ORGANIZATION = "Organiszation"
    GROUP = "Group"


class Customer(DigiTpBaseModelWithUserAndCompany):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=False, blank=False)
    phone_option = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, choices=CustomerTypes.choices, blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.name}"
