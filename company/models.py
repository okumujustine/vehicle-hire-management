from django.db import models
from django.conf import settings


class Company(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)


class CompanyUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, null=False, blank=False, default="admin")
