from django.db import models


class Vehicle(models.Model):
    number_plate = models.CharField(max_length=50, null=False, blank=False)
    nick_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.number_plate}'
