from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User


from .models import Device


class ListDevicesViewTests(TestCase):

    def setUp(self):
        self.device1 = Device.objects.create(
            name='device1',
            device_type='type1',
            ip='10.0.0.1'
        )
        self.device2 = Device.objects.create(
            name='device2',
            device_type='type2',
            ip='10.0.0.2'
        )

    def test_list_devices(self):
        url = reverse('devices:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'device1')
        self.assertEqual(response.data[0]['device_type'], 'type1')
        self.assertEqual(response.data[1]['name'], 'device2')
        self.assertEqual(response.data[1]['device_type'], 'type2')


class AddNewDeviceViewTests(TestCase):

    def test_add_new_device_view(self):
        url = reverse('devices:add')
        data = {
            'name': 'device3',
            'device_type': 'some_type',
            'ip': '10.0.0.3'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data['name'], 'device3')
        self.assertTrue(response.data['device_type'], 'some_type')
        self.assertEqual(response.data['ip'], '10.0.0.3')


class DeleteDeviceViewTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user_that_authenticates',
            email='user@email.com',
            password='goodpassword'
        )
        self.device1 = Device.objects.create(
            name='device1',
            device_type='type1',
            ip='10.20.30.1'
        )
        self.device2 = Device.objects.create(
            name='device2',
            device_type='type2',
            ip='10.20.30.2'
        )
        self.jwt = self.get_jwt()

    def get_jwt(self):
        auth_url = reverse('get_jwt')
        data = {'username': 'user_that_authenticates', 'password': 'goodpassword'}
        response = self.client.post(auth_url, data, format='json')
        jwt = response.data['access']
        return jwt

    def test_delete_device_view(self):
        url = reverse('devices:delete', kwargs={'id': 1})
        response = self.client.delete(url, HTTP_AUTHORIZATION='Bearer {}'.format(self.jwt), format='json')
        self.assertEqual(response.status_code, 204)

    def test_delete_device_view_no_auth(self):
        """
        Check that unauthenticated users can not delete devices.
        """

        url = reverse('devices:delete', kwargs={'id': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)


class DevicesOnMaintenanceViewTests(TestCase):

    def setUp(self):
        self.device1 = Device.objects.create(
            name='device1',
            device_type='type1',
            ip='10.20.30.1',
            ongoing_maintenance=True
        )

        self.device2 = Device.objects.create(
            name='device2',
            device_type='type2',
            ip='10.30.50.1'
        )

    def test_devices_on_maintenance_view(self):
        url = reverse('devices:on_maintenance')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(str(self.device1.name), str(response.data))
        self.assertNotIn(str(self.device2.name), str(response.data))
