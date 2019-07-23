from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response

from .models import Device
from .serializers import DeviceModelSerializer, DeviceMaintenanceSerializer


class ListAllDevices(ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceModelSerializer


class DevicesOnMaintenance(ListAPIView):
    queryset = Device.maintenance_objects
    serializer_class = DeviceModelSerializer


class AddNewDevice(CreateAPIView):

    queryset = Device.objects.all()
    serializer_class = DeviceModelSerializer


class DeleteDevice(DestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceModelSerializer
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


