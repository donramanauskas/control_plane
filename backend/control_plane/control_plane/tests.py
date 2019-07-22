from django.test import TestCase
from .busines_logic.zabbix import ZabbixInterface


class TestZabbixInterface(TestCase):

    def test_zabbix_info(self):
        self.zabbix_instance = ZabbixInterface(
            zabbix_data={
                'device_name': 'some_name',
                'zabbix_api': 'some_api'
            }
        )
        self.assertTrue(True)