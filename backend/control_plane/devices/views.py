from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView

from .models import Device
from .serializers import DeviceSerializer


class ListAllDevices(ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DevicesOnMaintenance(ListAPIView):
    queryset = Device.maintenance_objects
    serializer_class = DeviceSerializer


class AddNewDevice(CreateAPIView):

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeleteDevice(DestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'id'


