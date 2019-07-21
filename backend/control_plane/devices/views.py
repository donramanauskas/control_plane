from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response

from .models import Device
from .serializers import DeviceSerializer, DeviceMaintenanceSerializer


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


class UpdateDeviceMaintenanceStatus(UpdateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceMaintenanceSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        instance = self.get_object()
        try:
            maintenance_status = bool(self.request.data['ongoing_maintenance'])
        except:
            return Response({status.HTTP_403_FORBIDDEN,
                             "Could not covert ongoing_maintenance field into valid value"})
        modified_instance = serializer.save(ongoing_maintenace=maintenance_status)


