from pyzabbix.api import ZabbixAPI


class ZabbixInterface:

    def __init__(self, zabbix_data):
        self.ip = zabbix_data['ip']

    def info(self):
        return self.ip

    def get_all_monitored_hosts(self):
        zapi = ZabbixAPI(url="http://"+ self.ip + "/zabbix/", user='Admin', password='zabbix')
        result1 = zapi.host.get(monitored_hosts=1, output='extend')
        return result1
