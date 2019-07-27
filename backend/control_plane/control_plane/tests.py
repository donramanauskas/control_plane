from django.test import TestCase
from business_logic.zabbix import ZabbixInterface


class TestZabbixInterface(TestCase):

    def test_zabbix_info(self):
        self.zabbix_instance = ZabbixInterface(
            zabbix_data={
                'ip': '10.1.1.1',
            }
        )
        self.assertTrue(True)