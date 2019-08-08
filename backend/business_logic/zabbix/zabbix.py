from pyzabbix import ZabbixAPI, ZabbixAPIException
import json


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

    def get_template_details(self):

        params = {
            "output": "extend",
            "filter": {
                "host": [
                    "Template OS Linux",
                    "Template OS Windows"
            ]}
        }

        try:
            zabix_response = self.zapi.do_request(method="template.get", params=params)
            return zabix_response
        except ZabbixAPIException as e:
            print(e)

    def configuration_export(self, host_id):
        """
        {
        "jsonrpc": "2.0",
        "method": "configuration.export",
        "params": {
        "options": {
            "hosts": [
                "10161"
            ]
        },
        "format": "xml"
        },
        "auth": "038e1d7b1735c6a5436ee9eae095879e",
        "id": 1
        }

        :return:
        """
        params = {
            "options": {
                "hosts": [
                   host_id
                ]
            },
            "format": "json"
        }
        try:
            zabix_response = self.zapi.do_request(method="configuration.export", params=params)
            r_json = json.dumps(zabix_response["result"])
            return r_json
        except ZabbixAPIException as e:
            print(e)

    def template_import(self, host_id):
        params = {
            "options": {
                "hosts": [
                    host_id
                ]
            },
            "format": "json"
        }
        try:
            zabbix_response = self.zapi.do_request(method="configuration.import", params=params)
        except ZabbixAPIException as e:
            print(e)


    def configuration_import(self, template):

        params = {
            "format": "json",
            "rules": {
                "hosts": {
                    "createMissing": True,
                    "updateExisting": True
                },
                "items": {
                    "createMissing": True,
                    "updateExisting": True,
                    "deleteMissing": True
                }
            }
        }
        try:
            zabbix_response = self.zapi.confimport(confformat='json', source=template, rules={})
        except ZabbixAPIException as e:
            print(e)


z = ZabbixInterface(zabbix_data={'ip': '34.253.200.61'})
exp = z.configuration_export(host_id="10084")
print(exp)

with open("exported_template", 'w') as f:
    template = f.write(exp)

z2 = ZabbixInterface(zabbix_data={'ip': '34.242.73.63'})
result = z.configuration_import(exp)

