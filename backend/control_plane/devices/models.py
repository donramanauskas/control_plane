from django.db import models


class DeviceMaintenanceManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(ongoing_maintenance=True)


class Device(models.Model):

    name = models.CharField(max_length=20)
    device_type = models.CharField(max_length=20)
    ip = models.GenericIPAddressField()
    ongoing_maintenance = models.BooleanField(default=False)

    objects = models.Manager()
    maintenance_objects = DeviceMaintenanceManager()
