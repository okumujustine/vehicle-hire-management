from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.code


class SampleMedia(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="media")

    def __str__(self):
        return self.name
