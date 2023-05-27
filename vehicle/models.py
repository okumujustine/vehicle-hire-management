from django.db import models

from digi_tp.utils.models import DigiTpBaseModelWithUserAndCompany


class VehicleTypes(models.TextChoices):
    SUV = "Suv"
    TOYOTA = "Toyota"


class VehicleModels(models.TextChoices):
    SUPER_CUSTOME = "Super Custom"
    PRADO = "prado"


class Vehicle(DigiTpBaseModelWithUserAndCompany):
    number_plate = models.CharField(max_length=50, null=False, blank=False)
    nick_name = models.CharField(max_length=50, null=True, blank=True)
    vehcile_type = models.CharField(max_length=50, choices=VehicleTypes.choices, default="default type")
    vehcile_model = models.CharField(max_length=50, choices=VehicleModels.choices, default="default model")

    def __str__(self) -> str:
        return f"{self.number_plate}"

    class Meta:
        ordering = ['id']
