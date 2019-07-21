from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    ip = models.GenericIPAddressField()
    ongoing_maintenance = models.BooleanField(default=False)
