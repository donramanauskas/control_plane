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


class AddNewDeviceViewTests(TestCase):

    def test_add_new_device_view(self):
        url = reverse('devices:add')
        data = {
            'name': 'device3',
            'type': 'some_type',
            'ip': '10.0.0.3'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data['name'], 'device3')
        self.assertTrue(response.data['type'], 'some_type')
        self.assertEqual(response.data['ip'], '10.0.0.3')