from django.db import models


class VehicleTypes(models.TextChoices):
    SUV = "Suv"
    TOYOTA = "Toyota"


class VehicleModels(models.TextChoices):
    SUPER_CUSTOME = "Super Custom"
    PRADO = "prado"


class Vehicle(models.Model):
    number_plate = models.CharField(max_length=50, null=False, blank=False)
    nick_name = models.CharField(max_length=50, null=True, blank=True)
    vehcile_type = models.CharField(max_length=50, choices=VehicleTypes.choices, default="default type")
    vehcile_model = models.CharField(max_length=50, choices=VehicleModels.choices, default="default model")

    def __str__(self) -> str:
        return f"{self.number_plate}"
