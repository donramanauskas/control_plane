from rest_framework.generics import CreateAPIView

from .models import Device
from .serializers import DeviceSerializer


class AddNewDevice(CreateAPIView):

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
