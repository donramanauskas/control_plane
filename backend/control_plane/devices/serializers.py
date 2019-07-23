from rest_framework import serializers
from .models import Device


class DeviceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ['id', 'name', 'device_type', 'ip', 'ongoing_maintenance']


class DeviceMaintenanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ['ongoing_maintenance']


class DeviceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    device_type = serializers.CharField(max_length=20)
    ip = serializers.IPAddressField(protocol="both")
    ongoing_maintenance = serializers.BooleanField(default=False)