
class ZabbixInterface:

    def __init__(self, zabbix_data):
        self.zabbix_data = zabbix_data

    def info(self):
        return self.zabbix_data