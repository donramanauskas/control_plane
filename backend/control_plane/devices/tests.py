from django.test import TestCase
from django.urls import reverse


from .models import Device


class ListDevicesViewTests(TestCase):

    def setUp(self):
        self.device1 = Device.objects.create(
            name='device1',
            type='type1',
            ip='10.0.0.1'
        )
        self.device2 = Device.objects.create(
            name='device2',
            type='type2',
            ip='10.0.0.2'
        )

    def test_list_devices(self):
        url = reverse('devices:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'device1')
        self.assertEqual(response.data[0]['type'], 'type1')
        self.assertEqual(response.data[1]['name'], 'device2')
        self.assertEqual(response.data[1]['type'], 'type2')
