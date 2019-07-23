from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ['id', 'name', 'device_type', 'ip', 'ongoing_maintenance']


class DeviceMaintenanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ['ongoing_maintenance']