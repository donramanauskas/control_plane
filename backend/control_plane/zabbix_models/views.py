from rest_framework.response import Response
from rest_framework.views import APIView
from business_logic.zabbix import ZabbixInterface
from rest_framework import status

class GetZabbixMonitoredHosts(APIView):

    def post(self, request):
        try:
            ip = request.data.get('ip')
            zabbix_data = {
                "ip": ip
            }

            zi = ZabbixInterface(zabbix_data=zabbix_data)
            zabbix_host_data = zi.get_all_monitored_hosts()
            print(zabbix_host_data)
        except:
            return Response(status.HTTP_409_CONFLICT)
        return Response(zabbix_host_data, status.HTTP_200_OK)
