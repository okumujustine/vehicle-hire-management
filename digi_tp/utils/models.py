from django.conf import settings
from django.db import models

from company.models import Company


class DigiTpBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DigiTpBaseModelWithCompany(DigiTpBaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='%(class)s_company')

    class Meta:
        abstract = True


class DigiTpBaseModelWithUser(DigiTpBaseModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_created_by'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_updated_by'
    )

    class Meta:
        abstract = True


class DigiTpBaseModelWithUserAndCompany(DigiTpBaseModel):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_created_by'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='%(class)s_updated_by'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='%(class)s_company'
    )

    class Meta:
        abstract = True
