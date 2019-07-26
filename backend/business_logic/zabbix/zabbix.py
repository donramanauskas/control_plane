from pyzabbix.api import ZabbixAPI


class ZabbixInterface:

    def __init__(self, zabbix_data):
        self.zabbix_data = zabbix_data

    def info(self):
        return self.zabbix_data

    def get_all_monitored_hosts(self):
        zapi = ZabbixAPI(url="http://34.242.236.94/zabbix/", user='Admin', password='zabbix')
        result1 = zapi.host.get(monitored_hosts=1, output='extend')
        print(result1)

