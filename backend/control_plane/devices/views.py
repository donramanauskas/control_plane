from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Device
from .serializers import DeviceSerializer


class ListAllDevices(ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class AddNewDevice(CreateAPIView):

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
