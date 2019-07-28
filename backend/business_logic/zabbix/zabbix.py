from pyzabbix import ZabbixAPI, ZabbixAPIException


class ZabbixInterface:

    def __init__(self, zabbix_data):
        self.ip = zabbix_data['ip']
        self.username = 'Admin'
        self.password = 'zabbix'
        self.zapi = ZabbixAPI("http://"+ self.ip + "/zabbix/")
        self.zapi.login(self.username, self.password)

    def info(self):
        return self.ip

    def get_all_monitored_hosts(self):

        result1 = self.zapi.host.get(output='extend')
        return result1

    def add_zabbix_host(self, host_id, name, key_, type, value_type):
        try:
            item = self.zapi.item.create(
                host_id=host_id,
                name=name,
                key_=key_,
                type=type,
                value_type=value_type
            )
        except ZabbixAPIException as e:
            print(e)


